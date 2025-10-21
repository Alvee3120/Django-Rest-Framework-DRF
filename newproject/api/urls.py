# Function Based View

# from django.urls import path
# from .views import get_user,create_user,user_details

# urlpatterns = [
#     path('users/', get_user, name = 'get_user'),
#     path('users/create', create_user, name = 'create_user'),
#     path('users/<int:pk>', user_details, name = 'user_details')

# ]



# Class Based View

# from django.urls import path
# from .views import UserList, UserDetail

# urlpatterns = [
#     # List all users OR create a new user
#     path('users/', UserList.as_view(), name='user_list'),

#     # Retrieve, update, or delete a specific user
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
# ]

# Routers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users',UserViewSet, basename='user')

urlpatterns = [

    path('',include(router.urls)),
]
