from django.urls import path
from .views import *


urlpatterns = [
    path('', mainpage, name='home'),
    path('route-glinka/', routes_1, name='route-glinka'),
    path('routes/', routes, name='routes'),
    path('route-smolensk/', routes_2, name='route-smolensk'),
    path('food/', food, name='food'),
    path('hotels/', hotels, name='hotels')
]