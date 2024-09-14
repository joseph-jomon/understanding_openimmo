The command `git remote add origin https://github.com/joseph-jomon/immo_suche.git` is not enough by itself to push the local branch to a new remote and set it as the head. This command only adds a new remote reference (named `origin` in this case) to your local repository, linking it to the specified URL.

To push your current branch to this new remote and set it as the head, you should follow these steps:

1. **Add the new remote (if not already added):**

   ```bash
   git remote add new-origin https://github.com/joseph-jomon/immo_suche.git
   ```

   *(Here, we're using `new-origin` to avoid confusion if `origin` already exists.)*

2. **Push the current branch to the new remote:**

   ```bash
   git push -u new-origin <branch-name>
   ```

   - Replace `<branch-name>` with the name of the branch you want to push (e.g., `main`, `master`, `dev`, etc.).
   - The `-u` flag sets up upstream tracking, making `new-origin/<branch-name>` the default remote branch for future `git push` and `git pull` commands on this branch.

3. **Set the branch as the default (if needed):**

   - You might need to go to the GitHub repository settings in your browser and manually set the default branch if it's not done automatically.

### In Summary

Your command only adds a remote reference. You need to use `git push -u` to push the branch and set up tracking. After that, the remote repository's settings (on GitHub, for example) might need to be adjusted to set the branch as the default head if required.