from django.db import models

class Developer(models.Model):
    dev_name = models.CharField('Developer', max_length=20)

    def __str__(self):
        return self.dev_name

class Package(models.Model):
    pack_name = models.CharField('Package', max_length=20)

    def __str__(self):
        return self.pack_name

class Gen_info(models.Model):
    name = models.CharField('Name', max_length=20)
    launched = models.IntegerField('Launched(year)', max_length=20)
    clock_rate = models.CharField('Clock_rate', max_length=20)
    bit = models.IntegerField('Bit', max_length=20)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
