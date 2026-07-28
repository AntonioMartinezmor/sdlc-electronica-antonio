from fastapi import APIRouter
router = APIRouter()
@router.APIRouter()
def health_check():
    return{"status": "ok"}
