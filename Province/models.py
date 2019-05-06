from django.db import models


class Canton(models.Model):
    province = models.CharField(max_length=200)
    name = models.CharField(max_length=200) 
    code = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.name, self.province)

class Distric(models.Model):
    canton = models.ForeignKey(Canton,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s %s' % (self.canton, self.name, self.code)