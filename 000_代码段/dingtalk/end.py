import subprocess
import requests
import json
import time


def send_message(message):
    # access_token = 'e82a44f2e415a9dbd4fe4259beece66537c5ed40122c11812ad9e26712e17554'
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


def get_dev_label():
    (k_status, k_log) = subprocess.getstatusoutput("echo `kubectl get pod`")
    if k_status == 0:
        data = k_log.split()[5:]
        for index in range(0, len(data)):
            label = data[index]
            if index % 5 == 0 and "ufc-be-dev" in label and "mysql" not in label and "rabbit" not in label:
                return label
    return "未知 PodName"


if __name__ == '__main__':
    (status, log) = subprocess.getstatusoutput("echo `git log --pretty=format:\"%h@@@%s@@@%cn\" | awk NR==1`")
    if status == 0:
        log_arrary = log.split('@@@')
        deploy = "是" if ("部署" in log) else "否",
        msg = {
            "msgtype": "actionCard",
            "actionCard": {
                "title": "构建完成",
                "text":
                    "![screenshot](http://pic.zhoutao123.com/picture/k8s.jpg)"
                    "\n <font  style='font-weight:900;font-size:18px'> Docker构建完成, 开始部署</font>  \n"
                    "---\n"
                    "+ CommitID: <font  style='font-weight:bold'> %s </font>  \n"
                    "+ 提交内容: <font  style='font-weight:bold'> %s </font> \n"
                    "+ 提交作者：<font  style='font-weight:bold'> %s </font>\n"
                    "+ 删除Pod：<font  style='font-weight:bold'> %s </font>\n"
                    "+ 构建完成: <font  style='font-weight:bold'> %s </font>\n"
                    "+ 测试环境将会自动部署，预计 <font color=#FF0000 style='font-weight:900'>4分钟</font> 内启动完成 \n"
                    % (
                        log_arrary[0],
                        log_arrary[1],
                        log_arrary[2],
                        get_dev_label(),
                        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())),
                "hideAvatar": "0",
                "btnOrientation": "0",
                "singleTitle": "查看详情(内网)",
                "singleURL": "http://172.16.5.71:8080/job/ufc-be%20%E5%90%8E%E7%AB%AF%E9%A1%B9%E7%9B%AE%E6%9E%84%E5%BB%BA%E9%80%9A%E7%9F%A5/"
            }
        }
        send_message(json.dumps(msg))
