from django.views import generic
from django.shortcuts import render
from .models import Category

# Create your views here.
class homepage_show(generic.Listview):
    model = Category
