# challenge-simulation

Requirements:
	• Create a page that the trainee should only view and save the simulations that their client has access to.
Assumption:
	• No API connection other than listed APIs(No client update API).
	• No responsive design.

Tech Stack:
	• Frontend: React
	• Backend: Python, Flask
	• Protocol: RestAPI

API End points: 
	• GET /trainees - Retrieve list of existing trainees
	• GET /trainees?clientId={clientId} - Retrieve the trainee that the client belongs to
	• POST /trainees - Create a trainee with the body of firstName & lastName
	• GET /clients - Retrieve list of existing clients [2.a]
	• GET /clients?traineeId={traineeId} - Retrieve the client that the trainee belongs to
	• POST /clients - Create a trainee with the body of name & code
	• GET /simulations - Retrieve list of existing simulations [2.b]
	• GET /simulations?traineeId={traineeId} - Retrieve the simulation that the trainee belongs to [2.d]
	• POST /simulations - Create a simulation with the body of name
	• POST /client-simulation-mapping - Create a client-simulation mapping [2.c]

Setup Instructions:
	• Cloning git repository
		○ Clone URL: https://github.com/FoxeyesJK/challenge-simulation.git
		○ cd backend
	• Installing virtual environment & packages
		○ pip3 install virtualenv - Create isolated Python environments
		○ virtualenv env
		○ source env/bin/activate or source env/scripts/activate
		○ pip3 install -r requirements.txt - Install all required packages from requirements.txt
		○ python app.py - Run the application, leave this running.
	• Creating initial data to the sqlite database
		○ Open a new terminal. Make sure app.py is running from the other terminal.
		○ cd backend
		○ source env/bin/activate or source env/scripts/activate
		○ python test.py - Create initial trainee, client, and simulation data as provided
	• Open frontend application
		○ cd frontend
		○ cd app
		○ npm install - Install all packages that were listed in package.json
		○ npm start - run react application
	• Select trainee from Dropdown list
	• Assign multiple simulations to the trainee & client
	• Click save to store the data
  
  ![image](https://user-images.githubusercontent.com/25089799/109428334-ae509680-79c4-11eb-977e-5b5167ff48fc.png)
	
	
Reference
	• https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
	• https://flask-restplus.readthedocs.io/en/stable/marshalling.html
  • https://react.semantic-ui.com/

