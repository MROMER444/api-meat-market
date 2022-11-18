from django.contrib import admin
from django.urls import path
# from meat_shop.api import api
from ninja import NinjaAPI

from meat_shop.api import meat_shop
from restauth.api import auth_router

api = NinjaAPI(
    title='MEAT SHOP App',
    version='0.1',
    description='A BackEnd to offer an APIs to a meat shop application',
    # csrf=True,
)

api.add_router('/auth' , auth_router)

api.add_router('/endpoints', meat_shop)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
