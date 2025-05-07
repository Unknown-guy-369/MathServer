from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lamp-power/', views.lamp_power, name="lamp_power"),
    path('', views.lamp_power, name="lamp_power_root")
]