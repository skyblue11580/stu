from django.test import TestCase

# Create your tests here.
# 插入数据
# 方式一：
from book.models import BookInfo, PeopleInfo
book = BookInfo(
    name='python入门',
    pub_date='2020-10-1'
)
BookInfo.objects.create(
    name='python进阶',
    pub_date='2020-10-1',
    readcount=20,
    commentcount=10
)
book.save()
# 方式二：
PeopleInfo.objects.create(
    name='itheima',
    book=book
)
# 修改数据
# 方式一：
person = PeopleInfo.objects.get(name='itheima')
person.name = '小白'
person.save()
person
# 方式二：
books = BookInfo.objects.filter(name='python进阶').update(name='python高级')


PeopleInfo.objects.create(
    name='小李',
    book=book
)

# 删除数据
# 方式一：
person = PeopleInfo.objects.get(name='小李')
person.delete()
# 方式二：
book = BookInfo.objects.get(name='python入门').delete()
book
book = BookInfo.objects.filter(name='python高级').delete()
book

# 查询
# all查询全部数据 相当于 select * from bookinfo;
BookInfo.objects.all()
BookInfo.objects.all().count()

# 过滤查询 filter  exclude  get  相当于  select * from book where xxx
# 1. filter 过滤出多个结果
BookInfo.objects.filter(name__contains='传')  # 名字里包含传的
# 属性名__运算符=值
# 2. get   过滤出一个结果  条件不满足会抛出异常
BookInfo.objects.get(name__startswith='2')  # 以什么开头，
# 3. exclude   过滤出不符合条件的  相当于非
BookInfo.objects.exclude(name__endswith='传')  # 以什么结尾
#  范围查询
#  查询id 是 1或者3 的数据
BookInfo.objects.filter(id__in=[1, 3])


# 比较查询
'''
gt  >
lt  <
gte >=
lte <=
'''
# 查询标号大于3的图书
BookInfo.objects.filter(id__gt=3)

# 日期查询
BookInfo.objects.filter(pub_date__year=1980)


# F对象(可以同时使用多个属性)
from django.db.models import F, Q
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount'))
# 查询阅读量大于2倍评论量的图书
BookInfo.objects.filter(readcount__gt=F('commentcount')*2)

# Q对象  多个连用时，可以实现 且， 或，的关系
# 阅读量>20且 id<3的图书
BookInfo.objects.filter(readcount__gt=20, id__lt=3)
# 改写为Q对象
BookInfo.objects.filter(Q(readcount__gt=20) & Q(id__lt=3))
# 阅读量>20 获取id<3的图书 | 表示或
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))
