import os
import re
import click

from ._version import *

def mv(search, replace, files, force=False):

    for file in files:
        if not os.path.isfile(file) and not os.path.isdir(file):
            raise IOError('Input {0:s} does not exist'.format(file))

    # only keep input files that match the input regular-expression
    files = [file for file in files if re.match(search, file)]

    # rename the remaining files
    ret = [re.sub(search, replace, file) for file in files]

    # only keep files that will be renamed
    idx = [i for i, (old, new) in enumerate(zip(files, ret)) if old != new]
    files = [files[i] for i in idx]
    renamed = [ret[i] for i in idx]

    # no files remaining -> quit
    if len(renamed) == 0:
        return ret

    # prompt the user for confirmation
    if not force:

        # - construct print-format to align output
        w = max([len(file) for file in files])
        fmt = 'mv {file:'+str(w)+'s} {new:s}'

        # - print all files
        for file,new in zip(files,renamed):
            print(fmt.format(file=file,new=new))

        # - prompt user
        if not click.confirm('Proceed?'):
            raise IOError('Aborted')

    # proceed with the renaming of all files
    for file, new in zip(files,renamed):
        os.rename(file, new)

    return ret
