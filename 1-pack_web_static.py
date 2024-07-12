#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        a = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(a.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except:
        return None
