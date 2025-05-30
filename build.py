from pybtex.database.input import bibtex


def github_link_to_star_badge(github_url):
    try:
        # Extract the user and repo from the URL
        parts = github_url.strip("/").split("/")
        if len(parts) < 5:
            raise ValueError("Invalid GitHub URL format.")
        user, repo = parts[-2], parts[-1]

        # Create the badge URL
        badge_url = f"https://img.shields.io/github/stars/{user}/{repo}?style=social"

        # Return the HTML code for the badge
        return f'<img src="{badge_url}">'
    except Exception as e:
        return str(e)


def get_personal_data():
    name = ["Zilong", "Chen"]
    bio_text = f"""
                <p>
                    I am a Ph.D candidate at Department of Computer Science and Technology, Tsinghua University, where I am advised by <a href="https://sites.google.com/site/thuliuhuaping/home" target="_blank">Prof. Huaping Liu</a> and work closely with <a href="https://wangfeng18.github.io/" target="_blank">Dr. Feng Wang</a> and <a href="https://yikaiw.github.io/" target="_blank">Prof. Yikai Wang</a>. Before joining Tsinghua University, I completed my undergraduate studies at Xi'an Jiaotong University under the supervision of <a href="https://gr.xjtu.edu.cn/web/minnluo/" target="_blank">Prof. Minnan Luo</a>, focusing on knowledge graphs and their applications in natural language processing.
                </p>
                <p>
                    <a href="./assets/Zilong_Chen_CV.pdf" target="_blank" style="margin-right: 5px"><i class="fa-solid fa-circle-user"></i> Resume</a>|
                    <a href="mailto:jaysonabcchen@gmail.com" style="margin-right: 5px"><i class="fa-regular fa-envelope fa-lg"></i> Email</a>|
                    <a href="./assets/img/heheyas-wechat.jpg" style="margin-right: 5px"><i class="fab fa-weixin"></i> Wechat</a>|
                    <a href="https://scholar.google.com.hk/citations?user=2pbka1gAAAAJ&hl=en" target="_blank" style="margin-right: 5px"><i class="fa-brands fa-google-scholar"></i> Google Scholar</a>|
                    <a href="https://github.com/heheyas" target="_blank" style="margin-right: 5px"><i class="fab fa-github fa-lg"></i> Github</a>|
                    <a href="https://www.linkedin.com/in/zilong-chen-99671523b/" target="_blank" style="margin-right: 5px"><i class="fa-brands fa-linkedin fa-lg"></i> LinkedIn</a>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Acknowledgement</h4>
                <p>
                    This website is built based on <a href="https://m-niemeyer.github.io/" target="_blank">Michael Niemeyer's</a> personal website. Thanks for his open-source code.
                </p>
            </div>
    """
    return name, bio_text, footer


DEFAULT_URL = "http://www.google.com/search?q="


def get_author_dict():
    return {
        "Feng Wang": "https://wangfeng18.github.io/",
        "Yikai Wang": "https://yikaiw.github.io/",
        "Huaping Liu": "https://sites.google.com/site/thuliuhuaping/home",
        "Zhengyi Wang": "https://thuwzy.github.io/",
        "Yiwen Chen": "https://buaacyw.github.io/",
        "Wenqiang Sun": "",
    }


def generate_person_html(
    persons,
    connection=", ",
    make_bold=True,
    make_bold_name="Zilong Chen",
    add_links=True,
):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        co_first_author = False
        for name_part_i in p.get_part("first") + p.get_part("last"):
            if string_part_i != "":
                string_part_i += " "
            if "*" in name_part_i:
                co_first_author = True
                name_part_i = name_part_i.replace("*", "")
            string_part_i += name_part_i
        extra_name_part_i = "*" if co_first_author else ""
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i + extra_name_part_i}</a>'
        elif string_part_i != make_bold_name and add_links:
            string_part_i = f'<a href="{DEFAULT_URL + string_part_i}" target="_blank">{string_part_i + extra_name_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold; text-decoration:underline";>{make_bold_name + extra_name_part_i}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""

    ## add support for video
    if "img" in entry.fields.keys():
        if entry.fields["img"].split(".")[-1] == "mp4":
            s += f"""<video width="100%" muted loop class="vid"><source src="{entry.fields['img']}" type="video/mp4"></video>"""
        else:
            s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""

    s += """</div><div class="col-sm-9">"""

    if "project" in entry.fields.keys():
        s += f"""<a href="{entry.fields['project']}" target="_blank">{entry.fields['title']}</a> <br>"""
    else:
        s += f"""<a href="{DEFAULT_URL + entry.fields["title"]}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']}"""
    if "award" in entry.fields.keys():
        s += f""" <span style="color: red; font-weight: bold">({entry.fields['award']})</span>"""
    s += """<br>"""

    artefacts = {
        "project": "Project Page",
        "youtube": "Video",
        "poster": "Poster",
        "github": "Code",
        "arxiv": "Arxiv",
    }

    i = 0
    for k, v in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += " / "
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
            if k == "github":
                s += f""" {github_link_to_star_badge(entry.fields[k])}"""
            if k == "arxiv":
                pass
        else:
            print(f"[{entry_key}] Warning: Field {k} missing!")

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += (
        "\tauthor = {"
        + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}"
        + "}, \n"
    )
    for entr in ["title", "booktitle", "year"]:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += (
        " /"
        + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    )
    s += """ </div> </div> </div>"""
    return s


def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {"slides": "Slides", "video": "Recording"}
    i = 0
    for k, v in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += " / "
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f"[{entry_key}] Warning: Field {k} missing!")
    s += """ </div> </div> </div>"""
    return s


def get_project_entry(entry_key, entry):
    pass


def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("zilong.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s


def get_projects_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("project.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_paper_entry(k, bib_data.entries[k])
    return s


def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file("talk_list.bib")
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s += get_talk_entry(k, bib_data.entries[k])
    return s


def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    projects = get_projects_html()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <script src="https://kit.fontawesome.com/6f34d50cde.js" crossorigin="anonymous"></script>

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/img/avatar.jpg">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-10" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-2" style="">
                        <img src="assets/img/avatar.jpg" 
                        class="img-thumbnail" 
                        width="280px" 
                        alt="Profile picture" 
                        style="float: right;"
                        onmouseover="this.src='assets/img/zilong_chen.jpg'" 
                        onmouseout="this.src='assets/img/avatar.jpg'">
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Selected publications (* indicates equal contribution) [<a href="full_list.html">Full list</a>] [<a href="">Download bibtex</a>]</h4>
                        {pub}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <h4>Open-source Projects</h4>
                        {projects}
                    </div>
                </div>
                <!--
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <h4>Talks</h4>
                        {talks}
                    </div>
                </div>
                -->
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <h4>Services</h4>
                        <b>Reviewer for conferences</b>: CVPR, NeurIPS, ICLR, ICML, ICCV, AAAI, ACL, IROS, ICRA</br>
                        <b>Reviewer for journals</b>: T-PAMI, Neurocomputing, TIP, JMLR</br>
                    </div>
                </div>
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
            <div class="col-md-1"></div>
        </div?
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
    <script src="./common.js"></script>
</body>

</html>
    """
    return s


def write_index_html(filename="index.html"):
    s = get_index_html()
    with open(filename, "w") as f:
        f.write(s)
    print(f"Written index content to {filename}.")


if __name__ == "__main__":
    write_index_html("index.html")
