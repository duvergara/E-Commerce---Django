from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from  django.views import View
from . import  models
from django.http import HttpResponse


from django.http import HttpResponse
# Create your views here.
class  ListaProduto(ListView):
  model = models.Produto
  template_name = 'produto/lista.html'
  context_object_name = 'produtos'
  paginate_by =  3

class  AdicionarAoCarrinho(View):
    def get ( self , *args , **kwargs ) :
        return HttpResponse ( 'criar' )
class  RemoverDoCarrinho(View):
    def get ( self , *args , **kwargs ) :
        return HttpResponse ( 'criar' )
class  DetalheProduto(DetailView):
    model = models.Produto
    template_name = 'produto/detalhe.html'
    context_object_name = 'produto'
    slug_url_kwarg = 'slug'

class  Carrinho(View):
    def get ( self , *args , **kwargs ) :
        return HttpResponse ( 'criar' )
class  Finalizar(View):
    def get ( self , *args , **kwargs ) :
        return HttpResponse ( 'criar' )