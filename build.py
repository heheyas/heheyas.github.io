from pybtex.database.input import bibtex
from pybtex.errors import set_strict_mode

# Tolerate messy .bib entries (e.g. duplicate fields) instead of crashing.
set_strict_mode(False)

# ------------------------------------------------------------------
#  Static homepage generator.
#  Renders index.html (about + news + selected pubs + projects +
#  services) and full_list.html (all publications) from .bib files.
#  Self-contained: Hanken Grotesk + IBM Plex Mono, off-white paper,
#  green accent, light/dark themes. No Bootstrap / jQuery / FontAwesome.
# ------------------------------------------------------------------

DEFAULT_URL = "http://www.google.com/search?q="

# ---- link icons (line = stroke; brand marks = filled) ------------
IC = {
    "cv": '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 13h6M9 17h4"/></svg>',
    "mail": '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "scholar": '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M22 9 12 4.5 2 9l10 4.5L22 9z"/><path d="M6 11v5c0 1.1 2.7 2.6 6 2.6s6-1.5 6-2.6v-5"/></svg>',
    "github": '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-4 1.3-4-2.3-5.6-2.7M15 21v-3.3c0-.9-.3-1.6-.8-2 2.7-.3 5.4-1.3 5.4-5.9 0-1.3-.5-2.4-1.2-3.2.1-.3.5-1.5-.1-3.1 0 0-1-.3-3.3 1.2a11 11 0 0 0-5.6 0C6.5 1.5 5.5 1.8 5.5 1.8c-.6 1.6-.2 2.8-.1 3.1-.7.8-1.2 1.9-1.2 3.2 0 4.6 2.7 5.6 5.4 5.9-.4.4-.7.9-.8 1.7"/></svg>',
    "linkedin": '<svg class="ic" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM10 9h3.8v1.7h.05c.53-.95 1.83-1.95 3.76-1.95 4.02 0 4.76 2.5 4.76 5.76V21h-4v-5.3c0-1.26-.02-2.9-1.77-2.9-1.77 0-2.04 1.38-2.04 2.8V21h-4z"/></svg>',
    # official brand marks (Simple Icons, CC0) — filled, not hand-drawn
    "x": '<svg class="ic" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754 11.09h-3.182z"/></svg>',
    "wechat": '<svg class="ic" viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446 1.703-1.415 3.882-1.98 5.853-1.838-.576-3.583-4.196-6.348-8.596-6.348zM5.785 5.991c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178A1.17 1.17 0 0 1 4.623 7.17c0-.651.52-1.18 1.162-1.18zm5.813 0c.642 0 1.162.529 1.162 1.18a1.17 1.17 0 0 1-1.162 1.178 1.17 1.17 0 0 1-1.162-1.178c0-.651.52-1.18 1.162-1.18zm5.34 2.867c-1.797-.052-3.746.512-5.28 1.786-1.72 1.428-2.687 3.72-1.78 6.22.942 2.453 3.666 4.229 6.884 4.229.826 0 1.622-.12 2.361-.336a.722.722 0 0 1 .598.082l1.584.926a.272.272 0 0 0 .14.047c.134 0 .24-.111.24-.247 0-.06-.023-.12-.038-.177l-.327-1.233a.582.582 0 0 1-.023-.156.49.49 0 0 1 .201-.398C23.024 18.48 24 16.82 24 14.98c0-3.21-2.931-5.837-6.656-6.088V8.89c-.135-.01-.27-.027-.407-.03zm-2.53 3.274c.535 0 .969.44.969.982a.976.976 0 0 1-.969.983.976.976 0 0 1-.969-.983c0-.542.434-.982.97-.982zm4.844 0c.535 0 .969.44.969.982a.976.976 0 0 1-.969.983.976.976 0 0 1-.969-.983c0-.542.434-.982.969-.982z"/></svg>',
}

SUN = '<svg class="ic sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg class="ic moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'


