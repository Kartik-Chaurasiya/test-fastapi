"""create posts

Revision ID: 73662b7c4129
Revises: db651424638d
Create Date: 2022-04-21 19:26:59.801963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73662b7c4129'
down_revision = 'db651424638d'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('user_id'),
                    sa.UniqueConstraint('username')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
