def large_sum_pos(a, b):
    if len(a) > len(b):
        b = '0'*(len(a)-len(b)) + b
    else:
        a = '0'*(len(b)-len(a)) + a
    s = ''
    increase = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i]) + int(b[i]) + increase > 9:
            s = str(int(a[i])+int(b[i])+increase-10) + s
            increase = 1
        else:
            s = str(int(a[i])+int(b[i])+increase) + s
            increase = 0
    s = str(increase) + s
    return s

def large_sum_neg(a, b):
    b = '0'*(len(a)-len(b)) + b
    s = ''
    decrease = 0
    for i in range(len(a)-1, -1, -1):
        if int(a[i])-decrease >= int(b[i]):
            s = str(int(a[i])-int(b[i])-decrease) + s
            decrease = 0
        else:
            s = str(10+int(a[i])-int(b[i])-decrease) + s
            decrease = 1
    return s

def post_process(res):
    if '-' not in res:
        return res.lstrip('0')
    return '-'+res.replace('-','').lstrip('0')

def large_sum(a, b):
    if '-' not in a and '-' not in b:
        res = large_sum_pos(a,b)
    elif '-' in a and '-' in b:
        res = '-'+large_sum_pos(a.replace('-',''),b.replace('-',''))
    else:
        if '-' in a:
            temp = a
            a = b
            b = temp
        if int(a) >= int(b.replace('-','')):
            res = large_sum_neg(a,b.replace('-',''))
        else:
            res = '-'+large_sum_neg(b.replace('-',''),a)
    return post_process(res)


if __name__ == '__main__':
    results = []

    with open('input','rb') as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        a, b = line.split(',')
        results.append(large_sum(a,b))

    with open('output', 'wb') as f:
        f.write('\n'.join(results))

