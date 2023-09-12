from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from portifolio.models import Credits

from products.forms import BuyProductForm, ProductForm
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

# from boutique ado


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.objects.get(id=self.kwargs.get("pk"))
        context['product'] = product
        return context


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def buy_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    credits = get_object_or_404(Credits, user=request.user.id)

    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            price = product.price
            quantity = form.cleaned_data['quantity']

            if (quantity * price <= credits.amount) and\
                    (product.quantity >= quantity):
                product.quantity -= quantity
                product.save()
                total_cost = quantity * price
                credits.amount -= total_cost
                credits.save()

                return redirect('success')
    else:
        form = BuyProductForm()

    return render(request, 'products/buy_product.html',
                  {'form': form, 'product': product})


def success(request):
    credits = get_object_or_404(Credits, user=request.user.id)
    return render(request, 'products/success.html', {'credits': credits, })
