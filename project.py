from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Room, RoomItem, User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///itemCatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Show all rooms


@app.route('/')
@app.route('/rooms/')
def showRooms():
    rooms = session.query(Room).order_by(asc(Room.name))
    return render_template('rooms.html', rooms = rooms)

# New room


@app.route('/room/new/', methods=['GET', 'POST'])
def newRoom():
    return "ok"


# Edit room


@app.route('/room/<int:room_id>/edit/', methods=['GET', 'POST'])
def editRoom(room_id):
    return "ok"


# Delete room


@app.route('/room/<int:room_id>/delete/', methods=['GET', 'POST'])
def deleteRoom(room_id):
    return "ok"


# Show room items


@app.route('/room/<int:room_id>/')
@app.route('/room/<int:room_id>/items/')
def showItems(room_id):
    room = session.query(Room).filter_by(id=room_id).one()
    creator = getUserInfo(room.user_id)
    items = session.query(RoomItem).filter_by(
        room_id=room_id).all()
    return render_template('roomitems.html', items = items, room = room, creator = creator)


# Create a new room item


@app.route('/room/<int:room_id>/items/new/', methods=['GET', 'POST'])
def newRoomItem(room_id):
    return "ok"


# Edit a room item


@app.route('/room/<int:room_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editRoomItem(room_id, item_id):
    return "ok"


# Delete a menu item


@app.route('/room/<int:room_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteRoomItem(room_id, item_id):
    return "ok"


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
