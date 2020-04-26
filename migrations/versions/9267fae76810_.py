"""empty message

Revision ID: 9267fae76810
Revises: 3b7d9016fa35
Create Date: 2020-04-25 22:37:17.658180

"""

# revision identifiers, used by Alembic.
revision = '9267fae76810'
down_revision = '3b7d9016fa35'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('zip_alert', sa.Column('current_count', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('zip_alert', 'current_count')
    # ### end Alembic commands ###