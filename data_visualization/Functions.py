import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LC


class apicall:
    def __init__(self, url):
        self.url = url
        self.stars = list() # The API choice
        self.name = list() # The API choice.

    def assign_url(self):
        """This function takes the Api call i.e the Url"""
        url = requests.get(self.url)
        return url

    def json_file(self):
        """This convert the file into json format """
        j_file = self.assign_url()
        repo_dict = j_file.json()
        return repo_dict

    def testcondition(self):
        p = self.assign_url()
        return p.status_code

    def get_total_item(self):
        return self.json_file()['items']

    def amount_of_repository(self):
        """Total Amount of repository extracted from the call"""
        val = len(self.get_total_item())
        return val

    def details(self):
        """Using some of the extracted data from the api
        call to plot the graph.They can be interchanged with
        any other data to determine details or rather plot the graph of the details """

        for repos_dict in self.get_total_item():
            self.name.append(repos_dict['name'])
            self.stars.append(repos_dict['stargazers_count'])

    def list_all_first_30_account_with_highest_stared(self):
        for k, repo_dict in enumerate(self.json_file()['items']):
            print(f'\nPrint details of {k + 1} highest stared repository:')
            print('name : ', repo_dict['name'])
            print('owner : ', repo_dict['owner']['login'])
            print('star: ', repo_dict['stargazers_count'])
            print('repository : ', repo_dict['html_url'])
            print('created : ', repo_dict['created_at'])
            print('last updated : ', repo_dict['updated_at'])
            print('description : ', repo_dict['description'])

    def chart_display(self):
        self.details()
        my_style = LC(base_style=LCS)
        chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
        chart.title = 'Most stared c++ project on github'
        chart.x_labels = self.name
        chart.add('', self.stars)
        chart.render_to_file('repository_chart.svg')


if __name__ == '__main__':
    # This takes input from the user.
    val = str(input('Check top account for stat: '))
    Apicall = apicall(f'https://api.github.com/search/repositories?q=language:{val}&sort=stars')
    Apicall.chart_display()

    # List all account generated from the call.
    Apicall.list_all_first_30_account_with_highest_stared()
