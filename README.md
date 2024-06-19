Celestial Archive Project

- the purpose of this project is to create a dataset management system where users can explore a 
public library of datasets, modify and download them for use.


Example Workflow:
Sign Up/Login: Users sign up and log in to access the system.

Homepage: Users are directed to a homepage where they can search through the public library of datasets and
see their personal library contents.

Dataset Exploration: Users search for and find a dataset of interest in the public library.

Personal Library Management: Users copy the dataset into their personal library, where they can perform various operations 
such as sorting, filtering, adding entries, and deleting entries.

Download: Users download the modified dataset for personal use.


Current Implementation:
- Functionality Focus: The current implementation focuses on the core functionality of the system.
- Interactive Terminal: The application is controlled through an interactive terminal, with no user interface yet.
- Data Storage: Pickle is used to store and maintain app data, with no database setup currently.

Future Implementation:
- User Interface: A user interface will be added for more intuitive use.
- Database Integration: A database will be used to store user data and public library contents.
- O-Auth Integration: O-Auth will be implemented for secure login and signup.
- Expanded Operations: A more comprehensive list of operations will be available for datasets in the personal library.
- Download Formats: The ability to download datasets in a variety of formats will be added.
- Addition of Calender of envents: The homepage will display a calender of events including upcoming conjunctions, eclipses, meteor showers, etc

Intended Use:
The project is designed for a community to collectively maintain a public library of celestial object datasets (e.g., stars, nebulas, galaxies). 
Together, they can build a robust repository for personal use in classification models, data analytics, and more. 
The system allows users to modify datasets, ensuring they get tailored datasets that meet their specific needs.

Running the app:
step 1:
create a virtual environment (conda reccomended)
step2:
activate the virtual environment
step 3:
install dependencies (example with conda)
conda install pandas
step 4:
run the application
python -m app.app_functionality.runner
