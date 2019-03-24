##import json
from django.shortcuts import render, redirect

from .models import Product, Category
from .forms import CategoryForm, CategoryModelForm

def product_list(request):
##    with open('products/fixtures/data/data.json') as file:
##        return render(
##            request,
##            'products/index.html',
##            {'object_list': json.load(file)})
    return render(
        request,
        'products/index.html',
        {'object_list': Product.objects.all()})

def product_detail(request, pk):
##    with open('products/fixtures/data/data.json') as file:
##        return render(
##            request,
##            'products/detail.html',
##            {'object': json.load(file)[pk]})
    return render(
        request,
        'products/detail.html',
        {'object': Product.objects.get(id = pk)})


def category_create(request):
    form = CategoryModelForm()
    if request.method =='POST':
        form = CategoryModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            # Category.objects.create(
            #     name=form.cleaned_data.get('name')
            # )
            return redirect('products:main')
    return render(
        request,
        'categories/create.html',
        {'form':form}
    )
