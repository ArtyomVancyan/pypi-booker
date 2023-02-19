import requests
import setuptools

name = input("Project name: ")
url = "https://pypi.org/project/%s/" % name

response = requests.get(url)
assert response.status_code == 404, "Project already exists"

setuptools.setup(
    url=url,
    name=name,
    version="0.0.0",
    author="<author name>",
    author_email="<author email>",
    description="The package is coming soon...",
)
