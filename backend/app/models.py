from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)

class ContentBlock(Base):
    __tablename__ = "content_blocks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(100), nullable=False)
    post_id: Mapped[int] = mapped_column(nullable=False)
    order: Mapped[int] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(String(255), nullable=True)
    text: Mapped[str] = mapped_column(String(1000), nullable=True)