
from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_api_list/',views.Student_api_list.as_view(), name='student-api-list'),
    path('student_api_list/<int:pk>/',views.Student_detail.as_view(), name='student-detail'),
]
