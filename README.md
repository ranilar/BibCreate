# BibCreate
Create bibtex citations.

Tiimitapaamiset viikottain: 
Ke klo 10-12,
To klo 09.45-10.45,
To klo 11-11.30 (Sprintti)

## Links
Backlogs:
https://docs.google.com/spreadsheets/d/1VMvwVkrx3sCwMhOg9KaBRGVdFl2taQKhlVoZCgXNELQ/edit?gid=1#gid=1


## Installation Guide

### Follow these steps to set up and run the project locally:

#### 1. Clone the Repository.
```
git clone <repository_url>
```

#### 2. Navigate to the project directory.
```
cd BibCreate
```

#### 3. Create a .env file in the directory.
Add following contents to .env file.
```
DATABASE_URL=postgresql:///lowdodo # Replace with your database connection string
SECRET_KEY=<your_secret_key>    # Replace with your desired secret key
```

#### 4. Install dependencies.
```
poetry install
```

#### 5. Launch virtual environment.
```
poetry shell
```

#### 6. Run the program.
```
python3 src/index.py
```

