from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_3d_model_file(value):
    """Allow only .obj, .gltf, .glb file formats"""
    ext = os.path.splitext(value.name)[1].lower()
    allowed_extensions = ['.obj', '.gltf', '.glb']
    if ext not in allowed_extensions:
        raise ValidationError(f"Unsupported file format. Allowed formats: {', '.join(allowed_extensions)}")

class Model3D(models.Model):
    file = models.FileField(upload_to="models/", validators=[validate_3d_model_file])

    def __str__(self):
        return self.name
