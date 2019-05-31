import sys

if __name__ == '__main__':
    for line in sys.stdin:
        url = line.strip()
        print '%s\t%s' % (url, 1)
        dns = url.split('/')[0]
        print '%s\t%s' % (dns, 1)