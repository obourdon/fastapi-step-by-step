from fastapi import APIRouter

from api.responses.detail import DetailResponse

router = APIRouter(prefix="/api/v1/demo")


# this annotation correspond to the router variable
# defined above
@router.get("/", response_model=DetailResponse)
def hello_world():
    """
    This is the hello world endpoint

    """
    return DetailResponse(message="Hello from FastAPI")
