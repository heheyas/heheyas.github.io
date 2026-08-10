
#import "@preview/fontawesome:0.5.0": fa-icon

#let name = "Zilong Chen"
#let locale-catalog-page-numbering-style = context { "Zilong Chen - Page " + str(here().page()) + " of " + str(counter(page).final().first()) + "" }
#let locale-catalog-last-updated-date-style = "Last updated in Aug 2026"
#let locale-catalog-language = "en"
#let design-page-size = "us-letter"
#let design-colors-text = rgb(0, 0, 0)
#let design-colors-section-titles = rgb(0, 79, 144)
#let design-colors-last-updated-date-and-page-numbering = rgb(128, 128, 128)
#let design-colors-name = rgb(0, 79, 144)
#let design-colors-connections = rgb(0, 79, 144)
#let design-colors-links = rgb(0, 79, 144)
#let design-section-titles-font-family = "Source Sans 3"
#let design-section-titles-bold = true
#let design-section-titles-line-thickness = 0.5pt
#let design-section-titles-font-size = 1.4em
#let design-section-titles-type = "with-partial-line"
#let design-section-titles-vertical-space-above = 0.5cm
#let design-section-titles-vertical-space-below = 0.3cm
#let design-section-titles-small-caps = false
#let design-links-use-external-link-icon = true
#let design-text-font-size = 10pt
#let design-text-leading = 0.6em
#let design-text-font-family = "Source Sans 3"
#let design-text-alignment = "justified"
#let design-text-date-and-location-column-alignment = right
#let design-header-photo-width = 3.5cm
#let design-header-use-icons-for-connections = true
#let design-header-name-font-family = "Source Sans 3"
#let design-header-name-font-size = 30pt
#let design-header-name-bold = true
#let design-header-small-caps-for-name = false
#let design-header-connections-font-family = "Source Sans 3"
#let design-header-vertical-space-between-name-and-connections = 0.7cm
#let design-header-vertical-space-between-connections-and-first-section = 0.7cm
#let design-header-use-icons-for-connections = true
#let design-header-horizontal-space-between-connections = 0.5cm
#let design-header-separator-between-connections = ""
#let design-header-alignment = center
#let design-highlights-summary-left-margin = 0cm
#let design-highlights-bullet = "•"
#let design-highlights-nested-bullet = "-"
#let design-highlights-top-margin = 0.25cm
#let design-highlights-left-margin = 0.4cm
#let design-highlights-vertical-space-between-highlights = 0.25cm
#let design-highlights-horizontal-space-between-bullet-and-highlights = 0.5em
#let design-entries-vertical-space-between-entries = 1.2em
#let design-entries-date-and-location-width = 0.01cm
#let design-entries-allow-page-break-in-entries = true
#let design-entries-horizontal-space-between-columns = 0cm
#let design-entries-left-and-right-margin = 0.1cm
#let design-page-top-margin = 2cm
#let design-page-bottom-margin = 2cm
#let design-page-left-margin = 2cm
#let design-page-right-margin = 2cm
#let design-page-show-last-updated-date = true
#let design-page-show-page-numbering = true
#let design-links-underline = false
#let design-entry-types-education-entry-degree-column-width = 1cm
#let date = datetime.today()

// Metadata:
#set document(author: name, title: name + "'s CV", date: date)

// Page settings:
#set page(
  margin: (
    top: design-page-top-margin,
    bottom: design-page-bottom-margin,
    left: design-page-left-margin,
    right: design-page-right-margin,
  ),
  paper: design-page-size,
  footer: if design-page-show-page-numbering {
    text(
      fill: design-colors-last-updated-date-and-page-numbering,
      align(center, [_#locale-catalog-page-numbering-style _]),
      size: 0.9em,
    )
  } else {
    none
  },
  footer-descent: 0% - 0.3em + design-page-bottom-margin / 2,
)
// Text settings:
#let justify
#let hyphenate
#if design-text-alignment == "justified" {
  justify = true
  hyphenate = true
} else if design-text-alignment == "left" {
  justify = false
  hyphenate = false
} else if design-text-alignment == "justified-with-no-hyphenation" {
  justify = true
  hyphenate = false
}
#set text(
  font: design-text-font-family,
  size: design-text-font-size,
  lang: locale-catalog-language,
  hyphenate: hyphenate,
  fill: design-colors-text,
  // Disable ligatures for better ATS compatibility:
  ligatures: true,
)
#set par(
  spacing: 0pt,
  leading: design-text-leading,
  justify: justify,
)
#set enum(
  spacing: design-entries-vertical-space-between-entries,
)

