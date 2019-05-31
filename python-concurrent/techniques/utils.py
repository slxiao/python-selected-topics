import urllib2

def do_work(task):
    if task.startswith("http"): # IO bound task
        urlHandler = urllib2.urlopen(task)
        html = urlHandler.read()
    else: #CPU bound task, counter
        task = int(task)
        while task > 0:
            task -= 1
