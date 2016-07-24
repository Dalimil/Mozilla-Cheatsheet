#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ $# -eq 1 ]
	then
	$DIR/firefox/firefox $1 -no-remote -P "TestNightly" --jsdebugger
else
	$DIR/firefox/firefox -no-remote -P "TestNightly" --jsdebugger 
fi


