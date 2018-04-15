from django.shortcuts import render, get_object_or_404

from backscratcher.models import Backscratcher


def home(request):
    backscratchers = Backscratcher.objects.all()

    return render(request, 'backscratcher/home.html', {
        'backscratchers': backscratchers,
    })


def backscratcher_detail(request, bs_pk):
    backscratcher = get_object_or_404(Backscratcher, pk=bs_pk)

    return render(request, 'backscratcher/bs_detail.html', {
        'backscratcher': backscratcher,
    })
