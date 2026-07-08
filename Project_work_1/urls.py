from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from management.views import create_sale
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("sales/new/", create_sale, name="create_sale"),
    path("reports/", views.report_view, name="reports")
]
    
