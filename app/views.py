from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

def paginate(objects_list, request, per_page):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    content = paginator.get_page(page_number)
    return content

questions =[
    {
        "title": f"Question {i}",
        "text": f"This is text for {i} question."
    } for i in range(1,100)
]

answers =[
    {
        "title": f"Answer {i}",
        "text": f"This is text for {i} answer."
    } for i in range(1,3)
]

def index(request):
    content= paginate(questions,request, 5)
    return render(request, "index.html" , {'questions': content})

def hot(request):
    content = paginate(questions,request, 5)
    return render(request, "hot.html" , {'questions': content})

def ask(request):
    return render(request, "ask.html" , {})

def tag (request):
    content= paginate(questions,request, 5)
    return render(request, "tag.html" , {'questions': content})

def login(request):
    return render(request, "login.html" , {})

def settings(request):
    return render(request, "settings.html" , {})

def signup(request):
    return render(request, "signup.html" , {})

def question(request):
    return render(request, "question.html" , {'answers': answers})