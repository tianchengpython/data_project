from apscheduler.schedulers.background import BackgroundScheduler
# 创建后台调度器
scheduler = BackgroundScheduler()
# 添加定时任务到调度器
# scheduler.add_job(job,
#                   'interval',  # 指定触发器类型为间隔触发
#                   seconds=10,  # 指定间隔时间为 10 秒
#                   args=['Hello, World!'],  # 传递位置参数
#                   id='my_job',  # 指定任务的唯一标识符
#                   name='My Job',  # 指定任务的名称
#                   max_instances=3)  # 最大并发执行实例数为 3

# 间隔写法
# scheduler.add_job(my_job, 'interval', seconds=10,id="my_job")

# 每天晚上跑定时任务，可以开始时间和结束时间
# 创建一个定时任务跑一个文件夹下所有的pdf文件，将pdf文件中的文字提取出来写到txt文档中去
# 结束时间，



# 定义一个定时任务
def my_job():
    print("》》》》》》》》》》》》》》》》》》》》》》》》》》》》》定时任务执行！")


# 指定周期写法
scheduler.add_job(my_job,'cron',hour=9, minute=12,id="my_job")

# 启动调度器
scheduler.start()
# 定义一个停止任务的函数
def stop_job():
    scheduler.remove_job("my_job")
    print("》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》定时任务已停止！")
scheduler.add_job(stop_job, 'cron',hour=9, minute=13)


















