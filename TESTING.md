**Testing during development**

I followed these initial steps to verify that my simple Flask app was working, was connected to my database and was deploying to Heroku:

I manually set up the database in Mongodb and inserted a document to test connection later. 

I installed Flask  via the terminal and created the app.py and env.py files.

Made sure env.py and __pycache__/ were included in the .gitignore file.

Ran a simple function in app.py  to return “Hello World” to check that the app was working and would show this in the browser.

Successfully deployed to Heroku and connected to Github for autoupdates with each push from Gitpod.

I verified the basic app was rendering “Hello World” to the browser in Heroku. 

In order to get Flask to communicate with my database I installed flask-pymongo in Gitpod.

I then installed dnspython and  updated the requirements.txt file. 

I tested the connection of Flask to MongoDB by successfully rendering my poem.html template in the browser using the data I set up earlier.

I then verified that it was pushing successfully to Heroku and rendering to the browser.


**Creating templates.**

When creating the html templates I verified new content and jinja templating was working via the browser which opens from Gitpod.

For example, after adding external links and scripts for Materialize and font awesome,  I  tested to verify if the base template was recognising the static CSS file by adding a background colour to the body in the style.css.

This colour showed in the browser to confirm this. 


**Setting up functionality with register form.**

I tried to submit the register form with only blank spaces. I then checked the user collection in Mongodb and a new blank user had been created. 
I fixed this by adding required inputs from the user of minimum and maximum length of characters and using regular expressions to control user input criteria. 
 
**Setting up functionality with login form.**

To test functionality when setting up the Login form, I tried to login using credentials previously registered and then checked in the Gitpod terminal to verify if there was a Post login with a status of 200, which there was. 
After creating all functionality for the login form, I tried to submit using false username and/or password to verify if it would display the appropriate error message and return me to the login, which it did.
I then tried to submit using a real username and password to verify if it would log me in and display the Welcome message, which it did. 