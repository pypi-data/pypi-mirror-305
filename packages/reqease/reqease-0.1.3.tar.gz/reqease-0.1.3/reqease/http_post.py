import urllib.request
import urllib.parse
import ssl
import certifi
import json
from .data_classes import Response
from .response_processor import ResponseProcessor

class Post(ResponseProcessor):
    """
    A class to handle HTTP POST requests and process the responses.

    ### Attributes
        `url (str)`: 
            The URL to which the POST request will be sent.
        
        `data (dict)`:
            The data to be sent in the body of the POST request.
        
        `headers (dict | None)`:
            Optional HTTP headers to include with the request.
        
        `response (Response)`:
            The Response object containing the HTTP response data.

    ### Parameters
        `url (str)`:
            The URL for the POST request.
        
        `data (dict)`:
            The data to be sent with the request, encoded appropriately.
        
        `headers (dict | None)`:
            Optional headers to include in the request.

    ### Methods
        `_make_request() -> Response`:
            Sends the POST request and retrieves the response.

    ### Raises
        `ValueError`:
            If the data cannot be encoded properly.
    """
    def __init__(self, url: str, data: dict, headers: dict | None = None) -> None:
        self.url = url
        self.data = data
        self.headers = headers
        self.response = self._make_request()

    def _make_request(self) -> Response:
        """
        Sends the POST request to the specified URL with the provided data and headers.

        ### Returns
            `Response`:
                The response object containing the HTTP response data.

        ### Raises
            `ValueError`:
                If the Content-Type is invalid or the data cannot be encoded.
        """
        # Encode the data as bytes, if headers contains "application/json" use json to encode
        if "Content-Type" in self.headers.keys():
            if self.headers['Content-Type'] == "application/json":
                encode_data = json.dumps(self.data).encode("utf-8")
        else:
            encode_data = urllib.parse.urlencode(self.data).encode("utf-8")
        
        # Create a Request object
        request = urllib.request.Request(self.url, encode_data, method='POST')

        # Add headers to the request if provided
        if self.headers:
            for key, value in self.headers.items():
                request.add_header(key, value)
        
        # Create a secure SSL context
        context = ssl.create_default_context(cafile=certifi.where())

        # Send the request and retreive response
        with urllib.request.urlopen(request, context=context) as response:
            body_bytes = response.read()
            return Response(status_code= response.getcode(),
                            headers= response.getheaders(),
                            body_bytes= body_bytes,
                            body_str= body_bytes.decode("utf-8"))