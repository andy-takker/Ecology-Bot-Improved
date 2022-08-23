"""empty message

Revision ID: 582ca935d161
Revises: 8da0c2842cb3
Create Date: 2022-08-19 08:06:16.611560

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '582ca935d161'
down_revision = '8da0c2842cb3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_district_organization_district_id', table_name='district_organization')
    op.drop_index('ix_district_organization_id', table_name='district_organization')
    op.drop_index('ix_district_organization_organization_id', table_name='district_organization')
    op.drop_table('district_organization')
    op.alter_column('employee', 'login',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
    op.create_unique_constraint(None, 'employee', ['login'])
    op.add_column('organization', sa.Column('district_id', sa.BigInteger(), nullable=False))
    op.create_index(op.f('ix_organization_district_id'), 'organization', ['district_id'], unique=False)
    op.create_foreign_key(None, 'organization', 'district', ['district_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'organization', type_='foreignkey')
    op.drop_index(op.f('ix_organization_district_id'), table_name='organization')
    op.drop_column('organization', 'district_id')
    op.drop_constraint(None, 'employee', type_='unique')
    op.alter_column('employee', 'login',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)
    op.create_table('district_organization',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('district_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('organization_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['district.id'], name='district_organization_district_id_fkey'),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], name='district_organization_organization_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='district_organization_pkey')
    )
    op.create_index('ix_district_organization_organization_id', 'district_organization', ['organization_id'], unique=False)
    op.create_index('ix_district_organization_id', 'district_organization', ['id'], unique=False)
    op.create_index('ix_district_organization_district_id', 'district_organization', ['district_id'], unique=False)
    # ### end Alembic commands ###