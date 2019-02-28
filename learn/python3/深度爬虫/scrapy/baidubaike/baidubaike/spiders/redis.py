import redis
my_redis = redis.Redis(host='127.0.0.1', password='xzx199110', port=6379)

my_redis.lpush('xiao', 'xiaojian', 'xiaojianjian')