#!/bin/bash

PWD=command pwd
python3 ~/bash/bash_bookmarks/bash_bookmark.py $1 $PWD
BOOKMARK_PATH=$(cat ~/bash/bash_bookmarks/result.txt)

cd "$BOOKMARK_PATH"
