from django.core.management.base import BaseCommand
from mainApp.models import Product, ProductReview
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):
        comments_file = pd.read_excel('Predictor/dataset.xlsx', header=0)
        for index, row in comments_file.iterrows():
            p, _ = Product.objects.get_or_create(product_id=row[0])
            r = ProductReview(
                product=p,
                review=str(row[1]),
                polarity=str(row[2]),
                score=int(row[3])
            )
            r.save()
