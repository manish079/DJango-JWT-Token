from django.urls import path
from screener.views import Aliens, ghost

urlpatterns = [
    path('aliens/', Aliens.as_view(), name='aliens-list'),
    path('ghost/', ghost, name='ghost'),
]