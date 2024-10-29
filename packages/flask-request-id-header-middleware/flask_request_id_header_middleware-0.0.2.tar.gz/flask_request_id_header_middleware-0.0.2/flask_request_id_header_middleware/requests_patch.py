# import requests

# from .request_id import current_request_id

# # Monkey patching requests module
# original_request = requests.request
# def changed_request(method, url, **kwargs):
#     headers = kwargs.get('headers', None)
#     if headers is None:
#         headers = {}
#     headers["X-REQUEST-ID"] = current_request_id()
#     kwargs['headers'] = headers
#     return original_request(method, url, **kwargs)

# requests.request = changed_request