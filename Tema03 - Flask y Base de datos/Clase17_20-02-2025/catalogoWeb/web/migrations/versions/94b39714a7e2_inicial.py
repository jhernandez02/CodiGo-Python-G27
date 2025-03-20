"""inicial

Revision ID: 94b39714a7e2
Revises: 
Create Date: 2025-02-20 22:24:13.358925

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '94b39714a7e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('imagen', sa.String(length=100), nullable=False),
    sa.Column('estado', sa.Enum('Disponible', 'Agotado', 'Descontinuado'), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    op.drop_table('prestamos')
    with op.batch_alter_table('libros', schema=None) as batch_op:
        batch_op.drop_index('isbn')

    op.drop_table('libros')
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_index('email')

    op.drop_table('usuarios')
    with op.batch_alter_table('generos', schema=None) as batch_op:
        batch_op.drop_index('nombre')

    op.drop_table('generos')
    op.drop_table('autores')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('autores',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('nacionalidad', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('fecha_nacimiento', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('generos',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('generos', schema=None) as batch_op:
        batch_op.create_index('nombre', ['nombre'], unique=True)

    op.create_table('usuarios',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('telefono', mysql.VARCHAR(length=15), nullable=True),
    sa.Column('fecha_registro', mysql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.create_index('email', ['email'], unique=True)

    op.create_table('libros',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('titulo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('autor_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('genero_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('anio_publicacion', mysql.SMALLINT(display_width=4), autoincrement=False, nullable=True),
    sa.Column('isbn', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('stock', mysql.INTEGER(display_width=11), server_default=sa.text("'1'"), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['autor_id'], ['autores.id'], name='libros_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['genero_id'], ['generos.id'], name='libros_ibfk_2'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('libros', schema=None) as batch_op:
        batch_op.create_index('isbn', ['isbn'], unique=True)

    op.create_table('prestamos',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('usuario_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('libro_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('fecha_prestamo', sa.DATE(), nullable=False),
    sa.Column('fecha_devolucion', sa.DATE(), nullable=True),
    sa.Column('estado', mysql.ENUM('Prestado', 'Devuelto'), server_default=sa.text("'Prestado'"), nullable=True),
    sa.ForeignKeyConstraint(['libro_id'], ['libros.id'], name='prestamos_ibfk_2', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], name='prestamos_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('productos')
    op.drop_table('categorias')
    # ### end Alembic commands ###
