from django.db import models

# Create your models here.
Job_Type = (
    ('Full Time1', 'Full Time'),
    ('Part Time1', 'Part Time'),
)
class job (models.Model) :
    titre = models.CharField(max_length=30)
    #location

    job_type = models.CharField(max_length=22, choices=Job_Type)
    description = models.TextField(max_length=10000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)


    def __str__(self):
        return self.titre

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name