from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView , UpdateView
from django.core.paginator import Paginator
# from django.views.generic import ListView

# Create your views here. 
def index(request):  
    return render(request, 'myapp/index.html') 


def product_list(request): 
    page_obj = products = Product.objects.all()   
    product_name = request.GET.get('product_name') 
    if product_name != '' and product_name is not None: 
        page_obj = products.filter(name__icontains = product_name) 

    paginator = Paginator(page_obj, 4) 
    page_num = request.GET.get('page') 
    page_obj = paginator.get_page(page_num) 

    context = {
        'page_obj' : page_obj, 
        # "products": products  
    }
    return render(request, 'myapp/product.html', context) 


class ProductListView(ListView):
    model = Product
    template_name = 'myapp/product.html'
    context_object_name = 'products' 
    paginate_by = 4 



def product_detail(request, pk): 
    product = Product.objects.get(pk=pk) 
    context = {
        "product": product
    }
    return render(request, 'myapp/detail.html', context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/detail.html' 



@login_required
def add_product(request): 
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        desc = request.POST['desc'] 
        image = request.FILES['image']
        seller_name = request.user
        Product.objects.create(name=name, price=price, desc=desc, image= image , seller_name = seller_name)
        return redirect('myapp:products') 
    return render(request, 'myapp/add_product.html') 

class ProductCreateView(CreateView):
    model = Product 
    fields = ['name', 'price', 'desc', 'image', 'seller_name'] 
    # modelname_form.html 
    


@login_required
def update_product(request, pk): 
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.desc = request.POST['desc'] 
        product.image = request.FILES['image']    
        product.save()    
        return redirect('myapp:products')  
    context ={
        "product" : product, 
    }
    return render(request, 'myapp/update_product.html', context)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price', 'desc', 'image', 'seller_name']
    template_name_suffix = '_update' 
    # modelname_update  


@login_required
def delete_product(request,pk):
    product = Product.objects.get(pk=pk) 
    if request.method == "POST":
        product.delete()
        return redirect("myapp:products") 
    context = {
        "product" : product
    }
    return render(request, 'myapp/delete.html', context)  


@login_required 
def my_listings(request):
    products = Product.objects.filter(seller_name = request.user)  
    context ={
        "products" : products, 
    }
    return render(request,'myapp/mylistings.html' ,context) 