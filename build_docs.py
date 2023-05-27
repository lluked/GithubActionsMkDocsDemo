import os
from pathlib import Path
import shutil

from jinja2 import Environment, FileSystemLoader

## Create Folder Structure
Path(os.path.join('docs', 'pages')).mkdir(parents=True, exist_ok=True)
Path(os.path.join('docs', 'css')).mkdir(parents=True, exist_ok=True)

## Copy static files
shutil.copyfile('extra.css', os.path.join('docs', 'css', 'extra.css'))

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
    filename = f"docs/pages/test_{page['title'].lower()}.md".replace(" ", "_")
    content = page_template.render(
        title=page['title'],
        body=page['body']
    )
    with open(filename, mode="w", encoding="utf-8") as page:
        page.write(content)
        print(f"... wrote {filename}")

#### Render index
index_template = environment.get_template("index.md.j2")
filename = f"docs/index.md"
content = index_template.render(
    pages=pages
)
with open(filename, mode="w", encoding="utf-8") as page:
    page.write(content)
    print(f"... wrote {filename}")

#### Render mkdocs
mkdocs_template = environment.get_template("mkdocs.yml.j2")
filename = f"mkdocs.yml"
content = mkdocs_template.render(
    pages=pages
)
with open(filename, mode="w", encoding="utf-8") as page:
    page.write(content)
    print(f"... wrote {filename}")
