from django.db import models


"""
first thing frist, construct a class for all the stock name in MySQL
"""


# the table of all the stock names
class Stocks(models.Model):
    nane = models.CharField(u'Name', max_length=50)

    def __unicode__(self):
        return self.name


# the Alibaba_Group_Holding_Limited table
class Alibaba_Group_Holding_Limited(models.Model):
    table = models.TextField(u'Content')
    stock = models.ForeignKey('Stocks', blank=True, null=True,
                              on_delete=models.CASCADE)

    def __unicode__(self):
        return self.table
