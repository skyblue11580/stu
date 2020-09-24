from django.db import models

# Create your models here.


class BookInfo(models.Model):
    """
    图书表
    """

    # 创建字段，字段类型
    name = models.CharField(max_length=10, null=False, verbose_name='书名')
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '图书'

    def __str__(self):
        return self.name



class PeopleInfo(models.Model):
    """
    人物表
    """
    GENDER_CHOICES = (
        (0, 'SEX'),
        (1, 'MAN'),
        (2, 'WOMEN')
    )
    name = models.CharField(max_length=10, null=False, verbose_name='姓名')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=100, null=True, verbose_name='描述')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书编号')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name





