
# 创建Milvus表结构：
from pymilvus import connections,Collection, FieldSchema, CollectionSchema, DataType,MilvusClient
import random

# connections.connect(host='192.168.88.54', port='19530')
#
# # 定义向量字段
# field_list = [
#             FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
#             FieldSchema(name="QA", dtype=DataType.VARCHAR, max_length=5000),
#             FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128),
#         ]
#
# # 创建集合模式
# schema = CollectionSchema(fields=field_list, description="My_collection")
#
# #创建库
# collection = Collection(name="my_Miluvs", schema=schema)
# #创建索引：
# index = {
#     "index_type": "Trie", #一种高效的索引结构
#     "metric_type": "IP",   #相似度
#     "params": {"nlist": 128}, #倒排的数量
# }
#
#
# collection.create_index(field_name="QA",index_params=index)
#
# # 关闭数据库连接：
# connections.disconnect(alias="my_Miluvs")


# 向Milvus向量数据库中添加数据：
# data = [
#     {"id":2,"QA":"我是My_Miluvs2","vector":[random.random() for _ in range(128)]}
# ]
#
#
# collection.insert(data)




# 进行搜索：
# 构建查询向量
# query_vector = [random.random() for _ in range(128)]
#
# # 在索引中进行相似度搜索
# search_result = collection.search(data=[query_vector], anns_field="vector", param={"nprobe": 10}, limit=1)
#
# # 处理搜索结果
# print("Search result:")
# for result in search_result:
#     print(result)
#
# # 断开连接
# connections.disconnect(alias="my_Miluvs")


# 删除和查询有问题


client = MilvusClient(
    uri="http://192.168.88.54:19530",
    token="root:Milvus"
)



# 删除：
# client.delete(collection_name="my_Miluvs",ids=1)


# 查询数据：
# res = client.query(collection_name="my_Miluvs",filter="id < 3",limit=2)
# print(res)


# 获取数据
# res = client.get(collection_name="my_Miluvs",ids=[1,2])
# print(res)



#明日解决：更新插入，和查询多个数据和获取多个数据