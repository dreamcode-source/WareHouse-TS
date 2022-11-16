from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid please'
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admini')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def logout_view(request):
    logout(request)
    return render(request, 'login.html')


def admini(request):
    # if not request.user.is_authenticated():
    #     return redirect('login_view')
    # else:
        return render(request, 'admini/admini.html')


def customer(request):
    return render(request, 'customer.html')


def employee(request):
    return render(request, 'employee.html')

def register_users(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid please'
    else:
        form = SignUpForm()

    return render(request, 'admini/users.html', {'form': form, 'msg': msg})

def customer_view(request):
    return render(request, 'admini/customer.html')

def sales_view(request):
    return render(request, 'admini/sales.html')

def supplier_view(request):
    return render(request, 'admini/supplier.html')

def warehouse_view(request):
    return render(request, 'admini/warehouse.html')

def goodmaster_view(request):
    return render(request, 'admini/goodsmaster.html')

def incominggoods_view(request):
    return render(request, 'admini/incoming_goods.html')

def outgoinggoods_view(request):
    return render(request, 'admini/outgoing_goods.html')

def shop_view(request):
    return render(request, 'admini/shops.html')

def expenses_view(request):
    return render(request, 'admini/expenses.html')
    


