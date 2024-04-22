class Project:
    def __init__(self, name, description, lisenssi, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.lisenssi = lisenssi
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLisence: {self.lisenssi or '-'}"
            f"\n"
            f"\nAuthors: "
            f"\n - {'\n - '.join([str(lst) for lst in self.authors]) or '-'}"
            f"\n"
            f"\nDependencies: "
            f"\n - {'\n - '.join([str(lst) for lst in self.dependencies]) or '-'}"
            f"\n"
            f"\nDevelopment dependencies: "
            f"\n - {'\n - '.join([str(lst) for lst in self.dev_dependencies]) or '-'}"
        )
