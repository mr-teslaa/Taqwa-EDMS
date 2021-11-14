"""empty message

Revision ID: ab498c68ef57
Revises: 
Create Date: 2021-11-10 17:00:26.019339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab498c68ef57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notice', sa.Column('status', sa.String(length=20), nullable=False))
    op.add_column('students_info', sa.Column('birth_date', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students_info', 'birth_date')
    op.drop_column('notice', 'status')
    # ### end Alembic commands ###