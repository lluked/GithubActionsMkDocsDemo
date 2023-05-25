import os
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader

site_name = "example_site"

## Delete site folder
shutil.rmtree(site_name) 

## Create Folder Structure
Path(os.path.join(site_name, 'docs', 'pages')).mkdir(parents=True, exist_ok=True)
Path(os.path.join(site_name, 'docs', 'css')).mkdir(parents=True, exist_ok=True)

## Copy static files
shutil.copyfile('extra.css', os.path.join(site_name, 'docs', 'css', 'extra.css'))

## Template
environment = Environment(loader=FileSystemLoader("templates/"))

### Pages
pages = [
    {"title": "Page 1",  "body": "Hello"},
    {"title": "Page 2", "body": "World"},
    {"title": "Page 3", "body": "Hello World"},
]

#### Render Pages
page_template = environment.get_template("page.md.j2")
for page in pages:
    filename = f"{site_name}/docs/pages/test_{page['title'].lower()}.md".replace(" ", "_")
    content = page_template.render(
        title=page['title'],
        body=page['body']
    )
    with open(filename, mode="w", encoding="utf-8") as page:
        page.write(content)
        print(f"... wrote {filename}")

#### Render index
index_template = environment.get_template("index.md.j2")
filename = f"{site_name}/docs/index.md"
content = index_template.render(
    pages=pages
)
with open(filename, mode="w", encoding="utf-8") as page:
    page.write(content)
    print(f"... wrote {filename}")

#### Render mkdocs
mkdocs_template = environment.get_template("mkdocs.yml.j2")
filename = f"{site_name}/mkdocs.yml"
content = mkdocs_template.render(
    pages=pages
)
with open(filename, mode="w", encoding="utf-8") as page:
    page.write(content)
    print(f"... wrote {filename}")
