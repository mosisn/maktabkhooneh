from django.http.response import HttpResponse, JsonResponse
from .models import Course, Main_Learn, Sub_Learn, Sub_Sub_Learn, Teacher,Ticket, teacher_courses
from django.shortcuts import render
from random import randint


def course_list(request):
    #  this is view for list of courses
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'main_page/main_page.html', context=courses)

def course_page(request):
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'course_page/course_page.html', context=courses)

def teacher_page(request, name):
    #  this is a view for teacher page
    try:
        teacher = Teacher.objects.get(name=name)
    except:
        teacher=None
    teachers = {
        'Teachers' : teacher
    }
    return render(request, 'teachers_list/teacher_page.html', context=teachers)


def teacher_page_courses(request, name):
    #  this is a view for teacher page course list
    teacher_course = teacher_courses(name)
    return render(request, 'teachers_list/teacher_page.html', context=teacher_course)

def teachers_page(request):
    #  this is a view for teacher list
    teacher = Teacher.objects.all()
    teachers = {
        'Teachers' : teacher
    }
    return render(request, 'teachers_list/teachers_list.html', context=teachers)

def course_page(request, code):
    if request.method == 'GET':
            try:
                course = Course.objects.get(number=code)
            except:
                course = None
            courses = {
                'courses' : course
            }
            return render(request, 'course_page/course_page.html', context=courses)
    if request.method == 'POST':
        current_course = Course.objects.get(number=code)
        email = request.POST['email']
        name = request.POST['name']
        lastname = request.POST['lastname']
        phonenumber = request.POST['nationalid']
        # seat = request.POST['seat']
        Ticket.objects.create(
            #  course= Sub_Sub_Learn.objects.get(number=code),
             course= current_course,
             email=email,
             name=name,
             last_name=lastname,
             phonenumber=phonenumber,
            #  seat=seat,
             reservation= generate_random_code()
            )
        return HttpResponse('The ticket reserved!')

def generate_random_code():
    code = randint(10000000,99999999)
    try:
        Ticket.objects.get(reservation=code)
        generate_random_code()
    except:
        return code
