from ninja import Schema


class User_Info(Schema):
    email: str


class Display_Product(Schema):
    name: str
    price: str
    image: str
    description: str


class add_Fav(Schema):
    product_id: int


class Display_favorite(Schema):
    # user : User_Info
    product : Display_Product


class Profilee(Schema):
    name:str
    user: User_Info
    phone_number: str
    city: str


class add_to_cart(Schema):
    product_id: int



class display_cart(Schema):
    product: Display_Product


class remove_prod(Schema):
    favorite_id: int


class remove_prod_cart(Schema):
    cart_id: int



class Display_Order(Schema):
    user : User_Info
    product : Display_Product