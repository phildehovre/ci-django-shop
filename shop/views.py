from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderItem, ProductTag, Order, Feature, ProductSpecs, ProductImage
from base.models import Address
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .helpers import calculations
from django.db.models import Q
from .forms import UpdateProductForm, UpdateFeatureForm, ProductSpecsForm, ProductImageForm
import json


def shop_view(request, selected_tags=None):
    page = "product_list"
    product_list = Product.objects.all()
    product_tags = ProductTag.objects.all()

    if request.method == "POST":
        selected_tags = request.POST.getlist("tag") if request.POST.getlist("tag") else ['all']
        search = request.POST.get('search')
        
        if selected_tags != ['all']:
            product_list = product_list.filter(tags__id__in=selected_tags)
        if search:
            product_list = product_list.filter(Q(name__contains=search) | Q(description__contains=search))

    edit_perm = False
    add_perm = False
    if request.user:
        edit_perm = request.user.has_perm('shop/change_product')
        add_perm = request.user.has_perm('shop/add_product')

    return render(
        request, 
        'shop/product_list.html', 
        {
            "products": product_list, 
            "tags": product_tags,
            "selected_tags": selected_tags,
            'page': page,
            "edit_perm": edit_perm,
            "add_perm": add_perm
        }
    )


@login_required
def add_to_basket(request, pk):
    quantity = int(request.POST.get("quantity", 1))
    product = Product.objects.get(id=pk)

    try:
        order = Order.objects.get(user=request.user, status=0)
    except Order.DoesNotExist:
        order = Order.objects.create(user=request.user, status=0)

    if quantity > product.stock:
        messages.error(request, "Not enough stock")
    else:
        product.stock -= quantity
        product.save()
        # Check if item is already part of the order and increase
        try:
            print(order)
            order_item = OrderItem.objects.get(product=product, order=order)
            order_item.quantity += quantity
            order_item.save()
        except OrderItem.DoesNotExist:
            order_item = OrderItem.objects.create(product=product, quantity=quantity, order=order)
        messages.success(request, f"{product.name} ({quantity}) added to basket")

    return redirect("shop")
        

def product_detail(request, pk):
    queryset = Product.objects.all()
    product = get_object_or_404(queryset, id=pk)

    if request.method == "POST":
        try:
            add_to_basket(request, pk)
        except:
            messages.error(request, "Something went wrong, please try again.")

    try:
        specs = product.productspecs.specs
    except ProductSpecs.DoesNotExist:
        specs = {}

    edit_perm = request.user.has_perm('shop.change_product')
    add_perm = request.user.has_perm('shop.add_product')

    images = ProductImage.objects.filter(product=product)

    context = {
        "product": product, 
        "specs": specs,
        "edit_perm": edit_perm,
        "add_perm": add_perm,
        "images": images
    }

    return render(request, 'shop/product_detail.html', context)


@login_required
def update_basket(request):
    print("Updating basket")
    order_id = request.POST.get("order_item_id")
    input_quantity = int(request.POST.get("quantity"))
    order_item = OrderItem.objects.get(id=order_id)
    product = order_item.product

    diff = input_quantity - order_item.quantity
    # Check if quantity is the same as order_item quantity
    # if so, return to basket
    if (order_item.quantity == input_quantity):
            return

        # Check stock
    if input_quantity > product.stock:
            messages.error(request, f"Not enough stock, {product.stock} left")
            return redirect("basket")
        
        # Check if quantity is greater than order quantity, 
        # updates as necessary
    if diff > 0:
            messages.success(request, f"{product.name}, {diff} added to basket")
    if diff < 0:
            messages.success(request, f"{product.name}, {abs(diff) } removed from basket")
        
    product.stock -= diff
    order_item.quantity += diff
    product.save()
    order_item.save()

def remove_from_basket(request):
    order_item_id = request.POST.get("order_item_id")
    order_item = OrderItem.objects.get(id=order_item_id)
    product = order_item.product
    product.stock += order_item.quantity
    product.save()
    order_item.delete()
    messages.success(request, f"{product.name} removed from basket")
    return redirect("basket")

