from django.shortcuts import render
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_details(request):
    print(request.user)
    if request.user.is_authenticated:
        # The user is authenticated, and you can access their attributes
        user_pk = request.user.pk
        username = request.user.username
        email = request.user.email

        user_details = {
            'user_pk': user_pk,
            'username': username,
            'email': email,
        }

        return JsonResponse(user_details)
    else:
        # Handle the case when the user is not authenticated
        return JsonResponse({'message': 'Ubd'}, status=401)