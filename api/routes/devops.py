from fastapi import APIRouter Depends

from api.schemas.message import MessageResponse, MessageSend

router = APIRouter(
	prefix="/DevOps",
	dependencies=[Depends(get_api_key)]
)


@router.post("/DevOps", response_model=MessageResponse, status_code=200)
def post_devops(message: MessageSend):
    return {"message": f"Hello {message.to} your message will be send"}


@router.get("/DevOps", response_model=MessageResponse, status_code=405)
def get_devops(message: MessageSend = None):
    return {"message": "ERROR"}


@router.put("/DevOps", response_model=MessageResponse, status_code=405)
def put_devops(message: MessageSend):
    return {"message": "ERROR"}


@router.patch("/DevOps", response_model=MessageResponse, status_code=405)
def patch_devops(message: MessageSend):
    return {"message": "ERROR"}


@router.delete("/DevOps", response_model=MessageResponse, status_code=405)
def delete_devops(message: MessageSend = None):
    return {"message": "ERROR"}
