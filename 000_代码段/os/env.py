import os

env_dist = os.environ  # environ是在os.py中定义的一个dict environ = {}


# 输出系统的环境变量
if __name__ == '__main__':
    for key in env_dist:
        print(key + ' : ' + env_dist[key])
