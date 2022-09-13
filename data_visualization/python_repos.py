import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LC
import json

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code: ', r.status_code)

# Store the response in a .json file
response_dict = r.json()
with open('check.json', 'w') as p:
    json.dump(response_dict, p)

print(response_dict.keys())

print('Total repositories: ', response_dict['total_count'])

# To examine information about the repository
repos_dicts = response_dict['items']
print('Total length', len(repos_dicts))

# Now we want to get and append to a list,
# names and mostly sttared projects in github

names, stars = [], []

for repos_dict in repos_dicts:
    names.append(repos_dict['name'])
    stars.append(repos_dict['stargazers_count'])

# Using pygal to make visualization of the results above
my_style = LC(base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most stared python project on github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('repository_chart.svg')
