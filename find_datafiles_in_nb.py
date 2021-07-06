import glob
import os
import sys
import re

def find_data_files_in_notebook(notebook, key='../data/'):
    """Return a tuple containing the lists of
    data files and the notebook name"""

    with open(notebook) as f:
        s = f.read()
        start_ids = [m.start() for m in re.finditer(key, s)]
        data_fnames = []
        for match in start_ids:
            # print(match)
            substr = s[match: match + 50]
            # print('\t' + substr)
            data_fnames.append(substr)
        if data_fnames:
            return (notebook, data_fnames)
        else:
            return (notebook, ['NONE'])

notebooks = glob.glob('master/*.ipynb')
for notebook in notebooks:
    print("\n\n*********************")
    print(notebook.strip('master/'))
    notebook, data_fnames = find_data_files_in_notebook(notebook)
    for data_fname in set(data_fnames):
        print('\t' + data_fname)
    print('*********************\n')