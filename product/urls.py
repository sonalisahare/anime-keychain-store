from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('shop/', views.shop, name='shop'),
    path('new-arrivals/', views.new_arrivals, name='new_arrivals'),
    path('best-sellers/', views.best_sellers, name='best_sellers'),

    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),

    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('increase/<int:id>/', views.increase_quantity, name='increase'),
    path('decrease/<int:id>/', views.decrease_quantity, name='decrease'),
    path('remove-from-cart/<int:id>/', views.remove_from_cart, name='remove_from_cart'),

    path('buy/', views.buy, name='buy'),

    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('track-order/', views.track_order, name='track_order'),
    path('help/', views.help_page, name='help'),
]