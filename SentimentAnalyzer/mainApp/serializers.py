from django.contrib.auth.models import User
from django.db.models import manager
from rest_framework import fields, serializers
from rest_framework.serializers import ModelSerializer
from mainApp.models import Product, ProductReview, Check
from Predictor import test
from rest_framework import permissions
from rest_framework_simplejwt.tokens import SlidingToken
from django.contrib.auth.models import Group, UserManager
from django.contrib.auth import authenticate


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

    def create(self, validated_data):

        print(validated_data['review'])
        score_tuple = test.score_calculator(validated_data['review'])
        validated_data['polarity'] = score_tuple[0]
        validated_data['score'] = score_tuple[1]

        xx = Check(review=validated_data['review'],
                   polarity=validated_data['polarity'], score=validated_data['score'])
        xx.save()

        return validated_data


class UserSerializer(serializers.ModelSerializer):
   # jwt = serializers.SerializerMethodField(read_only=True)
    group = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'password', 'group']

    # def get_jwt(self, obj):
     #   return str(SlidingToken.for_user(obj))

    # Action if existing
    def create(self, validated_data):
        user = User(
            # first_name=validated_data.get('first_name'),
            # last_name=validated_data.get('last_name'),
            username=validated_data['username'],
            # email = validated_data.get('email'),
        )
        user.set_password(validated_data['password']),
        user.save()
        g = Group.objects.get(name='Inactive')
        g.user_set.add(user)
        return user

    def check(self, validated_data):
        user = User.objects.filter(username=validated_data['username'])
        if user.groups.filter(name='Inactive').exists():
            print('it is inactive')


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    group = serializers.ReadOnlyField()

    def checkGroup(request, validated_data):
        if User.objects.get(username=validated_data['username']):
            user = User.objects.get(username=validated_data['username'])
        else:
            return
        x = user.groups.all()
        print('Gtop'+str(x[0]))
        if str(x[0]) == 'Inactive':
            x = 'Inactive'
        else:
            x = 'None'
        return x


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ['name']


class UserGroupSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'email', 'password', 'groups']


class UserGetSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = fields.ReadOnlyField()
    last_name = fields.ReadOnlyField()
    email = fields.ReadOnlyField()
    groups = GroupedSerializer(many= True, read_only=True)

    def to_representation(self, instance):
            user = User.objects.get(username=instance['username'])
            instance['first_name']=user.first_name
            instance['last_name']=user.last_name
            instance['email']=user.email
            x= user.groups.all()
            
            if x.exists():
                if str(x[0])=='Inactive':
                    instance['groups']='Inactive'    
                elif str(x[0])=='Active':
                    instance['groups']='Active'   
            else:
                instance['groups']='Null'
            return(instance)