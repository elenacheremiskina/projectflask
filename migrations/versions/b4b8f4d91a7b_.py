"""empty message

Revision ID: b4b8f4d91a7b
Revises: 
Create Date: 2020-05-20 14:13:26.637831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4b8f4d91a7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('revoked_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('semantic')
    op.drop_table('freq')
    op.drop_table('syntax')
    op.drop_table('text')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('text',
    sa.Column('id_text', sa.INTEGER(), nullable=False),
    sa.Column('text', sa.VARCHAR(length=8000, collation='Cyrillic_General_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(length=1000, collation='Cyrillic_General_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('file', sa.VARCHAR(length=1000, collation='Cyrillic_General_CI_AS'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_text', name='PK__text__C6D3C1EF854E909B')
    )
    op.create_table('syntax',
    sa.Column('id_result', sa.INTEGER(), nullable=False),
    sa.Column('id_text', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=1000, collation='Cyrillic_General_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_text'], ['text.id_text'], name='FK__syntax__id_text__1BFD2C07'),
    sa.PrimaryKeyConstraint('id_result', name='PK__syntax__12EEC0B8DAAD02BE')
    )
    op.create_table('freq',
    sa.Column('id_result', sa.INTEGER(), nullable=False),
    sa.Column('freqword', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('count', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('word', sa.VARCHAR(length=20, collation='Cyrillic_General_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('id_text', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_text'], ['text.id_text'], name='FK__freq__id_text__164452B1'),
    sa.PrimaryKeyConstraint('id_result', name='PK__freq__12EEC0B8CA53FFFE')
    )
    op.create_table('semantic',
    sa.Column('id_result', sa.INTEGER(), nullable=False),
    sa.Column('id_text', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('comment', sa.VARCHAR(length=1000, collation='Cyrillic_General_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_text'], ['text.id_text'], name='FK__semantic__id_tex__1920BF5C'),
    sa.PrimaryKeyConstraint('id_result', name='PK__semantic__12EEC0B892F1FCCF')
    )
    op.drop_table('revoked_token')
    # ### end Alembic commands ###