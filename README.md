# Insta-clone

#### A clone of the popular social media photo app [Instagram](https://www.instagram.com/)

>----------------------------------------------------------------------------------------------

## Description
This is a web clone of the instagram website. A user can create an account and sign into it. The site supports uploading images,liking and commenting on images as well as following other users. Logged in users can view photos uploaded by other users in the home page of app.

## Created by [Elizabeth Otieno](https://github.com/Libb521)

Codebeat rating
[![codebeat badge](https://codebeat.co/badges/a39ec926-35e8-48de-a736-bf34616d1129)](https://codebeat.co/projects/github-com-libb521-insta-clone-master)

## SET UP INSTRUCTIONS AND INSTALLATION

### What you need

- python3.6
- python virtual environment - run this command to create it 'python3.6 -m vent virtual'
- activate the virtual environment using this command 'source virtual/bin/activate'
- postgres (DB dependancy), to install it run the following command in your home directory:
    - 'sudo apt-get update`
    - `sudo apt-get install postgresql postgresql-contrib libpq-dev`
    - `sudo service postgresql start`
    - `sudo -u postgres createuser --superuser $USER`
    - `sudo -u postgres createdb $USER`
    - `touch .psql_history`

### installation
- clone the repo - 'git clone https://github.com/Libb521/insta-clone
- Activate virtual environment: 
   `python3.6 -m venv --without-pip virtual` then `source virtual/bin/activate`

- Install all the dependancies in the requirements.txt file to get a development env running
   `pip3 install -r requirements.txt`

- Create a database 
  ```bash
  psql
  CREATE DATABASE instagram;
  ```

- Create .env file and paste the following filing where appropriate:
  ```python
  SECRET_KEY = '<Secret_key>'
  DBNAME = 'insta'
  USER = '<Username>'
  PASSWORD = '<password>'
  DEBUG = True

  EMAIL_USE_TLS = True
  EMAIL_HOST = 'smtp.gmail.com'
  EMAIL_PORT = 587
  EMAIL_HOST_USER = '<your-email>'
  EMAIL_HOST_PASSWORD = '<your-password>'
  ```

- Run initial migration
  ``` bash
  python3.6 manage.py makemigrations instaclone
  python3.6 manage.py migrate
  ```

- Run the app

   - `python3.6 manage.py runserver`

- Open the `localhost:8000` to check if the app is running successfully.

### Dependancies

All the project's dependancies are found in the requirements.txt file.Open it for reference.

## known bugs
- Some of the main functionalities are not working as they should

## Technologies used
    - python3.6
    - Django3.0.4
    - HTML
    - CSS
    - Bootstrap
    - Postgresql

## contacts
In case of any inquieries or patnership opportunities kindly reach me through: eotieno39@yahoo.com

## Licence
> MIT LICENCE

> Copyright (c) 2020 Elizabeth Otieno