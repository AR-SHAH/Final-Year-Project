from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import PositiveSmallIntegerField
from django.db.models.signals import post_save
from Predictor import test


class Product(models.Model):
    product_id = models.CharField(max_length=50, db_index=True)


class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, on_delete=CASCADE, related_name="reviews")
    review = models.CharField(max_length=8000)
    polarity = models.CharField(max_length=10, null=True)
    score = PositiveSmallIntegerField(blank=True, null=True)


class Check(models.Model):
    review = models.CharField(max_length=8000)
    polarity = models.CharField(max_length=10, null=True)
    score = PositiveSmallIntegerField(blank=True, null=True)
    
def check_post_save(instance, *args, **kwargs):

    if instance.score is None:
        score_tuple = test.score_calculator(instance.review)
        instance.score = score_tuple[1]
        instance.polarity = score_tuple[0]
        instance.save()


post_save.connect(check_post_save, sender=ProductReview)
