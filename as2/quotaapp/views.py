from django.shortcuts import render
from .models import Course, Student, Subject
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        subjects = Course.objects.filter(status=True)
        return render(request, 'quotaapp/index.html', {
            'subjects': subjects
        })


def quota_request(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        student = User.objects.get(username=request.user)
        student_info = Student.objects.get(student=student)
        course_apply = student_info.applys.all()
        other_course = Course.objects.exclude(
            id__in=course_apply.values_list('id', flat=True)).filter(status=True)

        return render(request, 'quotaapp/quota_request.html', {
            'student_info': student_info,
            'course_apply': course_apply,
            'other_course': other_course,
        })


def quota_semester2(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        student = User.objects.get(username=request.user)
        student_info = Student.objects.get(student=student)
        course_apply = student_info.applys.all()
        other_course = Course.objects.exclude(
            id__in=course_apply.values_list('id', flat=True)).filter(status=True)

        return render(request, 'quotaapp/quota_semester2.html', {
            'student_info': student_info,
            'course_apply': course_apply,
            'other_course': other_course,
        })


def complete(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        student = User.objects.get(username=request.user)
        student_info = Student.objects.get(student=student)
        course_apply = student_info.applys.all()

        return render(request, 'quotaapp/complete.html', {
            'student_info': student_info,
            'course_apply': course_apply,
        })


def cancel(request, course):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        course = course.split(' ')
        student = User.objects.get(username=request.user)
        student_info = Student.objects.get(student=student)
        subject_course = Subject.objects.get(subject_id=course[0])
        cancel_course = Course.objects.filter(
            course=subject_course, semester=course[1], year=course[2]).first()

        student_info.applys.remove(cancel_course)
        cancel_course.current_seat = cancel_course.student_apply.count()
        if cancel_course.is_seat_available():
            cancel_course.q_status = 'Available'
        cancel_course.save()

        if cancel_course.semester == '1':
            return quota_request(request)
        else:
            return quota_semester2(request)


def request(request, course):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    else:
        course = course.split(' ')
        student = User.objects.get(username=request.user)
        student_info = Student.objects.get(student=student)
        subject_course = Subject.objects.get(subject_id=course[0])
        request_course = Course.objects.filter(
            course=subject_course, semester=course[1], year=course[2]).first()

        if request_course.is_seat_available():
            student_info.applys.add(request_course)
            request_course.current_seat = request_course.student_apply.count()
            if not request_course.is_seat_available():
                request_course.q_status = 'Full'
            request_course.save()

        if request_course.semester == '1':
            return quota_request(request)
        else:
            return quota_semester2(request)
