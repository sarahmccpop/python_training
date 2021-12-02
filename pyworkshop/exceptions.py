# It is common practice to put a lot of your custom exceptions in an exceptions module

# this inherits from Exception
class GitHubApiError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit reached"
        else:
            message = f"The status code was: {status_code}"
        super().__init__(message)
