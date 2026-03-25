import sqlalchemy as sa
from sqlalchemy import String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from .enums import ContentBlockType


class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)

    content_blocks: Mapped[list["ContentBlock"]] = relationship(
        back_populates="post",
        cascade="all, delete-orphan",
        order_by="ContentBlock.order"
    )

class ContentBlock(Base):
    __tablename__ = "content_blocks"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[ContentBlockType] = mapped_column(
    sa.Enum(
        ContentBlockType,
        name="content_block_type",
        values_callable=lambda enum_cls: [e.value for e in enum_cls],
    ),
    nullable=False
)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    order: Mapped[int] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(String(255), nullable=True)
    text: Mapped[str] = mapped_column(String(1000), nullable=True)


    post: Mapped["Post"] = relationship(back_populates="content_blocks")


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)