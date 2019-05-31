# Introduction
This project presents our ML solution for [IJCAI 2018 Alimama pCTR competition](https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.100150.711.6.7c552784Mhia35&raceId=231647).

# Composition
- `run.ipynb`: [Jupyter Notebook](http://jupyter.org/) of our solution. 
- `data_processing.py`: Feature engineering part of our solution.
- datasets: train and test datasets of the competition can be found [here](https://tianchi.aliyun.com/competition/information.htm?spm=5176.100067.5678.2.48da2163ovoiSR&raceId=231647).

# Feature Engineering
Following categories of features are extracted.
- **User Features**: features describing user properties (such as age, gender) and user behaviors (such as user's queries during a day/hour).
- **Item Features**: features describing item properties.
- **Shop Features**: features describing shop properties.
- **Context Features**: features describing context properties.
- **Other Features**: such as instance id, day, hour, etc.

# ML algorithm
Our algorithm is based on [LightGBM](https://lightgbm.readthedocs.io/en/latest/), which is a fast, distrbuted and high performance gradient boosting framework based on decision tree algorithms. Specifically, we use the `LGBMClassifier` to efficiently train our model and predict on unknown instances.

# Outcome
Our solution achieved top 10% scores in the competition.