# ---- personal data ------------------------------------------------
def get_personal_data():
    name = ["Zilong", "Chen"]
    role = "Ph.D. Candidate &middot; Tsinghua University"
    interests = "multimodal generation &middot; world model"
    bio = (
        '<p class="bio">I am a Ph.D. candidate at the Department of Computer Science and Technology, '
        'Tsinghua University, advised by <a href="https://sites.google.com/site/thuliuhuaping/home" target="_blank">Prof. Huaping Liu</a> '
        'and working closely with <a href="https://wangfeng18.github.io/" target="_blank">Dr. Feng Wang</a> and '
        '<a href="https://yikaiw.github.io/" target="_blank">Prof. Yikai Wang</a>. Before Tsinghua, I completed my '
        'undergraduate studies at Xi\'an Jiaotong University under <a href="https://gr.xjtu.edu.cn/web/minnluo/" target="_blank">Prof. Minnan Luo</a>, '
        'focusing on knowledge graphs and their applications in natural language processing.</p>'
    )
    links = [
        (IC["cv"], "CV", "./cv/rendercv_output/Zilong_Chen_CV.pdf", True),
        (IC["mail"], "Email", "mailto:jaysonabcchen@gmail.com", False),
        (IC["scholar"], "Scholar", "https://scholar.google.com.hk/citations?user=2pbka1gAAAAJ&hl=en", True),
        (IC["github"], "GitHub", "https://github.com/heheyas", True),
        (IC["x"], "X", "https://x.com/heheyChen", True),
        (IC["linkedin"], "LinkedIn", "https://www.linkedin.com/in/zilong-chen-99671523b/", True),
        (IC["wechat"], "WeChat", "./assets/img/heheyas-wechat.jpg", False),
    ]
    link_html = '<nav class="links">'
    for icon, label, href, blank in links:
        tgt = ' target="_blank"' if blank else ""
        link_html += f'<a href="{href}"{tgt}>{icon}{label}</a>'
    link_html += "</nav>"
    return name, role, interests, bio, link_html


# ---- news / updates (from PRISM content/news.toml) ----------------
NEWS = [
    ("Mar 2025", 'MeshGen accepted to CVPR 2025 as a <b>Highlight</b>.'),
    ("Jan 2025", 'V3D accepted to <b>T-PAMI</b>.'),
    ("Sep 2024", 'Vidu4D accepted to NeurIPS 2024.'),
    ("Feb 2024", 'GSGEN and GaussianEditor accepted to CVPR 2024.'),
    ("Sep 2023", 'MSTH accepted to NeurIPS 2023 as a <b>Spotlight</b>.'),
]


def get_news_html():
    items = "".join(
        f'<li><span class="nd">{date}</span><span class="nc">{content}</span></li>'
        for date, content in NEWS
    )
    return f'<ul class="news">{items}</ul>'


def get_author_dict():
    return {
        "Feng Wang": "https://wangfeng18.github.io/",
        "Yikai Wang": "https://yikaiw.github.io/",
        "Huaping Liu": "https://sites.google.com/site/thuliuhuaping/home",
        "Zhengyi Wang": "https://thuwzy.github.io/",
        "Yiwen Chen": "https://buaacyw.github.io/",
        "Wenqiang Sun": "",
    }


def github_link_to_star_badge(github_url):
    try:
        parts = github_url.strip("/").split("/")
        if len(parts) < 5:
            raise ValueError("Invalid GitHub URL format.")
        user, repo = parts[-2], parts[-1]
        badge_url = f"https://img.shields.io/github/stars/{user}/{repo}?style=social"
        return f'<img src="{badge_url}" alt="stars">'
    except Exception as e:
        return str(e)


def generate_person_html(persons, connection=", ", make_bold=True,
                         make_bold_name="Zilong Chen", add_links=True):
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
        extra = "*" if co_first_author else ""
        if string_part_i in links.keys() and links[string_part_i]:
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i + extra}</a>'
        elif string_part_i != make_bold_name and add_links:
            string_part_i = f'<a href="{DEFAULT_URL + string_part_i}" target="_blank">{string_part_i + extra}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span class="me">{make_bold_name + extra}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s


def _venue(f):
    return (f.get("booktitle") or f.get("journal") or "").strip()


def _bibtex_block(entry_key, entry):
    f = entry.fields
    cite = "@InProceedings{" + f"{entry_key},\n"
    cite += ("  author = {"
             + generate_person_html(entry.persons["author"], make_bold=False, add_links=False, connection=" and ")
             + "},\n")
    cite += "  title = {" + f.get("title", "") + "},\n"
    cite += "  booktitle = {" + _venue(f) + "},\n"
    cite += "  year = {" + f.get("year", "") + "},\n"
    cite += "}"
    return cite


