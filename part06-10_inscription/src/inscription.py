

folder = 'C:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'
name = input('Whom should I sign this to: ')
file_name = input('Where shall I save it: ')

path = folder + file_name

with open(path, 'w') as new_file:
    new_file.write(f'Hi {name}, we hope you enjoy learning Python with us!  Best, Mooc.fi Team')