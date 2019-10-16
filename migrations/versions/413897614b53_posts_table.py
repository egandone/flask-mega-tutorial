"""posts table

Revision ID: 413897614b53
Revises: fe84cb9cdfef
Create Date: 2019-10-16 09:03:53.040906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413897614b53'
down_revision = 'fe84cb9cdfef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('POST_ID', sa.Integer(), nullable=False),
    sa.Column('POST_BODY', sa.String(length=140), nullable=True),
    sa.Column('POST_WHEN', sa.DateTime(), nullable=True),
    sa.Column('POST_USER_ID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['POST_USER_ID'], ['user.USER_ID'], ),
    sa.PrimaryKeyConstraint('POST_ID')
    )
    op.create_index(op.f('ix_post_POST_WHEN'), 'post', ['POST_WHEN'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_POST_WHEN'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###
