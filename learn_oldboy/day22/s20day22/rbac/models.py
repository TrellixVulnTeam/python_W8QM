from django.db import models

# Create your models here.



class UserInfo(models.Model):

    name=models.CharField(max_length=32)
    pwd=models.CharField(max_length=32)
    roles=models.ManyToManyField("Role")
    def __str__(self):
        return self.name

class Role(models.Model):
    title=models.CharField(max_length=32)
    permissions=models.ManyToManyField("Permission")
    def __str__(self):
        return self.title

class Permission(models.Model):
    title=models.CharField(verbose_name="权限名称",max_length=32)
    url=models.CharField(max_length=32)


    def __str__(self):
        return self.title
