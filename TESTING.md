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

### **User Story Tests**
The following section shows how the project meets the user's needs as outlined in the user stories and illustrates these with screenshots of the finished project. 

**1. As a poet, I want to document my work so that I can be organised and have each item readily available.** 

These user's needs are met via:
* The Profile page feature that lists all of the registered user's poems and lets them view each one by clicking the popout.
* The search feature on the home page that lets users find poems quickly and if logged in they can edit or delete their own poems directly from their search results. 


![Profile](/documentation/screenshots/profile-mob.png)

Profile page on mobile device (Above)

![Profile](/documentation/screenshots/profile-tab.png)

Profile page on a tablet (Above)

![Profile](/documentation/screenshots/profile-desk.png)

Profile page on a desktop (Above)


**2. As a poet, I want to add/store my poems so that I can more easily manage them in the future.**

These user's needs are met via:
* The Add Poem form.
* The Profile and home page listings.

![Add Poem Form](/documentation/screenshots/add-mob.png)

Add Poem form on mobile (Above)

![Add Poem Form](/documentation/screenshots/add-poem-tab.png)

Add Poem form on a tablet (Above)

![Add Poem Form](/documentation/screenshots/add-desk.png)

Add Poem form on a desktop (Above)


**3. As a poet, I want to be able to edit and delete existing poems so that I can improve and update my collection.** 

These user's needs are met via:
* The Edit Poem form.
* The delete button.

![Edit Poem Form](/documentation/screenshots/edit-mob.png)

Edit Poem form on mobile (Above)

![Edit Poem Form](/documentation/screenshots/edit-tab.png)

Edit Poem form on a tablet (Above)

![Edit Poem Form](/documentation/screenshots/edit-desk.png)

Edit Poem form on a desktop (Above)

![Delete button](/documentation/screenshots/delete-mob.png)

Delete button on mobile (Above)


**4. As a poet, I want to be able to add new poems to existing types such as Haiku or Sonnet so that I can build a body of work.**

These user's needs are met via:
* The dropdown type selector on the add poem form.

![Select Type](/documentation/screenshots/selector-mob.png)

Type selector on Add Poem form on mobile (Above)

![Select Type](/documentation/screenshots/selector-tab.png)

Type selector on Add Poem form on a tablet (Above)

![Select Type](/documentation/screenshots/selector-desk.png)

Type selector on Add Poem form on a desktop (Above)


**5. As a poet, I want to be able to view all of my poems in one place so that it’s easy to see and manage my work.**

These user's needs are met via:
* The profile page. (See screenshots at 1. above)

**6. As a poet, I want to be able to find a particular poem in my collection so that I can view, edit or delete it.**

These user's needs are met via:
* The search feature on the home page which allows logged in users to view, edit and delete.

![Search](/documentation/screenshots/search-mob.png)

Search feature on mobile (Above)

![Search](/documentation/screenshots/search-tab.png)

Search feature on a tablet (Above)

![Search](/documentation/screenshots/search-desk.png)

Search feature on a desktop (Above)


**7. As a poet, I want to be able to submit the title and text of my poems, so that I can add them to my collection and identify them later.**

These user's needs are met via:
* The title and text area inputs on the Add Poem form. (See screenshots at 2. above)

**8. As a poetry fan, I want to be able to submit poems by well known authors, so that I can store my favourites and share with the community.**

These user's needs are met via:
* The Name of Author inputs on the Add Poem form. (See screenshots at 2. above)
* Author's name appears in each listing. 

![Author](/documentation/screenshots/author-mob.png)

Author's name on mobile (Above)

**9. As a poet I want to be able to share my poems online with the poetry community and see the work of my fellow poets.**

These user's needs are met via:
* Community Poems listings on home page. 
* Social links and useful poetry links in the footer encourage sharing with a wider poetry community.

![Community Poems](/documentation/screenshots/community-tab.png)

Community Poems on a tablet (Above)

![Social Links](/documentation/screenshots/footer-mob.png)

Social links and useful poetry links in the footer on mobile (Above)

**10. As an administrator of the site, I want to be able to add, read, update and delete poetry types so that I can provide the best experience for the user.**

These user's needs are met via:
* The Manage Types page (only available to admin users). 

![Manage Types](/documentation/screenshots/manage-mob.png)

