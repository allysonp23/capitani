from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .kafka import send_to_kafka

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        product = serializer.save()
        data = ProductSerializer(product).data
        send_to_kafka('produtos-persistidos', data)
