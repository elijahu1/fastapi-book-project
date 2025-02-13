from fastapi import APIRouter

router = APIRouter()

@router.get("/stage2")
def stage2():
    return {"status": "Stage 2 is working!"}
