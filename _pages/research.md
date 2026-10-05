---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

I am primarily interested in binary interaction: how the exchange of mass, energy and angular momentum between two stars changes their evolution and final fates. My work combines targeted observations of small samples of binary interaction products with data-driven methods applied to large-scale surveys. A full list of papers can be found on my [publications](/publications/) page.

<figure class="wordcloud">
<img src="/images/research/wordcloud.png" alt="Word cloud of terms from the titles and abstracts of my papers">
<figcaption>Buzzwords from my papers.</figcaption>
</figure>

<div class="project">
<img class="project__img" src="/images/research/he_star_orbits.png" alt="Phase-folded radial velocity curves for five helium stars in binaries">
<div class="project__text" markdown="1">
### Intermediate-mass helium stars in the Magellanic Clouds

[Drout et al. (2023)](https://www.science.org/doi/10.1126/science.ade4970) and [Götberg et al. (2023)](https://ui.adsabs.harvard.edu/abs/2023ApJ...959..125G/abstract) discovered a population of hot, helium-rich stars with masses from 2 to 8 M<sub>⊙</sub> in the Magellanic Clouds, which are thought to have lost their hydrogen envelopes via interaction with a binary companion. Using multi-epoch Magellan/MagE spectroscopy, I measured radial velocities for eight of these helium stars. Five are in binaries with orbital periods from 16 hours to 300 days and companions that are invisible in the optical spectra, while three show no binary motion. Based on their orbits, the optically dark companions could be low-mass stars near the main sequence, low-mass stripped stars, or compact objects. The binaries are hydrogen-poor and the apparently-single stars are nearly hydrogen-free, which suggests that the two groups formed through different evolutionary pathways. I also contributed to the [Stripped-Star Ultraviolet Magellanic Cloud Survey](https://ui.adsabs.harvard.edu/abs/2026ApJ...999...73L/abstract) (SUMS) led by Bethany Ludwig, which identified hundreds of stripped star candidates from their UV excess.

**Laroche** et al. (2026), [arXiv:2609.30384](https://arxiv.org/abs/2609.30384); Ludwig, Drout, Götberg, Lang & **Laroche** (2026), [ApJ 999, 73](https://ui.adsabs.harvard.edu/abs/2026ApJ...999...73L/abstract)
</div>
</div>

<div class="project">
<img class="project__img" src="/images/research/xp_svae.png" alt="Architecture of the scatter variational auto-encoder: an encoder maps an XP spectrum to a latent space, from which one decoder reconstructs the spectrum and another estimates its scatter">
<div class="project__text" markdown="1">
### Data-driven models for Gaia XP spectra

Data-driven models of stellar spectra are often trained to map stellar labels to spectra, which means their performance can be limited by the stellar label systematics. With Josh Speagle, I developed a variational auto-encoder that learns to generate Gaia BP/RP (XP) spectra and their intrinsic scatter without relying on stellar labels. The model reconstructs XP spectra as well as label-dependent models. When applied to giant stars with APOGEE abundances it recovers the [α/M] bimodality, robustly showing that XP spectra contain [α/M] information. Because the model needs only spectra to train, it can be applied to any and all of the ~220 million stars with XP spectra in Gaia DR3, and to the new XP spectra coming in [Gaia DR4](https://www.cosmos.esa.int/web/gaia/release) (Dec. 2026!). I have also applied a similar autoencoder framework to identify unresolved binaries in photometric surveys with Tobias Géron, beginning with Rubin observations of 47 Tucanae.

**Laroche** & Speagle (2025), [ApJ 979, 5](https://ui.adsabs.harvard.edu/abs/2025ApJ...979....5L/abstract); **Laroche** & Speagle (2023), [ICML ML4Astro workshop](https://arxiv.org/abs/2307.06378); Géron, **Laroche** et al. (2026), [arXiv:2609.05616](https://arxiv.org/abs/2609.05616)
</div>
</div>

<div class="project">
<img class="project__img" src="/images/research/uldm.jpg" alt="Simulated ultra-light dark matter halo density">
<div class="project__text" markdown="1">
### Ultra-light dark matter and strong lensing

With Jo Bovy and Daniel Gilman, I used the flux ratios of eleven quadruply-imaged quasars to constrain ultra-light dark matter (ULDM), including the wave-interference fluctuations ULDM should produce in the host halo density profile, calibrated against simulations. These quantum fluctuations can masquerade as dark matter halos, perturbing the flux ratios in much the same way, and including them substantially changes the inferred particle mass. Even so, the data disfavor particle masses below 10<sup>−21.5</sup> eV.

**Laroche** et al. (2022), [MNRAS 517, 1867](https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.1867L/abstract)
</div>
</div>

## Talks

<div class="video">
<iframe src="https://www.youtube-nocookie.com/embed/B0eRddAMYsk" title="Radial velocity survey of stars stripped in binaries in the Magellanic Clouds (TASTY talk, University of Toronto)" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

*Radial velocity survey of stars stripped in binaries in the Magellanic Clouds*, TASTY talk, Department of Astronomy & Astrophysics, University of Toronto.
