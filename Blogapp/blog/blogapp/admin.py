from django.contrib import admin
from .models import Post, Categories
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','title','content','author','category','date']
    
    def __str__(self):
        return self.title
    
@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display=["name"]