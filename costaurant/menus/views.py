from django.shortcuts import render
from datetime import datetime
from menus.models import Menu


# Create your views here.
def index(request):
    context = dict()
    today = datetime.now().date()
    context['today'] = today
    context['menus'] = Menu.objects.all()
    return render(request, 'menus/index.html', context)


def detail(request, pk):
    menu = Menu.objects.get(id=pk)
    context = {'menu':menu}
    return render(request, 'menus/detail.html', context)
