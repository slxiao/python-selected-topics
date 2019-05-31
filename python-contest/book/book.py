def get_min_money(case):
    num = [0] * 5
    for i in case.strip():
        num[int(i)-1] += 1
    a,b,c,d,e = sorted(num)
    if a > (c-b):
        return 30*(a-c+b) + 25.6*(2*c-a-b) + 15.2*(d-c) + 8*(e-d)
    else:
        return 25.6*(b+a) + 21.6*(c-a-b) + 15.2*(d-c) + 8*(e-d)

if __name__ == '__main__':
    with open('input', 'rb') as f:
        cont = f.readlines()
    with open('output', 'wb') as f:
        f.write('\n'.join([cont[0].strip()]+[str(get_min_money(cont[i+1])) for i in xrange(len(cont[1:]))]))
