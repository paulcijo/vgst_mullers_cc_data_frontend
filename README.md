# VGST DATA ENTRY

The app provides a frontend with basic validation to ensure the integrity of data entered during the data collection
phase of the project. It's designed to make sure you don't have to keep entering the same data over and over again. 
Which is the case when you try to enter this data in excel.

# HOW DO YOU GET THIS RUNNING? 

## Pre requisites to the project

To run this project you need the following installed on your PC.
* Python3 onwards
* MySQL (Preferrably XAMP/ WAMP on windows)

## Step 1: How do you Download this project from github?
You should find a green clone or download button on this page. Click on it and Download a Zip of the project.

Extract the zip.

## Step 2: How  do you get MySQL ready?

We need to create a mysql user, a database to store data in, and give the user access to the database.

We have a script that has all those SQL commands.
You can find it here.

```bash
vgst_mullers_cc_data_frontend/database/setup.sql
```
Open up your MySQL prompt and copy paste these SQL statements one by one.

You should now have a MySQL User who has access to the database.

***DO NOT CHANGE THE USER NAME OR THE DATABASE NAME MENTIONED IN THE FILE. YOUR PROJECT WILL NOT WORK.***

## Step 3:  HOW TO GET THE FRONTEND READY?
Create a User for the Fronted and Let the Application create all the SQL Tables

### Step 3.1: Install the Project Dependencies:


Open command prompt in your project folder. (vgst_mullers_cc_data)

```bash
python3.7 -m venv venv # create your virtual environment
venv\bin\activate.bat  # activate virtual environment
pip install -r requirements.txt  # install the dependencies
```

After running these commands your dependencies should be installed.

### Step 3.2: Let the application create the tables:
```bash
cd datacollection  # cd into the data collection application
 
# to create the database tables automagically
python manage.py migrate collector
python manage.py migrate
``` 

### Step 3.3: Create an Admin User
```bash
python manage.py createsuperuser
```
Enter a Username

Enter a password

When asked to bypass password check type in 'y'. THis happens when you enter a weak password. Its okay to enter a weak password. 

**DON'T FORGET YOUR PASSWORD AND USERNAME**

## FINAL STEP: Run the app

```bash
python manage.py runserver 127.0.0.1:8000
```

open up your browser and type in the following url:

```buildoutcfg
127.0.0.1:8000/admin
```
You should be greeted with a login screen. Enter theusername and password you just entered. And you are good to go!

All the besht. :) 