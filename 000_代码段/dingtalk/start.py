import subprocess
import requests
import json
import time
import os


def send_message(message):
    access_token = 'b0a08aee65ea0fd3a5caee0cef64093f96a719e2a57246c4bb84a3c57d8e59a1'
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % access_token
    headers = {"Content-Type": "application/json;"}
    try:
        response = requests.post(url, headers=headers, data=message)
        response_msg = str(response.status_code) + ' ' + str(response.content)
    except Exception as error_msg:
        print('error_msg===' + str(error_msg))
        response_msg = error_msg
    print(response_msg)
    return response_msg


if __name__ == '__main__':
    (status, log) = subprocess.getstatusoutput("echo `git log --pretty=format:\"%h@@@%s@@@%cn\" | awk NR==1`")
    log_arrary = log.split('@@@')
    build = "no_deploy" not in log_arrary[1]
    if status == 0:
        msg = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": log[1],
                "text":
                    "![screenshot](http://pic.zhoutao123.com/picture/build.jpeg)"
                    "\n<font  style='font-weight:900;font-size:18px'> 正在开始构建镜像 </font>  \n"
                    "---\n"
                    "+ CommitID: <font  style='font-weight:bold'> %s </font> \n"
                    "+ 提交日志: <font  style='font-weight:bold'> %s </font>\n"
                    "+ 提交作者: <font  style='font-weight:bold'> %s </font>\n"
                    "+ 构建时间: <font  style='font-weight:bold'> %s </font>\n"
                    "+ 是否构建: <font  color=#FF000 style='font-weight:bold'> %s </font>\n"
                    % (
                        log_arrary[0],
                        log_arrary[1],
                        log_arrary[2],
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                        build
                    ),
                "hideAvatar": "0",
                "btnOrientation": "0",
                "singleTitle": "查看详情(内网)",
                "singleURL": "http://172.16.5.71:8080/job/ufc-be%20%E5%90%8E%E7%AB%AF%E9%A1%B9%E7%9B%AE%E6%9E%84%E5%BB%BA%E9%80%9A%E7%9F%A5/"
            }
        }
        send_message(json.dumps(msg))

    # 提交日志中包含 no_deploy 则不会部署
    if "no_deploy" in log_arrary[1]:
        os._exit(1)
    else:
        os._exit(0)
