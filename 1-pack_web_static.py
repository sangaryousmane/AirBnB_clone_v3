#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB Clone repo,
using the function do_pack """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive"""

    local("mkdir -p versions")
    formatter = datetime.strftime(datetime.now(), "%Y%m%d%I%M%S")
    path_file = 'versions/web_static_{}.tgz'.format(formatter)

    complete = 'tar -cvzf {} web_static'.format(path_file)
    tar_file = local(complete)
    if tar_file.failed:
        return None
    return path_file
