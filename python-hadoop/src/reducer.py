import sys

if __name__ == '__main__':
    current_item = None
    current_count = 0
    item = None

    for line in sys.stdin:
        line = line.strip()
        item, count = line.split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue # ignore value exception

        if current_item == item:
            current_count += count
        else:
            if current_item:
                print '%s\t%s' % (current_item, current_count)
            current_count = count
            current_item = item

    if current_item == item:
        print '%s\t%s' % (current_item, current_count)
