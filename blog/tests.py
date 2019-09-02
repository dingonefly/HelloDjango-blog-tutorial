from django.test import TestCase

# Create your tests here.
from datetime import datetime
now=datetime.now()
print('当前时间：',now.month)
utcnow=datetime.utcnow()
print('世界标准时间：',utcnow)
dt=datetime(2017, 5, 23, 12, 20)
print('指定日期：',dt)