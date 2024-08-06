from fastapi import APIRouter, Depends

from models.model import User
from security.get_current_user import get_current_user

router = APIRouter(prefix="", tags=["endpoint_test"])


@router.get("/")
def public_route():
    return {"message": "Welcome to endpoint test"}


@router.get("/protected")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}"}