def basket_view(request):
    """
    This view handles the basket page. 
    It allows users to view the items in their basket,
    update the quantity of items in their basket,
    and remove items from their basket.
    """
    page = 'basket'
    if request.method == "POST":
        if request.POST.get("action") == "delete":
            remove_from_basket(request)
        else:
            update_basket(request)

    basket = OrderItem.objects.filter(Q(order__user=request.user), Q(order__status=0))
    print(len(basket))
    return render(
         request, 
         'shop/basket.html', 
        {
            "basket": basket, 
            "total": calculations.calculate_total(basket),
            'page': page
        })

@login_required
def checkout_view(request):
    address_id = request.GET.get('address')
    page = 'checkout'
    order = Order.objects.get(user=request.user, status=0)
    basket = OrderItem.objects.filter(order__user=request.user, order=order)
    addresses = Address.objects.filter(user=request.user).order_by('-default')
 

    if len(addresses) == 0:
        messages.error(request, f"There are no shipping addresses, please enter your address in you account settings")

    if order.DoesNotExist:
         redirect('shop')

    if request.method == "POST":
        if order.DoesNotExist:
            redirect('shop')
        try:
            if address_id:
                address = Address.objects.get(id=address_id)
            else:
                address = Address.objects.filter(user=request.user, default=True).first()

            # Update order status
            # CHANGE THIS TO 0 FOR DEBUG
            order.status = 0
            order.shipping = address
            order.save()
            
            # Redirect to confirmation page
            page = 'confirmation'

            
        except Address.DoesNotExist:
            # Handle case when address doesn't exist
            messages.error(request, "Selected address does not exist.")
        except Order.DoesNotExist:
            messages.error(request, "This order does not exist or is being processed.")

        except Exception as e:
            messages.error(request, f"There was an error: {str(e)}")

    return render(request, 'shop/checkout.html', {
        'basket': basket, 
        'total': calculations.calculate_total(basket),
        'page': page,
        'addresses': addresses,
        'order': basket,
        'shipping': address
    })

def save_specs_and_images(product, request):
    # Save product specs
    specs = {}
    keys = request.POST.getlist('key')
    values = request.POST.getlist('value')
    for key, value in zip(keys, values):
        specs[key] = value
    ProductSpecs.objects.update_or_create(product=product, defaults={'specs': specs})

    # Save product images
    images = request.FILES.getlist('images')
    for image in images:
        ProductImage.objects.create(product=product, image=image, alt=product)

@login_required
def add_product(request):
    page = "add"
    if request.method == 'POST':
        product_form = UpdateProductForm(request.POST, request.FILES)
        specs_form = ProductSpecsForm(request.POST)
        if product_form.is_valid():
            product = product_form.save()
            save_specs_and_images(product, request)
            return redirect('shop')  # Replace with your actual product list view
    else:
        product_form = UpdateProductForm()
        specs_form = ProductSpecsForm()
        image_form = ProductImageForm()

    return render(request, 'base/form.html', {
        'page': page,
        'form': product_form,
        'specs_form': specs_form,
        'image_form': image_form
    })

@login_required
def edit_product(request, pk):
    page = 'edit'
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        form = UpdateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            save_specs_and_images(product, request)
            messages.success(request, f'{product.name} was updated successfully.')
            return redirect('shop')
        else:
            messages.error(request, "There was an error with your form submission.")
    else:
        form = UpdateProductForm(instance=product)
        specs_form = ProductSpecsForm(initial={'specs': product.productspecs.specs if hasattr(product, 'productspecs') else {}})
        image_form = ProductImageForm()

    context = {
        'product': product,
        'page': page,
        'form': form,
        'specs_form': specs_form,
        'image_form': image_form,
        'heading': 'Edit Product'
    }
    return render(request, 'base/form.html', context)
@login_required
def edit_feature(request, pk):
        feature = Feature.objects.get(id=pk)
        if request.method == "POST":
            try:
                form = UpdateFeatureForm(request.POST, request.FILES, instance=feature)
                if form.is_valid():
                    form.save()
                    messages.success(request, f'{feature.title} was updated succesfully.')
                    return redirect('/')
            except Exception as e:
                messages.error(request, f"There was an error: {str(e)}")
        else:
            form = UpdateFeatureForm(instance=feature)

        context = {
            'feature': feature,
            'form': form
        }
        return render(request, 'base/form.html', context)

