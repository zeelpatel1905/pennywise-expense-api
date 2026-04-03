from rest_framework import serializers
from .models import Category, Expense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    # This adds a "url" field to every JSON object automatically
    category_name = serializers.StringRelatedField(source='category', read_only=True)

    class Meta:
        model = Expense
        fields = ['url', 'id', 'title', 'amount', 'date', 'category', 'category_name']