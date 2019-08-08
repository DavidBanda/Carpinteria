from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product
from django.views.generic import ListView, DetailView
from .forms import ProductCategoryList

# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'products/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Product'
    ordering = ['-date_posted']
    extra_context = {'title': 'Home', 'ProductFilter': Product.objects.all()[:3]}


def about(request):
    return render(request, 'products/about.html', {'title': '¿Quienes somos?'})

"""
def product_grid(request):
    context = {
        'title': 'Productos',
        'Product': Product.objects.all()
    }

    return render(request, 'products/product_grid.html', context)
"""


class ProductListView(ListView):

    model = Product
    template_name = 'products/product_grid.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Product'
    ordering = ['-date_posted']
    extra_context = {'title': 'Productos', 'category': 'Todo'}
    paginate_by = 4

    def post(self, request):
        category = request.POST['drop']
        # print(category)
        if category != 'Todo':
            categoryProd = self.get_queryset().filter(category=category)
            return render(request, 'products/product_grid.html', {
                'title': category,
                'Product': categoryProd,
                'category': category
            })
        else:
            return render(request, 'products/product_grid.html', {
                'title': 'Productos',
                'Product': Product.objects.all(),
                'category': category
            })


class productSingle(DetailView):
    model = Product
    template_name = 'products/product-single.html'
