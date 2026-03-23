from pydantic import BaseModel, model_validator
from typing import Literal, Optional

class PostCreate(BaseModel):
    title: str


class ContentBlock(BaseModel):
    type: Literal["text", "image"]
    post_id: int
    order: int
    img_url: Optional[str] = None
    text: Optional[str] = None

    @model_validator(mode="after")
    def validate_content(self):
        
        if self.type == "text":
            if not self.text:
                raise ValueError("Поле text обязательно для блока типа text")
            if self.img_url is not None:
                raise ValueError("Поле img_url должно быть пустым для блока типа text")

        if self.type == "image":
            if not self.img_url:
                raise ValueError("Поле img_url обязательно для блока типа image")
            if self.text is not None:
                raise ValueError("Поле text должно быть пустым для блока типа image")

        return self