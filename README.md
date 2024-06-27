# CAPSTONE - GroupUp

## Screencast on YT

**Demo video:** [Watch Demo](https://youtu.be/aQwq971m4FQ)

## Description

Welcome to GroupUp!

This is my Final Project for the course CS50’s Web Programming with Python and JavaScript. It's crafted using Django, HTML, CSS, JavaScript, Python, and Bootstrap.

Group up was born from a simple idea: connecting people through shared passions and shared friends. Seeing two friends of mine bond over a mutual love for bouldering inspired me to realize the potential for friendships waiting to be formed among different groups of my friends who may not have met yet.

The app aims to make it effortless to find companions for activities you enjoy, whether it's hiking, cooking, gaming, or any hobby or interest you're passionate about. It allows users to discover like-minded individuals because they already share friends, create activity plans, and join groups centered around shared interests.


## File Structure
The project has the following structure:

- `capstone/`: Main application directory. It contains the following important files:
    - `migrations/`: Contains Django migration files. 
    - `static/`: Contains static files like CSS and JavaScript
    - `capstone/templates/`: This directory contains all the HTML templates. Here are some of the key templates:
        - `layout.html`: This is the main layout file for the application. It includes the navigation bar and the structure for all pages.
        - `index.html`: This is the template for the home page of the application. It displays a list of all groups and provides options to join a group or click on the group for details.
        - `group_detail.html`: This template displays the details of a specific group.
        - `create_activity.html`: This template is used so the user can create a new Acitivity
        - `create_group.html`: This template is used so the user can create a new Group
        - `calendar.html`: This template is used so the user can view his/ her calendar to check events of the groups he/ she is part of.
        - `login.html`: This template is used for the login page.
        - `signup.html`: This template is used for the user registration.
    - `admin.py`: Configuration for the admin interface.
    - `forms.py`: Contains form definitions.
    - `models.py`: Defines the data models for the application, like Group and Activity.
    - `test.py`: Contains the tests for the project.
    - `urls.py`: Defines the URL structure of the application.
    - `views.py`: Handles the logic of the project, like joining a group, creating a group and more.
- `project5/`: Contains settings and configuration files.
- `db.sqlite3`: SQLite database file.
- `README.md`: The current file.

## Distinctiveness and Complexity
GroupUp is a unique web application that stands out from the projects in this course. Unlike a social network, GroupUp is not focused on posting content, liking or disliking posts, or following and unfollowing users, like in the previous developed Project 4. Instead, it is centered around the concept of creating and joining groups based on shared interests and activities and viewing the events in a personal calendar - every user has its own calendar with their own group events - This makes it distinct from Project 4.

GroupUp is also not an e-commerce site. There is no concept of uploading listings for sale or bidding on items, which distincts from Project 2.

The application utilizes Django on the back-end, with models defined in [`capstone/models.py`](capstone/models.py) like  `Group` and `Activity`. These models are used to store and manage data of groups and a set of activities to chose from for those groups that users can create and join.

On the front-end, JavaScript is used to enhance the user experience and provide dynamic behavior. For example in the creation of the calendar.

GroupUp is designed to be mobile-responsive, so users can use GroupUp on different devices. This is achieved through the use of Bootstrap for styling.


## How to Run the Application
Run the Django server, with: python3 manage.py runserver

Open your web browser: http://127.0.0.1:8000/.


## Additional Information
The application is mobile-responsive and uses Bootstrap for styling. It also uses JavaScript for dynamic behavior on the front-end.

This project is a culmination of the lessons learned in CS50’s Web Programming with Python and JavaScript. It showcases the use of Django and Python for back-end development, JavaScript for front-end interactivity, and Bootstrap for the design.
