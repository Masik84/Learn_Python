"""Comments added

Revision ID: 843752e8180d
Revises: e9684110b0e6
Create Date: 2022-06-09 19:28:57.753376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '843752e8180d'
down_revision = 'e9684110b0e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_news_id'), 'comment', ['news_id'], unique=False)
    op.create_index(op.f('ix_comment_user_id'), 'comment', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_user_id'), table_name='comment')
    op.drop_index(op.f('ix_comment_news_id'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###
