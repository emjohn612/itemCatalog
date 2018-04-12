from sqlalchemy import create_engine
import datetime
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, CategoryItem, User

engine = create_engine('sqlite:///itemCatalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create user
User1 = User(name="Eric Johnston", email="eric.j294@gmail.com",
             picture="https://farm5.staticflickr.com/4579/38204075404_4e89aeb9f1_k.jpg")
session.add(User1)
session.commit()

# Category1
category1 = Category(user_id=1, name="Snowboarding")

session.add(category1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Goggles", description="Protect your eyes from the sun and snow while riding down the slopes.",
                             category=category1, date=datetime.datetime.now())

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="Jacket", description="Keep warm with a well insulated coat.",
                             category=category1, date=datetime.datetime.now())

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Snowboard", description="Several types: freestyle, freeride, all terrain, camber, rocker, etc. It is best to find a board that suits your style of riding.",
                             category=category1, date=datetime.datetime.now())

session.add(categoryItem3)
session.commit()


# Category2
category2 = Category(user_id=1, name="Soccer")

session.add(category2)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Soccer Ball", description="There are different types of soccer balls: turf, training ball, and a match ball. ",
                             category=category2, date=datetime.datetime.now())

session.add(categoryItem1)
session.commit()


categoryItem2 = CategoryItem(user_id=1, name="Shin Guards", description="Protect your shins from unwanted contact.",
                             category=category2, date=datetime.datetime.now())

session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="Cleats", description="A well contructed cleat can go a long way. Better ball controll, more explosive power/speed, and flexability/comfort.",
                             category=category2, date=datetime.datetime.now())

session.add(categoryItem3)
session.commit()


print "added category items!"