def get_paper_entry(entry_key, entry):
    f = entry.fields
    img = f.get("img", "").strip()
    has_media = bool(img)
    media = ""
    if has_media:
        if img.split(".")[-1].lower() == "mp4":
            media = (f'<video muted loop autoplay playsinline><source src="{img}" '
                     f'type="video/mp4"></video>')
        else:
            media = f'<img src="{img}" alt="{f.get("title", "")}">'

    title = f.get("title", "")
    title_href = f["project"] if "project" in f.keys() and f["project"].strip() else DEFAULT_URL + title
    authors = generate_person_html(entry.persons["author"])
    venue, year = _venue(f), f.get("year", "")
    award = f'<span class="award">{f["award"]}</span>' if "award" in f.keys() else ""

    artefacts = [("project", "Project"), ("youtube", "Video"),
                 ("poster", "Poster"), ("github", "Code"), ("arxiv", "arXiv")]
    parts = []
    for k, label in artefacts:
        v = f.get(k, "").strip()
        if v:
            a = f'<a href="{v}" target="_blank">{label}</a>'
            if k == "github":
                a += f' {github_link_to_star_badge(v)}'
            parts.append(a)
    links_html = '<span class="sep">·</span>'.join(parts)

    meta = ""
    if venue:
        meta += f'<span class="venue">{venue}</span> '
    if year:
        meta += f'<span class="yr">{year}</span>'
    meta += award

    cite = _bibtex_block(entry_key, entry)
    body = (
        '<div class="pub-body">'
        f'<a class="t" href="{title_href}" target="_blank">{title}</a>'
        f'<div class="au">{authors}</div>'
        f'<div class="meta">{meta}</div>'
        + (f'<div class="plinks">{links_html}</div>' if links_html else '')
        + '<details class="bib"><summary>bibtex</summary><div class="bibbox">'
        '<button class="bibcopy" type="button">copy</button>'
        f'<pre>{cite}</pre></div></details>'
        + '</div>'
    )
    if has_media:
        return f'<div class="pub"><div class="pub-thumb">{media}</div>{body}</div>'
    return f'<div class="pub nomedia">{body}</div>'


def _entries_html(bib_file):
    parser = bibtex.Parser()
    bib_data = parser.parse_file(bib_file)
    return "".join(get_paper_entry(k, bib_data.entries[k]) for k in bib_data.entries.keys())


