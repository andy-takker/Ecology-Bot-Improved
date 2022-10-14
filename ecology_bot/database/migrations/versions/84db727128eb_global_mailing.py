"""global mailing

Revision ID: 84db727128eb
Revises: 84dc311cbb0a
Create Date: 2022-10-14 19:53:15.611624

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '84db727128eb'
down_revision = '84dc311cbb0a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_mailing',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.String(length=512), nullable=False),
    sa.Column('description', sa.String(length=3072), nullable=False),
    sa.Column('global_event_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['global_event_id'], ['global_event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_global_mailing_description'), 'global_mailing', ['description'], unique=False)
    op.create_index(op.f('ix_global_mailing_global_event_id'), 'global_mailing', ['global_event_id'], unique=False)
    op.create_index(op.f('ix_global_mailing_id'), 'global_mailing', ['id'], unique=False)
    op.create_index(op.f('ix_global_mailing_name'), 'global_mailing', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_global_mailing_name'), table_name='global_mailing')
    op.drop_index(op.f('ix_global_mailing_id'), table_name='global_mailing')
    op.drop_index(op.f('ix_global_mailing_global_event_id'), table_name='global_mailing')
    op.drop_index(op.f('ix_global_mailing_description'), table_name='global_mailing')
    op.drop_table('global_mailing')
    # ### end Alembic commands ###