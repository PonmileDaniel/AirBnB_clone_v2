#!/usr/bin/env python3
"""Function that create .tgz"""
from fabric.api import local
from fabric import task
from datetime import datetime


def do_pack():
    local('mkdir -p versions')
    date_str = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f"versions/web_static_{date_str}.tgz"
    result = local(f"tar -cvzf {archive_name} web_static")
    if result.succeeded:
        return archive_name
    else:
        return None