# ---- shared styles -----------------------------------------------
CSS = r"""
:root{--paper:#f6f6f2;--card:#fcfcf8;--ink:#1a1a17;--ink-strong:#0a0a0a;--muted:#5e574a;--soft:#8c8473;--rule:#e3e1d6;--accent:#1f7a4d;
  --topbar-bg:rgba(246,246,242,0.82);--accent-soft:rgba(31,122,77,0.11);--accent-line:rgba(31,122,77,0.28);--code-bg:#16160f;--code-fg:#e8e3d6;--thumb-bg:#efeee7;}
:root[data-theme="dark"]{--paper:#14140f;--card:#1d1c16;--ink:#e7e5db;--ink-strong:#f6f4ec;--muted:#a49e8f;--soft:#7c7669;--rule:#2d2b23;--accent:#5cb488;
  --topbar-bg:rgba(20,20,15,0.82);--accent-soft:rgba(92,180,136,0.15);--accent-line:rgba(92,180,136,0.38);--code-bg:#0e0e0a;--code-fg:#e8e3d6;--thumb-bg:#26251d;}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
html,body{margin:0;background:var(--paper);color:var(--ink);font-family:"Hanken Grotesk",system-ui,-apple-system,sans-serif;font-size:17px;line-height:1.62;-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;transition:background-color .25s ease,color .25s ease;}
a{color:var(--accent);text-decoration:none;}
a:hover{text-decoration:underline;}
::selection{background:var(--ink);color:var(--paper);}
.wrap{max-width:860px;margin:0 auto;padding:40px 28px 72px;}
/* sticky top nav */
.topbar{position:sticky;top:0;z-index:50;background:var(--topbar-bg);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--rule);}
.topbar-inner{max-width:860px;margin:0 auto;padding:10px 28px;display:flex;align-items:center;justify-content:space-between;gap:16px;}
.brand{font-weight:700;font-size:15px;letter-spacing:-0.02em;color:var(--ink-strong);}
.brand:hover{color:var(--accent);text-decoration:none;}
.navlinks{display:flex;gap:3px;align-items:center;}
.navlinks a{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--muted);padding:6px 11px;border-radius:100px;white-space:nowrap;transition:color .15s,background .15s;}
.navlinks a:hover{color:var(--accent);text-decoration:none;}
.navlinks a.active{color:var(--ink-strong);background:var(--accent-soft);}
.navlinks a.cv{color:var(--accent);}
.themebtn{margin-left:4px;display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border:1px solid var(--rule);border-radius:100px;background:transparent;color:var(--muted);cursor:pointer;transition:color .15s,border-color .15s;}
.themebtn:hover{color:var(--accent);border-color:var(--accent);}
.themebtn .ic{width:15px;height:15px;}
.themebtn .sun{display:none;}
:root[data-theme="dark"] .themebtn .sun{display:inline-flex;}
:root[data-theme="dark"] .themebtn .moon{display:none;}
section[id],header[id]{scroll-margin-top:64px;}
/* hero */
.hero{display:grid;grid-template-columns:1fr 168px;gap:32px;align-items:start;}
.name{font-size:clamp(2rem,5.2vw,3rem);font-weight:700;letter-spacing:-0.03em;line-height:1.0;margin:0 0 10px;color:var(--ink-strong);}
.role{font-family:"IBM Plex Mono",monospace;font-size:13px;color:var(--muted);margin:0 0 3px;letter-spacing:0.01em;}
.interests{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--accent);margin:0 0 16px;}
.bio{margin:0 0 16px;color:var(--ink);}
.bio a{font-weight:500;}
.photo-wrap{justify-self:end;}
.photo{width:168px;height:auto;border-radius:6px;border:1px solid var(--rule);display:block;}
.links{display:flex;flex-wrap:wrap;gap:8px;}
.links a{display:inline-flex;align-items:center;gap:7px;font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--ink);background:var(--card);border:1px solid var(--rule);border-radius:100px;padding:7px 14px;transition:border-color .15s,color .15s;}
.links a:hover{border-color:var(--accent);color:var(--accent);text-decoration:none;}
.links a .ic{width:15px;height:15px;flex:0 0 auto;}
/* sections */
section{margin-top:46px;}
h2{font-size:1.42rem;font-weight:700;letter-spacing:-0.02em;color:var(--ink-strong);margin:0 0 3px;}
h2 .extra{font-family:"IBM Plex Mono",monospace;font-size:11.5px;font-weight:400;color:var(--soft);letter-spacing:0;}
h2 .extra a{color:var(--muted);}
.sechr{border:none;border-top:1px solid var(--rule);margin:11px 0 24px;}
/* publications */
.pub{display:grid;grid-template-columns:196px 1fr;gap:22px;margin:0 0 27px;align-items:start;}
.pub.nomedia{grid-template-columns:1fr;}
.pub-body{min-width:0;}
.pub-thumb img,.pub-thumb video{width:100%;border-radius:4px;border:1px solid var(--rule);display:block;background:var(--thumb-bg);}
.pub-body .t{font-size:1.02rem;font-weight:600;color:var(--ink-strong);line-height:1.32;}
.pub-body .t:hover{color:var(--accent);text-decoration:none;}
.pub-body .au{font-size:0.87rem;color:var(--muted);margin:5px 0 4px;line-height:1.55;}
.pub-body .au a{color:var(--muted);}
.pub-body .au a:hover{color:var(--accent);}
.pub-body .au .me{font-weight:700;color:var(--ink-strong);}
.meta{font-family:"IBM Plex Mono",monospace;font-size:12px;margin:3px 0 8px;display:flex;align-items:center;flex-wrap:wrap;gap:7px;}
.meta .venue{font-weight:600;color:var(--ink-strong);}
.meta .yr{color:var(--muted);}
.award{font-family:"IBM Plex Mono",monospace;font-size:9.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--accent);background:var(--accent-soft);border:1px solid var(--accent-line);padding:2px 8px;border-radius:100px;}
.plinks{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--muted);display:flex;flex-wrap:wrap;align-items:center;gap:8px;}
.plinks img{vertical-align:middle;height:15px;}
.plinks .sep{color:var(--rule);}
details.bib{margin-top:9px;}
details.bib>summary{font-size:0;cursor:pointer;list-style:none;width:fit-content;}
details.bib>summary::-webkit-details-marker{display:none;}
details.bib>summary::before{content:"+ bibtex";font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--accent);}
details.bib[open]>summary::before{content:"− bibtex";}
.bibbox{position:relative;margin-top:8px;}
.bibbox pre{background:var(--code-bg);color:var(--code-fg);font-family:"IBM Plex Mono",monospace;font-size:11.5px;line-height:1.55;padding:14px 16px;border-radius:4px;overflow-x:auto;margin:0;white-space:pre;max-width:100%;}
.bibcopy{position:absolute;top:8px;right:8px;font-family:"IBM Plex Mono",monospace;font-size:10px;letter-spacing:.04em;text-transform:uppercase;color:#cbd5c0;background:rgba(255,255,255,0.09);border:1px solid rgba(255,255,255,0.2);border-radius:4px;padding:4px 8px;cursor:pointer;transition:background .15s,color .15s;}
.bibcopy:hover{background:rgba(255,255,255,0.18);color:#fff;}
.bibcopy.ok{color:#7fdda8;border-color:rgba(127,221,168,0.55);}
/* news */
.news{list-style:none;margin:0;padding:0;}
.news li{display:grid;grid-template-columns:84px 1fr;gap:16px;padding:5px 0;font-size:0.97rem;align-items:baseline;}
.news .nd{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--accent);white-space:nowrap;}
.news .nc{color:var(--ink);min-width:0;}
.news .nc b{font-weight:600;color:var(--ink-strong);}
/* services */
.svc{font-size:0.96rem;color:var(--ink);line-height:1.95;}
.svc b{font-weight:600;color:var(--ink-strong);}
/* full-list page header */
.fl-head{padding-top:6px;}
.fl-back{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--muted);}
.fl-back:hover{color:var(--accent);text-decoration:none;}
@media(max-width:640px){
  .wrap{padding:34px 20px 56px;}
  .topbar-inner{padding:8px 16px;gap:10px;}
  .navlinks{gap:0;overflow-x:auto;flex-wrap:nowrap;-ms-overflow-style:none;scrollbar-width:none;}
  .navlinks::-webkit-scrollbar{display:none;}
  .navlinks a{padding:6px 8px;font-size:11.5px;}
  .hero{grid-template-columns:1fr;gap:20px;}
  .photo-wrap{order:-1;justify-self:start;}
  .photo{width:132px;}
  .pub{grid-template-columns:1fr;gap:12px;}
  .pub-thumb{max-width:300px;}
}
@media(max-width:460px){
  .brand{display:none;}
  .navlinks{width:100%;justify-content:space-between;}
}
"""

