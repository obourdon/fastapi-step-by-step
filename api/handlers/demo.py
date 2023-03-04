from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/demo")


# this annotation correspond to the router variable
# defined above
@router.get("/")
def hello_world():
    return "Hello from FastAPI"
