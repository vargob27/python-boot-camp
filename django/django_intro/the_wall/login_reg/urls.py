"""login_reg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.urls import path, include
from login_app.models import User as User, Wall_Message, Comment
class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class Wall_MessageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Wall_Message, Wall_MessageAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Comment, CommentAdmin)

urlpatterns = [
    path('', include('login_app.urls')),
    path('admin/', admin.site.urls)
]
