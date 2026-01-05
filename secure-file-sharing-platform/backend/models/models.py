from django.db import models

class FileMetadata(models.Model):
    filename = models.CharField(max_length=255)
    encrypted_path = models.CharField(max_length=255)
    encrypted_key = models.BinaryField()
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True)
    revoked = models.BooleanField(default=False)
