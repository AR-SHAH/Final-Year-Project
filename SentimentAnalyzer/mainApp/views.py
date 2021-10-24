from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from mainApp.models import ProductReview, Product, Check
from mainApp.serializers import ProductSerializer, GroupedSerializer, CreateSerializer, UserSerializer
from mainApp.serializers import OnlyPolarityCheckSerializer
from Predictor import test


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

        