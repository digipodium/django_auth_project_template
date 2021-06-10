from app.forms import PurchaseForm
from django.shortcuts import redirect, render
from django.contrib import messages

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