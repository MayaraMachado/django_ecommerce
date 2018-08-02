from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns =[
    path('', views.CartItemView.as_view(), name="carrinho" ),
    path('adicionar/<str:slug>', views.CreateCartItemView.as_view(), name='create_cartitem'),
    path('finalizar-compra', views.CheckoutView.as_view(), name='finalizar'),
    path('confirmar-endereco', views.RedirectCheckoutView.as_view(), name='confirmar_endereco'),
    path('meus-pedidos/<int:pk>', views.OrderDetailView.as_view(), name="pedido_detail"),
]