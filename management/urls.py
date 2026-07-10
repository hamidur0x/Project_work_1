from django.urls import path
from . import views


urlpatterns = [

    path(
        "sale/new/",
        views.create_sale,
        name="create_sale"
    ),

]