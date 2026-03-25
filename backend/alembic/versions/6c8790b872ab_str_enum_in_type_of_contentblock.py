"""str -> enum in type of ContentBlock

Revision ID: 6c8790b872ab
Revises: 931a75ff49a5
Create Date: 2026-03-25 16:30:47.723952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '6c8790b872ab'
down_revision: Union[str, Sequence[str], None] = '931a75ff49a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    content_block_type = postgresql.ENUM(
        'text', 'image',
        name='content_block_type'
    )
    content_block_type.create(op.get_bind(), checkfirst=True)

    op.execute("""
        ALTER TABLE content_blocks
        ALTER COLUMN type TYPE content_block_type
        USING type::content_block_type
    """)


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
        ALTER TABLE content_blocks
        ALTER COLUMN type TYPE VARCHAR(100)
        USING type::text
    """)

    content_block_type = postgresql.ENUM(
        'text', 'image',
        name='content_block_type'
    )
    content_block_type.drop(op.get_bind(), checkfirst=True)
