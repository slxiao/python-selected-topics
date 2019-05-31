def get_counts(size, group):
    return [len(filter(lambda x: x==i, group)) for i in xrange(size)]

def get_more(size, group):
    if len(group) == 0:
        return 0
    return (len(group)-1)/size + 1

def get_more_2(c1,c2):
    a = [(0, 1),(1,1),(1,1),(1,2)]
    return a[c1][c2]

def get_num(size, group):
    res = 0
    group = [ x % size for x in group]
    if size == 3:
        c0, c1, c2 = get_counts(size, group)
        res = res + c0 + min(c1, c2) + get_more(size, [1]*max(c1-c2,c2-c1))
    elif size == 2:
        c0, c1 = get_counts(size, group)
        res = res + c0 + get_more(size, [1]*c1)
    elif size == 4:
        c0, c1, c2, c3 = get_counts(size, group)
        c2 = c2 + min(c1,c3)*2
        c1 = max(c1-c3, c3-c1)
        res += c0 + c2/2 + c1/4
        res += get_more_2(c1%4, c2%2)
    return res

if __name__ == '__main__':
    with open('input', 'rb') as f:
        cont = f.readlines()

    cont = cont[1:]
    res = []
    l = len(cont)
    i = 0
    while True:
        first = cont[i].strip()
        second = cont[i+1].strip()
        _, size = first.split()
        group = [int(j) for j in second.split()]
        r = get_num(int(size), group)
        res.append(r)
        i = i+2
        if i > l-1:
            break
    with open('output','wb') as f:
        x = ['Case #%s: %s'%(i+1, res[i]) for i in xrange(len(res))]
        f.write('\n'.join(x))



