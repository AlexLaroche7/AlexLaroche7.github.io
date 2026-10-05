---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

This list is generated from my [ADS library](https://ui.adsabs.harvard.edu/user/libraries/8zUtfV-GT9KVqGIFMyOYVw); papers are also listed on [arXiv](https://arxiv.org/search/astro-ph?searchtype=author&query=Laroche%2C+A).

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
