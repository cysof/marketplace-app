from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *



def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	total_orders= orders.count()
	pending = orders.filter(status='Pending').count()
	delivered = orders.filter(status = 'Delivered').count()
	context = {'total_order': total_orders, 'pending': pending, 'Delivered':delivered, 'customers':customers,
	'orders':orders,

	 }


	return render(request, 'accounts/index.html', context)




def productview(request):
	products = Product.objects.all()
	return render(request, 'accounts/Products.html',{'products':products})


def customer(request, pk):
	customers = Customer.objects.get(id=pk)
	orders = customers.order_set.all()
	count_order = orders.count()
	context = { 'customers':customers, 'orders':orders, 'count_order':count_order }
	return render(request, 'accounts/customer.html', context)