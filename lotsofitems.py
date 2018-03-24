from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Room, Base, RoomItem, User

engine = create_engine('sqlite:///itemCatalog.db')
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


# Create user
User1 = User(name="Eric Johnston", email="eric.j294@gmail.com",
             picture="https://farm5.staticflickr.com/4579/38204075404_4e89aeb9f1_k.jpg")
session.add(User1)
session.commit()

# Kitchen
room1 = Room(user_id=1, name="Kitchen")

session.add(room1)
session.commit()

roomItem1 = RoomItem(user_id=1, name="Refrigerator", description="Keep food/liquids cold and fresh",
                     room=room1)

session.add(roomItem1)
session.commit()


roomItem2 = RoomItem(user_id=1, name="Dish-washer", description="Clean and dry dirty dishes",
                     room=room1)

session.add(roomItem2)
session.commit()

roomItem3 = RoomItem(user_id=1, name="Coffee Maker", description="Make fresh coffee in a flash",
                     room=room1)

session.add(roomItem3)
session.commit()


# Living Room
room2 = Room(user_id=1, name="Living Room")

session.add(room2)
session.commit()

roomItem1 = RoomItem(user_id=1, name="Sofa", description="A nice play to sit and relax.",
                     room=room2)

session.add(roomItem1)
session.commit()


roomItem2 = RoomItem(user_id=1, name="Television", description="Watch all of your favorite shows and movies.",
                     room=room2)

session.add(roomItem2)
session.commit()

roomItem3 = RoomItem(user_id=1, name="Coffee Table", description="Prop up your feet or use it for what it's really meant for.",
                     room=room2)

session.add(roomItem3)
session.commit()



print "added menu items!"
