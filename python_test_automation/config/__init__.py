import json
import os
import sys

def get_conf():
    return json.load(open(os.path.abspath(os.path.join(os.path.dirname(__file__), "config_test.json"))))