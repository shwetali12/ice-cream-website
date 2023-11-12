from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from datetime import datetime 
from home.models import Contact
from home.models import Cart,Product,Order
from django.shortcuts import render, get_object_or_404
from django.views import View


# Create your views here.
#@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

#@login_required(login_url='login')
def about(request):
    return render(request,'about.html')


#@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact =Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request,'contact.html')

def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your Password1  and password2 are not same.")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signuppage.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1= request.POST.get('password1')
        print(username,password1)
        user=authenticate(request,username=username,password=password1)
        
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            print(username,password1)
            return HttpResponse("Password is incorrect")
        
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')

def services(request):
    service_data = Product.objects.all()
    data ={
            'service_data':service_data
        }
    return render(request,"services.html",data)


   



def details(request,id):
    
    details_data= get_object_or_404(Product,id=id)
    return render(request, "details.html" ,{'details_data':details_data})

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart': cart})


    

def add_to_cart(request):
    user = request.user
    prod_id = request.GET.get('id')
    product_name = Product.objects.get(id=prod_id)
    product = Product.objects.filter(pk=prod_id)
    for p in product:
        image = p.image
        price = p.price
    Cart(user = user,product=product_name,image=image,price=price).save()
    return redirect('services')



       


def remove_item(request,id):
    cart_item = Cart.objects.get(id=id,user=request.user)
    cart_item.delete()
    return redirect('cart')



def place_order(request,id):
    if request.method == 'POST':
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        user = request.user

        # Assuming you have a Cart model with a 'product' field
        
        cart_item = Cart.objects.get(id=id)
        order = Order(user=user, address=address, pincode=pincode, product=cart_item.product, total=cart_item.price)
        order.save()
        cart_item.delete()  # Remove the cart item after creating the order
        return redirect('services')
        
    else:
        # Handle cases where the request method is not POST
        # You might want to display an error message or redirect to an error page

       # user = request.user
        #prod_id = request.GET.get('id')
        #product_name = Cart.objects.get(id=prod_id)
       # product = Cart.objects.filter(id=prod_id)
       # for p in product:
       #     price = p.price
       # Order(user = user,product=product_name,total=price).save()
        return redirect('services')

def view_order(request,id):
    
    order_data= get_object_or_404(Cart,id=id)
    return render(request, "view_order.html" ,{'order_data':order_data})

def myorders(request):
    data = Order.objects.filter(user=request.user)
    return render(request,'myorders.html',{'data':data})


       