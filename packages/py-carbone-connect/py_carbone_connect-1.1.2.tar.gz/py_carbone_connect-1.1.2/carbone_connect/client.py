import requests
from typing import Optional, Dict, Any, Union, BinaryIO
import json
import os
import mimetypes


class CarboneError(Exception):
    """Custom exception for Carbone-related errors"""
    pass


class CarboneConnect:
    def __init__(self, api_url: str):
        """
        Initialize CarboneConnect with API URL.

        Args:
            api_url (str): The base URL of the Carbone API server
        """
        self.api_url = api_url.rstrip('/')
        self.headers = {
            'Content-Type': 'application/json'
        }

    def _handle_response(self, response: requests.Response) -> Any:
        """
        Handle API response and errors.

        Args:
            response (requests.Response): Response from the API

        Returns:
            Any: Response data

        Raises:
            CarboneError: If API returns an error
        """
        try:
            if not response.ok:
                error_msg = response.json().get('error', 'Unknown error')
                raise CarboneError(f"API error: {error_msg}")
            return response
        except requests.exceptions.JSONDecodeError:
            return response

    def render(self, template: Union[str, BinaryIO], data: Dict[str, Any],
               options: Optional[Dict[str, Any]] = None) -> bytes:
        """
        Render a template with provided data.

        Args:
            template (Union[str, BinaryIO]): Path to template file or file-like object
            data (dict): Data to render in the template
            options (dict, optional): Rendering options

        Returns:
            bytes: Generated document as binary data
        """
        # Prepare the files and data
        files = {}
        if isinstance(template, str):
            template_path = template
            content_type = mimetypes.guess_type(template_path)[0] or 'application/octet-stream'
            files['template'] = (
                os.path.basename(template_path),
                open(template_path, 'rb'),
                content_type
            )
        else:
            files['template'] = ('template', template, 'application/octet-stream')

        # Prepare the payload
        payload = {
            'data': json.dumps(data),
        }

        if options:
            payload['options'] = json.dumps(options)

        try:
            response = requests.post(
                f"{self.api_url}/render",
                files=files,
                data=payload
            )

            response = self._handle_response(response)
            return response.content

        except requests.exceptions.RequestException as e:
            raise CarboneError(f"Request failed: {str(e)}")
        finally:
            # Close file if it was opened here
            if isinstance(template, str) and 'template' in files:
                files['template'][1].close()

    def render_stream(self, template: Union[str, BinaryIO], data: Dict[str, Any],
                      options: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Render a template and return a stream response.

        Args:
            template (Union[str, BinaryIO]): Path to template file or file-like object
            data (dict): Data to render in the template
            options (dict, optional): Rendering options

        Returns:
            requests.Response: Streaming response object
        """
        # Similar to render but with stream=True
        files = {}
        if isinstance(template, str):
            template_path = template
            content_type = mimetypes.guess_type(template_path)[0] or 'application/octet-stream'
            files['template'] = (
                os.path.basename(template_path),
                open(template_path, 'rb'),
                content_type
            )
        else:
            files['template'] = ('template', template, 'application/octet-stream')

        payload = {
            'data': json.dumps(data),
        }

        if options:
            payload['options'] = json.dumps(options)

        try:
            response = requests.post(
                f"{self.api_url}/render",
                files=files,
                data=payload,
                stream=True
            )

            return self._handle_response(response)

        except requests.exceptions.RequestException as e:
            raise CarboneError(f"Request failed: {str(e)}")
        finally:
            if isinstance(template, str) and 'template' in files:
                files['template'][1].close()