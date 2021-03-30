from django.shortcuts import render
from .models import Question, Choice
from django.shortcuts import render, redirect


def quiz_start(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    choices = Choice.objects.filter(question=latest_question_list[0])
    return render(request, "questions.html", {'question':latest_question_list[0], 'choices':choices})

def room(request, room_name):
    print("Room view called..........")
    return render(request, 'room.html', {
        'room_name': room_name
    })

def join_quiz(request):
    """
    As user is going to join with temperory username a session is getting
    created and if she/he is already logged in then ignore the request
    """
    if request.method == "POST":
        print(request.POST)
        room = request.POST.get("quizcode")
        return redirect('/qz/ws/%s'%(room))
        if request.session.get('has_joined', False):
            # Already logged in user redirect to quiz page

            return redirect('quiz_start')
            #return render(request,"join_quiz.html",{'message':"You have already joined."})
        else:
            print(request.POST.get("quizcode"))
            request.session['has_joined'] = True
            request.session['quizcode'] = request.POST.get("quizcode")
            request.session['username'] = request.POST.get("username")
            return redirect('quiz_start')
    else:
        if request.session.get('has_joined', False):
            return render(request,"join_quiz.html",{'joined':True})

        return render(request,"join_quiz.html")

def quiz_logout(request):
    del request.session['has_joined']
    del request.session['quizcode']
    del request.session['username']
    return redirect('join_quiz')