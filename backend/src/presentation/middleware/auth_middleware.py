from flask import request, jsonify, g
from functools import wraps
from typing import Callable, Any

def authenticate_user(f: Callable) -> Callable:
    pass

def authorize_user(required_permissions: list = None):
    def decorator(f: Callable) -> Callable:
        pass
    return decorator

def validate_request_data(schema: dict):
    def decorator(f: Callable) -> Callable:
        pass
    return decorator

def rate_limit(max_requests: int = 100, window_minutes: int = 60):
    def decorator(f: Callable) -> Callable:
        pass
    return decorator

class AuthMiddleware:

    def __init__(self, secret_key: str):
        pass

    def verify_token(self, token: str) -> dict:
        pass

    def generate_token(self, user_data: dict) -> str:
        pass

    def extract_user_from_token(self, token: str) -> dict:
        pass

    def check_permissions(self, user: dict, required_permissions: list) -> bool:
        pass