from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128) #region column

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128) #iso column

    def __str__(self) :
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128) #state column

    def __str__(self) :
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=128) #name column
    description=models.CharField(max_length=500) #description column
    justification=models.CharField(max_length=500) #justification column
    year = models.IntegerField(null=True) #year column
    longitude=models.FloatField(null=True) #longitude column
    latitude=models.FloatField(null=True) #latitude column
    area_hectares= models.FloatField(null=True) #area_hectares column
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    state=models.ForeignKey(States, on_delete=models.CASCADE, null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def __str__(self) :
        return self.name
