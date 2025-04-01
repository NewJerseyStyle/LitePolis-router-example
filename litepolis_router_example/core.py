from typing import Union, List
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from litepolis_database_example.Actor import DatabaseActor

router = APIRouter()
prefix = __name__.split('.')[-2]
prefix = '_'.join(prefix.split('_')[2:])
dependencies = []
DEFAULT_CONFIG = {}

tags_metadata = [
    {
        "name": "Users",
        "description": "Operations related to users",
    },
    {
        "name": "Conversations",
        "description": "Operations related to conversations",
    }
]

class UserResponseMessage(BaseModel):
    id: int
    email: str
    privilege: str

class ConversationResponseMessage(BaseModel):
    id: int
    title: str
    description: str
    creator_id: int

class ResponseMessage(BaseModel):
    detail: Union[str, UserResponseMessage, ConversationResponseMessage, List[UserResponseMessage], List[ConversationResponseMessage]]
    error: str | None = None
    message: str | None = None
    status_code: int = 200

@router.get("/", tags=["Default"])
async def get_testroute():
    """This is a test route."""
    return ResponseMessage(detail="OK")

@router.post("/users/", response_model=ResponseMessage, tags=["Users"])
async def create_user(user_data: dict):
    """
    Create a new user.
    Expected input: {"email": "user@example.com", "password": "password", "privilege": "user"}
    """
    try:
        created_user = DatabaseActor.create_user(
            email=user_data["email"],
            password=user_data["password"],
            privilege=user_data.get("privilege", "user")
        )
        return ResponseMessage(
            detail=UserResponseMessage(
                id=created_user.id,
                email=created_user.email,
                privilege=created_user.privilege
            ),
            message="User created successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create user: {e}")

@router.post("/conversations/", response_model=ResponseMessage, tags=["Conversations"])
async def create_conversation(conv_data: dict):
    """
    Create a new conversation.
    Expected input: {"title": "Title", "description": "Description", "creator_id": 1}
    """
    try:
        created_conv = DatabaseActor.create_conversation(
            title=conv_data["title"],
            description=conv_data["description"],
            creator_id=conv_data["creator_id"]
        )
        return ResponseMessage(
            detail=ConversationResponseMessage(
                id=created_conv.id,
                title=created_conv.title,
                description=created_conv.description,
                creator_id=created_conv.creator_id
            ),
            message="Conversation created successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create conversation: {e}")

@router.get("/users/", response_model=ResponseMessage, tags=["Users"])
async def list_users():
    """List all users."""
    try:
        users = DatabaseActor.read_users()
        return ResponseMessage(
            detail=[
                UserResponseMessage(
                    id=user.id,
                    email=user.email,
                    privilege=user.privilege
                ) for user in users
            ],
            message="Users retrieved successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list users: {e}")

@router.get("/conversations/", response_model=ResponseMessage, tags=["Conversations"])
async def list_conversations():
    """List all conversations."""
    try:
        conversations = DatabaseActor.read_conversations()
        return ResponseMessage(
            detail=[
                ConversationResponseMessage(
                    id=conv.id,
                    title=conv.title,
                    description=conv.description,
                    creator_id=conv.creator_id
                ) for conv in conversations
            ],
            message="Conversations retrieved successfully"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list conversations: {e}")
