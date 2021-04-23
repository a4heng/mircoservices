from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):
    # /api/products
    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):  # /api/products/<str:id>
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
