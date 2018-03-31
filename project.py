from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem, User
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

# Show all category's


@app.route('/')
@app.route('/categorys/')
def showCategorys():
    categorys = session.query(Category).order_by(asc(Category.name))
    return render_template('categorys.html', categorys = categorys)

# New category


@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['name'])
        session.add(newCategory)
        flash('New Category "%s" Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('showCategorys'))
    else:
        return render_template('newCategory.html')


# Edit category


@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategorys'))
    else:
        return render_template('editCategory.html', category=editedCategory)


# Delete catagory


@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('"%s" Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategorys', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)



# Show category items


@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    #creator = getUserInfo(category.user_id)
    items = session.query(CategoryItem).filter_by(
        category_id=category_id).all()
    return render_template('categoryitems.html', items = items, category = category)


# Create a new category item


@app.route('/category/<int:category_id>/items/new/', methods=['GET', 'POST'])
def newCategoryItem(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        newItem = CategoryItem(name=request.form['name'], description=request.form['description'], category_id=category_id)
        session.add(newItem)
        session.commit()
        flash('New item "%s" Successfully Created for %s' % (newItem.name, category.name))
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('newCategoryItem.html',category = category, category_id=category_id)



# Edit category item


@app.route('/category/<int:category_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
def editCategoryItem(category_id, item_id):
    editedItem = session.query(CategoryItem).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('Category Item Successfully Edited')
        return redirect(url_for('showItems', category_id=category_id))
    else:
        return render_template('editCategoryItem.html', category_id=category_id,
         item_id=item_id, item=editedItem, category=category)


# Delete category item


@app.route('/category/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteCategoryItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Category Item "%s" Successfully Deleted for %s' % (itemToDelete.name, category.name))
        return redirect(url_for('showItems', category_id=category_id, category=category))
    else:
        return render_template('deleteCategoryItem.html', item=itemToDelete)


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
