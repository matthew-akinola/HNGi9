from .serializer import ProfileSerializer
from .models import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

username= "Akinola Matthew"
age=27
bio= "I am a proficient backend developer, I have interest in building highly scalable database(s)"



@api_view(["GET"])
def get_profile(request):
    # Profile.objects.create(username=username,age=age,bio=bio)

    #returned the first object created
    profile = Profile.objects.all().first() 
    profile_get = ProfileSerializer(profile)
    return Response(profile_get.data, status=status.HTTP_200_OK)

