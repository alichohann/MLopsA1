# MLOPS Assignment 1
You are supposed to design a CI/CD pipeline for a project that shall have a model as well as a
dataset while the dataset shall be unique across each group. Note, this is a group assignment and
you are supposed to have only two members per group.

The tools that can be used while constructing the pipeline can be
1. Jenkins.
2. Github.
3. Github Actions.
4. Git.
5. Docker.
6. Python.
7. Flask.
8. 
Moreover there should be an admin in each group when any member of the group pushes the
changes to the remote repository; it will merge to the repo once the admin approves the changes
(recall the concept of pull requests).
Similarly there should be a workflow (github actions) that will check the quality of the code by
utilising any third party package (flake8). The changes should be made to the dev branch only.
Moreover, suppose a specific features gets completed and is pushed to the remote dev branch
then a pull request should be made to merge the new feature to the test branch that will triggers
another workflow that shall perform unit testing (execution of automated test cases).
Once the automated testing gets its successful completion then a pull request shall be made to
merge changes to the master branch and along with it the given push shall triggers a jenkins job
that shall containerize the application and push it to the docker hub.
Additionally once the merge to the master gets completed there should be a notification (email)
to the administrator informing the successful execution of jenkins job.
