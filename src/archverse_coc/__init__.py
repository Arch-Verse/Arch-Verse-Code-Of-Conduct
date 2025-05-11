import jinja2
import json

def open_json(path: str):
    result = {}
    with open(path, "r") as file:
        raw = file.read()
        result = json.loads(raw)
    return result

def main() -> int:
    definitions: list = open_json("sections/definitions.json")
    rules: list = open_json("sections/rules.json")

    env = jinja2.Environment(
        loader=jinja2.PackageLoader("archverse_coc", "."),
        autoescape=False
    )

    output: str = ""

    with open("README.md.jinja", "r") as file:
        template = env.from_string(file.read())
        output = template.render(rules=rules, definitions=definitions)

    with open("README.md", "w") as file:
        print(output, file=file)
    
    return 0