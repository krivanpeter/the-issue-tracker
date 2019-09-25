[![Build Status](https://travis-ci.org/krivanpeter/the-issue-tracker.svg?branch=master)](https://travis-ci.org/krivanpeter/the-issue-tracker)

# The Issue Tracker

I'm a student at Code Institute and I've reached my fifth and also my last milestone project which was to create this webapplication.
I needed to use all of my knowledge I got through the course.

The website can be viewed [here](https://the-issue-tracker.herokuapp.com/)
## UX

This website is made for users who use a given software.
The users can read the news, report bugs, ask features and upvote them, so the developer team will know what to do first.
For transparency, there is a page with all the statistic about the page.
Users also can speak to each other via comments under every piece of news, bugs or features.

### User Stories
1.  Register/Login/Password Reset:
    * As a user I'd like to be able to register, so I can see the content of the page
    * As a user I'd like to be able to change my password, so I can log in despite a forgotten password
2. News/Features/Bugs
    * As a user I'd like to be able to see all the news, so I can know what the developer team has done
    * As a user I'd like to be able to see all the new reported bugs, so I can know what bug to report
    * As a user I'd like to be able to upvote bugs, so the developer team'll know what to do next
    * As a user I'd like to be able to see all the new asked features, so I can know what'll be in the next update
3. Comments
    * As a user I'd like to be able to talk with the other user, so I can know what they think about the page and the software
4. Packages/Cart/Purchase
    * As a user I'd like to be able to buy 'UpVote Packages', so I can upvote new features, so the developer team'll know what to do next
    * As a user I'd like to be able to see what's in my 'Cart', so I can purchase exactly what I'd like to
5. Statistics
    * As a user I'd like to see the information of the page, so I can know if anything's happened
6. Profile
    * As a user I'd like to see what I and other users have upvoted, commented or reported, so I can see what they like
    * As a user I'd like to be able to change my information (Name, Gender, Avatar etc.), so my profile can be accurate
    
## Features
### Existing Features

* Eye catching front page
* Registration / Password-reset / Login
* News 
    * allows users to read the recent news
* Feature - allows users to:
    * check all the asked features
    * upvote any of the features
    * ask new features
* Bug - allows users to:
    * check all the reported bugs
    * upvote any of the bugs
    * report new bugs
* Comments - allows users to comment under any piece of news, bugs or features
* Profile - allows users to:
    * see their own or other users' profile
    * see any reported/upvoted bugs and asked/upvoted features
    * change any detail about their own profile
* Packages - allows users to put any upvote package into their cart
* Cart - allows users to modify quantity of package(s) or delete them
* Purchase - allows users to buy the selected upvote packages, so they can upvote features
* Statistic - allows users to see information of the page
* (Superusers/Admins can add/change:
    * new piece of news
    * information of users
    * information of bugs
    * information of features
    * information of orders
    * information of comments
    * information of packages
    )

## Tech Used
### Front-end
* HTML, CSS and Javascript
    * Base languages used to create website
* [Bootstrap](https://getbootstrap.com/)
    * I used Bootstrap to give my project a simple, responsive layout
* [Font Awesome](https://fontawesome.com/)
    * For responsive and stylish icons
* [JQuery](https://jquery.com/)
    * I used JQuery for animations(transitions) and to display bootstrap modals
    * I used AJAX to partly handle page routing and to receive data from pages
* [Charts.js](https://www.chartjs.org/)
    * For creating charts on 'Statistic' page
    
### Back-End
* [Python language](https://www.python.org/)
    * Used for the whole logic. 
* [Django](https://www.djangoproject.com/) - Python Framework

### Packages/Modules
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Imaging Library for Python  
* [Stripe](https://stripe.com/gb) - Used to securely process online payments  
* [Dj Database URL](https://pypi.org/project/dj-database-url/) - a package that allows us to connect to a database url, allow to use DATABASE_URL environment variable to configure our Django application.  
* [Gunicorn](https://gunicorn.org/) - WSGI HTTP Server for UNIX  
* [AWS S3 services](https://aws.amazon.com/s3/) - used to store media and static files in deployment  
* [Django Storages](https://django-storages.readthedocs.io/en/latest/) - a collection of custom storage backends for Django  
* [Django Rest Framework](https://www.django-rest-framework.org/) - toolkit for building Web APIs
* [Sendgrid](https://sendgrid.com/) - An email API (used for password recovery emails)

## Database
SQLite3 database was used in development and Heroku Postgres in deployment.
<br>  
[Database Schema](https://raw.githubusercontent.com/krivanpeter/the-issue-tracker/master/static/img/IssueTrackerdb.png) - this is a representation of the Database Schema.

## Testing
Most of the page has been tested using django's built in testing tools, where not it was tested manually.
Separated test files were written for all applications.
They can be found in files with the name of ,,test_xy.py"

### How to run the tests
After [Local Deployment](https://github.com/krivanpeter/the-issue-tracker/blob/master/deployment.md) you need to run the following command:

    python manage.py test  

#### Manual Testing
* Cart:
    * Modifying Quantity:
     - Delete item
     - Modifying quantity to 0
     - Modifying quantity to a character
    * Remove Item
* Checkout
    * Checkout:
    - STRIPE handles payment form
* Comment
    * Reply to comment
    * Delete a comment
* Statistic
    * API:
    - Check statistics
    - Add new feature, statistic refreshes

Site viewed and tested in the following browsers:
* Google Chrome
* Microsoft Edge
* Mozilla Firefox  

## Deployment
You need to have Python installed.
You can download it from [here](https://www.python.org/)

You can view how to get the application up and running [here](https://github.com/krivanpeter/the-issue-tracker/blob/master/deployment.md)

## Credits
This Project has solely educational purpose. 
#### Media
The images for news page were obtained from [Pexels](https://www.pexels.com)
The default avatar used for profile application were obtained from [WikiMedia](wikimedia.org)
The photos used in the shop application were obtained from [FatSoundRecords](www.fatsoundrecords.com)
#### Acknowledgements
I received inspiration for this project from students of Code Institute.