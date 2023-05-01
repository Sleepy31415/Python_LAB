"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny database "my_second_sql_database.db" i din eksisterende mappe “data”.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, select


Database = 'sqlite:///my_second_sql_database.db'
Base = declarative_base()

def select_all(classparam):  # return a list of all records in classparams table
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):  # return the record in classparams table with a certain id   https://docs.sqlalchemy.org/en/14/tutorial/data_select.html
    with Session(engine) as session:
        # in the background this creates the sql query "select * from persons where id=record_id" when called with classparam=Person
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record
def create_test_data():  # Optional. Used to test data base functions before gui is ready.
    with Session(engine) as session:
        new_items = []
        new_items.append(Customers(name="peter", address="30 rnd Str",age=18))
        new_items.append(Customers(name="susan",address="3 block drive", age=19))
        new_items.append(Customers(name="jane",address="5th on Queens", age=21))
        new_items.append(Customers(name="harry",address="20 Park Avenue ", age=20))
        new_items.append(Products(products_number=0, price="250$", brand="Levi"))
        new_items.append(Products(products_number=5, price="40$", brand="Victorinox"))
        new_items.append(Products(products_number=60, price="3$", brand="Oreos"))
        new_items.append(Products(products_number=80, price="2.50£", brand="Heinz"))
        for item in new_items:
            print(type(item))
        session.add_all(new_items)
        session.commit()



class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address= Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer({self.id=}    {self.name=} {self.address}  {self.age=})"



class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    products_number = Column(Integer)
    price = Column(String)
    brand = Column(String)


    def __repr__(self):
        return f"Products({self.id=}    {self.products_number=} {self.price}  {self.brand=})"

engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

# print(select_all(Products))
# create_test_data()
print(get_record(Customers,2))