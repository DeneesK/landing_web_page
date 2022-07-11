from django.db import models

# Create your models here.
from django.db.models import CharField

class CmsSlider(models.Model):
    cms_image = models.ImageField(upload_to="slidering/")
    cms_title = models.CharField(max_length=200, verbose_name="Title")
    cms_text = models.CharField(max_length=200, verbose_name='Text')
    cms_css = models.CharField(max_length=200, null=True, default='-',verbose_name='Css class')

    def __str__(self):
        return self.cms_title

    class Meta():
        verbose_name = "Slide"
        verbose_name_plural = "Slides"