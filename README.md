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
Then use:
```
git checkout master
git checkout -b bug12345
git commit -m "Bug 12345 - Summary of the bug. r=<name of reviewer>"
git hgp HEAD > Bug12345.patch`
```

## Running Tests
https://wiki.mozilla.org/DevTools/Hacking#Running_DevTools_Tests
```
./mach mochitest devtools/client/path/to/the/test_you_want_to_run.js
```

## TRY Server
First get Mozilla Git Tools (+ add this directory to your $PATH in your .bash_profile):
```
git clone git@github.com:mozilla/moz-git-tools.git
```
Modify moz-git-tools/git-push-to-try:42 to include your email ssh://example@gmail.com@hg.mozilla.org/try  
Make sure your Mercurial repository (fx-team) is up to date.  
Make sure that your Git repository (gecko-dev) is in sync with it, with the addition of your patch.  
Next, navigate to your gecko-dev directory and push to try with a command like this:
```
git-push-to-try ../fx-team -b do -p linux,linux64,macosx64,win32 -u xpcshell,mochitests -t none
```