// Highlights settings:
#let highlights(..content) = {
  list(
    ..content,
    marker: design-highlights-bullet,
    spacing: design-highlights-vertical-space-between-highlights,
    indent: design-highlights-left-margin,
    body-indent: design-highlights-horizontal-space-between-bullet-and-highlights,
  )
}
#show list: set list(
  marker: design-highlights-nested-bullet,
  spacing: design-highlights-vertical-space-between-highlights,
  indent: 0pt,
  body-indent: design-highlights-horizontal-space-between-bullet-and-highlights,
)

// Entry utilities:
#let bullet-entry(..content) = {
  list(
    ..content,
    marker: design-highlights-bullet,
    spacing: 0pt,
    indent: 0pt,
    body-indent: design-highlights-horizontal-space-between-bullet-and-highlights,
  )
}
#let three-col(
  left-column-width: 1fr,
  middle-column-width: 1fr,
  right-column-width: design-entries-date-and-location-width,
  left-content: "",
  middle-content: "",
  right-content: "",
  alignments: (auto, auto, auto),
) = [
  #block(
    grid(
      columns: (left-column-width, middle-column-width, right-column-width),
      column-gutter: design-entries-horizontal-space-between-columns,
      align: alignments,
      ([#set par(spacing: design-text-leading); #left-content]),
      ([#set par(spacing: design-text-leading); #middle-content]),
      ([#set par(spacing: design-text-leading); #right-content]),
    ),
    breakable: true,
    width: 100%,
  )
]

#let two-col(
  left-column-width: 1fr,
  right-column-width: design-entries-date-and-location-width,
  left-content: "",
  right-content: "",
  alignments: (auto, auto),
  column-gutter: design-entries-horizontal-space-between-columns,
) = [
  #block(
    grid(
      columns: (left-column-width, right-column-width),
      column-gutter: column-gutter,
      align: alignments,
      ([#set par(spacing: design-text-leading); #left-content]),
      ([#set par(spacing: design-text-leading); #right-content]),
    ),
    breakable: true,
    width: 100%,
  )
]

// Main heading settings:
#let header-font-weight
#if design-header-name-bold {
  header-font-weight = 700
} else {
  header-font-weight = 400
}
#show heading.where(level: 1): it => [
  #set par(spacing: 0pt)
  #set align(design-header-alignment)
  #set text(
    font: design-header-name-font-family,
    weight: header-font-weight,
    size: design-header-name-font-size,
    fill: design-colors-name,
  )
  #if design-header-small-caps-for-name [
    #smallcaps(it.body)
  ] else [
    #it.body
  ]
  // Vertical space after the name
  #v(design-header-vertical-space-between-name-and-connections)
]

#let section-title-font-weight
#if design-section-titles-bold {
  section-title-font-weight = 700
} else {
  section-title-font-weight = 400
}

#show heading.where(level: 2): it => [
  #set align(left)
  #set text(size: (1em / 1.2)) // reset
  #set text(
    font: design-section-titles-font-family,
    size: (design-section-titles-font-size),
    weight: section-title-font-weight,
    fill: design-colors-section-titles,
  )
  #let section-title = (
    if design-section-titles-small-caps [
      #smallcaps(it.body)
    ] else [
      #it.body
    ]
  )
  // Vertical space above the section title
  #v(design-section-titles-vertical-space-above, weak: true)
  #block(
    breakable: false,
    width: 100%,
    [
      #if design-section-titles-type == "moderncv" [
        #two-col(
          alignments: (right, left),
          left-column-width: design-entries-date-and-location-width,
          right-column-width: 1fr,
          left-content: [
            #align(horizon, box(width: 1fr, height: design-section-titles-line-thickness, fill: design-colors-section-titles))
          ],
          right-content: [
            #section-title
          ]
        )

      ] else [
        #box(
          [
            #section-title
            #if design-section-titles-type == "with-partial-line" [
              #box(width: 1fr, height: design-section-titles-line-thickness, fill: design-colors-section-titles)
            ] else if design-section-titles-type == "with-full-line" [

              #v(design-text-font-size * 0.4)
              #box(width: 1fr, height: design-section-titles-line-thickness, fill: design-colors-section-titles)
            ]
          ]
        )
      ]
     ] + v(1em),
  )
  #v(-1em)
  // Vertical space after the section title
  #v(design-section-titles-vertical-space-below - 0.5em)
]

