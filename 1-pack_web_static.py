#!/usr/bin/python3
""" Function that create a folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        f = "%Y%m%d%H%M%S"
        arcpath = 'versions/web_static_{}.tgz'.format(datetime.now().strftime(f))
        local('tar -cvzf {} web_static'.format(arcpath))
        return arcpath
    except:
        return None