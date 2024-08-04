import re
from django.http import JsonResponse

class RoleCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user_role = "default" 
        
        role_based_access = {
            'admin': [r'^/screener/.*', r'^/admin/.*'],
            'screener': [r'^/screener/.*'],
            'default' : [r'^/default/.*']
        }

        current_path = request.path_info
        print(f"Current path: {current_path}")

        allowed_paths = role_based_access.get(request.user_role, [])
        print(f"Allowed paths for role '{request.user_role}': {allowed_paths}")

        has_access = any(re.match(pattern, current_path) for pattern in allowed_paths)

        if not has_access:
            print("Access Denied")
            return JsonResponse({"message": "Forbidden"}, status=403)

        response = self.get_response(request)
        return response
