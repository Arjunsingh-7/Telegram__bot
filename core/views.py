from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({'message': 'This is a public API. Anyone can access this.'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({'message': f'Hello {request.user.username}, you are authenticated!'})

