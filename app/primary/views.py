from django.shortcuts import render, get_object_or_404
from primary import models


def index(request, slug):
    obj = get_object_or_404(models.PrimaryProperty, slug=slug)
    context = {'obj': obj}
    return render(request, 'primary/index.html', context)