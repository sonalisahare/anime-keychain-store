from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .models import Wishlist



def home(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'home.html', {'products': products})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def signin(request):
    return render(request,'signin.html')

def add_to_cart(request, id):

    cart = request.session.get('cart', {})

    # Convert old list cart to dictionary
    if isinstance(cart, list):
        cart = {}

    id = str(id)

    if id in cart:
        cart[id] += 1
    else:
        cart[id] = 1

    request.session['cart'] = cart

    return redirect('home')





def cart(request):

    cart = request.session.get('cart', {})

    cart_products = []

    total = 0

    for product_id, quantity in cart.items():

        product = Product.objects.get(id=product_id)

        subtotal = product.price * quantity

        total += subtotal

        cart_products.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {
        'cart_products': cart_products,
        'total': total
    })



def increase_quantity(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        cart[id] += 1

    request.session['cart'] = cart

    return redirect('cart')




def decrease_quantity(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:

        cart[id] -= 1

        if cart[id] <= 0:
            del cart[id]

    request.session['cart'] = cart

    return redirect('cart')



def remove_from_cart(request, id):

    cart = request.session.get('cart', {})

    id = str(id)

    if id in cart:
        del cart[id]

    request.session['cart'] = cart

    return redirect('cart')



def buy(request):
    return render(request, 'buy.html')

from django.shortcuts import render, redirect

def buy(request):
    return render(request, 'buy.html')


def wishlist(request):
    wishlist_items = Wishlist.objects.all()
    return render(request, 'wishlist.html', {
        'wishlist': wishlist_items
    })


def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    Wishlist.objects.get_or_create(product=product)

    return redirect('wishlist')



def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def new_arrivals(request):
    products = Product.objects.order_by('-id')[:5]
    return render(request, 'new_arrivals.html', {'products': products})


def best_sellers(request):
    products = Product.objects.filter(id__in=[1, 2, 5, 11])
    return render(request, 'best_sellers.html', {
        'products': products
    })


def track_order(request):
    return render(request, "track_order.html")

def help_page(request):
    return render(request, "help.html")