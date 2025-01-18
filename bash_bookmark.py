import sys
import os

# used during writing process to confirm arguments were passed by bash script
# for i, item in enumerate(sys.argv):
#     print(str(i)+item)

# three arguments are passed by the bash script
# 1 the path of the python script that is called. can be ignored
# 2 the name of the bookmarked directory. if a new bookmark is being created this arugment is not passes by bash script
# 3 the current working directory

script_path = os.path.join(os.path.expanduser('~'), 'bash', 'bash_bookmarks')

def save_bookmark(path):
    bookmark_name = input('enter bookmark name: ') # used to name a new bookmark upon creation
    
    with open((f'{script_path}/bookmarks.csv'), 'a') as file: # .csv file storing existing bookmarks
#        print (f'{bookmark_name},{path}') # used to check values written to bookmarks.csv. not esential
        file.write(f'{bookmark_name},{path}\n') # bookmark name and path written to .csv
    print (f'bookmark {bookmark_name} created') # info message
    sys.exit() # SystemExit raised

def return_path(bookmark, path):
    with open((f'{script_path}/bookmarks.csv'), 'r') as file:
        for item in file:
            if bookmark in item:
                with open((f'{script_path}/result.txt'), 'w') as path_file:
                    path_file.write((item.split(','))[1])
                sys.exit()
            else:
                save_bookmark()
            
if __name__ == '__main__':

    if len(sys.argv) <= 2: 
        save_bookmark(sys.argv[1])

    else:
        return_path(sys.argv[1], sys.argv[2])
        