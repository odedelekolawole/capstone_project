from django.db import models
import uuid

# Create your models here.

class Category2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    tagline = models.TextField(max_length=200) 
    
    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name





class News2(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="new_images")
    category = models.ForeignKey(Category2, on_delete=models.CASCADE)
    reporter = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ["created"]

    def __str__(self):
        return self.title

