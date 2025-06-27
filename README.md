Follow the steps below to set up and run the project:
1. Open your terminal and navigate to the project root directory.
2. Run the following command to create a virtual environment:
   
   ` py -m venv . `
3. Close and reopen your VS Code editor to ensure it detects the virtual environment.
4. In your terminal (Command Prompt), navigate to the `Scripts` directory:

  ` cd Scripts `
  
5. Then activate the virtual environment by running:

  ` activate `
  
You should now see the project name in parentheses `(e.g., (project-name))` before the prompt.

6. Navigate back to the root project directory:
  
   ` cd .. `
   
8. Install the required dependencies:

  ` pip install -r requirements.txt `

8. Once installation is complete, run the backend server:

  ` py run.py `

10. You should see a message indicating the server has started successfully.

Adding migration scripts:

1. pip install alembic

2. alembic init alembic

    now you can see the below
      a. alembic directory
      b. `alembic.ini` file

3. modify `alembic.ini` file 
    in line 86 update the URL With your database connection string.
  
4. in alembic directory you can find `env.py` file

    modify `env.py` as below

      add - from shared.database.database import Base
      target_metadata = Base.metadata <- line 23


5. after all use the below commands for migration

    a. alembic revision --autogenerate -m "your migration message"

    by running the above command alembic will compare the old and new changes in the models file and the new changes will be added to new revision with a unique id.

    and you can observe a new file created in `alembic.versions` directory.

6. for updating the database run the below

    a. alembic upgrade head