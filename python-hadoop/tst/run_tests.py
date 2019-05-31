import unittest
import subprocess

class TestURLCount(unittest.TestCase):
    def test_mapper_reducer(self):
        with open('./tst/url_data.txt', 'rb') as f:
            url_data = f.read()

        map_res = subprocess.check_output('echo "%s" | python ./src/mapper.py' % url_data.strip(), shell=True)
        self.assertEqual(map_res, 'www.taobao.com/index.html\t1\nwww.taobao.com\t1\nwww.tmall.com/index.xml\t1\nwww.tmall.com\t1\nwww.taobao.com/example.html\t1\nwww.taobao.com\t1\nwww.taobao.com/index.html\t1\nwww.taobao.com\t1\n')

        red_res = subprocess.check_output('echo "%s" | sort -k1,1 | python ./src/reducer.py'% map_res.strip(), shell=True)
        self.assertEqual(red_res, 'www.taobao.com\t3\nwww.taobao.com/example.html\t1\nwww.taobao.com/index.html\t2\nwww.tmall.com\t1\nwww.tmall.com/index.xml\t1\n')

if __name__ == '__main__':
    unittest.main()
