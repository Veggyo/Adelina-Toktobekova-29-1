from django.shortcuts import render, redirect
from posts.models import Product, Categories
from posts.forms import ProductCreateForm, CategoryCreateForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from posts.constans import PAGINATION_LIMIT
from django.views.generic import ListView, View, CreateView, DetailView


class MainPageCBV(ListView):
    model = Product
    template_name = 'layouts/main.html'


class ProductsCBV(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, *args, **kwargs):
        products = self.model.objects.all()
        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        if search_text:
            """startswith, endswith, contain"""
            products = products.filter(Q(title__contains=search_text) | Q(description__contains=search_text))

        context_data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context_data)


class CategoriesCBV(ListView):
    model = Product
    template_name = 'products/categories.html'

    def get(self, request, *args, **kwargs):
        categories = self.model.objects.all
        context_data = {
            'categories': categories
        }
        return render(request, self.template_name, context=context_data)


class ProductDetailCBV(DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            products = self.model.objects.get(id=pk)
        except Product.DoesNotExist:
            return render(request, self.template_name)
        context_data = {
            'product': products
        }

        return render(request, self.template_name, context=context_data)


class ProductCreateCBV(ListView):
    model = Product
    template_name = 'products/create.html'

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            context_data = {
                'form': ProductCreateForm
            }
            return render(request, self.template_name, context=context_data)

        if request.method == 'POST':
            data, file = request.POST, request.FILES
            form = ProductCreateForm(data, file)

            if form.is_valid():
                Product.objects.create(
                    image=form.cleaned_data.get('image'),
                    title=form.cleaned_data.get('title'),
                    description=form.cleaned_data.get('description'),
                    price=form.cleaned_data.get('price'),
                    categories=form.cleaned_data.get('categories')
                )
                return redirect('/products/')

            return render(request, 'products/create.html', context={
                'form': form
            })


@method_decorator(login_required(login_url='/categories/'), name='dispatch')
class CategoriesCreateCBV(ListView):
    model = Product
    template_name = 'products/categories.create.html'
    form_class = CategoryCreateForm
    success_url = '/categories/'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': self.form_class if not kwargs.get('form') else kwargs['form']
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, **kwargs):
        data = request.POST
        form = CategoryCreateForm(data)

        if form.is_valid():
            Categories.objects.create(
                title=form.cleaned_data.get('categories'),
            )
            return redirect('/categories/')

        return render(request, self.template_name, context=self.get_context_data(
            form=form
        ))
