from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

API_KEY = "mysecretkey123"  # Replace with your actual key
API_KEY_NAME = "X-Parse-REST-API-Key"  # Custom header name

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


async def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API KEY")
    return api_key
