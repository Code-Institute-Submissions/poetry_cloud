# **Poetry Cloud Website**

* Poetry Cloud is a useful and accessible app for poets allowing the user to manage their poems in one convenient place.
* Unregistered users can search the database on the homepage to view poems by author, title or keywords. 
* Users can register and login to access their personal profile which lists only their poems.
* Once registered, users can add, view, edit and delete their poems as they choose.
* When adding new poems, users may select from a list of popular poetry types such as Haiku, Sonnet or Limerick, for example.
* An admin user can create, read, update and delete the poetry types themselves.


Link to website - https://poetry-cloud.herokuapp.com/get_poems

### User goals:
* To be able to store and manage poems in a convenient online location. 
* To be able to register an account and login to view their personal profile featuring poems they've added.
* To be able to add, view, edit and delete their poems. 
* To be able to share their work with a community of fellow authors and poetry fans.
* To be able to search the database and find work by fellow authors, by title of poem or keyword. 

### Business goals of the website:
* To provide a useful and convenient app for poets to store, share and manage their work.
* To promote poetry and encourage poets to develop a body of work and share it with their community.
* To enable users to contribute their own poems or share their favourite poems by other writers. 
* Build a minimal viable product to test the market and establish interest. 

## **UX**

The user types can be defined as one of the following:

* Amateur/professional poets.
* Poetry readers/fans.
* Publishers.
* Writers or bloggers of poetry. 

These groups make up the target audience and each user type has a reason or need to visit the site.

The site has been designed to meet those needs as well as the needs of the business.

Clear sections which relate specifically to all of the user types above are built into the website's design.

A mobile first approach was taken to create this project with consideration of ease of use and navigation to each of the features/sections. 

### **User Stories**

1. As a poet, I want to document my work so that I can be organised and have each item readily available. (Profile page with a list of my poems. Search feature on home page to find poems)
2. As a poet, I want to add/store my poems so that I can more easily manage them in the future. (Add poem form, Edit poem form, view all in in profile or home page, edit and delete poems from profile or home page.)
3. As a poet, I want to be able to add new poems to existing types such as Haiku or Sonnet so that I can build a body of work. (Easily add a new poem to an existing poetry type with add poem form)
4. As a poet, I want to be able to view all of my poems in one place so that it’s easy to see and manage my work. (Profile page)
5. As a poet, I want to be able to find a particular poem in my collection so that I can view, edit or delete it. (Search function on home page)
6. As a poet, I want to be able to submit the title and text of my poems, so that I can add them to my collection and identify them later. (Text area on add poem form)
7. As a poetry fan, I want to be able to submit poems by well known authors, so that I can store my favourites and share with the community. (Text area on form to add any poem text. Name of author/submitted by clearly shown in listing)
8. As a poet I want to be able to share my poems online with the poetry community and see the work of my fellow poets. (Poems auto display on home page and return specific search results via search function. Social links to share from.)
9. As an administrator of the site, I want to be able to add, read, update and delete poetry types so that I can provide the best experience for the user. (Manage Types page only avaiable to admin)


