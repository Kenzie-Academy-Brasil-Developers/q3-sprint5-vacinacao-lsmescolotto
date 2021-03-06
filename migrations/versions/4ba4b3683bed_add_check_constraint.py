"""add check constraint

Revision ID: 4ba4b3683bed
Revises: 
Create Date: 2022-04-12 14:17:52.551680

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ba4b3683bed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('first_shot_date', sa.DateTime(), nullable=True),
    sa.Column('second_shot_date', sa.DateTime(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=False),
    sa.Column('health_unit_name', sa.String(), nullable=False),
    sa.CheckConstraint("cpf ~ '\\d{11}'"),
    sa.PrimaryKeyConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###
