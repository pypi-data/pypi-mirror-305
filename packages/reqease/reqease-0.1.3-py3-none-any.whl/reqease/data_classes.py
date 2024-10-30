from dataclasses import dataclass

@dataclass
class Response:
    """
    A class representing an HTTP response.

    ### Attributes
        `status_code (int)`:
            The HTTP status code of the response.
        
        `headers (list)`:
            A list of response headers.
        
        `body_bytes (bytes)`:
            The raw bytes of the response body.
        
        `body_str (str)`:
            The decoded string representation of the response body.
    """
    status_code:int
    headers:list
    body_bytes: bytes
    body_str:str