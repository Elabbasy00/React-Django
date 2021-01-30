Setup Instructions
--------
Install Required Python Modules


`pip install -r requirements.txt`


*Start Web Server*

`python manage.py runserver`


------

Install Node.js
Install Node Modules

First cd into the frontend folder.

`cd frontend`


Next install all dependicies.

`yarn `

Compile the Front-End


Run the production compile script

touch webpack.config.js 

`NODE_ENV: JSON.stringify("production")`


`yarn  build`

or for development:

`yarn dev`