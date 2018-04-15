from django.shortcuts import render, get_object_or_404

from backscratcher.models import Backscratcher


def home(request):
    backscratchers = Backscratcher.objects.all()

    return render(request, 'backscratcher/home.html', {
        'backscratchers': backscratchers
    })
