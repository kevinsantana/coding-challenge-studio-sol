from fastapi import APIRouter


router = APIRouter()


@router.get(
    "/",
    status_code=200,
)
def health():
    """
    Check whether or not the api is able to provide responses.
    """
    return "OK"
