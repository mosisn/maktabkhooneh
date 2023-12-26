from django.urls import path
from .views import course_list, course_page, teachers_page,teacher_page
urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:code>', course_page, name='course_page'),
    path('teachers', teachers_page, name='teachers_page'),
    path('<str:name>', teacher_page, name='teachers_page'),

    
]