from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from entries import get_all_entries, get_single_entry


# Here's a class. It inherits from another class.
class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was from
        # '/animals' or '/animals/2'
        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"
            
                    
        # Response from parse_url() is a tuple with 3
        # items in it, which means the request was for 
        # '/resource?parameter=value'
        # elif len(parsed) == 3:
        #     ( resource, key, value ) = parsed

        #     # Is the resource 'customers' and was there a 
        #     # query parameter that specified the customer
        #     # email as a filtering value?
        #     if key == "email" and resource == "customers":
        #         response = get_customers_by_email(value)
        #     elif key == "location_id" and resource == "animals":
        #         response = get_animal_by_location(value)
        #     elif key == "location_id" and resource == "employees":
        #         response = get_employee_by_location(value)
        #     elif key == "status" and resource == "animals":
        #         response = get_animals_by_status(value)
        
        self.wfile.write(response.encode())

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:
            # GIVEN: /customers?email=jenna@solis.com

            param = resource.split("?")[1]  # email=jenna@solis.com
            resource = resource.split("?")[0]  # 'customers'
            pair = param.split("=")  # [ 'email', 'jenna@solis.com' ]
            key = pair[0]  # 'email'
            value = pair[1]  # 'jenna@solis.com'

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: /animals
            except ValueError:
                pass  # Request had trailing slash: /animals/

            return (resource, id)

# This function is not inside the class. It is the starting
# point of this application.
def main(): 
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()
