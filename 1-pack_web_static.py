#!/usr/bin/env python3
"""Function that create .tgz"""
from fabric.api import local
import os
from datetime import datetime


def do_pack():
    if not os.path.exists("versions"):
        local('mkdir versions')
        a = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(a.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    else:
        return None
