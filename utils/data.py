from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear una instancia de la clase declarative_base
Base = declarative_base()

# Definir la clase para la tabla "contacts"
class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    phone = Column(String)
    email = Column(String)


database_url = 'mysql://root:UltraMarineDela13vaLegion@localhost:3306/contacts_data' 

engine = create_engine(database_url)

# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)
