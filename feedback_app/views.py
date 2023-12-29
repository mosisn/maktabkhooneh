from django.http.response import HttpResponse, JsonResponse
from .models import Comments
from course.models import Course
from django.shortcuts import render
from random import randint
import requests
import pyzt


def comments_list(request, code, name):
    if request.method == 'GET':
            '''
            if the request method is GET it returns the comment list requested by url.
            '''
            try:
                comment = Comments.objects.filter(course__name=name)
            except:
                comment = None
            comments = {
                'comments' : comment
            }
            return render(request, 'course_page/comments_page.html', context=comments)
    if request.method == 'POST':
        '''
        if the request method is POST the information received from comment page are saved to Comments model.
        '''
        current_course = Course.objects.get(number=code)
        email = request.POST['email']
        name = request.POST['name']
        lastname = request.POST['lastname']
        comment = request.POST['comment']
        Comments.objects.create(
             course= current_course,
             email=email,
             name=name,
             last_name=lastname,
             comment=comment,
            )
        return HttpResponse(f'The comment has been submitted successfully!')