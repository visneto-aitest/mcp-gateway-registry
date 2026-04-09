import hashlib
import hmac
import secrets
from datetime import datetime

# Application-level key for HMAC-based API key hashing.
# This adds a layer of domain separation beyond plain SHA-256.
_HASH_KEY: bytes = b"mcp-gateway-metrics-api-key-v1"


def generate_api_key() -> str:
    """Generate a new API key."""
    return f"mcp_metrics_{secrets.token_urlsafe(32)}"


def hash_api_key(api_key: str) -> str:
    """Hash API key for storage using HMAC-SHA256."""
    return hmac.new(_HASH_KEY, api_key.encode(), hashlib.sha256).hexdigest()


def generate_request_id() -> str:
    """Generate a unique request ID."""
    return f"req_{secrets.token_hex(8)}"
