from django.urls import path
from .views import course_list, course_page, teachers_page,teacher_page, holiday
urlpatterns = [
    path('', course_list, name='course_list'),
    path('<int:code>', course_page, name='course_page'),
    # path('<int:code>/<str:name>',comments_list,name='comments_list'  ),
    path('teachers', teachers_page, name='teachers_page'),
    path('<str:name>', teacher_page, name='teacher_page'),

    
]