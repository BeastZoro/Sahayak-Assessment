from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=250)
    teacher = models.ManyToManyField('Teachers', related_name='students')

    def __str__(self):
        return self.name

class Teachers(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teachers', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"certificate for {self.std.name} from {self.teacher}"