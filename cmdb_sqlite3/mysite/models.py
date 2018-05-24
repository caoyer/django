from django.db import models

# Create your models here.


class CMDB(models.Model):
    GROUP_CHOICE = (
        (u'0', u'运维组'),
        (u'1', u'测试组'),
        (u'2', u'网络组'),
        (u'3', u'软件组'),
    )
    host = models.GenericIPAddressField(u'主机地址', max_length=50)
    port = models.CharField(u'主机端口', max_length=10)
    team = models.CharField(u'使用部门', choices=GROUP_CHOICE, max_length=50)
    func = models.CharField(u'机器用途', max_length=50)
    config = models.CharField(u'硬件配置', max_length=50)
    operation = models.CharField(u'运维人员', max_length=30)
    update_date = models.DateTimeField(u'更新时间', auto_now=True)

    def __str__(self):
        return self.host
