import subprocess
import requests
import json
import time


def get_dev_label():
    (status, log) = subprocess.getstatusoutput("echo `git log --pretty=format:\"%h@@@%s@@@%cn\" | awk NR==1`")
    if status == 0:
        data = log.split('@@@')
        print(data[0])
        print(data[1])
        print(data[2])


if __name__ == '__main__':
    get_dev_label()
