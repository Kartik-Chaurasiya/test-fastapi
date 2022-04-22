"""create posts

Revision ID: ac0698124e69
Revises: 
Create Date: 2022-04-21 19:21:05.990980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac0698124e69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('post_id', sa.Integer(), nullable = False, primary_key="true"), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
