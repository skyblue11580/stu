from redis import Redis


redis_cli = Redis(host='localhost', port=6379, db=0)
name = '静夜思'

title = '床前明月光，疑似地上霜。举头望明月，低头思故乡。'
redis_cli.set('name', name.encode('utf-8'))
redis_cli.set('title', title)
print(redis_cli.get('name'))
print(redis_cli.get('title'))
print((redis_cli.get('nt')).decode())
# 获取redis 中的键
result = redis_cli.keys()
print(result)
# from redis import *
# if __name__ == "__main__":
#     try:
#         # 创建Redis对象，与redis服务器建⽴连接
#         sr = Redis()
#         # 添加键name，值为itheima
#         result = sr.set('name', 'itheima')
#         # 输出响应结果，如果添加成功则返回True，否则返回False
#         print(result)
#     except Exception as e:
#         print(e)
redis_cli.setex(name='name1', time=60, value='name1')

