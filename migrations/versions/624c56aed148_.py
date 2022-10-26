"""empty message

Revision ID: 624c56aed148
Revises: 
Create Date: 2022-10-24 21:05:39.206402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '624c56aed148'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['position_id'], ['employee.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('department', sa.String(length=100), nullable=True),
    sa.Column('wage', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('position')
    op.drop_table('employee')
    # ### end Alembic commands ###
