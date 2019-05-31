def get_ball_score(i, bout):
    if bout[i] == 'X':
        return 10
    if bout[i] == '/':
        if bout[1-i] == '-':
            return 10
        return 10 - int(bout[1-i])
    if bout[i] == '-':
        return 0
    return int(bout[i])

def get_bout_score(bout):
    return [get_ball_score(i, bout) for i in xrange(len(bout))]

def get_added_score(i, scores, bouts):
    if 'X' in bouts[i]:
        if len(scores[i+1]) == 2:
            return sum(scores[i+1])
        else:
            return sum(scores[i+1]) + scores[i+2][0]
    elif '/' in bouts[i]:
        return scores[i+1][0]
    return 0

def get_bowling_score(pattern):
    if '||' in pattern:
        bouts, bonus = pattern.split('||')
    else:
        bouts = pattern
        bonus = ''
    bouts = bouts.split('|')
    scores = [get_bout_score(i) for i in bouts] + [get_bout_score(bonus)]
    return sum([sum(scores[i])+get_added_score(i, scores, bouts) for i in xrange(10)])

if __name__ == '__main__':
    scores = []

    with open('input','rb') as f:
        lines = f.readlines()

    for line in lines:
        if '|' in line:
            line = line.strip()
            score = get_bowling_score(line)
            scores.append(str(score))

    with open('output', 'wb') as f:
        f.write('\n'.join(scores))