// Links:
#let original-link = link
#let link(url, body) = {
  body = [#if design-links-underline [#underline(body)] else [#body]]
  body = [#if design-links-use-external-link-icon [#body#h(design-text-font-size/4)#box(
        fa-icon("external-link", size: 0.7em),
        baseline: -10%,
      )] else [#body]]
  body = [#set text(fill: design-colors-links);#body]
  original-link(url, body)
}

// Last updated date text:
#if design-page-show-last-updated-date {
  let dx
  if design-section-titles-type == "moderncv" {
    dx = 0cm
  } else {
    dx = -design-entries-left-and-right-margin
  }
  place(
    top + right,
    dy: -design-page-top-margin / 2,
    dx: dx,
    text(
      [_#locale-catalog-last-updated-date-style _],
      fill: design-colors-last-updated-date-and-page-numbering,
      size: 0.9em,
    ),
  )
}

#let connections(connections-list) = context {
  set text(fill: design-colors-connections, font: design-header-connections-font-family)
  set par(leading: design-text-leading*1.7, justify: false)
  let list-of-connections = ()
  let separator = (
    h(design-header-horizontal-space-between-connections / 2, weak: true)
      + design-header-separator-between-connections
      + h(design-header-horizontal-space-between-connections / 2, weak: true)
  )
  let starting-index = 0
  while (starting-index < connections-list.len()) {
    let left-sum-right-margin
    if type(page.margin) == "dictionary" {
      left-sum-right-margin = page.margin.left + page.margin.right
    } else {
      left-sum-right-margin = page.margin * 4
    }

    let ending-index = starting-index + 1
    while (
      measure(connections-list.slice(starting-index, ending-index).join(separator)).width
        < page.width - left-sum-right-margin
    ) {
      ending-index = ending-index + 1
      if ending-index > connections-list.len() {
        break
      }
    }
    if ending-index > connections-list.len() {
      ending-index = connections-list.len()
    }
    list-of-connections.push(connections-list.slice(starting-index, ending-index).join(separator))
    starting-index = ending-index
  }
  align(list-of-connections.join(linebreak()), design-header-alignment)
  v(design-header-vertical-space-between-connections-and-first-section - design-section-titles-vertical-space-above)
}

#let three-col-entry(
  left-column-width: 1fr,
  right-column-width: design-entries-date-and-location-width,
  left-content: "",
  middle-content: "",
  right-content: "",
  alignments: (left, auto, right),
) = (
  if design-section-titles-type == "moderncv" [
    #three-col(
      left-column-width: right-column-width,
      middle-column-width: left-column-width,
      right-column-width: 1fr,
      left-content: right-content,
      middle-content: [
        #block(
          [
            #left-content
          ],
          inset: (
            left: design-entries-left-and-right-margin,
            right: design-entries-left-and-right-margin,
          ),
          breakable: design-entries-allow-page-break-in-entries,
          width: 100%,
        )
      ],
      right-content: middle-content,
      alignments: (design-text-date-and-location-column-alignment, left, auto),
    )
  ] else [
    #block(
      [
        #three-col(
          left-column-width: left-column-width,
          right-column-width: right-column-width,
          left-content: left-content,
          middle-content: middle-content,
          right-content: right-content,
          alignments: alignments,
        )
      ],
      inset: (
        left: design-entries-left-and-right-margin,
        right: design-entries-left-and-right-margin,
      ),
      breakable: design-entries-allow-page-break-in-entries,
      width: 100%,
    )
  ]
)

