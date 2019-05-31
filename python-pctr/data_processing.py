import pandas as pd
import lightgbm as lgb
import numpy as np
from sklearn.metrics import log_loss
import sys
import sklearn
from datetime import datetime
import pytz
import time

def timestamp_datetime(value):
    fmt = '%Y-%m-%d %H:%M:%S'
    utc_dt = pytz.utc.localize(datetime.utcfromtimestamp(float(value)))
    sh_tz = pytz.timezone("Asia/Shanghai")
    sh_dt = utc_dt.astimezone(sh_tz)
    return sh_dt.strftime(fmt)

def drop_duplicate(data):
    return data.drop_duplicates()

def instance_time(data):   
    def map_hour(x):
        if x >= 7 and x<= 12:
            return 1
        elif x >= 13 and x <= 20:
            return 2
        return 3
    data.loc[:,'time'] = data.context_timestamp.apply(timestamp_datetime)
    data.loc[:,'day'] = data.time.apply(lambda x: int(x[8:10]))
    data.loc[:,'hour'] = data.time.apply(lambda x: int(x[11:13]))
    data.loc[:,'hour_seg'] = data.hour.apply(map_hour)
    return data

def user_query_counts(data):
    user_query_day = data.groupby(['user_id', 'day']).size().reset_index().rename(columns={0: 'user_query_counts_day'})
    data = pd.merge(data, user_query_day, 'left', on=['user_id', 'day'])
    user_query_day_hour = data.groupby(['user_id', 'day', 'hour']).size().reset_index().rename(columns={0: 'user_query_counts_dayhour'})
    data = pd.merge(data, user_query_day_hour, 'left', on=['user_id', 'day', 'hour'])
    return data

def user_already_queried_item(data):
    counts = data.groupby(['item_id', "user_id", "context_timestamp"]).size().reset_index().rename(columns={0: 'counts'})
    counts.sort_values(["user_id", "item_id", "context_timestamp"], inplace=True)
    counts['same_item']=counts['item_id'].diff().eq(0)
    counts['same_user']=counts['user_id'].diff().eq(0)
    counts['user_already_queried_item']=counts.same_item & counts.same_user
    counts.drop(columns=["counts", "same_item", "same_user"], inplace=True)
    data = pd.merge(data, counts, 'left', on=['item_id', 'user_id', 'context_timestamp'])
    return data

def item_total_query_counts(data):
    counts = data.groupby(['item_id']).size().reset_index().rename(columns={0: 'item_total_query_counts'})
    return data.merge(counts, 'left', on=['item_id'])

def item_total_trade_counts(data):
    counts = data[data.is_trade == 1].groupby(['item_id']).size().reset_index().rename(columns={0: 'item_total_trade_counts'})
    data = data.merge(counts, 'left', on=['item_id'])
    data.item_total_trade_counts.fillna(0, inplace=True)
    return data

def item_total_trade_rate(data):
    data['item_total_trade_rate'] = data.item_total_trade_counts / data.item_total_query_counts
    return data

def further_processing_on_train(data):
    data = item_total_query_counts(data)
    data = item_total_trade_counts(data)
    data = item_total_trade_rate(data)
    data = user_already_queried_item(data)
    return data

def user_already_queried_item2(data, train):
    counts1 = train.groupby(['item_id', "user_id", "context_timestamp"]).size().reset_index().rename(columns={0: 'counts'})
    counts2 = data.groupby(['item_id', "user_id", "context_timestamp"]).size().reset_index().rename(columns={0: 'counts'})
    counts = counts1.append(counts2)
    counts.sort_values(["user_id", "item_id", "context_timestamp"], inplace=True)
    counts['same_item']=counts['item_id'].diff().eq(0)
    counts['same_user']=counts['user_id'].diff().eq(0)
    counts['user_already_queried_item']=counts.same_item & counts.same_user
    counts.drop(columns=["counts", "same_item", "same_user"], inplace=True)
    data = pd.merge(data, counts, 'left', on=['item_id', 'user_id', 'context_timestamp'])
    return data

def item_total_query_counts2(data, train):
    counts = train.groupby(["item_id"]).size().reset_index().rename(columns={0:"item_total_query_counts"})
    data = data.merge(counts, 'left', on=['item_id'])
    data.item_total_query_counts.fillna(1, inplace=True)
    return data

def item_total_trade_counts2(data, train):
    counts = train[train.is_trade == 1].groupby(['item_id']).size().reset_index().rename(columns={0: 'item_total_trade_counts'})
    data = data.merge(counts, 'left', on=['item_id'])
    data.item_total_trade_counts.fillna(0, inplace=True)
    return data

def further_processing_on_test(data, train):
    data = item_total_query_counts2(data, train)
    data = item_total_trade_counts2(data, train)
    data = item_total_trade_rate(data)
    data = user_already_queried_item2(data, train)
    return data

def basic_processing(data, lbl):
    def map_user_star(star):
        if star in [-1, 3000]:
            return 1
        elif star in [3009, 3010]:
            return 3
        return 2
    
    print "basic processing on time features"
    data = instance_time(data)
    
    print "basic processing on user features"
    data.loc[:,'user_gender'] = data['user_gender_id'].apply(lambda x: 1 if x == -1 else 2)
    data.loc[:,'user_occupation'] = data['user_occupation_id'].apply(lambda x: 1 if x == -1 or x == 2003 else 2)
    data.loc[:,'user_star'] = data['user_star_level'].apply(map_user_star)
    data.loc[:,'user_age'] = data['user_age_level'].apply(lambda x: 1 if x in  [1004, 1005, 1006, 1007] else 2)
    data.loc[:,'user_id'] = lbl.fit_transform(data["user_id"])
    data = user_query_counts(data)
    
    print "basic processing on item features"
    data['item_property_len'] = data['item_property_list'].map(lambda x: len(str(x).split(';')))
    for i in range(10):
        data.loc[:,'item_property_' + str(i)] = lbl.fit_transform(data['item_property_list'].map(lambda x: str(str(x).split(';')[i]) if len(str(x).split(';')) > i else ''))
    data['item_category_len'] = data['item_category_list'].map(lambda x: len(str(x).split(';')))
    for i in range(1, 3):
        data.loc[:,'item_category_' + str(i)] = lbl.fit_transform(data['item_category_list'].map(lambda x: str(str(x).split(';')[i]) if len(str(x).split(';')) > i else '')) 
    for col in ['item_id', 'item_brand_id', 'item_city_id']:
        data.loc[:,col] = lbl.fit_transform(data[col])
        
    print "basic processing on shop features"
    data.loc[:,"shop_id"] = lbl.fit_transform(data["shop_id"])
    data.loc[:,'shop_score_delivery'] = data['shop_score_delivery'].apply(lambda x: 0 if x <= 0.98 and x >= 0.96  else 1)
    
    print "basic processing on context features"
    data.loc[:,'context_page'] = data['context_page_id'].apply(lambda x: 1 if x in [4001, 4002, 4003, 4004, 4007] else 2)
    data.loc[:,'context_predict_category_property_len'] = data['predict_category_property'].map(lambda x: len(str(x).split(';')))
    for i in range(5):
        data.loc[:,'context_predict_category_property_' + str(i)] = lbl.fit_transform(data['predict_category_property'].map(
            lambda x: str(str(x).split(';')[i]) if len(str(x).split(';')) > i else ''))
    return data
