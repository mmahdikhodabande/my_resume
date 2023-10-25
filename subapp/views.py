from django.shortcuts import render
from subapp import models


# Create your views here.


def Home(request):
    return render(request, 'index.html')


def resume_cart(request):
    my_models: models.Me = models.Me.objects.all().first()
    Cyberspace: models.Cyberspace = models.Cyberspace.objects.all().first()
    context = {
        'my_models': my_models,
        'Cyberspace': Cyberspace,
    }
    return render(request, 'shared/cart_resume.html', context)


def Description_resume(request):
    Educational_records: models.Educational_records = models.Educational_records.objects.all()
    work_experience: models.work_experience = models.work_experience.objects.all()
    languages: models.languages = models.languages.objects.all()
    interests: models.interests = models.interests.objects.all()
    Work_samples: models.Work_samples = models.Work_samples.objects.all()
    Skills: models.Skills = models.Skills.objects.all()
    context = {
        'Educational_records': Educational_records,
        'work_experience': work_experience,
        'languages': languages,
        'interests': interests,
        'Work_samples': Work_samples,
        'skills': Skills,
    }
    return render(request, 'shared/Description_resume.html', context)


def header_component(request):
    my_models: models.Me = models.Me.objects.all().first()
    context = {
        'my_models': my_models,
    }
    return render(request, 'shared/header_component.html', context)