#let two-col-entry(
  left-column-width: 1fr,
  right-column-width: design-entries-date-and-location-width,
  left-content: "",
  right-content: "",
  alignments: (auto, design-text-date-and-location-column-alignment),
  column-gutter: design-entries-horizontal-space-between-columns,
) = (
  if design-section-titles-type == "moderncv" [
    #two-col(
      left-column-width: right-column-width,
      right-column-width: left-column-width,
      left-content: right-content,
      right-content: [
        #block(
          [
            #left-content
          ],
          inset: (
            left: design-entries-left-and-right-margin,
            right: design-entries-left-and-right-margin,
          ),
          breakable: design-entries-allow-page-break-in-entries,
          width: 100%,
        )
      ],
      alignments: (design-text-date-and-location-column-alignment, auto),
    )
  ] else [
    #block(
      [
        #two-col(
          left-column-width: left-column-width,
          right-column-width: right-column-width,
          left-content: left-content,
          right-content: right-content,
          alignments: alignments,
        )
      ],
      inset: (
        left: design-entries-left-and-right-margin,
        right: design-entries-left-and-right-margin,
      ),
      breakable: design-entries-allow-page-break-in-entries,
      width: 100%,
    )
  ]
)

#let one-col-entry(content: "") = [
  #let left-space = design-entries-left-and-right-margin
  #if design-section-titles-type == "moderncv" [
    #(left-space = left-space + design-entries-date-and-location-width + design-entries-horizontal-space-between-columns)
  ]
  #block(
    [#set par(spacing: design-text-leading); #content],
    breakable: design-entries-allow-page-break-in-entries,
    inset: (
      left: left-space,
      right: design-entries-left-and-right-margin,
    ),
    width: 100%,
  )
]

= Zilong Chen

// Print connections:
#let connections-list = (
  [#fa-icon("location-dot", size: 0.9em) #h(0.05cm)Tsinghua University, Beijing, China],
  [#box(original-link("mailto:jaysonabcchen@gmail.com")[#fa-icon("envelope", size: 0.9em) #h(0.05cm)jaysonabcchen\@gmail.com])],
  [#box(original-link("tel:+86-186-2945-1544")[#fa-icon("phone", size: 0.9em) #h(0.05cm)186 2945 1544])],
  [#box(original-link("https://heheyas.github.io/")[#fa-icon("link", size: 0.9em) #h(0.05cm)heheyas.github.io])],
  [#box(original-link("https://linkedin.com/in/zilong-chen-99671523b")[#fa-icon("linkedin", size: 0.9em) #h(0.05cm)zilong-chen-99671523b])],
  [#box(original-link("https://github.com/heheyas")[#fa-icon("github", size: 0.9em) #h(0.05cm)heheyas])],
  [#box(original-link("https://scholar.google.com/citations?user=2pbka1gAAAAJ")[#fa-icon("graduation-cap", size: 0.9em) #h(0.05cm)Google Scholar])],
)
#connections(connections-list)



== Summary


#one-col-entry(
  content: [I work on multimodal generation, currently on turning the text interface of a generative model into something that can be measured and scaled. My earlier work covers 3D and 4D reconstruction and generation, including text-to-3D with Gaussian splatting, video diffusion models as 3D generators, and native mesh generation, published at CVPR, NeurIPS, and T-PAMI. Before Tsinghua I worked on knowledge graphs and their applications in natural language processing.]
)


== Education


// NO DATE, YES DEGREE
#two-col-entry(
  left-column-width: 1cm,
  right-column-width: 1fr,
  alignments: (left, left),
  left-content: [
    #strong[PhD]
  ],
  right-content: [
    #strong[Tsinghua University], Computer Science (#emph[Sept 2022 – present])
  ],
)
#block(
  [
    #set par(spacing: 0pt)
    #v(design-highlights-top-margin);#highlights([Advisor: #link("https://sites.google.com/site/thuliuhuaping")[Huaping Liu]],)
  ],
  inset: (
    left: design-entry-types-education-entry-degree-column-width + design-entries-horizontal-space-between-columns + design-entries-left-and-right-margin,
    right: design-entries-left-and-right-margin,
  ),
)

#v(design-entries-vertical-space-between-entries)
// NO DATE, YES DEGREE
#two-col-entry(
  left-column-width: 1cm,
  right-column-width: 1fr,
  alignments: (left, left),
  left-content: [
    #strong[BS]
  ],
  right-content: [
    #strong[Xi'an Jiaotong University], Physics (#emph[Sept 2018 – July 2022])
  ],
)
#block(
  [
    #set par(spacing: 0pt)
    #v(design-highlights-top-margin);#highlights([Advisor: #link("https://gr.xjtu.edu.cn/web/minnluo")[Minnan Luo]],)
  ],
  inset: (
    left: design-entry-types-education-entry-degree-column-width + design-entries-horizontal-space-between-columns + design-entries-left-and-right-margin,
    right: design-entries-left-and-right-margin,
  ),
)



== Experience



#one-col-entry(
  content: [
    #strong[ByteDance Seed.], Top Seed intern on multimodal generation, led by #link("https://haoqifan.github.io/")[Haoqi Fan] -- #emph[Beijing, China] (#emph[July 2025 – present])

    #v(-design-text-leading)
    #v(design-highlights-top-margin);#highlights([#strong[Seedream 5.0]:

 

    - Designed the structured prompt \(SP\) annotation pipeline and verified the effectiveness of SP on DiT.

 

    - Trained the prompter rewriting user prompts into SPs, exploring reward models, RL recipes, self-distillation, and thinking patterns.

 

    - Built the editing SP data pipeline, mining supervision from video and extending structured prompts from generation to instruction-based editing.

],[#strong[Scaling Properties of Text Conditioning in Visual Generation] \[1\]:

 

    - Showed that scaling visual generation means scaling caption informativeness and the LLM that produces it, not the DiT alone.

 

    - Across 15 controlled runs with data, architecture, and compute fixed, converged diffusion loss tracks caption informativeness, not caption length.

 

    - Proposed the diffusability × promptability decomposition of the caption interface, separating what the diffuser can use from what an LLM can instantiate.

],[#strong[Open-sourced unified model and data engine]:

 

    - Co-led LightFusion \[3\], fusing off-the-shelf generation and understanding models via interleaved multimodal self-attention: 0.91 GenEval and 82.16 DPG-Bench on \~35B tokens.

 

    - Co-led VQ-VA World \[2\], an agentic pipeline crawling \~1.8M interleaved image-text samples plus the IntelligentBench benchmark, lifting LightFusion from 7.78 to 53.06.

],[#strong[Seed world model] \(ongoing\):

 

    - Continued training on top of Seedance 2.5.

 

    - Built the captioning workflow, annotating both event-level and global information.

 

    - Owned its prompt enhancement model, proposing an offline + online scheme that meets the world model's latency budget.

 

    - Designed the 4D structured prompt and reference-to-world interfaces, giving control through 3D bounding boxes, reference views, and object references.

],[#strong[Negative results]: tested a pretrained ViT as the VAE and a fully discrete unified model, among other alternatives to the continuous latent; none outperformed VAE-based latent diffusion in our settings.],)
  ],
)

