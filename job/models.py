from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

Job_Type = (
    ('Full Time1', 'Full Time'),
    ('Part Time1', 'Part Time'),
)
def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)
class job (models.Model) :
    titre = models.CharField(max_length=30)
    #location
    #owner = models.Foreignkey(User, related_name='', on_delete=models.CASCADE)
    job_type = models.CharField(max_length=22, choices=Job_Type)
    description = models.TextField(max_length=10000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(job, self).save(*args, **kwargs)


    def __str__(self):
        return self.titre

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey('Job',related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv =models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length='1000')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name