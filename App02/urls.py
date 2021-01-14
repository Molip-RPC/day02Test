from django.urls import path

from App02 import views

app_name = 'App02'
urlpatterns = [
    path('', views.index, name='index'),
    path('example/', views.handle_example, name='example'),
    path('render/', views.load_template, name='render'),
    path('var/', views.handle_var, name='var'),
    path('filter/', views.handle_filter, name='filter')
]
