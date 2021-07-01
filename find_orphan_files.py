import glob
import os
import sys

def find_file_in_notebook(fname, notebook):
    """Returns a the filename and notebook name 
    if the filename is in the notebook, returns the 
    filename and None if otherwise

    Args:
        fname (str): path to filename
        notebook (str): notebook name
    """

    with open(notebook) as file:
        s = file.read()
        first_find = s.find(fname)
        if (first_find != -1):
            return fname.strip('data/'), notebook.strip('master/')
        else:
            return 

def lower(s):
        return s.lower()

if len(sys.argv) > 1:
    fname, notebook = sys.argv[1:]
    print(find_file_in_notebook(fname, notebook))

else:
    fnames = glob.glob('data/*')
    fnames = sorted(fnames, key=lower)
    notebooks = glob.glob('master/*.ipynb')
    for fname in fnames:    
        for notebook in notebooks:
            result = find_file_in_notebook(fname, notebook)
            if result:
                print(find_file_in_notebook(fname, notebook))