#v(design-entries-vertical-space-between-entries)

#one-col-entry(
  content: [
    #strong[Shengshu Inc.], Research intern on video and 3D generation -- #emph[Beijing, China] (#emph[Nov 2023 – Mar 2025])

    #v(-design-text-leading)
    #v(design-highlights-top-margin);#highlights([Alleviating Janus problem in optimization-based 3D generation methods. \(CVPR 2024 \[6\]\)],[Finetune video diffusion model for 3D generation.],[Native 3D generation using limited 3D data. \(CVPR 2025 Highlight \[4\]\)],)
  ],
)



== Publications \(= Indicates Equal Contribution\)


#one-col-entry(content:[
  #strong[\[1\] Scaling Properties of Text Conditioning in Visual Generation] -- #emph[ByteDance Seed 2026]

  #v(-design-text-leading)
#v(design-highlights-top-margin);#strong[#underline[Zilong Chen]], Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan

#v(design-highlights-top-margin - design-text-leading)#link("https://heheyas.github.io/context-scaling/")[heheyas.github.io/context-scaling]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[2\] VQ-VA World: Towards High-Quality Visual Question-Visual Answering] -- #emph[CVPR 2026]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Chenhui Gou=, #strong[#underline[Zilong Chen]=], Zeyu Wang=, Feng Li, Deyao Zhu, Zicheng Duan, Kunchang Li, Chaorui Deng, Hongyi Yuan, Haoqi Fan, Cihang Xie, Jianfei Cai, Hamid Rezatofighi

