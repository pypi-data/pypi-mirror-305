import subprocess
import json
import os


def get_cpu_use():
    snapshot = subprocess.run(["docker", "stats", "--no-stream", "--format", "json"], capture_output=True)
    snapshot.stdout.decode("utf-8").strip().split("\n")

    containers=dict()

    for container in list(map(json.loads,snapshot.stdout.decode("utf-8").strip().split("\n"))):
        containers[container["Name"]]=container["CPUPerc"]

    cnts = len(list(filter(lambda x:"samdul-blog" in x,containers.keys())))

    cpu_use = containers["samdul-blog-1"]

    return cpu_use, cnts

def get_config():
    from configparser import ConfigParser

    cfp = ConfigParser()

    cfp.read(f"{os.path.dirname(os.path.abspath(__file__))}/config/config.ini")

    return cfp

def get_limit():

    limit_cfg = get_config()["limit"]

    return limit_cfg["scale_in_value"],limit_cfg["scale_out_value"]
