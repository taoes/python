import subprocess
import requests
import json
import time


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
    (status, log) = subprocess.getstatusoutput("echo `git log --oneline |awk 'NR==1'`")
    if status == 0:
        msg = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": "正在构建" + log,
                "text":
                    "![screenshot](http://pic.zhoutao123.com/picture/build.jpeg)"
                    "\n<font  style='font-weight:900;font-size:18px'> 正在开始构建镜像 </font>  \n"
                    "---\n"
                    "+ CommitID: <font  style='font-weight:bold'> %s </font> \n"
                    "+ 提交日志: <font  style='font-weight:bold'> %s </font>\n"
                    "+ 构建时间: <font  style='font-weight:bold'> %s </font>\n"
                    % (
                        log[0:9],
                        log[9:],
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                "hideAvatar": "0",
                "btnOrientation": "0",
                "singleTitle": "查看详情(内网)",
                "singleURL": "http://172.16.5.71:8080/job/ufc-be%20%E5%90%8E%E7%AB%AF%E9%A1%B9%E7%9B%AE%E6%9E%84%E5%BB%BA%E9%80%9A%E7%9F%A5/"
            }
        }
        send_message(json.dumps(msg))
