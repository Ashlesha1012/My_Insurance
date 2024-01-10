# middleware.py

class RequestResponseLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before the view (if needed)
        # For example, logging information about the request
        self.log_request_info(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after the view (if needed)
        # For example, logging information about the response
        self.log_response_info(response)

        return response

    def log_request_info(self, request):
        # Logging request information
        print(f"Request path: {request.path}")
        print(f"Request method: {request.method}")
        # You can add more information to log here

    def log_response_info(self, response):
        # Logging response information
        print(f"Response status code: {response.status_code}")
        # You can add more information to log here
