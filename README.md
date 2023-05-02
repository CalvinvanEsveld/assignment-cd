---REPORT---

These are the components of my solution and how they relate to each other:

GitHub Actions: GitHub Actions is a feature of GitHub that allows you to automate tasks 
and workflows in response to events such as code pushes, pull requests, and issue comments. 
In this solution, we are using GitHub Actions to run tests and deploy code.

Ubuntu: Ubuntu is an operating system that is used as the target environment for
this solution. It provides the necessary infrastructure to execute the tests and deploy the code.

SSH: SSH (Secure Shell) is a network protocol that allows secure communication between two 
computers. In this solution, we are using SSH to connect to the remote server and execute commands.


This is how these three elements are linked together:

Every time a push event takes place on the repository, GitHub Actions launches a workflow. 
Run-tests and deploy are the two jobs that make up the workflow.

The run-tests job fetches the repository, installs dependencies, configures Python, 
and launches pytest to run tests.

The deploy job connects to the target server using the SSH protocol and issues commands, 
depending on the run-tests job. The commands are in charge of restarting the server and 
pulling the most recent changes from the repository.

Overall, this solution makes use of GitHub Actions' automation features to make it easier 
to test and deploy code. It uses SSH to run commands remotely and Ubuntu as the target environment.


These are the problems I encountered and I how solved them:

Incorrect VPS configuration:
Problem: If the VPS is not configured correctly, the deployment script might not run, 
which would result in deployment errors.
Solution: Make sure the VPS is configured correctly with all required dependencies, tools, and 
configurations. Check that the deployment script can connect to and access the VPS.

SSH key problems:
Problem: If the deployment script is unable to connect to the VPS due to incorrect 
or missing SSH keys, deployment will fail.
Solution: Check that the correct SSH keys and access information are provided in the 
YAML file's secrets section. Make sure the keys have the authority needed to run the deployment script.