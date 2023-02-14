from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_view', views.login_view, name='login_view'),
    path('register', views.register, name='register'),
    path('new', views.new, name='new'),
    path('police', views.police, name='police'),
    path('view_compl/<int:id>/', views.view_compl,name='view_compl'),
    path('view_user/<int:id>/', views.view_user,name='view_user'),
    path('update_compl/<int:id>/', views.update_compl, name='update_compl'),
    path('update_user/<int:id>/', views.update_user, name='update_user'),
    path('complainant', views.complainant_view, name='complainant'),
    path('user', views.user_view, name='user'),
    path('complainant_last_page', views.complainant_last_page, name='complainant_last_page'),
    path('last_user_page', views.last_user_page, name='last_user_page'),
    path('search/<int:id>', views.search, name='search'),
    path('success', views.success, name='success'),
    path('search_child/<int:id>', views.search_child, name='search_child'),
    # path('image/<str:image_url>/', views.image_details, name='image_details'),
    path('image_details', views.image_details, name='image_details'),
]
