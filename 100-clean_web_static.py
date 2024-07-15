#!/usr/bin/python3
# This fabric script delete out of date archive
from fabric.api import *
import os

env.hosts = ["54.145.156.219", "18.233.67.185"]


def do_clean(number=0):
    """This delete out-of-date archive"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
