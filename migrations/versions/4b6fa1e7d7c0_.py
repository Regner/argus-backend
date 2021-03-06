"""empty message

Revision ID: 4b6fa1e7d7c0
Revises: 30ba5fcd6cc6
Create Date: 2016-12-27 19:18:43.161856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b6fa1e7d7c0'
down_revision = '30ba5fcd6cc6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('_character_owner_uc', 'users', ['character_id', 'character_owner_hash'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_character_owner_uc', 'users', type_='unique')
    # ### end Alembic commands ###
