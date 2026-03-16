import urllib.request
import json


def retrieve_all() -> list:
    url = 'https://studies.cs.helsinki.fi/stats-mock/api/courses'
    web_data = urllib.request.urlopen(url).read()

    all_courses = json.loads(web_data)
    active_courses = []
    
    for i in all_courses:
        if i['enabled']:
            next_course = (i['fullName'],i['name'],i['year'],list_sum(i['exercises']))
            active_courses.append(next_course)

    return active_courses

def list_sum(my_list: list) -> int:
    total = 0
    for i in my_list:
        total += int(i)
    
    return total

if __name__ == '__main__':
    all_courses = retrieve_all()
    print(all_courses)