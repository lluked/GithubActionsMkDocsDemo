from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))

# Pages
pages = [
    {"title": "Page 1",  "body": "Hello"},
    {"title": "Page 2", "body": "World"},
    {"title": "Page 3", "body": "Hello World"},
]

## Render Pages
page_template = environment.get_template("page.md.j2")
for page in pages:
    filename = f"example-site/docs/pages/test_{page['title'].lower()}.md".replace(" ", "_")
    content = page_template.render(
        title=page['title'],
        body=page['body']
    )
    with open(filename, mode="w", encoding="utf-8") as page:
        page.write(content)
        print(f"... wrote {filename}")

## Render index
index_template = environment.get_template("index.md.j2")
filename = f"example-site/docs/index.md"
content = index_template.render(
    pages=pages
)
with open(filename, mode="w", encoding="utf-8") as page:
    page.write(content)
    print(f"... wrote {filename}")

## Render mkdocs
mkdocs_template = environment.get_template("mkdocs.yml.j2")
filename = f"example-site/mkdocs.yml"
content = mkdocs_template.render(
    pages=pages
)
with open(filename, mode="w", encoding="utf-8") as page:
    page.write(content)
    print(f"... wrote {filename}")
