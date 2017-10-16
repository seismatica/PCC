import requests
from pprint import pprint as pp
from operator import itemgetter
import pygal
from pygal.style import DarkSolarizedStyle as DS


def main():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    r = requests.get(url)
    print("Status code:", r.status_code)

    ids = r.json()
    dicts = []
    for id in ids[:30]:
        url = 'https://hacker-news.firebaseio.com/v0/item/' + str(id) + '.json'
        r = requests.get(url)
        print('Status code:', r.status_code)
        story_dict = r.json()
        edited_dict = {
            'title': story_dict['title'],
            'response link': 'https://news.ycombinator.com/item?id=' + str(id),
            'article link': story_dict['url'],
            'comments': story_dict.get('descendants', 0)
        }
        dicts.append(edited_dict)

    sorted_dicts = sorted(dicts, key=itemgetter('comments'), reverse=True)
    plot_dicts = []
    titles = []
    for story_dict in sorted_dicts:
        plot_dict = {
            'value': story_dict['comments'],
            'label': story_dict['title'],
            'xlink': story_dict['article link']
        }
        title = story_dict['title']
        titles.append(title)
        plot_dicts.append(plot_dict)

    my_config = pygal.Config()
    my_config.show_y_guides = False
    my_config.x_label_rotation = 45
    my_config.show_legend = False

    bar_graph = pygal.Bar(my_config, style=DS)
    bar_graph.title = 'Articles on Hacker News with most comments'
    bar_graph.x_labels = titles
    bar_graph.y_title = 'Number of comments'
    bar_graph.add('', plot_dicts)
    bar_graph.render_to_file('hackernews.svg')


main()