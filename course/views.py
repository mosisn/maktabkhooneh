from django.http.response import HttpResponse, JsonResponse
from .models import Course, Main_Learn, Sub_Learn, Sub_Sub_Learn, Teacher,Ticket, teacher_courses
from django.shortcuts import render
from random import randint


def course_list(request):
    '''
    args:
    the request from user(using the url in urls.py file)

    returns:
    all of course objects in json format.
    (for showing in home page)
    '''
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'main_page/main_page.html', context=courses)

def course_page(request):
    '''
    args:
    the request from user(using the url in urls.py file)

    returns:
    all of course objects in json format.
    (for showing in a specefic course page.)
    '''
    course = Course.objects.all()
    courses = {
        'courses' : course
    }
    return render(request, 'course_page/course_page.html', context=courses)

def teacher_page(request, name):
    '''
    args:
    the request from user(using the url in urls.py file).
    the teacher name provided by url.

    returns:
    the one teacher object with the same name as the name provided to function.
    '''
    try:
        teacher = Teacher.objects.get(name=name)
    except:
        teacher=None
    teachers = {
        'Teachers' : teacher
    }
    return render(request, 'teachers_list/teacher_page.html', context=teachers)

def teacher_page_courses(request, name):
    '''
    args:
    the request from user(using the url in urls.py file).
    the teacher name provided by url.

    returns:
    the course list for teacher page
    (does not work!)
    '''
    teacher_course = teacher_courses(name)
    return render(request, 'teachers_list/teacher_page.html', context=teacher_course)

def teachers_page(request):
    '''
    args:
    the request from user(using the url in urls.py file).

    returns:
    all the teacheers names for teacher list page.
    '''
    teacher = Teacher.objects.all()
    teachers = {
        'Teachers' : teacher
    }
    return render(request, 'teachers_list/teachers_list.html', context=teachers)

def course_page(request, code):
    '''
    args:
    the request from user(using the url in urls.py file).
    the ccourse code provided by url.

    returns:
    the one course object with the same code as the code provided to function.
    '''
    if request.method == 'GET':
            '''
            if the request method is GET it returns the one course object requested by url.
            '''
            try:
                course = Course.objects.get(number=code)
            except:
                course = None
            courses = {
                'courses' : course
            }
            return render(request, 'course_page/course_page.html', context=courses)
    if request.method == 'POST':
        '''
        if the request method is POST the information received from course page are saved to ticket model.
        '''
        current_course = Course.objects.get(number=code)
        email = request.POST['email']
        name = request.POST['name']
        lastname = request.POST['lastname']
        phonenumber = request.POST['nationalid']
        Ticket.objects.create(
            #  course= Sub_Sub_Learn.objects.get(number=code),
             course= current_course,
             email=email,
             name=name,
             last_name=lastname,
             phonenumber=phonenumber,
             reservation= generate_random_code()
            )
        return HttpResponse(f'The course has been purchased successfully!')

def generate_random_code():
    '''
    creates a random 8 digit code for reservation
    
    '''
    
    code = randint(10000000,99999999)
    try:
        Ticket.objects.get(reservation=code)
        generate_random_code()
    except:
        return code
