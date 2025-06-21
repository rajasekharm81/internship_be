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
