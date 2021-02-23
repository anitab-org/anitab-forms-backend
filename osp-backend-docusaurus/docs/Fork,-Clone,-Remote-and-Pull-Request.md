---
id: Fork,-Clone,-Remote-and-Pull-Request
title: Fork, Clone, Remote & Pull Request
---

To contribute to the project you may work on the [frontend](https://github.com/anitab-org/open-source-programs-web) or [backend](https://github.com/anitab-org/open-source-programs-backend) of the project.
### Fork the repo
![Forking](https://user-images.githubusercontent.com/45794450/108760348-8c45b700-7573-11eb-8b2b-0d341baaaf52.png)
Click on the Fork button. This will create your copy of the repo on GitHub.

### Clone
After forking, run the following commands in your terminal:
```
git clone https://github.com/<your-github-username-here>/open-source-programs-backend
```
OR
```
git clone https://github.com/anitab-org/open-source-programs-backend
```

### Add Remote
If you have forked and cloned the repo, on entering `git remote -v` you should see the following output:<br/><br/>
```
$ git remote -v
origin  https://github.com/<your-github-username-here>/open-source-programs-backend (fetch)
origin  https://github.com/<your-github-username-here>/open-source-programs-backend (push)
```
Now you need to add another remote named upstream (you may change if you wish, but this is a git convention). Run this command: <br/>
```
git remote add upstream https://github.com/anitab-org/open-source-programs-backend
```
The output of `git remote -v` now changes to:
```
$ git remote -v
origin  https://github.com/<your-github-username-here>/open-source-programs-backend (fetch)
origin  https://github.com/<your-github-username-here>open-source-programs-backend (push)
upstream  https://github.com/anitab-org/open-source-programs-backend (fetch)
upstream  https://github.com/anitab-org/open-source-programs-backend (fetch)
```

### Working on an Issue
Now that you have setup the project, you need to search for anything to work on which interests you. Have a look at the [Backend Issues](https://github.com/anitab-org/open-source-programs-backend/issues) or [Frontend Issues](https://github.com/anitab-org/open-source-programs-web/issues), whichever interests you. 
- Once you find an **unassigned** issue that you wish to solve, comment below the issue asking whether you should work on it or not.
- Wait for a Mentor/Admin to assign it to you and start working on it.

### Making a Pull Request
After working on an issue, adding relevant documentation and tests, you need to push your changes to your forked repository and make a pull request. You should always push your changes in a different branch (not master).
```
git checkout -b <new-branch-name>
```
Make the relevant changes and then commit with a proper message:
```
git add -a
git commit -m "<your-commit-message-here>"
```
Now push the changes:
```
git push origin <new-branch-name>
```
Now in the GitHub repo click on New Pull Request
![Screenshot from 2020-05-15 19-08-12](https://user-images.githubusercontent.com/43119923/82056501-af3b6480-96df-11ea-8992-29ed099ee1df.png)
Choose the branch you pushed. Make your PR informative by adding screenshots, Issue link and descriptive details regarding what it does and then submit it.

**Note:** _For more detailed understanding visit [this page](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/overview)_.

**Congratulations!** You have contributed to AnitaB.org Open Source successfully.
