"""empty message

Revision ID: 3ee88acf6d10
Revises: None
Create Date: 2015-03-14 14:31:58.921387

"""

# revision identifiers, used by Alembic.
revision = '3ee88acf6d10'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('question',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('slug', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('source', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'question_pkey')
    )


def downgrade():
    op.drop_table('question')
