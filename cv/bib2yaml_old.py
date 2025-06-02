import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text
import yaml

input_file = "zilong.bib"
output_file = "zilong.yaml"

lt = LatexNodes2Text()

months_to_num_dict = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}

new_output = []


def null_checker(bib_entry, key):
    return bib_entry[key] if key in bib_entry and bib_entry[key] is not None else None


with open(input_file) as f:
    db = bibtexparser.load(f)


for idx, entry in enumerate(db.entries):

    # TODO: Check if the any of the visible name is same as the CV author, if yes then encapsulate in "***"

    authors = [author.strip() for author in entry["author"].split("and")]
    authors_formatted = []

    for author in authors:
        author = author.strip().replace(" ", "")
        try:
            [last, first] = author.split(",")
        except:
            authors_formatted.append(author)
            continue
        if last == "Chen" and first == "Zilong":
            formatted = "**Zilong Chen**"
        else:
            formatted = f"{first} {last}"
        authors_formatted.append(formatted)

    filtered_entry = {
        "title": f"[{idx + 1}] " + entry["title"],
        "authors": authors_formatted,
    }

    year = entry.get("year")
    month = None

    if year:
        full_date = str(year)
        if month:
            full_date = f"{year}-{months_to_num_dict[month]:02d}"

    filtered_entry["date"] = full_date

    new_output.append(
        {key: value for key, value in filtered_entry.items() if value is not None}
    )

with open(output_file, "w") as yaml_file:
    yaml.dump(new_output, yaml_file, sort_keys=False)

print(f"Filtered entries have been written to {output_file}")
