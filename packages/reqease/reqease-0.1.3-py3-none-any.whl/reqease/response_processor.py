import json
from .protocols import ResponseProtocol

class ResponseProcessor:
    """
    A class to process HTTP responses and provide utility methods for
    converting the response into different formats.

    ### Attributes
        `response (Response)`: 
            The Response object containing the HTTP response data.
        
        `url (str)`:
            The URL associated with the response.

    ### Parameters
        `protocol (ResponseProtocol)`: 
            An object that provides the HTTP response and URL.

    ### Methods
        `to_dict() -> dict`:
            Converts the response body from a JSON string to a Python dictionary.

        `to_file(file_path: str) -> None`:
            Writes the response body to a file. The format of the file is determined by the file extension.
            If the file path ends with '.json', the response body is written in JSON format;
            otherwise, it is written as plain text.

    ### Raises
        `ValueError`:
            If the response body cannot be converted to a dictionary format.
    """
    def __init__(self, protocol: ResponseProtocol) -> None:
        self.response = protocol.response
        self.url = protocol.url

    @property
    def to_dict(self) -> dict:
        """
        Converts the response body from a JSON string to a Python dictionary.

        ### Returns
            `dict`: 
                The response body as a dictionary.

        ### Raises
            `ValueError`:
                If the response body cannot be converted to a dictionary format.
        """
        try:
            return json.loads(self.response.body_str)
        except:
            raise ValueError(f"The endpoint '{self.url}' is not a valid dictionary format.")
        
    def to_file(self, file_path: str) -> None:
        """
        Writes the response body to a file. The format of the file is determined by the file extension.

        If the file path ends with '.json', the response body is written in JSON format;
        otherwise, it is written as plain text.

        ### Parameters
            `file_path (str)`:
                The path where the response body should be written.

        ### Raises
            `IOError`:
                If there is an issue writing to the specified file.
        """
        with open(file_path,'w') as file:
            if '.json' in file_path:
                data = self.to_dict
                json.dump(data, file, indent=4)
            else:
                file.write(self.response.body_str)