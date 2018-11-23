import pymongo

client = pymongo.MongoClient('127.0.0.1', port=27017)


db = client.zhihu


collection = db.qa

# 写入数据
# collection.insert({
#     'username': 'xiao',
#     'age': 21,
# })


# collection.insert_many([
#     {
#         'username': 'xiaojianjian',
#         'age': 23,
#         'password': '199110',
#     },
#     {
#         'username': 'zs',
#         'age': 24,
#         'password': '231233423',
#     }
# ])


# cursor = collection.find()
# for x in cursor:
#     print(x)

# result = collection.find_one({'age': 23})
# print(result)

# 更新数据
# collection.update_one({'username': 'xiaojianjian'}, {
#                       '$set': {'username': 'hello world'}})

# collection.update_many({'age': 25}, {'$set': {'age': 23}})

# 删除数据
collection.delete_one({'username': 'hello world'})
