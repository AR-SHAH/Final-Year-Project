from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import generics, request, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from mainApp.models import ProductReview, Product, Check
from mainApp.serializers import ProductSerializer, GroupedSerializer, CreateSerializer, UserSerializer,UserLoginSerializer, GroupSerializer,UserGroupSerializer, UserGetSerializer
from mainApp.serializers import OnlyPolarityCheckSerializer
from Predictor import test
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

class DetailView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serailizer = GroupedSerializer(product, many=True)
        return Response(serailizer.data)

    def post(self, request):
        p= Product.objects.get(product_id=request.POST['product'])
        r = ProductReview(
                product=p,
                review=request.POST['review'],
                 )
        r.save()

        return Response(None)
    
   
    # permission_classes = [permissions.IsAuthenticated]
    

class CreateView(generics.CreateAPIView):

    queryset = ProductReview.objects.all()
    serializer_class = CreateSerializer


class PolarityCheckView(APIView):

    def post(self, request):
        serializer = OnlyPolarityCheckSerializer(
            data=request.data)
        print(request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    def get(self, request):
        ch = Check.objects.last()
        serializer = OnlyPolarityCheckSerializer(ch)
        return Response(serializer.data)
    
class UserView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class Usercheck(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        print(request.POST.get('username'))
        return Response(serializer.data)        

class LoginView(APIView):

    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.data['group']=serializer.checkGroup(request.data)
        print(request.data['group'])
        return Response(serializer.data)

class testView(APIView):
  
  def get(self, request):
        product = User.objects.all()
        serailizer = UserGroupSerializer(product, many=True)
        return Response(serailizer.data)
 
  def post(self, request):

        print(request.data)
        product = User.objects.get(username=request.data['username'])
        serailizer = UserGroupSerializer(product, many=True)
        return Response(None)

class getUserView(APIView):
       def post(self, request):
        serializer = UserGetSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        print(request.user)
        return Response (serializer.data)     