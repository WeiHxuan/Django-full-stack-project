from django.db import models

# Create your models here.
class Shop(models.Model):
    # 标号 主键自增
    mid = models.AutoField(primary_key=True)
    #手机型号
    title = models.TextField()
    # 点击
    click = models.IntegerField()
    # 编号
    id = models.TextField()
    # 手机照片
    phone_img = models.TextField()
    # 市场价
    market_price = models.TextField()
    # 售价
    sell_price = models.TextField()
    # 库存
    stock_quantity = models.IntegerField()
    #配置
    disposition= models.TextField()
    #发售时间
    release_time= models.DateTimeField(auto_now_add=True)