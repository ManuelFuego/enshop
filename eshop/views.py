from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class ProductHome(ListView):
    ''' мониторинг состояния заказов '''
    model = Product
    template_name = 'eshop/index.html'


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



def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        print("print:", request.POST)
    context = {"form": form}
    return render(request, 'eshop/order.html', context)
