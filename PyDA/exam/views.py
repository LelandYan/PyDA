from django.shortcuts import render
from .models import *
from user.models import User
# Create your views here.
select_F = []
select_C = []
select_J = []


def exam(request):
    user = User.objects.get(name=request.session['user_name'])
    if not user.is_exam:
        print(user.is_exam)
        F = Question.objects.filter(question_type="F").order_by('?')[:2]
        C = Question.objects.filter(question_type="C").order_by('?')[:4]
        J = Question.objects.filter(question_type="J").order_by('?')[:2]
        for i in F:
            select_F.append(i.id)
        for i in C:
            select_C.append(i.id)
        for i in J:
            select_J.append(i.id)
        # user.is_exam = True
        # user.save()
        return render(request, 'exam/exam.html', locals())
    else:
        return render(request, 'user/index.html')


def submit(request):
    t = 0
    f = 0
    for i in select_F:
        answer = Question.objects.filter(question_type="F").get(id=i).question_answer
        if answer == request.POST.get("answer" + str(i)):
            t += 1
        else:
            f += 1
    for i in select_C:
        answer = Question.objects.filter(question_type="C").get(id=i).question_answer
        if answer == request.POST.get("answer" + str(i)):
            t += 1
        else:
            f += 1
    for i in select_J:
        answer = Question.objects.filter(question_type="J").get(id=i).question_answer
        if answer == request.POST.get("answer" + str(i)):
            t += 1
        else:
            f += 1
    print(t,f)
    select_F.clear()
    select_C.clear()
    select_J.clear()
    user = User.objects.get(name=request.session['user_name'])
    user.is_work += (f+t)
    user.not_solve += f
    user.is_exam = True
    user.save()
    return render(request, 'user/index.html')
