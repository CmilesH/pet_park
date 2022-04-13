"""empty message

Revision ID: a16d1bd9b261
Revises: 94550166cd81
Create Date: 2022-04-13 11:20:46.923988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a16d1bd9b261'
down_revision = '94550166cd81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('owner', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner'], ['users.id'], name='pets_owner_fkey'),
    sa.PrimaryKeyConstraint('id', name='pets_pkey')
    )
    # ### end Alembic commands ###
