from django.shortcuts import render,redirect
from .models import order,orderd_Item
from django.contrib import messages
from products.models import product
from django.contrib.auth.decorators import login_required
# Create your views here.


def show_cart(request):
    user=request.user
    customer=user.customer_profile
    print("user",user)
    print("customer",customer)
    cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

def remove_item(request,pk):

    item=orderd_Item.objects.get(pk=pk)
    if item:
         item.delete()
    return redirect('cart')

def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=order.objects.get(
                owner=customer,
                order_status=order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message='your order is processed. your item will be delivered with in 3 days'
                messages.success(request, status_message)
            else:
                status_message=' unable to processed. no items in cart'
                messages.error(request,status_message)
        except Exception as e:
                status_message=' unable to processed. no items in cart'
                messages.error(request, status_message)
        return redirect('cart')
    
@login_required(login_url='account')

def view_orders(request):
    user=request.user
    customer=user.customer_profile
    
    return render(request,'cart.html')

         
@login_required(login_url='account')
def show_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=order.objects.filter(owner=customer).exclude(order_status=order.CART_STAGE)
    context={'orders':all_orders}
    return render(request,'orders.html',context)

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=order.objects.get_or_create(
            owner=customer,
            order_status=order.CART_STAGE
        )
        Product=product.objects.get(pk=product_id)
        orderdItem,created=orderd_Item.objects.get_or_create(
           Product=Product,
           owner=cart_obj,
         
        )
        if created:
            orderdItem.quantity=quantity
            orderdItem.save()
        else:
            orderdItem.quantity=orderdItem.quantity+quantity
            orderdItem.save()
    return redirect('cart')