#v(design-highlights-top-margin - design-text-leading)#link("https://chenhuigou.github.io/VQ-VA-World/")[chenhuigou.github.io/VQ-VA-World]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[3\] LightFusion: A Light-weighted, Double Fusion Framework for Unified Multimodal Understanding and Generation] -- #emph[ECCV 2026]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Zeyu Wang=, #strong[#underline[Zilong Chen]=], Chenhui Gou=, Feng Li, Chaorui Deng, Deyao Zhu, Kunchang Li, Weihao Yu, Haoqin Tu, Haoqi Fan, Cihang Xie

#v(design-highlights-top-margin - design-text-leading)#link("https://arxiv.org/abs/2510.22946")[arxiv.org/abs/2510.22946]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[4\] MeshGen: Generating PBR Textured Mesh with Render-Enhanced Auto-Encoder and Generative Data Augmentation] -- #emph[CVPR 2025 \(#strong[Highlight]\)]

  #v(-design-text-leading)
#v(design-highlights-top-margin);#strong[#underline[Zilong Chen]], Yikai Wang, Wenqiang Sun, Feng Wang, Yiwen Chen, Huaping Liu

#v(design-highlights-top-margin - design-text-leading)#link("https://heheyas.github.io/MeshGen")[heheyas.github.io/MeshGen]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[5\] V3D: Video Diffusion Models Are Effective 3D Generators] -- #emph[T-PAMI 2025]

  #v(-design-text-leading)
#v(design-highlights-top-margin);#strong[#underline[Zilong Chen]], Yikai Wang, Feng Wang, Zhengyi Wang, Huaping Liu

#v(design-highlights-top-margin - design-text-leading)#link("https://heheyas.github.io/V3D")[heheyas.github.io/V3D]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[6\] Text-to-3D Using Gaussian Splatting] -- #emph[CVPR 2024]

  #v(-design-text-leading)
#v(design-highlights-top-margin);#strong[#underline[Zilong Chen]], Feng Wang, Yikai Wang, Huaping Liu

#v(design-highlights-top-margin - design-text-leading)#link("https://gsgen3d.github.io/")[gsgen3d.github.io]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[7\] GaussianEditor: Swift and Controllable 3D Editing with Gaussian Splatting] -- #emph[CVPR 2024]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Yiwen Chen=, #strong[#underline[Zilong Chen]=], Chi Zhang, Feng Wang, Xiaofeng Yang, Yikai Wang, Zhongang Cai, Lei Yang, Huaping Liu, Guosheng Lin

#v(design-highlights-top-margin - design-text-leading)#link("https://buaacyw.github.io/gaussian-editor/")[buaacyw.github.io/gaussian-editor]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[8\] Masked Space-Time Hash Encoding for Efficient Dynamic Scene Reconstruction] -- #emph[NeurIPS 2023 \(#strong[Spotlight]\)]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Feng Wang=, #strong[#underline[Zilong Chen]=], Guokang Wang, Yafei Song, Huaping Liu

#v(design-highlights-top-margin - design-text-leading)#link("https://masked-spacetime-hashing.github.io/")[masked-spacetime-hashing.github.io]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[9\] Video4DGen: Enhancing Video and 4D Generation Through Mutual Optimization] -- #emph[T-PAMI 2025]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Yikai Wang, Guangce Liu, Xinzhou Wang, #strong[#underline[Zilong Chen]], Jiafang Li, Xin Liang, Fuchun Sun, Jun Zhu

#v(design-highlights-top-margin - design-text-leading)#link("https://vidu4d-dgs.github.io/")[vidu4d-dgs.github.io]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[10\] Vidu4D: Single Generated Video to High-Fidelity 4D Reconstruction with Dynamic Gaussian Surfels] -- #emph[NeurIPS 2024]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Yikai Wang, Xinzhou Wang, #strong[#underline[Zilong Chen]], Zhengyi Wang, Fuchun Sun, Jun Zhu

#v(design-highlights-top-margin - design-text-leading)#link("https://vidu4d-dgs.github.io/")[vidu4d-dgs.github.io]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[11\] MeshAnything V2: Artist-Created Mesh Generation with Adjacent Mesh Tokenization] -- #emph[arXiv 2024]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Yiwen Chen, Yikai Wang, Yihao Luo, Zhengyi Wang, #strong[#underline[Zilong Chen]], Jun Zhu, Chi Zhang, Guosheng Lin

