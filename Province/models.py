from django.db import models


class Canton(models.Model):
    province = models.CharField(max_length=200)
    name = models.CharField(max_length=20,unique=True) 
    code = models.CharField(max_length=10)
    
    def __str__(self):
        return '%s ' % (self.province)

class Distric(models.Model):
    
    province = models.ForeignKey(Canton,on_delete=models.CASCADE, related_name="distric_province")
    canton = models.ForeignKey(Canton,on_delete=models.CASCADE,to_field='name',related_name="distric_canton")
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s %s' % (self.canton, self.name, self.code)