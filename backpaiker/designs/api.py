from designs.models import Design
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from .serializers import DesignSerializer

# Design Viewset
class DesignViewSet(viewsets.ModelViewSet):
    queryset = Design.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DesignSerializer

    @action(detail=False, methods=["post"])
    def upload_design(self, request, pk=None):
        try:
            print(type(request.data))
            print(request.data)
            file = request.data["file"]
        except KeyError:
            raise ParseError("Request has no resource file")