#v(design-highlights-top-margin - design-text-leading)#link("https://buaacyw.github.io/meshanything-v2/")[buaacyw.github.io/meshanything-v2]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[12\] DimensionX: Create Any 3D and 4D Scenes from a Single Image with Controllable Video Diffusion] -- #emph[arXiv 2024]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Wenqiang Sun, Shuo Chen, Fangfu Liu, #strong[#underline[Zilong Chen]], Yueqi Duan, Jun Zhang, Yikai Wang

#v(design-highlights-top-margin - design-text-leading)#link("https://chenshuo20.github.io/DimensionX/")[chenshuo20.github.io/DimensionX]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[13\] FreePlane: Unlocking Free Lunch in Triplane-Based Sparse-View Reconstruction Models] -- #emph[arXiv 2024]

  #v(-design-text-leading)
#v(design-highlights-top-margin);Wenqiang Sun, Zhengyi Wang, Shuo Chen, Yikai Wang, #strong[#underline[Zilong Chen]], Jun Zhu, Jun Zhang

#v(design-highlights-top-margin - design-text-leading)#link("https://freeplane3d.github.io/")[freeplane3d.github.io]])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[14\] TwiBot-22: Towards Graph-Based Twitter Bot Detection] -- #emph[NeurIPS 2022]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Shangbin Feng=, Zhaoxuan Tan=, Herun Wan=, Ningnan Wang=, #strong[#underline[Zilong Chen]=], Binchi Zhang=, Qinghua Zheng, Wenqian Zhang, Zhenyu Lei, Shujie Yang, others])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[15\] Knowledge Graph Augmented Political Perspective Detection in News Media] -- #emph[arXiv 2021]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Shangbin Feng, #strong[#underline[Zilong Chen]], Qingyao Li, Minnan Luo])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[16\] Encoding Heterogeneous Social and Political Context for Entity Stance Prediction] -- #emph[arXiv 2021]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Shangbin Feng, #strong[#underline[Zilong Chen]], Peisheng Yu, Minnan Luo])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[17\] KCD: Knowledge Walks and Textual Cues Enhanced Political Perspective Detection in News Media] -- #emph[NAACL 2022 \(#strong[Oral]\)]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Wenqian Zhang=, Shangbin Feng=, #strong[#underline[Zilong Chen]=], Zhenyu Lei, Jundong Li, Minnan Luo])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[18\] BIC: Twitter Bot Detection with Text-Graph Interaction and Semantic Consistency] -- #emph[ACL 2023]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Zhenyu Lei, Herun Wan, Wenqian Zhang, Shangbin Feng, #strong[#underline[Zilong Chen]], Jundong Li, Qinghua Zheng, Minnan Luo])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[19\] KRACL: Contrastive Learning with Graph Context Modeling for Sparse Knowledge Graph Completion] -- #emph[WWW 2023]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Zhaoxuan Tan, #strong[#underline[Zilong Chen]], Shangbin Feng, Qingyue Zhang, Qinghua Zheng, Jundong Li, Minnan Luo])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[20\] KGAP: Knowledge Graph Augmented Political Perspective Detection in News Media] -- #emph[arXiv 2021]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Shangbin Feng, #strong[#underline[Zilong Chen]], Wenqian Zhang, Qingyao Li, Qinghua Zheng, Xiaojun Chang, Minnan Luo])

#v(design-entries-vertical-space-between-entries)
#one-col-entry(content:[
  #strong[\[21\] PAR: Political Actor Representation Learning with Social Context and Expert Knowledge] -- #emph[EMNLP 2022]

  #v(-design-text-leading)
  #v(design-highlights-top-margin);Shangbin Feng, Zhaoxuan Tan, #strong[#underline[Zilong Chen]], Ningnan Wang, Peisheng Yu, Qinghua Zheng, Xiaojun Chang, Minnan Luo])



== Awards



#one-col-entry(
  content: [
    #strong[Huiyan Scholarship \(Tsinghua University\)] (#emph[2024])

    
  ],
)

#v(design-entries-vertical-space-between-entries)

#one-col-entry(
  content: [
    #strong[Track winner, BMW hackathon] (#emph[2023])

    
  ],
)



== Technologies


#one-col-entry(
  content: [#strong[Languages:] C++, C, CUDA, Python]
)
#v(design-entries-vertical-space-between-entries)
#one-col-entry(
  content: [#strong[Software:] Blender]
)


