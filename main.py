
from flask import Flask,request
import json
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


# 创建后台调度器
# scheduler = BackgroundScheduler()
#
# # 定义一个定时任务
# def my_job():
#     print("》》》》》》》》》》》我是定时任务执行！")
#
# # 将定时任务添加到调度器中，并设定触发时间间隔为10秒
# scheduler.add_job(my_job, 'interval', seconds=10)
#
# # 启动调度器
# scheduler.start()



@app.route("/getz",methods=['GET'])
def get():
    print(">>>>>",666677)
    return json.dumps({"code":200,'msg':"66677"})




if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port=8000)





