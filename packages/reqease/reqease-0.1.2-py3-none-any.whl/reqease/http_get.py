import urllib.request
import ssl
import certifi
from data_classes import Response
from response_processor import ResponseProcessor

class Get(ResponseProcessor):
    """
    A class to handle HTTP GET requests and process the responses.

    This class sends a GET request to a specified URL and processes the response, 
    encapsulating the HTTP response status, headers, and body.

    ### Attributes
        `url (str)`: 
            The URL to which the GET request is sent.

        `headers (dict | None)`:
            Optional headers to include in the GET request.
        
        `response (Response)`:
            The processed response received from the GET request.

    ### Args
        `url (str)`:
            The target URL for the GET request.
        
        `headers (dict | None)`:
            Optional dictionary of headers to include with the request. Default is None.

    ### Methods
        `_make_request() -> Response`:
            Sends the GET request and returns the processed response.
    """
    def __init__(self, url: str, headers: dict | None = None) -> None:
        self.url = url
        self.headers = headers
        self.response = self._make_request()

    def _make_request(self) -> Response:
        """
        Sends the GET request to the specified URL.

        This method creates a Request object, adds headers if provided, 
        establishes a secure SSL context, and retrieves the response from the server.

        ### Returns
            `Response`: 
                An object encapsulating the HTTP response, including the status code, headers, and body content.

        ### Raises
            `URLError`:
                If there is a problem with the URL or network connection.
        """
        # Create a Request object
        request = urllib.request.Request(self.url)

        # Add headers to the request if provided
        if self.headers:
            for key, value in self.headers.items():
                request.add_header(key, value)

        # Create a secure SSL context    
        context = ssl.create_default_context(cafile=certifi.where())

        # Send the reuest and retreive the response
        with urllib.request.urlopen(request, context=context) as response:
            body_bytes = response.read()
            return Response(status_code = response.getcode(),
                            headers = response.getheaders(),
                            body_bytes = body_bytes,
                            body_str = body_bytes.decode('utf-8'))