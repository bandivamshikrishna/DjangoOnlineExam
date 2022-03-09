from django.db import models

# Create your models here.
class SubjectModel(models.Model):
    subject_name=models.CharField(max_length=100)
    subject_topic=models.CharField(max_length=100)
