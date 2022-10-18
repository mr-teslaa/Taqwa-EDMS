"""empty message

Revision ID: b63d71807671
Revises: 
Create Date: 2022-10-16 17:37:55.358883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b63d71807671'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exam',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_name', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exam_subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exam_subject', sa.String(length=100), nullable=False),
    sa.Column('full_marks', sa.String(length=100), nullable=False),
    sa.Column('pass_marks', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('exam_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['exam_id'], ['exam.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exam_subject')
    op.drop_table('exam')
    # ### end Alembic commands ###