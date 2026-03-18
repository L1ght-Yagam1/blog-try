from pydantic import BaseModel


class PostCreate(BaseModel):
    title: str


class ContentBlock(BaseModel):
    type: str
    post_id: int
    order: int
    img_url: str 
    text: str