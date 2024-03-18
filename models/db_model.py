# 连接数据库
# 连接数据库
import pymysql

# # 打开数据库连接
DB = pymysql.connect(host='123.249.3.67',
                     user='root',
                     password='123456',
                     database='data_center',
                     port=3004)

# 进行向数据库中添加数据:
def insert_data(insert_sql):
    with DB.cursor() as cursor:
        cursor.execute(insert_sql)
    # 提交更改
    DB.commit()
    print(">>>>>>提交数据成功")


# 进行查询数据库中的数据内容：
def select_data(select_sql):
        # 创建一个游标对象
    with DB.cursor() as cursor:
        # 执行 SQL 查询语句
        cursor.execute(select_sql)
        # 获取查询结果
        result = cursor.fetchall()
        # 打印查询结果
        # print(list(result))
        return list(result)



# if __name__ == '__main__':
#     insert_data(insert_sql)















