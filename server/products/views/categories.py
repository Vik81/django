from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from django.views.generic import (
    View
)
from products.models import Category
from products.forms import CategoryForm, CategoryModelForm


class ProductCreate(View):
    def get(self):
        pass

    def post(self):
        pass


class ProductUpdate(View):
    def get(self):
        pass

    def post(self):
        pass




class ProductUpdate(View):
    pass



def category_create(request):
    form = CategoryModelForm()
    if request.method == 'POST':
        form = CategoryModelForm(
            data=request.POST,
            files=request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect('products:main')
    return render(
        request,
        'categories/create.html',
        {'form': form}
    )


def category_update(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    form = CategoryModelForm(instance=obj)
    if request.method == 'POST':
        form = CategoryModelForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )
        if form.is_valid():
            form.save()
            return redirect('products:main')
    return render(
        request,
        'categories/update.html',
        {'form': form}
    )


def category_delete(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('products:main')
    return render(
        request,
        'categories/delete.html',
        {'object': obj})


def category_list(request):
    return render(
        request,
        'categories/index.html',
        {'object_list': Category.objects.all()}
    )


def category_detail(request, pk):
    obj = get_object_or_404(Category, pk=pk)
    return render(
        request,
        'categories/detail.html',
        {'object_list': obj}
    )
