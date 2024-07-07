from django.urls import path
from Login import views
from .views import RegisterView, LoginView, ProtectedView, AllUsersView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path('users/', AllUsersView.as_view(), name='all-users'),
]