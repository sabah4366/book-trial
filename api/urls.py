from django.contrib import admin
from django.urls import path,include
from .views import BookViewSet,UserViewSet
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

book__list=BookViewSet.as_view({
    'get':'list',
    'post':'create'
})

book_detail=BookViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})
user_list=UserViewSet.as_view({
    'get':'list'
})
user_detail=UserViewSet.as_view({
    'get':'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('books/',book__list,name='book-list'),
    path('book/<int:pk>/',book_detail ,name='book-detail'),
    path('users/',user_list,name='user-list'),
    path('users/<int:pk>/',user_detail,name='user-detail')
])
# Create a router and register our viewsets with it.
router=DefaultRouter()
router.register(r'books',views.BookViewSet ,basename='book')
router.register(r'users',views.UserViewSet , basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns=[
    path('',include(router.urls)),
]