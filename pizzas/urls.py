from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    #main page
    path('', views.index, name='index'),
    path('pizza1',views.pizza1, name='pizza1'),
    path('pizza1/<int:pizza2_id>/', views.pizza2, name='pizza2'),
    path('new_comment/<int:pizza2_id>/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment')
]