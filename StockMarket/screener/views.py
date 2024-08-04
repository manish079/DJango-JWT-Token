from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

HARD_CODED_USERS = [
    {"id": 1, "username": "user1", "email": "user1@example.com"},
    {"id": 2, "username": "user2", "email": "user2@example.com"},
    {"id": 3, "username": "user3", "email": "user3@example.com"},
]

class Aliens(generics.ListAPIView):
    def get_queryset(self):
        return HARD_CODED_USERS

    def list(self, request, *args, **kwargs):
        user = HARD_CODED_USERS[0]
        return Response({"message": "Hello, World!", "user": user})

@api_view(['GET'])
def ghost(request):
    return Response({"message": "Hello, World! I am Ghost!", "userId": HARD_CODED_USERS[0]["id"], "userEmail": HARD_CODED_USERS[0]["email"]})
