"""empty message

Revision ID: 2fdabf2bae04
Revises: ffb338ffe1f7
Create Date: 2016-08-25 23:06:44.798337

"""

# revision identifiers, used by Alembic.
revision = '2fdabf2bae04'
down_revision = 'ffb338ffe1f7'

import sqlalchemy as sa
from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('test', sa.Column('description', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('test', 'description')
    ### end Alembic commands ###