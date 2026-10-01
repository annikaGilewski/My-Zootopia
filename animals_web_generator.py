import json


def load_data(file_path):
    """Loads a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")


def load_html(html_file):
    with open(html_file, "r", encoding="utf-8") as handle:
        return handle.read()


html_template = load_html("animals_template.html")

def serialize_animal(animal_obj):
    output = ""

    output += '<li class="cards__item">'

    output += f"""
    <div class="card__title">{animal_obj['name']}</div>
    <p class="card__text">
    """

    if "diet" in animal_obj["characteristics"]:
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"

    if "locations" in animal_obj and animal_obj["locations"]:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"

    if "type" in animal_obj["characteristics"]:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"

    output += """
    </p>
    </li>
    """

    return output


animals_info = ""

for animal in animals_data:
    animals_info += serialize_animal(animal)


html = html_template.replace(
    "__REPLACE_ANIMALS_INFO__",
    animals_info
)


with open("animals.html", "w", encoding="utf-8") as handle:
    handle.write(html)