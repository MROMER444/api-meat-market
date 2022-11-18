from ninja import NinjaAPI
from typing import List
from meat_shop.schema import Display_Product
from meat_shop.schema import add_Fav
from meat_shop.schema import User_Info
from meat_shop.schema import Profilee
from meat_shop.schema import add_to_cart
from meat_shop.schema import Display_Order
from meat_shop.schema import display_cart
from meat_shop.models import Cart
from meat_shop.schema import remove_prod
from meat_shop.schema import remove_prod_cart
from meat_shop.models import Cart
from meat_shop.models import Order
from meat_shop.schema import Display_favorite
from meat_shop.models import Product
from meat_shop.models import Favorite
from meat_shop.models import Profile as pr
from ninja import Router
from django.contrib.auth import get_user_model
from restauth.authotization import AuthBearer
from django.shortcuts import get_object_or_404
from restauth.models import EmailAccount



api = NinjaAPI()
meat_shop = Router()

User = get_user_model()


@meat_shop.get("Display_Product", response=List[Display_Product])
def Display_All_Product(request):
    product = Product.objects.all()
    return product



@meat_shop.post("make_fav" , response=add_Fav , auth=AuthBearer())
def create_fav(request , payload:add_Fav):
    user = get_object_or_404(User, email= request.auth['email'])
    favorite = Favorite.objects.create(
        user = user,
        product_id = payload.product_id,
        )

    favorite.save()
    return favorite


@meat_shop.get("display_the_favorite_from_the_current_account" , response=List[Display_favorite] , auth=AuthBearer())
def Display_favorite_from_current_acc(request):
    user = get_object_or_404(User, email= request.auth['email'])
    fav = Favorite.objects.filter(user = user)
    return fav



@meat_shop.get("display_account" , response=List[Profilee] , auth=AuthBearer())
def display_account(request):
    user = get_object_or_404(User, email= request.auth['email'])
    profile = pr.objects.filter(user = user)
    return profile



@meat_shop.post("add_product_to_cart" , response=add_to_cart, auth=AuthBearer())
def add_prod_to_cart(request , payload: add_to_cart):
    user = get_object_or_404(User, email= request.auth['email'])
    cart = Cart.objects.create(
        user = user,
        product_id = payload.product_id,
        )

    cart.save()
    return cart



@meat_shop.get("display_the_cart_from_the_current_account" , response=List[display_cart] , auth=AuthBearer())
def Display_cart_from_current_acc(request):
    user = get_object_or_404(User, email= request.auth['email'])
    cart = Cart.objects.filter(user = user)
    return cart



@meat_shop.delete("remove_fav" ,response= remove_prod,auth=AuthBearer())
def remove_fav(request , payload:remove_prod):
    user = get_object_or_404(User, email= request.auth['email'])
    try:
        favorite = Favorite.objects.get(id = payload.favorite_id)
        favorite.delete()
        return favorite

    finally:
        if not favorite:
            raise Http404(f'this prod doesnt exist')




@meat_shop.delete("remove_cart" ,response= remove_prod_cart,auth=AuthBearer())
def remove_cart(request , payload:remove_prod_cart):
    user = get_object_or_404(User, email= request.auth['email'])
    try:
        cart = Cart.objects.get(id = payload.cart_id)
        cart.delete()
        return cart

    finally:
        if not cart:
            raise Http404(f'this prod doesnt exist')




@meat_shop.get("display_the_Order_from_the_current_account" , response=List[Display_Order] , auth=AuthBearer())
def Display_Order_from_current_acc(request):
    user = get_object_or_404(User, email= request.auth['email'])
    order = Order.objects.filter(user = user)
    return order