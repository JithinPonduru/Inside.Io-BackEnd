from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_3d_model_file(value):
    """Allow only .obj, .gltf, .glb file formats"""
    if not value or not value.name:
        raise ValidationError("Invalid file uploaded.")

    ext = os.path.splitext(value.name)[1].lower()
    allowed_extensions = ['.obj', '.gltf', '.glb']
    if ext not in allowed_extensions:
        raise ValidationError(f"Unsupported file format. Allowed formats: {', '.join(allowed_extensions)}")

class Model3D(models.Model):
    file = models.FileField(upload_to="models/", validators=[validate_3d_model_file])
    name = models.CharField(max_length=255, blank=True)
    format = models.CharField(max_length=10, blank=True)

    def save(self, *args, **kwargs):
        """Automatically set name and format before saving"""
        if self.file and self.file.name:
            self.name = os.path.basename(self.file.name)  # Extract filename
            self.format = os.path.splitext(self.file.name)[1][1:].lower()  # Extract file extension
        super().save(*args, **kwargs)

    @property
    def download_url(self):
        """Generate the full URL for file download"""
        return self.file.url if self.file else None

    def __str__(self):
        return self.name if self.name else "Unnamed Model"
