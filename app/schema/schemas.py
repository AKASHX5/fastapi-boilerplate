from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    content: str
    title: str

    model_config = ConfigDict(from_attributes=True) # Use this


class CreatePost(PostBase):
    model_config = ConfigDict(from_attributes=True) # Use this