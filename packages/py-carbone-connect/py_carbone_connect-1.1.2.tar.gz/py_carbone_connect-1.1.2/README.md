# CarboneConnect Python Client

A Python client library for interacting with the Carbone API service. This library provides a simple interface to render documents using templates and data.

## Installation

```bash
pip install py-carbone-connect
```

## Features

- Template rendering with data
- Support for both file paths and file-like objects as templates  
- Streaming response support
- Error handling with custom exceptions
- Automatic content type detection

## Usage

### Basic Usage

```python
from carbone_connect import CarboneConnect

# Initialize the client
carbone = CarboneConnect('http://selfhosted.carbone-server.com') # it does not have Auth yet

# Render a template with data
template_path = 'path/to/template.docx'
data = {
    'name': 'John Doe',
    'company': 'ACME Corp'
}

# Generate document
result = carbone.render(template_path, data)

# Save the result
with open('output.docx', 'wb') as f:
    f.write(result)
```

### Streaming Response

```python
# Get a streaming response
response = carbone.render_stream(template_path, data)

# Process the stream
with open('output.docx', 'wb') as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
```

## API Reference

### CarboneConnect

#### `__init__(api_url: str)`

Initialize the Carbone client with the API URL.

#### `render(template: Union[str, BinaryIO], data: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> bytes`

Render a template with provided data and return the result as bytes.

- `template`: Path to template file or file-like object
- `data`: Dictionary containing data to render in the template
- `options`: Optional rendering options

#### `render_stream(template: Union[str, BinaryIO], data: Dict[str, Any], options: Optional[Dict[str, Any]] = None) -> requests.Response`

Render a template and return a streaming response.

## Error Handling

The library includes a custom `CarboneError` exception class for handling API-related errors:

```python
try:
    result = carbone.render(template_path, data)
except CarboneError as e:
    print(f'Error: {e}')
```
## Test
### Install development dependencies
pip install -e .[dev]

### Run tests
pytest

### Run tests with coverage report
pytest --cov=carbone_connect --cov-report=term-missing

### Run specific test
pytest tests/test_client.py -k test_initialization

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.