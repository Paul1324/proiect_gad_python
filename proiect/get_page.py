
import requests
from bs4 import BeautifulSoup


class Repo:
    def __init__(self, name, url, language, description):
        self.name = name
        self.url = url
        self.description = description
        self.language = language

    def __str__(self):
        return f"{self.name}\n{self.url}\n{self.language}\n{self.description}"


class Profile:
    def __init__(self, image, fullname, username, bio, followers, following, public_repos):
        self.image = image
        self.fullname = fullname
        self.username = username
        self.bio = bio
        self.followers = followers
        self.following = following
        self.public_repos = public_repos

    def __str__(self):
        string = f"{self.image}\n{self.fullname}\n{self.username}\n{self.bio}\n{self.followers}\n{self.following}"
        for repo in self.public_repos:
            string += f"\n{repo}"
        return string

    def add_repo(self, repo):
        self.repos.append(repo)

    def add_fullname(self, name):
        self.fullname = name

    def add_username(self, name):
        self.username = name

    def add_bio(self, bio):
        self.bio = bio

    def add_followers(self, followers):
        self.followers = followers

    def add_following(self, following):
        self.following = following


def get_page(URL):
    URL = "https://github.com/" + URL
    page = requests.get(URL)
    if(page):
        soup = BeautifulSoup(page.content, 'html.parser')
        # user = PROFILE()
        main_page = soup.find(class_='application-main')

        # get image
        image = main_page.find(
            class_='avatar avatar-user width-full border color-bg-default')
        if(image):
            image = image['src']

        # get fullname and username
        name = main_page.find(class_='vcard-names')
        fullname = name.find(
            class_='p-name vcard-fullname d-block overflow-hidden')
        username = name.find(class_='p-nickname vcard-username d-block')
        if(fullname):
            fullname = fullname.text.strip()
        else:
            fullname = "fullname not found"
        if(username):
            username = username.text.strip()
        else:
            username = "username not found"

        # get bio
        bio_field = main_page.find(
            class_='p-note user-profile-bio mb-3 js-user-profile-bio f4')
        bio = bio_field.find('div')
        if(bio):
            bio = bio.text.strip()
        else:
            bio = 'bio not found'
        # get followers and following
        stats = main_page.find(
            class_='flex-order-1 flex-md-order-none mt-2 mt-md-0')
        if(stats):
            stats_field = stats.find_all(
                class_='Link--secondary no-underline no-wrap')
            followers = stats_field[0].find('span')
            following = stats_field[1].find('span')
            followers = followers.text.strip()
            following = following.text.strip()

        else:
            followers = 0
            following = 0

        # get public repos
        repos_container = main_page.find(
            class_='js-pinned-items-reorder-container')
        repos = repos_container.find_all(
            class_='pinned-item-list-item-content')

        repo_list = []

        for repo in repos:

            name = repo .find('span', class_='repo')
            if(name):
                name = name.text.strip()
            else:
                name = "name not found"
            url = repo.find('a')['href']
            url = 'https://github.com' + url
            description = repo.find(class_='pinned-item-desc')
            if(description):
                description = description.text.strip()
            else:
                description = "description not found"
            language = repo.find('span', itemprop='programmingLanguage')
            if(language):
                language = language.text.strip()
            else:
                language = 'unknown language'

            repo_list.append(Repo(name, url, language, description))

        profile = Profile(image, fullname, username, bio,
                          followers, following, repo_list)
        return profile
    else:
        return None