Manage Types page on mobile (Above)

![Manage Types](/documentation/screenshots/manage-desk.png)

Manage Types page on desktop (Above)


### **Interactivity Tests**
The following tests were carried out on mobile, tablet and desktop devices to confirm that all interactive parts of the site are working as expected:

**1. Main navigation links**

	i.  Go to the “Home” page.

    ii. Click each of the main navigation links to verify if the browser navigates to the correct page.

	iii. Click on all the other pages nav links and then click on the logo image to verify if this returns the
        user to the homepage.

	iv. Hover over the nav links to test the background colour changes to correct grey and the text is red. 

    v. On mobile devices click the hamburger icon to verify that the side menu pops out and click away to verify if it returns.

    vi. On mobile devices, click on all of the sidebar nav links to verify if the browser navigates to the correct page. 
 
The above tests were carried out and no errors were found. 

**2. Search Form**

	i. Go to the search form on the “Home” page

	ii. Enter a random title from a poem in the community poems below and click the search button to verify that the poem is returned in the search results. 

    iii. Click the reset button to verify that the page resets and displays all poems once again.
    
    iv. Repeat test ii. above with a different poem to confirm the search is true. 

    v. Repeat steps i to iii with author and keyword inputs to verify that all search terms are functioning correctly.

    vi. Hover over both buttons on the form to verify that the black 3d shadow effect is working.

    vii. Click both buttons to verify the waves effect is working.

The above tests were carried out and no errors were found.


**3. Community Poems**

	i. Click the red arrow on a random poem to verify if the collapsible popout opens up and click again to verify if it closes. 

    ii. Once logged in as a user go to add a poem and submit a poem. Then go to home page and verify if the poem you submitted has edit and delete buttons. Now log out to verify that they no longer display. 

The above tests were carried out and no errors were found. 


**4. Authentication** (To register, users must submit an alphanumeric username and password with no spaces between 5 and 15 characters)

	i. Go to home page and verify that only home, login and register links are displayed.

	ii. Go to register page and try to submit a blank form to verify that a tooltip pops up to ask you to fill in the username.

	iii. Try to fill in the username with a space in to verify that the tooltip pops up to match the format requested.

    iv. Fill in the username correct format such as bobjones to verify the input line goes green.

    v. Complete items iii and iv for the password input to verify the line goes green. 

    vi. When both lines are green click the register button to verify that you are redirected to the users profile and that flash message of "You have successfully registered" is displayed.

    vii. Click the Log Out link in the main navigation to verify that you are redirected to the log in page with flash message saying "You have successfully logged out".

    viii. Using the credentials you have now registered attempt to log in again to verify that you are redirected to the correct user profile page and "Welcome username" message displayed.

    ix. Log out again and using the admin credentials log back in to verify you are directed to admin's profile page and "Welcome Admin" is displayed.

    x. Whilst logged in as admin user, verify that Manage Types nav link now appears in main menu. Log out to verify you are returned to the log in page and flash message displays to say "You have successfully logged out".

The above tests were carried out and no errors were found. 


**6. Footer / Social Media Links**

	i.  Click on all social icons and poetry links to verify if this opens the link, in a new window, at the appropriate page.

	ii. Try to hover the pointer over all social icons in the footer to verify they display the black 3d effect. 

The above tests were carried out and no errors were found. 

**7. Add Poem Form**

    i. Once logged in as a registered user go to Add Poems via main nav link. Click the dropdown menu to verify the list of 13 types is displayed.

    ii. Attempt to submit a blank form to verify the tooltip pops up to request you select an item on the list. 

    iii. Fill out the whole form correctly with a sample poem and click the button to verify the "Poem Successfully Added" confirmation message displays. 

    The above tests were carried out and no errors were found. 


**8. Edit Poem Form**

    i. From the profile page click on the edit button of the poem your just submitted to verify the edit poem form is displayed.

    ii. Click the cancel button to verify that you are directed back the profile page. 

    iii. Repeat step i. then make some changes in the text and click update poem button to verify the confirmation message of "Poem Successfully Updated" is displayed.

    The above tests were carried out and no errors were found. 


