import sys

# used during writing process to confirm arguments were passed by bash script
for i, item in enumerate(sys.argv):
    print(str(i)+item)

# three arguments are passed by the bash script
# 1 the path of the python script that is called. can be ignored
# 2 the name of the bookmarked directory. if a new bookmark is being created this arugment is not passes by bash script
# 3 the current working directory


if len(sys.argv) <= 2: 
    bookmark_name = input('enter bookmark name: ') # used to name a new bookmark upon creation
    
    with open('bookmarks.csv', 'a') as file: # .csv file storing existing bookmarks
        print (f'{bookmark_name},{sys.argv[1]}') # used to check values written to bookmarks.csv. not esential
        file.write(f'{bookmark_name},{sys.argv[1]}\n') # bookmark name and path written to .csv
    print (f'bookmark {bookmark_name} created') # info message
    sys.exit() # SystemExit raised
else:
    pass

