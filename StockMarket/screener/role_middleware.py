from django.http import JsonResponse

class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Retrieve the user role from the request headers or session
        # request.user_role = request.headers.get('User-Role', None)
        request.user_role = "screener";
        
        # List of endpoints that require the 'Read' role
        protected_paths = ['/ghost/', '/aliens/']
        
        if request.user_role != 'screener':
            return JsonResponse({"message": "Forbidden"}, status=403)
        
        response = self.get_response(request)
        return response

