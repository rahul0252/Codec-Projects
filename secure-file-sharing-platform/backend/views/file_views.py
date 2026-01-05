from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FileUploadView(APIView):
    def post(self, request):
        return Response({"message": "Encrypted file upload endpoint"}, status=status.HTTP_200_OK)

class FileDownloadView(APIView):
    def get(self, request, file_id):
        return Response({"message": "Encrypted file download endpoint"}, status=status.HTTP_200_OK)
