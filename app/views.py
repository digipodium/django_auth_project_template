from app.forms import PurchaseForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Product
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def purchase_item(request):
    form = PurchaseForm()
    if request.method =="POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            fd = form.save(commit=False)
            fd.buyer = request.user
            fd.save()
            messages.success(request,f"well done {fd.id} done")
            return redirect('home')

        messages.error(request,"errors")
    ctx={
        'form':form,
        'price':40,
    }
    return render(request,"purchase.html",ctx)

def show_products(request):
    products = Product.objects.all()
    ctx = {'products':products}
    return render(request,'store/product_view.html',ctx)

def show_single_product(request,pk):
    product = get_object_or_404(Product,pk=pk)
    ctx = {'product':product}
    return render(request,'store/product_detail.html',ctx)

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("product_all")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
