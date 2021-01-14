from django.urls import path, re_path

from App import views
app_name = 'App'
urlpatterns = {
    path('', views.index, name='index'),
    path('show/<name>/<int:age>/', views.show, name='show'),
    re_path(r'^call/(\d{4}-\d{8})/$', views.call, name='call'),
    path('req/', views.req, name='req'),
}
