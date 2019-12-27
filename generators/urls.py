from django.urls import path
from . import views  # , include

urlpatterns = [
    # path('', views.index, name='index'),
    path('at_random/', views.at_random, name='at_random'),
    path('at_random/<int:generator_number>',
         views.at_random, name='at_random_with_number')
]
