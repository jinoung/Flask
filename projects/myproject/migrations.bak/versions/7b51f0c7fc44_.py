"""empty message

Revision ID: 7b51f0c7fc44
Revises: 7e1ad2ec0933
Create Date: 2021-11-11 23:41:41.435803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b51f0c7fc44'
down_revision = '7e1ad2ec0933'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('modify_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comment', schema=None) as batch_op:
        batch_op.drop_column('modify_date')

    # ### end Alembic commands ###
