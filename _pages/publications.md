---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign n_first = 0 %}{% assign n_contrib = 0 %}{% assign n_cites = 0 %}
{%- for p in site.data.publications -%}
  {%- unless p.conference -%}
    {%- if p.first_author -%}{%- assign n_first = n_first | plus: 1 -%}
    {%- else -%}{%- assign n_contrib = n_contrib | plus: 1 -%}{%- endif -%}
  {%- endunless -%}
{%- endfor -%}
{%- comment -%} total from the same per-year data as the chart, so the two agree {%- endcomment -%}
{%- for y in site.data.citations -%}{%- assign n_cites = n_cites | plus: y.citations -%}{%- endfor %}
I'm first author on {{ n_first }} papers and a contributing author on {{ n_contrib }}{% if n_cites > 0 %}, with {{ n_cites }} citations in total{% endif %}. This list is generated from my [ADS library](https://ui.adsabs.harvard.edu/user/libraries/8zUtfV-GT9KVqGIFMyOYVw); papers are also listed on [arXiv](https://arxiv.org/search/astro-ph?searchtype=author&query=Laroche%2C+A).

{% include citations_chart.html %}

## First-author

<ol class="pub-list">
{% for p in site.data.publications %}{% if p.first_author and p.conference != true %}
  {% include publication.html pub=p %}
{% endif %}{% endfor %}
</ol>

## Contributing author

<ol class="pub-list">
{% for p in site.data.publications %}{% unless p.first_author or p.conference %}
  {% include publication.html pub=p %}
{% endunless %}{% endfor %}
</ol>

## Conference proceedings

<ol class="pub-list">
{% for p in site.data.publications %}{% if p.conference %}
  {% include publication.html pub=p %}
{% endif %}{% endfor %}
</ol>
