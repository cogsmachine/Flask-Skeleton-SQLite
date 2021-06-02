## flask_db Skeleton (SQLite)

- This repo is a flask framework that utilizes an Application Factory structure.

- The database that this app uses is SQLite.

- The run.py file launches the application, which was imported from init.py.

The app is within a folder called application and utilizes a blueprint called "main". You can create more blueprints by following the same structure as the folder called "home". Just be sure to load them into init.py file under app_context.

To launch this app, follow these steps:

1. Create a Dotfile with *SECRET_KEY = 'passphrase_of_your_choice'* or simply enter into the command line: *export SECRET_KEY = 'passphrase_of_your_choice'*
2. Go to the config.py file and set your desired location / path for the database

    - 'sqlite:////path/to/db/name.db'
    
    
3. In the command line:

    *flask db init*
    
    *flask db migrate -m "Some message of choice"*
    
    *flask db upgrade*
    
4. flask run or python run.py

- if this doesn't work, specify: 

    *flask run --host=0.0.0.0*
    
5. Go to the IP address

6. Enter a message and submit

7. Go to /messages/
    - you can now see the message left by the user, which is saved to the SQLite database


