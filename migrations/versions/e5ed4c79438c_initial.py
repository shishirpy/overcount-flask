"""initial

Revision ID: e5ed4c79438c
Revises: 
Create Date: 2021-05-21 23:58:51.609820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5ed4c79438c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('created_timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('counts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.String(length=120), nullable=True),
    sa.Column('infection_count', sa.Integer(), nullable=False),
    sa.Column('fatality_count', sa.Integer(), nullable=False),
    sa.Column('long', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('counts')
    op.drop_table('users')
    # ### end Alembic commands ###