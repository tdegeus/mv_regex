import unittest
import subprocess
import os


def run(cmd, verbose=False):
    return subprocess.check_output(cmd, shell=True).decode('utf-8')


class Test_cli_mv_regex(unittest.TestCase):

    def test_basic(self):

        for file in ['foo.log', 'bar.log']:
            if os.path.isfile(file):
                os.remove(file)

        with open('foo.log', 'w') as file:
            file.write('foo')

        with open('bar.log', 'w') as file:
            file.write('bar')

        run(r'mv_regex -f "(.*)(\.log)" "\1\2.bak" *')

        self.assertTrue(not os.path.isfile('foo.log'))
        self.assertTrue(not os.path.isfile('bar.log'))
        self.assertTrue(os.path.isfile('foo.log.bak'))
        self.assertTrue(os.path.isfile('bar.log.bak'))

        os.remove('foo.log.bak')
        os.remove('bar.log.bak')


if __name__ == '__main__':

    unittest.main()

