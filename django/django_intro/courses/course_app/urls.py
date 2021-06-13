from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('create', views.create_course),
    path('destroy/<int:course_id>', views.destroy_course),
    path('delete/<int:course_id>', views.delete_course)
]
