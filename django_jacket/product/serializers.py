from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=(
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            # "id",
            # "category",
            # "name",
            # "slug",
            # "description",
            # "price",
            # "image",
            # "thumbnail",
            # "date_added",
        )