import requests
import math

r = requests.get('https://api.clever.com/v1.1/sections?limit=400', headers = {'Authorization':'Bearer DEMO_TOKEN'})

data = r.json()
num_sections = len(data['data'])
print('Number of sections: %d') % num_sections
num_students = 0

for section in data['data']:
	num_students += len(section['data']['students'])

print('Number of students: %d') % num_students
print('Average number of students = %d') % math.ceil(((num_students * 1.0)/num_sections))
