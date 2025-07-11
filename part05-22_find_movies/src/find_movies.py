# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    new_movie_dict = {'name': name, 'director': director, 'year': year, 'runtime': runtime}
    database.append(new_movie_dict)    


def find_movies(database: list, search_term: str) -> list:
    found_movies = []
    for item in database:
        name_list = item['name'].split(' ')
        for word in name_list:
            #print(f'word: {word.lower()} len: {len(word.lower())}')
            #print(f'term: {search_term.lower()} len: {len(search_term.lower())}')
            if search_term.lower() in word.lower():
                found_movies.append(item)
                break
    
    return found_movies
                

if __name__ == '__main__':
    database = []
    add_movie(database, "Gone with the Python Python", "Victor Pything", 2017, 116)
    add_movie(database, "Python on a Plane", "Renny Pytholin", 2001, 94)
    add_movie(database, "Jaws", "Renny Pytholin", 1988, 102)
    
    #print(database)

    my_movies = find_movies(database, 'ja')

    print(f'Found movie: {my_movies}')
    