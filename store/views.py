from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def main(request):
    if request.user.is_authenticated:

        cart_items = CartProduct.objects.filter(customer=request.user)
    else:
        return redirect('users:log_in')
    products = Product.objects.all()
    slides = Slide.objects.all()
    return render(request, 'main_page.html', {
        'slides': slides,
        'products': products,
        'cart_items': cart_items,
    })


def cart(request):
    if request.user.is_authenticated:
        cart_items = CartProduct.objects.filter(customer=request.user)
        total_price = sum([item.total_price() for item in cart_items])
        total_quantity = sum([item.quantity for item in cart_items])
    else:
        return redirect('users:log_in')

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
    })


def shop(request):
    if request.user.is_authenticated:

        cart_items = CartProduct.objects.filter(customer=request.user)
    else:
        return redirect('users:log_in')
    brands = Brand.objects.all()
    products = Product.objects.all()
    brand = request.GET.get('brand')
    flag = False
    brand_id = Brand.objects.get(pk=brand) if brand else None

    products = products.filter(brand=brand) if brand else products

    product_id = request.GET.get('product')

    if product_id:
        if request.user.is_authenticated:
            product = Product.objects.get(pk=product_id)
            cart_item = CartProduct.objects.filter(product=product,
                                                   customer=request.user)
            if not cart_item:
                if product.quantity > 0:
                    CartProduct.objects.create(customer=request.user, product=product,
                                               quantity=1)
                    return redirect('store:shop')
                else:
                    flag = True

            for item in cart_item:
                item.quantity += 1
                item.save()
        else:
            return redirect('users:log_in')

    return render(request, 'shop.html',
                  {'brands': brands, 'products': products, 'brand': brand_id, 'flag': flag, 'cart_items': cart_items, })


def search_page(request):
    if request.user.is_authenticated:

        cart_items = CartProduct.objects.filter(customer=request.user)
    else:
        return redirect('users:log_in')
    search = request.GET.get('search', '').strip()
    products = Product.objects.all()
    products = products.filter(title__iregex=search) if search else products
    return render(request, 'search_page.html', {'products': products, 'cart_items': cart_items, })


def delete_cart_item(request, pk):
    cart_item = CartProduct.objects.get(pk=pk).delete()
    return redirect('store:cart')


def edit_cart_item(request, pk):
    cart_item = get_object_or_404(CartProduct, pk=pk)
    action = request.GET.get('action')

    if action == 'decrement' and cart_item.quantity == 1:
        cart_item.delete()
        return redirect('store:cart')
    if action == 'decrement' and cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return redirect('store:cart')
    if cart_item.product.quantity > cart_item.quantity:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('store:cart')


def product_detail(request, pk):
    if request.user.is_authenticated:

        cart_items = CartProduct.objects.filter(customer=request.user)
    else:
        return redirect('users:log_in')
    product = get_object_or_404(Product, pk=pk)

    product_id = request.GET.get('product')
    reviews = Review.objects.filter(product=product)
    form = ReviewForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST" and form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.product = product
            instance.save()
            return redirect('store:product_detail', pk=product.pk)
    else:
        return redirect('users:log_in')
    if product_id:
        if request.user.is_authenticated:
            product = Product.objects.get(pk=product_id)
            cart_item = CartProduct.objects.filter(product=product,
                                                   customer=request.user)
            if not cart_item:
                CartProduct.objects.create(customer=request.user, product=product,
                                           quantity=1)
                return redirect('store:shop')

            for item in cart_item:
                item.quantity += 1
                item.save()
        else:
            return redirect('users:log_in')

    return render(request, 'product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews,
        'cart_items': cart_items,
    })


def make_order(request):
    cart_items = None
    total_price = None
    total_quantity = None
    form = None

    if request.user.is_authenticated:

        cart_items = CartProduct.objects.filter(customer=request.user)
        total_price = sum([item.total_price() for item in cart_items])
        total_quantity = sum([item.quantity for item in cart_items])
        form = OrderForm(request.POST)

        if not cart_items:
            return render(request, 'error.html')

        if request.method == 'POST' and form.is_valid():
            order = Order.objects.create(
                customer=request.user,
                address=request.POST.get('address'),
                phone=request.POST.get('phone'),
                total_price=total_price
            )
            for cart_item in cart_items:
                OrderProduct.objects.create(
                    order=order,
                    product=cart_item.product,
                    amount=cart_item.quantity,
                    total=cart_item.total_price()
                )
            cart_items.delete()
            return redirect('store:orders')
    else:
        return redirect('users:log_in')

    return render(request, 'order_creation_page.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_quantity': total_quantity,
        'form': form
    })


def orders(request):
    if request.user.is_authenticated:

        cart_items = CartProduct.objects.filter(customer=request.user)

        orders_list = Order.objects.filter(customer=request.user)
    else:
        return redirect('users:log_in')
    return render(request, 'orders.html', {'orders': orders_list, 'cart_items':cart_items})


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.user != review.user:
        return render(request, 'error.html', {'review': review})

    if request.method == "POST":
        review.delete()
        return redirect('store:product_detail', review.product.pk)
    return render(request, 'delete_review.html', {'review': review})


def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.user != review.user:
        return render(request, 'error.html', {'review': review})
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('store:product_detail', review.product.pk)
    return render(request, 'edit_review.html', {
        'form': form,
        'product': review.product
    })
