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

    @action(detail=False, methods=['get'])
    def generate_report(self, request):
        """
        Reads all stored files in the database and returns a report.
        """
        models = Model3D.objects.all()
        report_data = [
            {
                "id": model.id,
                "file_path": model.file.url if model.file else "No file",
                "uploaded_at": model.uploaded_at.strftime("%Y-%m-%d %H:%M:%S") if model.uploaded_at else "Unknown"
            }
            for model in models
        ]

        return Response({"report": report_data})
