# item catalog
  A web application that displays a list of items from various categories
  Uses a third party authentication system that allows registered users to post, edit and delete their own items.
  Uses python's framework, flask, to develop this RESTful web application

### What is needed

  python v2. or higher installed on computer
  vagrant (virtual machine)
  any web-browser
  flask installed on computer

### Installing

download/clone contents of the itemcatalog repository from github

- You will need to cd into the vagrant directory in the terminal
  - Run: vagrant up
      - this updates to the current VM software

## Running

  Opening using terminal

    - Run: vagrant ssh

    - Move to where the files project.py, database_setup.py and lotsofitems.py are held

    - Run the database_setup.py (this will create the database)

    - Run lotsofitems.py (this will populate the database with a view items)

    - Run project.py (opens up the server)

    - In your browser, go to localhost:5000

## Built With

  html
  css
  SQL
  python (flask)

## Authors

  Eric Johnston(A Udacity student) and The Udacity Team
