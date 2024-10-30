from typing import Protocol
from data_classes import Response

class ResponseProtocol(Protocol):
    """
    A protocol that defines the expected attributes for response handling.

    ### Attributes
        `url (str)`:
            The URL associated with the HTTP response.
        
        `response (Response)`:
            The Response object containing the HTTP response data.
    """
    url: str
    response: Response