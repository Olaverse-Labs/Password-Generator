# Password Generator API

[![Olaverse API](https://img.shields.io/badge/Olaverse-API%20Doc-blue?style=flat-square)](https://www.olaverse.co.uk/password-generator-api) [![Try on Vibeland](https://img.shields.io/badge/Vibeland-Try%20Live-orange?style=flat-square)](https://www.vibeland.co.uk/tools/password-generator)

This is a simple FastAPI-based API for generating random passwords.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```

## Docker

1. Build the Docker image:
   ```bash
   docker build -t password-generator-api .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 password-generator-api
   ```

## Usage

Send a GET request to `/generate-password` with the following optional query parameters:
- `length` (int, default 10, max 32): Length of each password
- `spchar` (int, default 2): Number of special characters
- `numbers` (int, default 2): Number of digits
- `umlauts` (bool, default true): Include German umlauts (ä, ö, ü, Ä, Ö, Ü, ß)
- `quantity` (int, default 10, max 10): Number of passwords to generate
- `use_uppercase` (bool, default true): Include uppercase letters
- `use_digits` (bool, default true): Include digits in the base character set
- `use_symbols` (bool, default true): Include special characters in the base character set

Example:
```
GET http://127.0.0.1:8000/generate-password?length=12&spchar=2&numbers=2&umlauts=true&quantity=5&use_uppercase=true&use_digits=true&use_symbols=false
```

Response:
```
{
  "passwords": [
    "...",
    "..."
  ]
}
``` 