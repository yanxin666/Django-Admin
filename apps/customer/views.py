from django.http import HttpResponse
from .models import CustomerUser
from django.utils import timezone
from datetime import timedelta, datetime

def testdb(request):
    # 添加一条数据到 CustomerUser 表
    # customer = CustomerUser(name='李四1', age=30)
    # customer.save()

    # 查询所有数据
    customers = CustomerUser.objects.all()
    print("所有客户数据：", customers[0], customers.count(), customers[0].name)

    # 按姓名查询
    customers = CustomerUser.objects.filter(name='李四').last()
    print("按姓名查询：", customers)
    if customers is None:
        print("没有找到姓名为李四的客户")

    # 按年龄范围查询
    young_customers = CustomerUser.objects.filter(age__lt=30)  # 小于30岁
    adult_customers = CustomerUser.objects.filter(age__gte=18)  # 大于等于18岁
    print("小于30岁的客户：", young_customers)
    print("大于等于18岁的客户：", adult_customers)

    # 按照创建时间范围查询
    one_week_ago = timezone.now() - timedelta(weeks=1)
    # 构造一个datetime，值为2026-02-05 16:16:18
    time1 = datetime(2026, 2, 6, 12, 10, 18)
    # time1 = timezone.make_aware(naive_time)
    print("一周前的时间：", time1)
    recent_customers = CustomerUser.objects.filter(created_at__gte=time1)
    print("一周内创建的客户：", recent_customers)

    # 查找 Id为 1 的客户的所有字段
    customer = CustomerUser.objects.get(id=1)
    print("Id为1的客户的全部信息：", customer.__dict__)
    print("Id为1的客户的姓名：", customer.name)
    print("Id为1的客户的年龄：", customer.age)
    print("Id为1的客户的创建时间：", customer.created_at)

    # 更新 Id为 1 的客户的年龄为 35
    customer.age = 35
    customer.save()
    print("更新后的客户信息：", customer.__dict__)


    return HttpResponse("<p>数据操作成功！</p>")