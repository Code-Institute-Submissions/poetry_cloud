**Testing During Development**

I followed these initial steps to verify that my simple Flask app was working, was connected to my database and was deploying to Heroku:

I manually set up the database in Mongodb and inserted a document to test connection later. 

I installed Flask via the terminal in Gitpod and created the app.py and env.py files.

Made sure env.py and __pycache__/ were included in the .gitignore file.

Ran a simple function in app.py to return “Hello World” to check that the app was working and would show this in the browser.

Successfully deployed to Heroku and connected to Github for autoupdates with each push from Gitpod.

I verified the basic app was rendering “Hello World” to the browser in Heroku. 

In order to get Flask to communicate with my database I installed flask-pymongo in Gitpod.

I then installed dnspython and updated the requirements.txt file. 

I tested the connection of Flask to MongoDB by successfully rendering my poems.html template in the browser using the data document I set up earlier in Mongodb.

I then verified that it was pushing successfully to Heroku and rendering to the browser there.


**Creating Templates.**

When creating new functions, html/jinja templates and styling with CSS, I verified new content was working throughout development, via the browser which opens from Gitpod.
For example, after adding external links and scripts for Materialize and font awesome, I tested to verify if the base template was recognising the static CSS file by adding a background colour to the body in style.css. 
I then confirmed this in the browser.
I continually tested how the page was rendering across all device sizes using Chrome DevTools.

**Setting up functionality for register form.**

I tried to submit the register form with only blank spaces. I then checked the user collection in Mongodb and a new blank user had been created. 
I fixed this by adding required inputs from the user of minimum and maximum length of characters and using regular expressions to control user input criteria. 
 
**Setting up functionality with login form.**

To test functionality when setting up the Login form, I tried to login using credentials previously registered and then checked in the Gitpod terminal to verify if there was a Post login with a status of 200, which there was. 
After creating all functionality for the login form, I tried to submit using false username and/or password to verify if it would display the appropriate error message and return me to the login, which it did.
I then tried to submit using a real username and password to verify if it would log me in and display the Welcome message, which it did. 

**Setting up search form functionality.**

* After creating the form and function for the search feature I tested the form in the browser preview from Gitpod.
* Using example poems I searched by title, author and any word from the poem text to verify if the correct results would return and display successfully, which they did. 

**Setting up functionality with custom error pages.**

After creating the html flask templates and error handler functions for 404 and 500 status codes, I manually tested to verify if each page would display appropriately. 
* 404 custom error page - I added a false ending to the url and tried to load the page. The 404 html page loaded successfully with 'Page Not Found' heading, explanation message and link back home.

* 500 custom error page - I imported 'abort' in flask and called the abort() method in the get_poems function to generate an error. This successfully displayed the custom 500 error page with 'Internal Server Errror' heading, explanation message and link back home.