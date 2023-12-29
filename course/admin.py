from django.contrib.admin import ModelAdmin,register
from .models import Course, Teacher, Main_Learn, Sub_Learn, Sub_Sub_Learn,Ticket

@register(Course)
class CourseAdmin(ModelAdmin):
    autocomplete_fields = [ 'teacher',
                            'category',
                            'other_courses_needed'
                            ]
    search_fields = ['teacher',
                     'category',
                     'other_courses_needed']

@register(Teacher)
class TeacherAdmin(ModelAdmin):
    search_fields = ['name']

    
@register(Main_Learn)
class MainLearnAdmin(ModelAdmin):
    pass
    
@register(Sub_Learn)
class SubLearnAdmin(ModelAdmin):
    pass

@register(Sub_Sub_Learn)
class SUbSubLearnAdmin(ModelAdmin):
    search_fields = ['name']

@register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display =['name', 'last_name', 'reservation']

# @register(Comments)
# class CommentsAdmin(ModelAdmin):
#     list_display =['name', 'last_name', 'email']