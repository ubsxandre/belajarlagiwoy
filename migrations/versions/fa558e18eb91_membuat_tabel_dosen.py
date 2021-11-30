"""membuat tabel dosen

Revision ID: fa558e18eb91
Revises: 32dc58cfcff5
Create Date: 2021-11-30 10:54:45.574399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa558e18eb91'
down_revision = '32dc58cfcff5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dosen',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nidn', sa.String(length=30), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('phone', sa.String(length=13), nullable=False),
    sa.Column('alamat', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dosen')
    # ### end Alembic commands ###