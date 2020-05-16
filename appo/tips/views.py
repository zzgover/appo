from django.shortcuts import render
from book.models import People1
from django.shortcuts import reverse,redirect
# Create your views here.
def comment(request):
    p2 = People1.objects.all()
    context = {'b_list': p2}
    return render(request, 'tips/comment.html', context)


def tips(request):
    p2 = People1.objects.all()
    context = {'b_list': p2}
    return render(request, 'tips/tips.html', context)
