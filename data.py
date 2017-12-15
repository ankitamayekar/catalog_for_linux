from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///dbentries.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for Panda Express 
restaurant1 = Restaurant(name="Panda Express")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Orange Chicken", information="Fried chicken with orange sauces",
                     price="$3.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="fried Rice", information="brown rice with herbs n veggies",
                     price="$2.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Fortune Cookie", information="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$0.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Subway")

session.add(restaurant2)
session.commit()

menuItem1 = MenuItem(name="Orange Chicken", information="Fried chicken with orange sauces",
                     price="$3.50", course="Appetizer", restaurant=restaurant2)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(name="fried Rice", information="brown rice with herbs n veggies",
                     price="$2.99", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Fortune Cookie", information="Juicy grilled chicken patty with tomato mayo and lettuce",
                     price="$0.50", course="Dessert", restaurant=restaurant2)

session.add(menuItem3)
session.commit()




print "Data Inserted..."
