# HTTP Status Code Example

def http_status_code(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 405:
            return "Method Not Allowed"
        case _:
            return "Unexpected Error"

print(http_status_code(200))
print(http_status_code(404))
print(http_status_code(405))
print(http_status_code(500))