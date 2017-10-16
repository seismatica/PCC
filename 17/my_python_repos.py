import requests
import pygal
from pprint import pprint as pp


def display_repo_info(repo_dict):
    print("-----")
    print("Selected information about repo:")
    print('Number of keys:', len(repo_dict))
    chosen_keys = ['name', ['owner', 'login'], 'stargazers_count', 'html_url', 'created_at', 'updated_at', 'description']
    for key in chosen_keys:
        if isinstance(key, str):
            print(key.title() + ": ", repo_dict[key])
        else:
            item = repo_dict
            prefix = ""
            for subkey in key:
                item = item[subkey]
                prefix += subkey.title() + ": "
            print(prefix + item)


url = 'https://api.github.com/search/repositories?q=language:julia&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

response_dict = r.json()

print('Total repos:', response_dict['total_count'])
repo_dicts = response_dict['items']

print('Returned repos:', len(repo_dicts))

names = []
plot_dicts = []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    description = repo_dict['description']
    if not description:
        description = 'No description available'

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': description,
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)


my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, show_legend=False)
chart.title = 'Most-starred Python repos'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos_hehehe.svg')