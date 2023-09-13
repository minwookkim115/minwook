from django.urls import path
from . import views


app_name = 'myapp'
urlpatterns = [
    path('myapp/', views.index, name="index"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('login/', views.login, name="login"),
    
    path('hello/<name>/', views.hello),
    # path('hello/<int:age>', views.hello2)
]