**9. Manage Types Page**

    i. Make sure you are logged in as an admin user and go to the Manage Types page by clicking on the main nav link. Click on the Add Poem Type button to verify the Add Type card is displayed.

    ii. Add a name in the input field and click the Add Type button to verify if you are redirected to the Manage Types page and the confirmation message "New Poem Type Added" is displayed. Verify if the new Type is also displayed as a card with buttons. 

    iii. Click the delete button on the newly created card to verify that the confirmation message is displayed, "Poem Type Successfully Deleted". 

    iv. Choose an existing Type card and click the edit button to verify the Edit Type form is displayed. Change the name and click Edit Type button to verify the changes are displayed in Manage Types.

    v. Choose an existing Type card and click the edit button to open the Edit Type form and click the Cancel button to verify you are redirected to the Manage Types page.

    The above tests were carried out and no errors were found. 

## **Responsiveness**

**Mobile:**

* On mobile devices the navbar collapses to a navbar toggler or hamburger icon.
  Clicking this produces a sidebar popout menu which displays the navigation links to all pages on the website, depending on user login status.
* Images on the homepage display at close to full width of the screen in a single column.
* The Search form displays at close to full width of the screen.
* The community poems on the home page display at close to full screen width and the popout collapsible header's text wraps beneath the line. 
* The poem text in the popout body resizes to fit a single column with appropriate line breaks in the text. 
* The footer's social links stack up on top of useful poetry links into a single column. 
* On the Manage Types page the type cards are single column width.

**Tablets:**

* On tablets such as the iPad the navbar collapses to a navbar toggler or hamburger icon as with mobile above.
  Clicking this produces a sidebar popout menu which displays the navigation links to all pages on the website, depending on user login status.
* On iPad Pro the full main navbar is shown. 
* The Search bar is close to the full width of the screen.
* The Community poems listings display at close to full screen width but the headings no longer wrap as with mobile. 
* The footers social icons and useful links split into two separate columns.
* Add Poem and Edit Poem forms display at full width of the screen.
* On the Manage Types page the type cards are three columns width.

**Desktop:**

* On desktop computers and laptops the full navigation bar is shown. 
* The images on the hompage are constrained to a maximum width and do not fill the width of the screen. 
* The Search form is constrained to a maximum width and does not fill the width of the screen. 
* The Community poems listings are also constrained in width.
* The footer displays at full width in two separate columns.
* All forms are also contrained in size and width.


## **Device Testing**

The website was tested on the following devices:

### **Mobile**

* Apple iPhone XR using Safari on IOS 14.3
* Apple iPhone 7 using Safari on IOS 11.3.1
* Apple iPhone 8 using Safari on IOS 13.4
* Motorola Moto E5 using Google Chrome on Android 8.1
* Google Pixel 3A using Google Chrome on Android 10
* Google pixel 3XL using Google Chrome on Android 10

### **Tablets**

* Apple iPad Air 2 using Safari on IOS 13.5.1
* Microsoft Surface Pro on Windows 10 Pro (Tested on Microsoft Edge & Google Chrome)

### **Desktop** 

The website was tested on the following browsers on Apple iMac running OS Catalina 10.15.7 :

* Google Chrome - VVersion 87.0.4280.88 (Official Build) (x86_64)
* Apple Safari - Version 14.0 (15610.1.28.1.9, 15610)
* Mozilla Firefox Version 78.0.1 (64-bit)

The website displayed well on all of the above browsers and devices. 
All interactive elements were tested and found to be working correctly except for the issues detailed below.

### **Issues**
1. On the Manage Types page a couple of the type cards were not aligning correctly in a block.
2. Found through testing that the user was returned to the home page instead of their profile after adding a poem. 

### **Fixes**
1. The cards were auto resizing to different lengths on tablet size screens. This issue has now been resolved by adjusting the title sizes.
2. Made sure to redirect to the users profile after poem was successfully added. This issue has now been resolved.  


### **Code Validators:**

The following websites were used to validate the code and there were no errors except for a single line indentation in python code that was easily fixed:
A few warnings were displayed with the html validator but these related to Jinja templating being in the code as it was unexpected. There were no errors in the html itself. 

HTML - [W3C Markup Validation Service](https://validator.w3.org/#validate_by_input)

CSS - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

Javascript - [JSHint javascript code analysis](https://jshint.com/)

Python - [PEP8 Online Check](http://pep8online.com/)