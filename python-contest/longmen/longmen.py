def get_adjs(i, m, n):
    x = i/n
    y = i%n
    cans = [(x-1, y),(x+1, y),(x,y-1),(x,y+1)]
    cans = filter(lambda x: x[0] in range(m) and x[1] in range(n), cans)
    return [n*x[0]+x[1] for x in cans]

def get_result(m, n, t, case):
    z = case.find('Z')
    l = case.find('L')
    path = []
    curr_hop = [z]
    while curr_hop:
        path.append(curr_hop)
        next_hop = []
        for c in curr_hop:
            next_hop += filter(lambda x: case[x] != '*', get_adjs(c, m, n))
        history_nodes = reduce(lambda x, y: x+y, path)
        next_hop = filter(lambda x: x not in history_nodes, next_hop)
        next_hop = list(set(next_hop))
        curr_hop = next_hop
    distance = 10000
    for i in xrange(len(path)):
        if l in path[i]:
            distance = i
            break;
    if distance <= t:
        return True
    return False

if __name__ == '__main__':
    with open('input','rb') as f:
        cont = f.readlines()
    cont = cont[1:]
    res = []
    order = 0
    for i in xrange(len(cont)):
        line = cont[i].strip()
        if line.replace(' ','').isdigit():
            order += 1
            m, n, t = line.split()
            lines = cont[i+1:i+1+int(n)]
            case = reduce(lambda x, y: ''.join(x.replace(' ','').split()) + ''.join(y.replace(' ', '')), lines, '')
            if get_result(int(n),int(m),int(t),case):
                res.append('Case #%s: YES'% order)
            else:
                res.append('Case #%s: NO'% order)
    with open('output','wb') as f:
        f.write('\n'.join(res))


