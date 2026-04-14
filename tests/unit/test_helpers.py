import pytest

from app.utils.auth import hash_password, verify_password

def test_hash_password():
    hashed = hash_password("mypassword")
    assert hashed != "mypassword"

def test_verify_password():
    hashed = hash_password("mypassword")
    assert verify_password("mypassword", hashed) == True


