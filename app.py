from flask import Flask, request, render_template
from fastai.tabular import *
import requests
import os.path

path = ''
export_file_url = 'https://www.dropbox.com/s/8o48lybasamjmiy/symptoms_export.pkl?dl=1'
export_file_name = 'symptoms_export.pkl'

def down_load_file(filename, url):
    """
    Download an URL to a file
    """
    with open(filename, 'wb') as fout:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        # Write response data to file
        for block in response.iter_content(4096):
            fout.write(block)
            
def download_if_not_exists(filename, url):
    """
    Download a URL to a file if the file
    does not exist already.
    Returns
    -------
    True if the file was downloaded,
    False if it already existed
    """
    if not os.path.exists(filename):
        down_load_file(filename, url)
        return True
    return False

download_if_not_exists(export_file_name, export_file_url)

learn = load_learner(path, export_file_name)

