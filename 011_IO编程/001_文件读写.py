#!/usr/bin/env python
# encoding: utf-8


"""
@author: 周涛
@contact: zhoutao825638@vip.qq.com
"""
import logging


# 读文件
def read_text(file_path):
    # 或者使用with语句
    try:
        file = open(file_path, 'r', encoding='utf8')
        print("readline ------>", file.readline())
        print("readline ------>", file.readline())
    except IOError as error:
        logging.error("Read File Has Error", error)
    finally:
        file.close()


# 写文件
def write_text(file_path, text_content):
    try:
        file = open(file_path, 'w',encoding="utf8")
        file.write(text_content)
    except IOError as error:
        logging.error("Write File has Error", error)
    finally:
        file.close()


if __name__ == '__main__':
    read_text("disk/example_001.txt")
    write_text("disk/write_001.txt", "君问归期未有期,Responsibility")
