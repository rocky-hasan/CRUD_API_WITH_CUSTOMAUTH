
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api_list/',views.student_api_list),
    path('studentapi/<int:pk>/',views.student_api),
]
