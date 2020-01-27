Welcome to Project Partner

To get started fork this repository and clone it down

You will need to activate the environment projectpartnerenv from the Scripts directory. If you are using a window machine
you will need to do this from the command prompt.

1. cd into projectpartnerenv
2. cd into Scripts
3. run command activate.bat to turn on projectpartnerenv

Once the environment is activated you will need to run the commands to migrate and create the database

In the root of the directory type commands
1. python manage.py makemigrations projectpartner app
2. python manage.py migrate

To Start the server
1. cd back to the root of the project - projectpartnerproject
2. type command python manage.py runserver

Open the database in your preferred SQL software

Project Partner is an app to help users organize their home projects, associated materials and costs. The goal is to reduce trips to the hardware store, store details on materials used to complete the project, and track the costs of the project.

New User As a first time user you will be asked to register a new account.

Once registered you will be able to create a new project from the Home page or the Projects page. The new project creation
process is three steps.

Step 1: add the details of the project you want to track
Step 2: add the tools associated with the project. The dropdown will allow you to choose multiple tools from your tool inventory. Clicks as many boxes as necessary to add all the tools you will need.
Step 3: add the materials associated with the project. To start you will only need to add the name of each material for your
project. Later you will be able to update the material to add details, costs, and quantities.

Navbar Tools - here you can add new tools to your inventory to be used in various projects. You will be asked to mark

whether or not you own the tool so you can add it to your shopping list for the project.

Navbar Materials - here you can track all the materials you have in all your projects.

Navbar Projects - here you can see all your Open and Closed Projects

Navbar Home - here you can see only your Open projects

Project Details - clicking this button will allow you to see all the projects details, tools, and materials.

Edit Project - clicking the edit button on the Project Details page will allow you to edit all aspects of the project details, delete/add tools, and delete/edit your materials to add description, cost, and quantities.




