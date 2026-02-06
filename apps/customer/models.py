from django.db import models

# CustomerUser 模型定义
class CustomerUser(models.Model):
    """
    客户表
    """
    id = models.BigAutoField(
        primary_key=True,
        verbose_name='主键 Id',
        help_text='主键 Id'
    )

    name = models.CharField(
        max_length=255,
        default='',
        verbose_name='姓名',
        help_text='姓名',
        db_collation='utf8mb4_general_ci'  # Django 4.2+ 支持
    )

    age = models.PositiveIntegerField(
        default=0,
        verbose_name='年龄',
        help_text='年龄'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间',
        help_text='创建时间'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='更新时间',
        help_text='更新时间'
    )

    class Meta:
        db_table = 'customer_user'  # 指定数据库表名
        verbose_name = '客户表'
        verbose_name_plural = '客户表'


        # 如果需要额外的索引
        indexes = [
            # 如果需要按姓名搜索
            # models.Index(fields=['name']),
            # 如果需要按年龄范围查询
            # models.Index(fields=['age']),
        ]

        # 如果需要唯一约束
        # unique_together = [
        #     ('field1', 'field2'),
        # ]

        # 如果需要排序规则
        # ordering = ['-created_at']  # 按创建时间倒序

    def __str__(self):
        return f'{self.name} (ID: {self.id})'