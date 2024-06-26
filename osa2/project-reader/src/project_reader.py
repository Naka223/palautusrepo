from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        #print(content)

        parsed = toml.loads(content)

        #print(parsed)
        #print()

        name = parsed.get('tool', {}).get('poetry', {}).get('name')
        description = parsed.get('tool', {}).get('poetry', {}).get('description')
        lisenssi = parsed.get('tool', {}).get('poetry', {}).get('license')
        authors = parsed.get('tool', {}).get('poetry', {}).get('authors')
        dependencies = parsed.get('tool', {}).get('poetry', {}).get('dependencies', {})
        dev_dependencies = parsed.get('tool', {}).get('poetry', {}).get('group', {}).get('dev', {}).get('dependencies', {})

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, lisenssi, authors, dependencies, dev_dependencies)