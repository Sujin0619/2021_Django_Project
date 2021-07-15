from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    goods = Product.objects.all()
    context = {'goods':goods}
    return render(request, 'goods/index.html', context)
