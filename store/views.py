from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template import *
from .models import Category, Book
from .forms import SellForm, BuyForm

def home(request):

	categories = Category.objects.all().order_by('name')
	return render(request,'store/home.html', {'categories':categories})

def cum_cumperi(request):
	
	categories = Category.objects.all().order_by('name')
	return render(request,'store/cum_cumperi.html', {'categories':categories})

def cumparam(request):

	categories = Category.objects.all().order_by('name')
	if request.method == 'GET':
		form = BuyForm()
		context = { 'categories': categories,
					'form': form,
		}
		return render(request,'store/cumparam.html', context)
	elif request.method == 'POST':
		form = BuyForm(request.POST)
		if form.is_valid():
			to_buy = form.save(commit=False)
			to_buy.save()
			return redirect('home')
		else:
			context = { 'categories': categories,
					'form': form,
			}
			return render(request,'store/cumparam.html', context)



def contact(request):
	
	categories = Category.objects.all().order_by('name')
	return render(request,'store/contact.html', {'categories':categories})


def category_search(request,pk):

	cat = Category.objects.filter(name=pk)
	books = Book.objects.filter(category=cat)
	categories = Category.objects.all().order_by('name')
	context = { 'categories':categories,
				'books':books,
	}
	return render(request,'store/category_search.html',context)


def book_details(request, pk, id):

	book = Book.objects.get(pk=id)
	categories = Category.objects.all().order_by('name')

	if request.method == "GET":
		form = SellForm()
		context = {'categories':categories,
					'book':book,
					'form':form,
		}
		return render(request,'store/book_details.html', context )

	elif request.method == "POST":
		form = SellForm(request.POST)
        if form.is_valid():
        	sold = form.save(commit=False)
        	sold.book = book
        	sold.save()
        	book.sell()
        	book.save()
        	context = {'categories':categories,
        	}
        	return redirect('category_search',pk=pk)
        else:
        	form = SellForm()
        	context = {'categories': categories,
        				'book': book,
        				'form': form,
        				}
  
		return render(request,'store/book_details.html', context )