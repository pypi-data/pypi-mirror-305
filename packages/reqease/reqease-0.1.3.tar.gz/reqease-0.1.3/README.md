# Project Description

**Reqease** is a lightweight, minimalistic library designed for performing essential HTTP operations with minimal complexity. It focuses on streamlining common HTTP tasks such as `GET` and `POST` requests, while avoiding the overhead of larger libraries.

Whether you're interacting with APIs, retrieving data from a web service, or submitting forms, Reqease offers a clean and intuitive interface that allows you to perform these tasks effortlessly. It handles HTTPS requests and responses, parses JSON content, and manages basic file handling, all with a simple and elegant design.

### Key Features:
- **Minimalistic**: Focuses on core HTTP functionality without unnecessary bloat.
- **Intuitive API**: Easy-to-use methods for common tasks like `GET` and `POST`.
- **SSL/TLS Support**: Ensures secure HTTPS connections out of the box.
- **JSON Handling**: Built-in functionality to decode and return JSON responses as Python objects.
- **File Support**: Write response data directly to files with simple method calls.

Reqease is perfect for developers who need basic HTTP operations without the complexity of larger frameworks, keeping the codebase clean and efficient.

# Installation

To install **Reqease**, use the following pip command:

```bash
pip install reqease
```

# Usage

## Simple GET Request

You can use the `Get` class to fetch data from a URL over HTTPS:

### Example 1: Using Get Without Headers:

This example sends a basic GET request without any headers.

```python
import reqease

# Define the URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send the request and capture the response
response = reqease.Get(url).response

# Access and print details from the response
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Body (as string):", response.body_str)
```

### Example 2: Using Get With Custom Headers:

In this example, we specify custom headers for the GET request, including a `Authorization` and `Accept` header.

```python
import reqease
# Define the URL and custom headers
url = "https://jsonplaceholder.typicode.com/posts/1"
headers = {
    "Authorization": "Bearer your_access_token",
    "Accept": "application/json"
}

# Send the request and capture the response
response = reqease.Get(url, headers).response

# Access and print details from the response
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Body (as string):", response.body_str)
```

## Simple POST Request

You can use the `Post` class to send data to a server over HTTPS:

### Example 1: Using Post Without Headers

This example sends a basic POST request with data without any custom headers.

```python
import reqease

# Define the URL and the data to be sent
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}

# Send the request and capture the response
response = reqease.Post(url, data).response

# Access and print details from the response
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Body (as string):", response.body_str)
```

### Example 2: Using Post With Headers

This example sends a basic POST request with data without any custom headers.

```python
import reqease

# Define the URL, data, and headers
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}
headers = {"Content-Type": "application/json"}

# Send the request and capture the response
response = reqease.Post(url, data, headers=headers).response

# Access and print details from the response
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Body (as string):", response.body_str)
```

## Using Shared Methods

### Converting Response to Dictionary

Both the `Get` and `Post` classes provide a property called `to_dict`, which allows you to convert the response body to a Python dictionary. This is particularly useful when the response is in JSON format.

### Example 1: Using `to_dict` with Get

```python
import reqease

# Define the URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send the request and capture the response to a dictionary
data = reqease.Get(url).to_dict

# Access and print details from the dictionary
print("Data as Dictionary:", data)
```

### Example 2: Using `to_dict` with Post

When sending JSON data with the Post class, be sure to include the appropriate headers.

```python
import reqease

# Define the URL and the data to be sent
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}

# Define headers with Content-Type for JSON
headers = {"Content-Type": "application/json"}

# Send the request and capture the response to a dictionary
data = Post(url, data, headers).to_dict

# Access and print details from the dictionary
print("Data as Dictionary:", data)
```

### Saving Response to a File

Both the `Get` and `Post` classes include a method called `to_file`, which allows you to save the response body to a file. The method automatically formats the output based on the content type of the response.

### Example 1: Using `to_file` with Get

```python
import reqease

# Define the URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Save the response to a JSON file
reqease.Get(url).to_file("data.json")

# You can also save as plain text
reqease.Get(url).to_file("data.txt")
```

### Example 2: Using `to_file` with Post

When sending JSON data with the Post class, you can also save the response using the to_file
method.

```python
import reqease

# Define the URL and the data to be sent
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "foo", "body": "bar", "userId": 1}

# Define headers with Content-Type for JSON
headers = {"Content-Type": "application/json"}

# Save the response to a JSON file
reqease.Post(url, data, headers).to_file("data.json")

# You can also save as plain text
reqease.Post(url, data, headers).to_file("data.txt")
```

# Dependencies

**Reqease** has a minimal dependency footprint, making it a clean and lean library. The only external dependency required for this project is:

- **`certifi`**: This library provides a curated collection of root certificates for validating the trustworthiness of SSL/TLS certificates. It ensures that HTTPS requests made by the library are secure and reliable.

By using only standard libraries of Python, alongside `certifi`, Reqease maintains a lightweight design that focuses on simplicity and efficiency in performing HTTP operations.