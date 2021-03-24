from biblib import *  # https://github.com/aclements/biblib
import sys
import warnings
from string import Template
from textwrap import dedent
import datetime

pub_mkdwn_template = Template(
    dedent(
        """\
    ---
    title: $TITLE

    authors: $AUTHORS

    journal: $JOURNAL
    doi: $DOI
    citation: $CITATION

    biorxiv: $BIORXIV
    arxiv: $ARXIV
    chemrxiv: $CHEMRXIV

    date: $DATE

    collection: publications
    permalink:  /publications/$KEY
    ---

    $CONTENT
    """
    )
)

inprep_mkdwn_template = Template(
    dedent(
        """\
    ---
    title: $TITLE

    authors: $AUTHORS

    biorxiv: $BIORXIV
    arxiv: $ARXIV
    chemrxiv: $CHEMRXIV

    status: $STATUS

    date: $DATE

    collection: inpreps
    permalink:  /inpreps/$KEY
    ---

    $CONTENT
    """
    )
)


def format_author_line(authors: str, annotations: str):
    names = algo.parse_names(authors)

    formatted_names = []
    author_string = ""
    for name in names:
        first = ". ".join([part[0] for part in name.first.split(" ")]) + "."

        formatted_names.append(f"{first} {name.last}")

    annotations_dict = dict()
    an_auth = annotations.split(";")
    for auth in an_auth:
        tmp = auth.split("=")
        k = int(tmp[0])
        v = [x.strip() for x in tmp[1].split(",")]
        annotations_dict[k] = v

    for i in range(1, len(formatted_names) + 1):
        tmp = formatted_names[i - 1]
        if i in annotations_dict:
            if "coauth" in annotations_dict[i]:
                tmp += "<sup>*</sup>"
            if "corresponding" in annotations_dict[i]:
                tmp += "<sup>$</sup>"
            if "highlight" in annotations_dict[i]:
                tmp = "<b>" + tmp + "</b>"
        if i == 1:
            author_string += tmp
        elif i == len(formatted_names):
            author_string += f", and {tmp}"
        else:
            author_string += f", {tmp}"
    return author_string


bib_file = "CTLBib.bib"

with open(bib_file, "r") as fp:
    db = bib.Parser().parse(fp, log_fp=sys.stderr).get_entries()

for entry in db.values():
    if entry.typ == "article":
        print("Parsing...", entry.typ, ":", entry.key)
        if "entrysubtype" in entry:
            if entry["entrysubtype"] == "unpublished":
                preprints = {
                    "biorxiv": "",
                    "chemrxiv": "",
                    "pmcid": "",
                    "arxiv": "",
                }
                # Regular article
                if "related" in entry and entry["related"] is not "":
                    for related in entry["related"].split(","):
                        related_item = db[related.strip().lower()]
                        preprints[related_item["eprinttype"].strip()] = related_item[
                            "eprint"
                        ]

                date = datetime.date.fromisoformat(entry["date"])

                d = {
                    "KEY": entry.key,
                    "TITLE": f"'{algo.tex_to_unicode(entry['title'])}'",
                    "AUTHORS": f"'{format_author_line(entry['author'], entry['author+an'])}'",
                    "STATUS": f"'{entry['pubstate']}'",
                    "BIORXIV": preprints["biorxiv"],
                    "ARXIV": preprints["arxiv"],
                    "CHEMRXIV": preprints["chemrxiv"],
                    "DATE": entry["date"],
                    "CONTENT": entry["abstract"],
                }

                res = inprep_mkdwn_template.substitute(d)
                # print(res)
                with open(f"../_inpreps/{entry.key}.md", "w") as fd:
                    fd.write(res)
                
            else:
                warnings.warn(
                    f"Unknown entry subtype {entry['entrysubtype']} for item {entry.key}"
                )
        else:
            preprints = {
                "biorxiv": "",
                "chemrxiv": "",
                "pmcid": "",
                "arxiv": "",
            }
            # Regular article
            if "related" in entry and entry["related"] is not "":
                for related in entry["related"].split(","):
                    related_item = db[related.strip().lower()]
                    preprints[related_item["eprinttype"].strip()] = related_item[
                        "eprint"
                    ]

            date = datetime.date.fromisoformat(entry["date"])

            citation = f"{entry['volume']}"
            if "number" in entry:
                citation += f".{entry['number']} ({date.strftime('%B %Y')})"
            else:
                citation += f" ({date.strftime('%B %Y')})"

            if "pages" in entry:
                citation += f", pp. {entry['pages']}"

            d = {
                "KEY": entry.key,
                "TITLE": f"'{algo.tex_to_unicode(entry['title'])}'",
                "JOURNAL": f"'{entry['journal']}'",
                "DOI": entry["doi"],
                "AUTHORS": f"'{format_author_line(entry['author'], entry['author+an'])}'",
                "CITATION": f"'{citation}'",
                "BIORXIV": preprints["biorxiv"],
                "ARXIV": preprints["arxiv"],
                "CHEMRXIV": preprints["chemrxiv"],
                "DATE": entry["date"],
                "CONTENT": entry["abstract"],
            }

            res = pub_mkdwn_template.substitute(d)

            with open(f"../_publications/{entry.key}.md", "w") as fd:
                fd.write(res)

    elif entry.typ == "phdthesis":
        print("skip phd thesis")
    elif entry.typ == "online":
        pass
    else:
        print("Skipping...", entry.typ, ":", entry.key)
