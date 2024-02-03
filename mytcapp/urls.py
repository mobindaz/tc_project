# mytcapp/urls.py
from django.urls import path
from .views import home, signup ,  CustomLoginView , logout_view , profile

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/profile/', profile, name='profile'),
]
