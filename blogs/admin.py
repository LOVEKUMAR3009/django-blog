from django.contrib import admin
from .models import Category ,Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('id','title','category','author','is_featured','status')
    search_fields = ('title','id','category__category_name','status')
    list_editable  = ('is_featured',)
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)