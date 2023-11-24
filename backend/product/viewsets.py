from rest_framework import mixins,viewsets

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
        get,getdetail,put,patch,delete,post
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default


class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """
        get, getdetail
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default

