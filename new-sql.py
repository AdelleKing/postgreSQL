from sqlalchemy import(
    create_engine, Column, Float, Integer, String, PickleType
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#executing the instructions from the chinook database
db=create_engine("postgresql:///chinook")
base=declarative_base()

class Wine(base):
    __tablename__ = "Wine"
    id= Column(Integer, primary_key=True)
    wine_name = Column(String)
    grape_variety= Column(String)
    location = Column(String)
    country = Column(String)
    ABV = Column(Float)

#instead of connecting to the database directly, we will ask for a session
#create a new instance of sessionmaker, then point to our engine
#(the db) 
Session = sessionmaker(db)
#opens an actual session by calling the Session() subclass defined above
session = Session()

base.metadata.create_all(db)

#creating records on our Programmer table
el_bombero = Wine(
    wine_name = "El Bombero",
    grape_variety= "Garnacha",
    location = "Carinena",
    country ="Spain",
    ABV = 14.0
)

house_DOCG = Wine(
    wine_name = "House DOCG",
    grape_variety= "Montepulciano D'abruzzo",
    location = " ",
    country ="Italy",
    ABV = 12.5
)

isla_negra = Wine(
    wine_name = "Isla Negra",
    grape_variety= "Merlot",
    location = " ",
    country ="Chile",
    ABV = 10.5
)

usa = Wine(
    wine_name = "USA",
    grape_variety= "Zinfandel",
    location = "California",
    country ="USA",
    ABV = 13.5
)

usa = Wine(
    wine_name = "USA",
    grape_variety= "Zinfandel",
    location = "California",
    country ="USA",
    ABV = 13.5
)



#add each instance of our programmers to our session
#session.add(el_bombero)
#session.add(house_DOCG)
#session.add(isla_negra)
#session.add(usa)

#wine = session.query(Wine).filter_by(id=2).delete()

#wname = input("Enter the wine name: ")
#grapeVariety = input("Enter the grape variety: ")

#userWine = Wine(
 #   wine_name = wname,
  #  grape_variety= grapeVariety,
   # location = " ",
    #country =" ",
    #ABV = 0.0
#)

#session.add(userWine)


wine = session.query(Wine).add_column(characteristics, PickleType)
#wine = session.query(Wine).filter_by(id=6).first()
#wine.country = "Italy"
#wine.ABV = 13.0
#commit our session to the database
session.commit()

vino = session.query(Wine)
for wine in vino:
    print(
        wine.id,
        wine.wine_name,
        wine.grape_variety,
        wine.location,
        wine.country,
        wine.ABV,
        sep=" | "
    )
