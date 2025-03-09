from rest_framework import serializers
from .models import Model3D

class Model3DSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3D
        fields = "__all__"

    def validate_file(self, value):
        """Ensure only valid 3D model formats are uploaded."""
        ext = value.name.split('.')[-1].lower()
        if ext not in ['obj', 'gltf', 'glb']:
            raise serializers.ValidationError("Only .obj, .gltf, and .glb files are allowed.")
        return value
