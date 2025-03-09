from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Model3D
from .serializers import Model3DSerializer

class Model3DViewSet(ModelViewSet):
    """
    API ViewSet for handling 3D models.
    """
    queryset = Model3D.objects.all()
    serializer_class = Model3DSerializer  

    def get_serializer_context(self):
        """
        Passes the request context to the serializer for absolute URLs.
        """
        return {"request": self.request}

    @action(detail=False, methods=['get'])
    def generate_report(self, request):
        """
        Reads all stored files in the database and returns a report.
        """
        models = Model3D.objects.all()
        serializer = self.get_serializer(models, many=True)

        return Response({"report": serializer.data})