SCRIPTS = r"""<script>
(function(){
  // active-section highlight (only fires when in-page #anchors exist)
  var links = {};
  document.querySelectorAll('.navlinks a[href^="#"]').forEach(function(a){ links[a.getAttribute('href').slice(1)] = a; });
  if(Object.keys(links).length){
    var obs = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(e.isIntersecting){
          for(var k in links) links[k].classList.remove('active');
          if(links[e.target.id]) links[e.target.id].classList.add('active');
        }
      });
    }, {rootMargin:'-45% 0px -50% 0px', threshold:0});
    document.querySelectorAll('section[id]').forEach(function(s){ obs.observe(s); });
  }
  // one-click BibTeX copy
  document.querySelectorAll('.bibcopy').forEach(function(btn){
    btn.addEventListener('click', function(){
      var pre = btn.parentNode.querySelector('pre');
      var text = pre.textContent;
      var done = function(){
        btn.textContent = 'copied ✓'; btn.classList.add('ok');
        setTimeout(function(){ btn.textContent = 'copy'; btn.classList.remove('ok'); }, 1400);
      };
      if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(text).then(done).catch(fallback);
      } else { fallback(); }
      function fallback(){
        var ta = document.createElement('textarea');
        ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
        document.body.appendChild(ta); ta.select();
        try{ document.execCommand('copy'); }catch(e){}
        document.body.removeChild(ta); done();
      }
    });
  });
  // theme toggle
  var tb = document.querySelector('.themebtn');
  if(tb){ tb.addEventListener('click', function(){
    var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', cur);
    try{ localStorage.setItem('theme', cur); }catch(e){}
  }); }
})();
</script>"""

PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="icon" type="image/x-icon" href="assets/img/avatar.jpg">
<script>(function(){try{var t=localStorage.getItem('theme');if(!t)t=matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';document.documentElement.setAttribute('data-theme',t);}catch(e){}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,300..700;1,400..600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>__CSS__</style>
</head>
<body>
__NAV__
<main class="wrap">
__BODY__
</main>
__SCRIPTS__
</body>
</html>
"""


def render_nav(base=""):
    def h(anchor):
        return (base + anchor) if base else anchor
    return (
        '<nav class="topbar"><div class="topbar-inner">'
        f'<a class="brand" href="{h("#about")}">Zilong Chen</a>'
        '<div class="navlinks">'
        f'<a href="{h("#news")}">News</a>'
        f'<a href="{h("#publications")}">Publications</a>'
        f'<a href="{h("#projects")}">Projects</a>'
        f'<a href="{h("#services")}">Services</a>'
        '<a class="cv" href="./cv/rendercv_output/Zilong_Chen_CV.pdf" target="_blank">CV &#8599;</a>'
        f'<button class="themebtn" type="button" aria-label="Toggle theme">{SUN}{MOON}</button>'
        '</div></div></nav>'
    )


def render_page(title, desc, nav, body):
    return (PAGE.replace("__CSS__", CSS).replace("__NAV__", nav)
            .replace("__BODY__", body).replace("__SCRIPTS__", SCRIPTS)
            .replace("__TITLE__", title).replace("__DESC__", desc))


SERVICES = (
    '<div class="svc">'
    '<b>Conference reviewer</b> &nbsp; CVPR &middot; NeurIPS &middot; ICLR &middot; ICML &middot; ICCV &middot; AAAI &middot; ACL &middot; IROS &middot; ICRA<br>'
    '<b>Journal reviewer</b> &nbsp;&nbsp;&nbsp; T-PAMI &middot; Neurocomputing &middot; TIP &middot; JMLR'
    '</div>'
)


def get_index_html():
    name, role, interests, bio, links_html = get_personal_data()
    full = name[0] + " " + name[1]
    body = (
        f'<header class="hero" id="about"><div class="hero-text">'
        f'<h1 class="name">{full}</h1>'
        f'<p class="role">{role}</p>'
        f'<p class="interests">{interests}</p>'
        f'{bio}{links_html}</div>'
        '<div class="photo-wrap"><img class="photo" src="assets/img/avatar.jpg" alt="' + full + '" '
        "onmouseover=\"this.src='assets/img/zilong_chen.jpg'\" onmouseout=\"this.src='assets/img/avatar.jpg'\"></div>"
        '</header>'
        f'<section id="news"><h2>News</h2><hr class="sechr">{get_news_html()}</section>'
        '<section id="publications"><h2>Selected publications '
        '<span class="extra">[<a href="full_list.html">full list</a>] &middot; * equal contribution</span></h2>'
        f'<hr class="sechr">{_entries_html("zilong.bib")}</section>'
        f'<section id="projects"><h2>Open-source projects</h2><hr class="sechr">{_entries_html("project.bib")}</section>'
        f'<section id="services"><h2>Services</h2><hr class="sechr">{SERVICES}</section>'
    )
    desc = f"{full} — Ph.D. candidate at Tsinghua University. Multimodal generation, world model."
    return render_page(full, desc, render_nav(""), body)


def get_fulllist_html():
    body = (
        '<header class="fl-head" id="about">'
        '<a class="fl-back" href="index.html">&larr; Zilong Chen</a>'
        '<h1 class="name" style="margin-top:12px;">Publications</h1>'
        '<p class="role">Full list &middot; * equal contribution</p>'
        '</header>'
        f'<section id="publications" style="margin-top:26px;"><hr class="sechr">{_entries_html("zilong_full.bib")}</section>'
    )
    return render_page("Publications — Zilong Chen", "Full publication list of Zilong Chen.",
                       render_nav("index.html"), body)


def write_site():
    with open("index.html", "w") as f:
        f.write(get_index_html())
    with open("full_list.html", "w") as f:
        f.write(get_fulllist_html())
    print("Written index.html and full_list.html.")


if __name__ == "__main__":
    write_site()
