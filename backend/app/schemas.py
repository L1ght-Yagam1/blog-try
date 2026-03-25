from pydantic import BaseModel, model_validator, ConfigDict

from .enums import ContentBlockType


class ContentBlockCreate(BaseModel):
    type: ContentBlockType
    img_url: str | None = None
    text: str | None = None

    @model_validator(mode="after")
    def validate_content(self):
        
        if self.type == ContentBlockType.TEXT:
            if not self.text:
                raise ValueError("Поле text обязательно для блока типа text")
            if self.img_url is not None:
                raise ValueError("Поле img_url должно быть пустым для блока типа text")

        if self.type == ContentBlockType.IMAGE:
            if not self.img_url:
                raise ValueError("Поле img_url обязательно для блока типа image")
            if self.text is not None:
                raise ValueError("Поле text должно быть пустым для блока типа image")

        return self
    

class ContentBlockPublic(BaseModel):
    id: int
    type: str
    order: int
    text: str | None = None
    img_url: str | None = None

    model_config = ConfigDict(from_attributes=True)


class PostPublic(BaseModel):
    id: int
    title: str
    content_blocks: list[ContentBlockPublic] | None = None

    model_config = ConfigDict(from_attributes=True)


class PostCreate(BaseModel):
    title: str
    content_blocks: list[ContentBlockCreate] | None


    
