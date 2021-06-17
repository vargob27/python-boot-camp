
from django.urls import path
from . import views

urlpatterns = [
path('', views.index),
path('success', views.success),
path('register', views.register),
path('login', views.login),
path('logout', views.logout),
path('make_post', views.post),
path('add_comment/<int:post_id>', views.comment),
path('user/<int:user_id>', views.profile),
path('like/<int:id>', views.add_like)
]