Further information and screenshots showing how this project meets the user's needs can be
found in the separate [TESTING.md](https://github.com/JohnW876/TESTING.md) file.

### **Data design**

When designing the database for the app I stuck closely to the needs represented in the user stories. These user stories guided the creation of three separate collections of users, types and poems. The collections are shown here below in their field and value pairs. The data records are stored in MongoDB as BSON documents with unique id numbers.

* Users Collection - In order for users to manage a store of their own uploaded poems it was obvious that authentication and a personal profile would be a key feature of the app so therefore a user collection would be required to store the usernames and passwords of registered users.

![Users Collection](documentation/screenshots/users-coll.png)

* Types Collection - Users need to be able to add certain types of poem. Research showed 13 popular types so I decided to build those into a form with a selection dropdown for the users to choose from when adding or editing poems. These types would also need to be managed by an admin user with CRUD functionality. This required the creation of 13 documents in the database represented by the diagram shown below.

![Types Collection](documentation/screenshots/types-coll.png)

* Poems Collection - When adding a poem to the database I designed the form to allow the user to first choose from the established list of poem type names. Then users can input the poem title, author and the text of the poem. Finally the database would store who the record was created by using the username. This would allow users to have full CRUD functionality and store poems in their own personal profile.

![Poems Collection](documentation/screenshots/poems-coll.png)

* Index - I created a text index on the poems collection to allow users to search the database for results based on fields relating to poem title, poem author or a word used in the poem text. 



### **Wireframe mockups:**
Below is a link to the project's wireframe mockups which were created using Balsamiq Wireframes software prior to development to help with visualisation of features and layout. 

https://github.com/JohnW876/poetry_cloud/tree/master/wireframes
 
Wireframe mockups were created for every page of the website at mobile, tablet and desktop sizes and I referred to them throughout development. 


### **User Expectations:**
* What will they expect to see? - Users will expect to see an intuitive app with accessible features and a well designed user interface. 

* Does the site look credible and trustworthy? - Many elements will contribute to the first impression of a trustworthy site. These include, clear and intuitive navigation, good design and functionality. 

* Does the site offer what the user wants? - The features will need to meet the user's goals whilst delivering expected functionality and a valuable user experience.

* Does the site seem valuable enough for users to stay and return? - The features, functionality, usability and design will need to meet or exceed expectations to provide the value needed to ensure continued usage.  
  

### **Market Research:**
* Online research shows a number of apps to help writers work on their technique and improve their writing skills.
* There are also a good number of apps that deliver work by famous poets in either spoken word or purely textual formats.
* However there are very few that allow any user, regardless of skill level, to contribute their own work to a community and to create their own collection and/or manage a store of their work. 
* This app aims to fill that gap in the market and be available to all poets as an accessible and useful tool to help develop their body of work.


### **Visual Design:**
* Colour scheme -
  When designing the site I wanted to convey themes relevant to poetry such as passion and human emotions. In colour psychology these themes closely align to red which suggests passion, danger, life and love. 
  Red is used consistently throughout the site in the key elements such as the brand logo, page headings, edit form buttons, form icons, nav mobile dropdown and the social footer background. 
  With red as such a dominant colour it would not help to introduce another strong colour but does balance in a classic scheme with black, white and grey and is suggestive of paper and ink colours and poetry writing.

* Imagery - I also wanted to think of the design from a poet's point of view giving an analogue writer's feel to the homepage with background images of paper textures. 
* This was also the reason I chose to use Materialize CSS to help build the site as I felt the Material Design ethos offered simplicity whilst being inspired by paper and ink and was appropriate for poetry.
* Typography - For the main body of the site including headings and navigation, the chosen font is Open Sans for clarity and legibility. I did consider a script type in reference to handwriting but wanted to keep the site looking modern and accessible and thought a script would look too old fashioned and stuffy!
* For the poem text I used 'pre' tags in html which helps with the problem of how to display poems with appropriate line breaks. The Courier font used with the poems allows the text to stand out and is more easy to read from a user's perspective. 
* The brand logo uses Averia Serif Libre font which is intended to be a warm and friendly rather than too stiff and formal. 
  
## **Features**

* The site has clear, simple and intuitive navigation.

* The site allows anyone to search the database for poems submitted by registered users.

* The site features authentication so that registered users can safely login to their profile and view their submitted poems. They can also add, edit or delete poems as they wish.

* A site administrator can login and manage the poem types. They can add, update or delete poem types as they wish. 

* The site is responsive to mobile, tablet and desktop screen sizes. 

* The footer contains links to social media websites and also to related poetry orgs and websites. 


### **Homepage**
There are a number of carefully chosen features on the homepage:

* Brand name and logo linking back to homepage.
* Site navigation links which are responsive and collapse into hamburger icon with side popout navbar on smaller devices.
* Navigation links are initially limited to 'Home', 'Login' and 'Register' and reveal further features once logged in.  
* Welcome header.
* Main feature headings on notepaper image background to convey the analogue theme. 
* Responsive images to complement the theme and design. 
* Search form to allow users to search the database of poems.
* A list of poems submitted by the community of registered users featuring pop out poems when clicked.
* If logged in, users may edit and delete poems they have submitted from both the home page and from their profile. 
* Responsive footer featuring social media icon links and useful links to poetry orgs and websites.

 
### **Login Page**
* A simple login form which requires the user to enter their previously registered username and password.
* Once registered and logged in, further nav links reveal to 'Add Poem', 'Profile' and 'Log Out'.
* The login button on the form changes to outline the type in black on hover and makes use of material design waves effect when clicked.
* There is a link to the register page if the user has yet to register.
* A successful login displays the flash message "Welcome, username!" and redirects the user to their Profile page.

### **Register Page**
* A simple form allowing the user to create a username and password.
* Register button with styling and effects consistent with the Log In form.
* Link to Log In page if already registered.
* Flash messages display appropriately based on user input such as "You have successfully registered!"

### **Profile Page**
* Once registered and logged in the user can visit their 'Profile' from the main navigation and view a list of their submitted poems by title and author.
* The username appears at the top of the profile page.
* When clicked, the poem pops out of the list and displays the poem type, the text of the poem itself and who submitted it.
* I have designed the data to allow differentiation between the author of each poem and who submitted it so that users could add either their own work or work created by others.
* Users are able to edit and delete poems from their profile page with the relevant buttons displayed next to each poem listed. 
* Clicking on the 'Edit' button opens a new page with an Edit Poem form.

### **Edit Poem**
* A simple form with dropdown selector and input sections allow the user to update an existing poem.
* Dropdown selector allows the user to select from one of thirteen poem types such as Sonnet, Haiku, Limerick etc. 
* With user inputs to add the poem's title and author.
* A text area to allow the text of the poem to be inputted. 
* Buttons at the bottom of the form allow the user to 'Cancel' the edit or to 'Update' the changes.

### **Add Poem Page**
* This key feature has a link in the main navigation at the top of the page.
* Users are able to add a new poem to their profile using a simple form. 
* All the input boxes are the same as the edit form above but there is a single add poem button. 

### **Manage Types Page (Admin user only)**
* Once logged in as an admin user the Manage Types page appears in the main navigation.
* There is an option button to add a new type at the top of the page.
* Existing types can also be edited or deleted using the buttons displayed.

### **Log Out**
* Once logged in the 'Log Out' link appears in the main navbar and when clicked the user is redirected to the log in page.
* Flash message displays appropriately, "You have successfully logged out"

### **Flash Messages**
* User friendly flash messages display on the screen to guide and inform the user at key events.

### **Features to implement in future**
When considering the trade off between importance and viability, the following features could not be implemented at this stage but would make valuable additions in future and improve the user experience.

* Image submissions - I would like to have allowed users the option of uploading and displaying images of their original writing to enhance the user experience but this wasn't a recommended option with MongoDB at the present time due to a number of issues.
* I would like to give registered users the option to submit poems to the community or to keep their poems private. I would build this into the profile sections so that users can toggle this on and off as they wish.
* I think it would be great to add social share buttons to each poem listed to allow the user to quickly post their poems on their social pages.  

## **Languages Used** 
* HTML, CSS, Javascript and Python are used in this project.

## **Technologies Used**
* [Gitpod](https://www.gitpod.io/) Gitpod IDE was used to develop the website.
* [Materialize CSS](https://materializecss.com/) A Material Design framework used to make the website responsive on all devices.
* [FontAwesome](https://fontawesome.com/v4.7.0/) Icons were used in social links and forms. 
* [Google Fonts](https://fonts.google.com/) Font styles chosen for the website were sourced from here. 
* [Balsamiq Wireframes](https://balsamiq.com/) Used prior to commencing coding to help with UX/UI design and were consulted throughout development.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) To inspect the code, test the data and preview changes on all device sizes.
* [Heroku](https://www.heroku.com/) To deploy the site.
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) To host and manage all data for the app. 


## **Testing**

Information regarding testing can be found in this separate [TESTING.md](https://github.com/JohnW876/TESTING.md) file.

## **Deployment**

This project was developed with the Gitpod IDE and then pushed to GitHub.

**The following steps were taken to deploy the project to GitHub pages.**

1. Login to GitHub.
2. Select JohnW876/Jokes-Quotes from the list of repositories.
3. Click on the Settings heading near the top of the page.
4. Scroll down to the GitHub pages section.
5. Under Source click on the 'None' button dropdown and select Master Branch.
6. The page will auto-refresh.
7. Scroll down again to the GitHub pages section and copy the link to the newly deployed website.
 - https://johnw876.github.io/Jokes-Quotes/

The Development Branch and the Master Branch are identical at the time of this project's submission. 

**How to run this code locally:**
1. Navigate to the github repository via this link - https://github.com/JohnW876/Jokes-Quotes
2. Click on the green dropdown labelled Code.
3. The box will display as below.

![Screenshot Clone Dropdown](/assets/screenshots/clone.png)

4. Copy the URL in the box to clone with HTTPS.
5. Open your preferred IDE.
6. Change the working directory to the location you want the cloned directory to be made.
7. Type git clone and paste the URL from step 4.
8. Press enter to create your local clone. 

**To run on Gitpod:**
1. Install the Gitpod browser extension. See link to instructions here - https://www.gitpod.io/docs/browser-extension/
2. Once you have the Gitpod extension installed then simply click on the green Gitpod button as shown in the screenshot above and it will create a new workspace for you. 

## **Credits**

### **Content**
All site content, except for example poems, was written by John Withey.

### **Media**
All images used in this project were created by the talented photographers at Unsplash.
https://unsplash.com/ 

### **Code**
I borrowed code from the Code Institute's Task Manager Mini Project and appropriated to help with building CRUD functions, search and authentication functionality.
* https://www.youtube.com/watch?v=y72Dq3GRxhc&feature=youtu.be

Form validation for select dropdown. Source code copied from Code Institute Mini Project.
* https://github.com/Code-Institute-Solutions/TaskManagerAuth/blob/main/04-AddingATask-WritingToTheDatabase/02-materialize-select-validation/static/js/script.js 

I used this code from Stack Overflow to change the default colour of the select options dropdown in my forms.
* https://stackoverflow.com/questions/54727612/materialize-css-dynamically-change-the-background-and-text-color-of-the-select

I used this code from Stack Overflow to help create responsive pre tags.
* https://stackoverflow.com/questions/34691470/responsive-pre-tag

From Materialize CSS I added code to help build my forms and collapsible popout lists.
* https://materializecss.com/

### **Acknowledgements**
Poetry can often be seen as stuffy and a bit inaccessible. I wanted, to create an app that let's anyone have a go and share it with a community of like minded people. 
On this app you can write anything you like as a Free Verse poem or be more specific and write a Sonnet if you want! 
It's a simple app for aspiring poets or even more established ones but hopefully it's a useful one that people will enjoy and find accessible. 

I'd like to thank my mentor Aaron Sinnott, once again, for helping with positive and constructive feedback during the project! 

 