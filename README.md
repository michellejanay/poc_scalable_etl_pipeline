# Proof of Concept - Scalable ETL Pipeline

Hi! Welcome to the proof of concept scalabable extract, transform, load pipeline. This project was built using Python, Docker, PostgreSQL, Adminer and Grafana. The project was created over a 3 week period, originally uploaded to a repository as part of a private organization, while learning AWS for the project's current migration. As the project progressed, I picked up a ticket for Data Visualization. In order to start this task, I created a fully functioning proof of concept, installing Grafana using Docker. 

## Client requirements

As a user I want to:

- 
- 
- 
- Visualize sales data across multiple store locations


## How to run the app

#### Create a virtual environment
#Mac/Unix <br>
`$ python3 -m venv .venv`<br>
or<br>
#Windows<br>
`$ py -m venv .venv`


#### Activate virtual environment
#Mac/Unix<br>
`$ source .venv/bin/activate`<br>
or<br>
#Windows<br>
`$ .venv\Scripts\activate.bat`<br>
or<br>
`$ .venv\Scripts\activate.ps1`

#### Install requirements
#Mac/Unix<br>
`(.venv) $ python3 -m pip install -r requirements.txt`<br>
or<br>
#Windows<br>
`(.venv) $ py -m pip install -r requirements.txt`<br>

#### Run Docker
Make sure Docker is open and, in the src directory, run <br>
`(.venv) $ docker compose up -d`<br>
-create a table called 'miniproject'
-use sql-backup.sql to input data in database

#### Load Data to Database
In the src directory, run <br>
#Mac/Unix<br>
`(.venv) $ python3 load_to_db.py`<br>
or<br>
#Windows<br>
`(.venv) $ py load_to_db.py`

## How view Data in Adminer
Head over to<br>
`localhost:8080`<br>
in your browser. Use login details from environment file.<br>

## How view Data in Grafana
Head over to<br>
`localhost:3000`<br>
in your browser. Use login details from environment file.<br>
Click on the hamburger menu to go to Dashboards.<br>
Select 'New' > 'Import'<br>
Upload the files from the grafana directory<br>
Select 'Postgres' as the datasource.

## Project Reflections

#### Design and Project Requirements


#### Guaranteeing Project Requirments
 

#### Improvements


#### What I most enjoyed implementing
 

### Credits
[Noor](https://github.com/Hunzaa)
[Evans](https://github.com/e-ldn)
[Adam](https://github.com/Adam5510)
[Alex](https://github.com/AlexH1000598)