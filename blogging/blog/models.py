from django.db import models
from django.utils.text import slugify



class Blog(models.Model):
    name = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=200)
    image = models.ImageField(max_length=40, upload_to='blog_images')
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs'

    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug from title if not set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




