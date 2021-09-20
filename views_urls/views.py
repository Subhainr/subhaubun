from django.shortcuts import render
from . import prediction_file

def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def elementary(request):
    return render(request, 'elementary.html')

def advanced(request):
    return render(request, 'advanced.html')

def rates(request):
    return render(request, 'rates.html')

def contact(request):
    return render(request, 'contact.html')


def result(request):
    First_name = request.GET['First_name']
    Second_name = request.GET['Second_name']
    email = request.GET['email']
    return render(request, 'result.html', {'First_name':First_name,'Second_name':Second_name,'email':email})

def ML_prediction(request):
        return render(request, 'ML_prediction.html')

def output_prediction(request):
    pclass = int(request.GET["pclass"])
    sex = int(request.GET["sex"])
    age = int(request.GET["age"])
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = float(request.GET["fare"])
    embarked = int(request.GET["embarked"])
    title = int(request.GET["title"])
    prediction = prediction_file.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    return render(request, 'ML_output.html', {'prediction':prediction})
