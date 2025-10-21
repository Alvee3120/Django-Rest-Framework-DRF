# Function Based View

    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status
    # from .models import DB_USER
    # from .serializer import UserSerializer

    # @api_view(['GET'])
    # def get_user(request):
    #     users = DB_USER.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)

    # @api_view(['POST'])
    # def create_user(request):
    #     serializer = UserSerializer(data= request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data , status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET','PUT','DELETE'])
    # def user_details(request,pk):
    #     try:
    #         user = DB_USER.objects.get(pk=pk)
    #     except DB_USER.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    #     if request.method == 'GET':
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data)

    #     elif request.method == 'PUT':
    #         serializer = UserSerializer(user, data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #     elif request.method == 'DELETE':
    #         user.delete()
    #         return Response(status = status.HTTP_204_NO_CONTENT)

 

# Class Based View 

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.http import Http404
# from .models import DB_USER
# from .serializer import UserSerializer


# class UserList(APIView):
#     """
#     List all users, or create a new user.
#     """

#     def get(self, request, format=None):
#         users = DB_USER.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserDetail(APIView):
#     """
#     Retrieve, update or delete a user instance.
#     """

#     def get_object(self, pk):
#         try:
#             return DB_USER.objects.get(pk=pk)
#         except DB_USER.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Generic Class Based View

# from rest_framework import generics
# from .models import DB_USER
# from .serializer import UserSerializer


# class UserList(generics.ListCreateAPIView):
#     """List all users, or create a new user."""
#     queryset = DB_USER.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     """ Retrieve, update, or delete a user instance."""
#     queryset = DB_USER.objects.all()
#     serializer_class = UserSerializer


# Viewset 

from rest_framework import viewsets
from .models import DB_USER
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = DB_USER.objects.all()
    serializer_class = UserSerializer
    