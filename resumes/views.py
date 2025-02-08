from rest_framework import status, views
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response


class RegisterUserView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

class LoginUserView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class LogoutUserView(views.APIView):
    def post(self, request):
        response = Response({'message': 'Logged out successfully'})
        response.delete_cookie('access_token')
        return response





# This is where you define the logic of your views
from rest_framework.views import APIView


class RegisterUserView(APIView):
    def post(self, request):
        # Logic for user registration (this is just an example)
        return Response({"message": "User registered successfully!"})

class LoginUserView(APIView):
    def post(self, request):
        # Logic for user login (this is just an example)
        return Response({"message": "User logged in successfully!"})

class LogoutUserView(APIView):
    def post(self, request):
        # Logic for user logout (this is just an example)
        return Response({"message": "User logged out successfully!"})



from rest_framework import generics
from .models import Resume, Template
from .serializers import ResumeSerializer, TemplateSerializer

# View to create or update a Resume
class ResumeCreateUpdateView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

# View to list and create Templates
class TemplateListView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer



from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse

def generate_pdf(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    html = render_to_string('resume_template.html', {'resume': resume})
    pdf = HTML(string=html).write_pdf()
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="resume_{resume_id}.pdf"'
    return response

