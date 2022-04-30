"""alter_users_table

Revision ID: 69bafa01fca1
Revises: c85385e62be2
Create Date: 2022-04-02 23:17:05.283078

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "69bafa01fca1"
down_revision = "c85385e62be2"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("user", sa.Column("is_recruiter", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "is_recruiter")
    # ### end Alembic commands ###
