from sqladmin import Admin, ModelView
from app.models.user import User
# from app.models.product import Product


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.user_type]
    column_searchable_list = [User.email]
    icon = "fa-solid fa-user"
    category = "Accounts"

# class ProductAdmin(ModelView, model=Product):
#     column_list = [Product.id, Product.name, Product.price, Product.ai_status]
#     column_filters = [Product.category, Product.ai_status]
#     icon = "fa-solid fa-cart-shopping"
#     category = "E-commerce"


def setup_admin(app, engine):
    admin = Admin(app, engine, title="CoGym Admin Panel")
    admin.add_view(UserAdmin)
    # admin.add_view(ProductAdmin)