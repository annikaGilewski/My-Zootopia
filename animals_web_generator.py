import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


for animal in animals_data:
    print(f"Name: {animal['name']}")

    if "diet" in animal["characteristics"]:
        print(f"Diet: {animal['characteristics']['diet']}")

    if "locations" in animal and animal["locations"]:
        print(f"Location: {animal['locations'][0]}")

    if "type" in animal["characteristics"]:
        print(f"Type: {animal['characteristics']['type']}")

    print()


def load_html(html_file):
    with open(html_file, "r", encoding="utf-8") as handle:
        return handle.read()


html_template = load_html("animals_template.html")

animals_info = ""

for animal in animals_data:
    animals_info += '<li class="cards__item">'

    animals_info += f"Name: {animal['name']}<br/>\n"

    if "diet" in animal["characteristics"]:
        animals_info += f"Diet: {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and animal["locations"]:
        animals_info += f"Location: {animal['locations'][0]}<br/>\n"

    if "type" in animal["characteristics"]:
        animals_info += f"Type: {animal['characteristics']['type']}<br/>\n"

    animals_info += "</li>"


html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    animals_info
)


with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html)