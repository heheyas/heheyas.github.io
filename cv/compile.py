import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text
import yaml

input_file = "zilong_full.bib"
output_file = "zilong_cv_w_refs.yaml"

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


def compile_bibtex_to_yaml(input_file):
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
                formatted = "**#underline[Zilong Chen]**"
            elif last == "Chen" and first == "Zilong*":
                formatted = "**#underline[Zilong Chen]=**"
            elif "*" in first:
                formatted = f"{first.replace('*', '')} {last + '='}"
            else:
                formatted = f"{first} {last}"
            authors_formatted.append(formatted)

        filtered_entry = {
            "title": f"[{idx + 1}] " + entry["title"],
            "authors": authors_formatted,
        }
        # filtered_entry["journal"] = null_checker(entry, "booktitle")
        filtered_entry["date"] = (
            null_checker(entry, "booktitle") + " " + null_checker(entry, "year")
        )

        if "award" in entry:
            filtered_entry["date"] += f" (**{entry['award']}**)"

        url = None
        if "project" in entry:
            url = entry["project"]
        elif "arxiv" in entry:
            url = entry["arxiv"]
        elif "github" in entry:
            url = entry["github"]

        if url is not None:
            filtered_entry["url"] = url

        new_output.append(
            {key: value for key, value in filtered_entry.items() if value is not None}
        )

    return new_output


def read_yaml_file(file_path):
    with open(file_path, "r") as file:
        try:
            yaml_data = yaml.safe_load(file)
            return yaml_data
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file: {e}")
            return None


if __name__ == "__main__":
    references = compile_bibtex_to_yaml(input_file)

    zilong_cv_file = read_yaml_file("Zilong_CV.yaml")

    zilong_cv_file["cv"]["sections"][
        "publications (= indicates equal contribution)"
    ] = references

    with open(output_file, "w") as yaml_file:
        yaml.dump(zilong_cv_file, yaml_file, sort_keys=False)
