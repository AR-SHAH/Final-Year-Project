from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from mainApp.models import Product, ProductReview,Check
from Predictor import test


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id']


class ProductReviewSerializer(ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ['review', 'polarity', 'score']


class GroupedSerializer(ModelSerializer):

    reviews = ProductReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['product_id', 'reviews']


class CreateSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ProductReview
        fields = ['product', 'review']


class OnlyPolarityCheckSerializer(serializers.Serializer):
    review = serializers.CharField()
    polarity = serializers.CharField(read_only=True)
    score = serializers.CharField(read_only=True)

    def create(self,validated_data):
        
        print(validated_data['review'])
        score_tuple = test.score_calculator(validated_data['review'])
        validated_data['polarity'] = score_tuple[0]
        validated_data['score'] = score_tuple[1]

        xx = Check(review=validated_data['review'], polarity=validated_data['polarity'], score= validated_data['score'])
        xx.save()
    
        return validated_data

class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']

    def create(self,validated_data):
        user = User.objects.create(
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        username=validated_data['username'], 
        email = validated_data['email'],
        password=validated_data['password'],
        
        is_active=False,
         )
        return user
