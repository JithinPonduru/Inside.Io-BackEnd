from rest_framework import serializers
from .models import Model3D

class Model3DSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    format = serializers.SerializerMethodField()
    downloadUrl = serializers.SerializerMethodField()

    class Meta:
        model = Model3D
        fields = ["id", "file", "name", "format", "downloadUrl"]

    def validate_file(self, value):
        """Ensure only valid 3D model formats are uploaded."""
        ext = value.name.split('.')[-1].lower()
        if ext not in ['obj', 'gltf', 'glb']:
            raise serializers.ValidationError("Only .obj, .gltf, and .glb files are allowed.")
        return value

    def get_name(self, obj):
        """Extracts and returns the original filename."""
        return obj.file.name.split("/")[-1] if obj.file else "No file"

    def get_format(self, obj):
        """Extracts and returns the file format."""
        return obj.file.name.split(".")[-1] if obj.file else "Unknown"

    def get_downloadUrl(self, obj):
        """Generates and returns the file download URL."""
        request = self.context.get("request")
        return request.build_absolute_uri(obj.file.url) if obj.file and request else "No file"
