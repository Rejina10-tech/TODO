from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from rest_framework import serializers

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                send_mail(
                    'Password Reset Request',
                    'Click the link to reset your password: /reset-link',
                    'webmaster@localhost',
                    [email],
                    fail_silently=False,
                )
                return Response({"message": "Password reset email sent."})
            except User.DoesNotExist:
                return Response({"error": "User with this email does not exist."}, status=400)
        return Response(serializer.errors, status=400)




class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField()

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if serializer.is_valid():
            token = serializer.validated_data['token']
            new_password = serializer.validated_data['new_password']

            try:
                user = User.objects.get(reset_token=token)
                if default_token_generator.check_token(user, token):
                    user.set_password(new_password)
                    user.save()
                    return Response({"message": "Password has been reset."})
                else:
                    return Response({"error": "Invalid token."}, status=400)
            except User.DoesNotExist:
                return Response({"error": "Invalid token."}, status=400)

        return Response(serializer.errors, status=400)
