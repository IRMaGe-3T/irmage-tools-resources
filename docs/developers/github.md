# Github information 

## Personal access token

[Personal access]((https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)) tokens are an alternative to using passwords for authentication to GitHub when using command line. 

**Create a token:**

- Connect to [Github web interface](https://github.com/)

- Go to **Settings** page (the menu at the top right), then in **Developer settings** and finally in **Personal access tokens** 

- Create a token by clicking on **Generate new token** in **Tokens (classic)**. Give a name. 

- If you want to use this token to use github operations on your computer (use commit, push...), check "repo".

- Make sure to copy your personal access token. You won’t be able to see it again! If you loose it you need to create a new one.

**Store the token in your computer:** 

- Run the command:
```
git config --global credential.helper store
``` 

This should modify the ~/.gitconfig file by adding the following lines:  [credential] helper = store

- Create a file ~/.git-credentials, containing: https://{login github}:{token}@github.com
 
- Add user name and email in .gitconfig. For the email use the email configured in github. If email privacy is enabled use the email provided by Github for Git operations (e.g : "4542githublogin@users.noreply.github.com")

```
git config --global user.name "Surname Name"
git config --global user.mail "4542githublogin@users.noreply.github.com"
```


## Pull request

It is one way to apply a pull request (there are others !!!)

1. Make a fresh fork:
    * Go to the project to fork (for ex. populse/populse_mia).
    * Click on the top right button - Fork -.
    * Then make the fork (for ex. servoz/populse_mia).

2. Local cloning of this fork:
    * In your local station:
        * git lfs clone xxx # xxx can be found on the forked project in the GitHub site page (i.e. see the green button "Clone or download", for ex. xxx = https://github.com/servoz/populse_mia.git)

3. Some configurations:
    * In the local station and in the project (for ex. in  /home/toto/Git_Projects/populse_mia/):
        * git config remote.pushdefault origin # by default publish (i.e. with git push) in your fork, i.e. in https://github.com/servoz/populse_mia
        * git config push.default current # by default publish (i.e. with git push) on a branch with the same name as the current branch in the local repository
        * git remote add upstream xxx # Define upstream as the target project (that you have forked, i.e. xxx = https://github.com/populse/populse_mia)
        * git fetch upstream # gets the latest history from the project target on the server

4. Creation of an inProgress (inProgress is only an example!! You can choose the name you want as why not "MyFuckingPrettyBranch") branch (it is strongly recommended to work on your branch rather than on the master branch):
    * In the local station and in the project (for ex. in  /home/toto/Git_Projects/populse_mia/):
        * git checkout -b inProgress upstream/master # by adding upstream/master, branch inProgress is set up to track remote branch master from upstream

5. Make the modifications you need on your local fork (for ex. in /home/toto/Git_Projects/populse_mia/)
    * During your changes and at least at the end, check that all is added in the Index space by using:
        * git status # must not display the red message "Changes not staged for commit:"  but must display the green message "Changes to be committed :" (except if you don't want to apply a change in a file!). For this use "git add/rm/etc.. FileUwantToBeCommitted". If needed see man git, man git add, etc.)

6. Save your changes to your local repository (save from the Index space to the Header space):
    * git commit -m "AlittleTextSummarizingTheChange" # At this stage the command "git status" would return the message "nothing to commit, working tree clean"

7. Push your changes in your fork/branch in the remote server:
    * Git push # answer the login_name/passwd. Your changes are now in your remote server's fork (for ex. in  servoz/populse_mia and in your branch, for ex. in inProgress)

8. Finally, you must go through the project's web interface to create the pull-request from your fork (for ex. servoz/populse_mia) inProgress branch to the master branch of the reference repository (for ex. populse/populse_mia):
    * In the web page of your fork inProgress branch, click on the "New pull request" button. Write or complete the title and the comment fields. Then, finnaly, click the green button "Create pull request"

9. Actually, now, take in one hand the bible, in other a very big candle and wait for the deliberation of the reviewer ...
