import subprocess
import requests
import json
import time


def send_message(message):
    access_token = 'e82a44f2e415a9dbd4fe4259beece66537c5ed40122c11812ad9e26712e17554'
    #access_token = 'b0a08aee65ea0fd3a5caee0cef64093f96a719e2a57246c4bb84a3c57d8e59a1'
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
                "title": "构建完成",
                "text":
                    "![screenshot](http://pic.zhoutao123.com/picture/nodejs.png)"
                    "\n <font  style='font-weight:900;font-size:18px'> Ufc-Web Docker 本地部署完成</font>  \n"
                    "---\n"
                    "+ CommitID: <font  style='font-weight:bold'> %s </font>  \n"
                    "+ 提交内容: <font  style='font-weight:bold'> %s </font> \n"
                    "+ 部署地址：http://172.16.5.71:80 \n"
                    "+ 构建完成: <font  style='font-weight:bold'> %s </font>\n"
                    % (
                        log[0:9],
                        log[9:],
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                "hideAvatar": "0",
                "btnOrientation": "0",
                "singleTitle": "查看详情(内网)",
                "singleURL": "http://172.16.5.71:8080/job/job/Ufc-LocalDeploy/"
            }
        }
        send_message(json.dumps(msg))
