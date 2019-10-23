from django.db import models

# Create your models here.
class Page(models.Model):
    page_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.page_name
