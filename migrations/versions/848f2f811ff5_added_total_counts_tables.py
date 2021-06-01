"""added total_counts tables

Revision ID: 848f2f811ff5
Revises: e5ed4c79438c
Create Date: 2021-05-28 23:09:08.135701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '848f2f811ff5'
down_revision = 'e5ed4c79438c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('total_counts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fatality', sa.Integer(), nullable=False),
    sa.Column('infection', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('total_counts')
    # ### end Alembic commands ###
