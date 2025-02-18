from django.http import HttpResponse
from constance import config

class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if config.maintenance_mode and not request.path.startswith("/admin/"):
            return HttpResponse("The system is currently under maintenance, Please try again later.", status=503)

        response = self.get_response(request)
        return response