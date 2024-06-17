from django.db import models

# Create your models here.
class MapPoint(models.Model):
    name= models.CharField(max_length=25)
    lat= models.FloatField()
    lon= models.FloatField()

    def __str__(self) -> str:
        return self.name
    
class Schools(models.Model):
    name= models.CharField(max_length=250)
    lat= models.FloatField()
    lon= models.FloatField()
    Level= models.CharField(max_length=250, blank=True, null=True)
    Status= models.CharField(max_length=250, blank=True, null=True)
    Sponsor	= models.CharField(max_length=250, blank=True, null=True)
    Classrooms= models.IntegerField(blank=True, null=True)
    # Stage= models.CharField(max_length=250, blank=True, null=True) # replaced by the following two fields  
    stage_number = models.IntegerField(null=True, blank=True)
    stage_name = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        verbose_name_plural = 'Schools'


    def __str__(self) -> str:
        return self.name
    