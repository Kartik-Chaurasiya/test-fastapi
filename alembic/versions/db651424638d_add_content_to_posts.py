"""add content to posts

Revision ID: db651424638d
Revises: ac0698124e69
Create Date: 2022-04-21 19:25:27.568510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db651424638d'
down_revision = 'ac0698124e69'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
