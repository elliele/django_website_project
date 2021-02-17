from django.contrib import admin
from .models import Post

# Register your models here.

#how to register model, 1. import,
# 2.run the command admin.site.register("what you want to register")
admin.site.register(Post)