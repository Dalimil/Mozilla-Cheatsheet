# Mozilla Contributing Cheat Sheet

https://developer.mozilla.org/en-US/docs/Tools/Contributing
https://developer.mozilla.org/en-US/docs/Tools/Contributing/Contribute_on_nightly

## Getting Source Code 
**Only clone the tip of master (mozilla-central) and fx-team (fx-team) branches**
```
git clone -b master --single-branch --depth 1 https://github.com/mozilla/gecko-dev.git
git remote set-branches --add origin fx-team
git pull
git checkout fx-team
```

## Gitconfig
```
[user]
    name = My Name
    email = me@my-domain.com
[alias]
	hgp = "show --binary --find-renames --format=\"# HG changeset patch%n# User %an <%ae>%n%B\" -U8"
```
*Then use:* 
```
git checkout master
git checkout -b bug12345
git commit -m "Bug 12345 - Summary of the bug. r=<name of reviewer>"
git hgp HEAD > Bug12345.patch`
```

TRY Server
First get Mozilla Git Tools:
```
git clone git@github.com:mozilla/moz-git-tools.git
```
Make sure the scripts in this repository are executable - add this directory to your $PATH in your .bash_profile.  Make sure your Mercurial repository (fx-team) is up to date.  
Make sure that your Git repository (gecko-dev) is in sync with it, with the addition of your patch.  
Next, navigate to your gecko-dev directory and push to try with a command like this:
```
git-push-to-try ../fx-team -b do -p linux,linux64,macosx64,win32 -u xpcshell,mochitests -t none
```