"""empty message

Revision ID: 579691d2b9eb
Revises: b086fc648294
Create Date: 2023-09-13 19:05:54.466328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '579691d2b9eb'
down_revision = 'b086fc648294'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.drop_column('cost')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reset_token', sa.String(length=200), nullable=True))
        batch_op.create_unique_constraint(None, ['reset_token'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('reset_token')

    with op.batch_alter_table('event', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###