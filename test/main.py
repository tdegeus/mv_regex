
import subprocess
import os

# support function
# ----------------

def run(cmd):
    subprocess.check_output(cmd,shell=True).decode('utf-8')

# run test
# --------

open('test1_foo.log', 'w').write('foo')
open('test1_bar.log', 'w').write('bar')

run(r'mv_regex -f "(.*)(\.log)" "\1\2.bak" *')

assert not os.path.isfile('test1_foo.log')
assert not os.path.isfile('test1_bar.log')
assert os.path.isfile('test1_foo.log.bak')
assert os.path.isfile('test1_bar.log.bak')
