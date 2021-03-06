![responsiveimage](readme/amiresponsive.png)

Willmore's Site Setups
---
## Table of Contents

- [**About**](#About)
- [**UX**](#UX)
    - [Goals](#Goals)
    - [User Stories](#User-Stories)
    - [Styling](#Styling)
    - [Wireframes](#Wireframes)
- [**Features**](#Features)
    - [Existing Features](#Existing-Features)
    - [Potential Future Features](#Potential-Future-Features)
- [**Technologies Used**](#Technologies-Used)
- [**Testing**](#Testing)
- [**Code Validation**](#CodeValidation)
- [**Deployment**](#Deployment)
    - [Live Website](#Live-Website)
    - [Repository Link](#Repository-Link)
    - [Running Code Locally](#RunningCode)
    - [Deploying to Heroku](#Deploy-to-heroku)
- [**Credits**](#Credits)

---

## About

The reason as to why I created this website is because I have worked for multiple different companies that do not have a centralised point to manage site installations for IT equipment. 

This has been in the construction industry all the way to working for an MSP. 

The mission was to reduce the amount of backlog and paperwork that is created by all different users trying to add the same information in as well as assigning and tracking tasks. 

The website has the ability for users to edit or delete tasks however this is only doable for their own tasks and not other users. This is managed by an if statement within the tasks.html page.

---

## UX

### Goals

The goals of the website were: 
1. To hold information on what tasks were needed to be done at which location on which date. 
2. The website must allow users to have their own logins instead of using a shared account - this leads to more accountability if a task is not added or completed. 
3. The website must show correctly on all devices from laptops to mobile phones.

---

### User Stories

From the designer's point of view:
- The site needs to be easy to use and navigate around due to the nature of the product. 
- The site needs to be accessible on all devices to ensure that engineers in the field can view it on their phones.
- New tasks must be easy to add to ensure that the user experience is good and not too complex for people to understand. 
- The site needs to be easily modified to allow the creator to sell the site to other companies to bring in revenue. 

From the users point of view:
- I need to be able to add new tasks in without the hassle of navigating through different links.
- I need to be able to add new locations in without navigating through different links.
- I need to be able to edit and delete tasks if I accidentally input it wrong or it's not needed anymore.
- I need to ensure that no one else can delete any of the tasks that I have entered in.

---

### Styling

The website must be easy to read and use whilst ensuring that the different functions are separate from the main colour scheme. I used a plain white background to ensure that nothing is hard to read if I added a picture to the background. To ensure that the colour scheme did not differ I used the same grey in the nav bar, the footer as well as the pop out accordion. I used a red colour for DELETE and a light blue colour for EDIT - this is maintained throughout the entirety of the site. 

For the font, I used Google Font's Roboto with Sans Serif as the backup just in case the Google Fonts did not load.

---

### Wireframes

Wireframes - [Wireframes](readme/wireframes/wireframes.pdf)

---

## Features

### Existing Features
- The navigation menu shows at the top of the page with the links on the left hand side however this will shrink to a hamburger icon on smaller devices and show on the left hand side. 
- Users are able to login/register - it will display a message if an incorrect username or password has been entered. It also displays a message if a username already exists in the database.
- Certain links will only show if the user is logged in, there is a link for adding, editing and deleting locations however this has been locked down to either the user "admin" or "lukewillmore". 
- Tasks are written in collapsible headers that popout which can be expanded to view more information in that particular task.
- The footer is fixed to the bottom of the page on all pages.
- The due date field is dd/mmmm/yyyy.
- There is a search function for users to be able to search for current tasks that are in the database. 
- There is an ability for users to edit and delete their own tasks however not other users.

### Features Left to Implement: 
- Completing tasks - this is to ensure that when tasks are completed they do not get deleted.
- More defensive programming - added the below if statement to ensure that a user to has to be logged in before manually navigating to the URL:
```
if "user" in session.keys() == True:
return redirect(url_for("login")
``` 

---

## Technologies Used
- Materialize
    - Materialize was used for page structures, theming and features such as NavBars, Collapsible, Footer.

- HTML
    - HTML was used for the main structure of the website.

- CSS
    - CSS was used to style and change sizes and positions of different items where Materialize was not able too or enhancing the styling that Materialize used.

- JQuery
    - JQuery was used for Materialize features that needed javascript functions. 

- Python
    - Flask
        - Flask was used for rendering templates, URI's, Redirects, Requests, Returns and Flash messages.
    
    - BSON
        - BSON was used to access the data in MongoDB and to access the ID's from the database.
    
    - Werkzeug
        - Werkzeug was used to hash password entries when registering, logging in to the site and encrypting on MongoDB.

- MongoDB
    - MongoDB was used to store all of the data used for the website.

- Google Chrome
    - Chrome inspect and developer tool was used for testing the website on different devices.

- Google Fonts 
    - Google Fonts was used for the font of the website.

- Font Awesome
    - FA was used for the icons on the forms and buttons.

- Balsamiq
    - Balsamiq was used to create the wireframes.

## Testing

### Main Testing

Throughout the entirety of the project, I have been testing the app in a web browser testing the functions and features that I have added and correcting the issues as I go. 

### Responsive Testing

To check how the site ran on different devices, I used Am-I-Responsive and inspecting in Google Chrome Developer Tools. I also pushed the app to Heroku to test throughout the project to test on other devices (iPhone, Wide Screen Monitor and iPad).

Throughout the responsive testing, I was testing on all devices and screen sizes the hamburger icon and side menu, the navigation and links on bigger sizes as well as the footer. 

### Additional Testing

I also carried out the following: 
- Adding users, tasks and locations to ensure that it passed through to the database. 
- I deleted tasks and locations to ensure that it deleted it from the database.
- I edited tasks and locations to ensure that the information pulled through to the edit page as well as updating it in the database. 

### Code Validation
- W3C Markup Validation for HTML.
- W3C CSS Validation Service was for validating the custom CSS code (custom code not being the Materialize CSS).

## Deployment

### Live Website Link
https://site-setup-todo.herokuapp.com/

### Repository Link
https://github.com/DrogrinHunter/site-setup-todo

### Running Code Locally

To deploy the project, the following is required: 
- Python3
- Github account
- Heroku account
- MongoDB account

To create a clone of the project, follow the below: 
1. Login into GitHub and browse to the specified URL.
2. Click Code and open with GitHub Desktop.
3. Follow the prompts in the GitHub Desktop Application.

## Deploying to Heroku

Heroku allows us to host Python projects which can have more features than static sites which is what GitHub allows.

### Creating Heroku App
1. Create an account on www.Heroku.com.
2. After going through the account setup and signing in, you will be on the Heroku dashboard.
3. You can click your chosen development language, Heroku will provide some helpful tips and tutorials about how to use it with Heroku.
4. From the dashboard, click "Create New App".
5. Enter a name for your app, it must be unique and only contain letters, numbers and hyphens. 
6. Choose a region that is closest to your Country. 
7. Create the app.

### Connecting Git repo to Heroku
1. At the top of the screen, find the "Deploy" tab.
2. Find "Deployment Method" and then "GitHub" from within the tab.
3. In the search bar, if you have multiple different repo's, search for the GitHub repo.
4. At this point, do not click "Enable Automatic Deployment" but instead click "Connect".

### Creating the Requirements.txt file
1. Heroku needs the requirements file so it knows what language is being used and the dependencies.
2. The quickest and easiest way to create this is to type, in the console: pip3 freeze --local > requirements.txt. 
3. Wait for Heroku to install what it needs to be able to run the project. From there, it will deploy to Heroku however if you try to open it then you will see an error - you will need to do the next step.

### Creating the Heroku Procfile
1. A Procfile is a specific file that Heroku uses in order to know how to run the project.
2. To create this, refirect an echo command by typing: echo web: python run.py > Procfile. *Please note - the capitalised P is crucial*.
3. Git add this, commit it with notes then push it GitHub. 

### Setting up the env.py file for the environment variables
1. Make sure to have created a .gitignore file and add the env.py file into it. 
2. The convention for the file holding the environment variables is "env.py".
3. In the env.py file, be sure to place the IP, PORT and any secret keys you are working with.
4. You can also set up the links between the Mongo DB (database) - please ensure to install the flask-pymongo and dnspython to allow the Flask application to work with MongoDB.

### Entering the variables into Heroku's config vars.
1. On the Project's Heroku page, go into the settings and scroll down to "config vars".
2. Add the information from your env.py files into the Heroku project - the reason for this is because the env.py file is not pushed to Heroku as it is ignored by the .gitignore files and GitHub / Heroku do not have access to this file which is vital for the running of the project.
3. Add the variables into the config vars as key-value pairs.
4. In the Heroku settings page, click "Enable Automatic Deployment". 
5. Under this section, in the "Manual Deploy" section choose the master branch of your project and click "Deploy Branch".
6. You will now be able to open the project via the "Open App" button.


## Credits

### Code 

I used the following links to help with this project:
- Code Institute's task project for basic setup and linking to the MongoDB. 
- https://stackoverflow.com/ - for various issues when writing queries in Python.
- https://www.w3schools.com/python/default.asp - for extra help with Python.

### Content

All content used for the site, whether Locations or Tasks are based on my current employer however it's been designed to be utilised for different companies.

### Acknowledgements

I would like to thank the below for help and guidance:
- Miguel Martinez (Mentor)
- The Slack community for the ability for me to search for similar issues that I've had. 
- Code Institute for the programme and the task mini project. 