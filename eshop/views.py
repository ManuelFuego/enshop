from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q, Count, Sum
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
import re

def Monitor(request):
    all_prods = Product.objects.all().count()
    full_price = Product.objects.aggregate(Sum("final_price"))
    full_price = [i for i in full_price.values()]
    summ = re.findall('\d+',str(full_price))
    all_clients = Client.objects.all().count()
    full_orders = Order.objects.all().count()

    return render(request, template_name='eshop/index.html', context={"all_clients": all_clients,
                                                                      "all_prods": all_prods,
                                                                      "full_price": int(summ[0]),
                                                                      "full_orders": full_orders, })


class CreateProduct(CreateView):
    model = Product
    template_name = 'eshop/create_product.html'
    success_url = '/eshop/balance'
    form_class = AddProduct


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'eshop/update_product.html'
    success_url = '/eshop/balance'
    form_class = AddProduct


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'eshop/delete_product.html'
    success_url = '/eshop/balance'


def balance(request):
    '''просмотр остатка'''
    search = request.GET.get("search", "")
    if search:
        info = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search))
    else:
        info = Product.objects.all().order_by("category")
    form = PriceFilter(request.GET)

    if form.is_valid():
        if form.cleaned_data["min_price"]:
            info = info.filter(final_price__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            info = info.filter(final_price__lte=form.cleaned_data["max_price"])
    return render(request, 'eshop/balance.html', context={'info': info, 'form': form})


class CreateClient(CreateView):
    model = Client
    template_name = 'eshop/create_client.html'
    form_class = AddClient
    success_url = '/eshop/add_client'

    def get_context_data(self, **kwargs):
        return dict(super(CreateClient, self).get_context_data(**kwargs),
                    clients=Client.objects.all())


class UpdateClient(UpdateView):
    model = Client
    form_class = AddClient
    template_name = 'eshop/update_client.html'
    success_url = '/eshop/add_client'


class DeleteClient(DeleteView):
    model = Client
    form_class = AddClient
    template_name = 'eshop/delete_client.html'
    success_url = '/eshop/add_client'

class CreateOrder(CreateView):
    model = Order
    template_name = 'eshop/order.html'
    form_class = OrderForm
    success_url = '/eshop/order'

def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'eshop/orders_list.html', context={'orders': orders})


class UpdateOrder(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'eshop/update_order.html'
    success_url = '/eshop/orders_list'


class DeleteOrder(DeleteView):
    model = Order
    form_class = OrderForm
    template_name = 'eshop/delete_order.html'
    success_url = '/eshop/orders_list'


