from django.shortcuts import render,redirect
from django.http import HttpResponse
from stock_manager.forms import RegisterMakerForm, RegisterProductForm, RegisterSmartPhoneForm, RegisterStockForm
from .models import Maker,Product,SmartPhone,Stock
from django.views import generic


def register_maker(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = RegisterMakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maker_list')
        else:
            params['message'] = '再入力して下さい'
            params['form'] = form
    else:
        params['form'] = RegisterMakerForm()
    return render(request, 'stock_manager/register_maker.html', params)


def register_product(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = RegisterProductForm(request.POST)
        form.save()
        return redirect('product_list')
    else:
        params['form'] = RegisterProductForm()
        return render(request, 'stock_manager/register_product.html', params)


def register_product(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = RegisterProductForm(request.POST)
        form.save()
        return redirect('product_list')
    else:
        params['form'] = RegisterProductForm()
        return render(request, 'stock_manager/register_product.html', params)


def register_smartphone(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = RegisterSmartPhoneForm(request.POST)
        form.save()
        return redirect('smartphone_list')
    else:
        params['form'] = RegisterSmartPhoneForm()
        return render(request, 'stock_manager/register_smartphone.html', params)


def register_stock(request):
    params = {'message': '', 'form': None}
    if request.method == 'POST':
        form = RegisterStockForm(request.POST)
        smartphone_id = form.data['smartphone']
        version = form.data['version']
        price = form.data['price']
        smartphone = SmartPhone.objects.get(id=smartphone_id)
        new_stock = Stock(smartphone=smartphone,version=version,price=price)
        new_stock.save()
        return redirect('stock_list')
    else:
        params['form'] = RegisterStockForm()
        return render(request, 'stock_manager/register_stock.html', params)


def maker_list(request):
    data = Maker.objects.all()
    params = {'message': 'メーカー一覧', 'data': data}
    return render(request, 'stock_manager/maker_list.html', params)


def product_list(request):
    data = Product.objects.all()
    params = {'message': '機種一覧', 'data': data}
    return render(request, 'stock_manager/product_list.html', params)


def smartphone_list(request):
    data = SmartPhone.objects.all()
    params = {'message': 'スマートフォン一覧', 'data': data}
    return render(request, 'stock_manager/smartphone_list.html', params)


def stock_list(request):
    data = Stock.objects.all()
    params = {'message': '在庫一覧', 'data': data}
    return render(request, 'stock_manager/stock_list.html', params)
