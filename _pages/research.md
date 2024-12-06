---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

## Data-driven, generative models for low-resolution spectra
----
![image](/images/xp_gif.gif){: style="float: left; margin-right: 1em;"}

Data-driven models for stellar spectra which depend on stellar labels suffer from label systematics which decrease model performance: the “stellar labels gap”. To close the stellar labels gap, we present a stellar label independent model for *Gaia* BP/RP spectra. We develop a novel implementation of a variational auto-encoder, which learns to generate an XP spectrum and accompanying ‘scatter’ without relying on stellar labels. We demonstrate that our model achieves competitive XP spectra reconstructions in comparison to stellar label dependent models. We find that our model learns stellar properties directly from the data itself. We then apply our model to XP/APOGEE giant stars to study the [$\alpha$/M] information in *Gaia* XP. We provide strong evidence that the XP spectra contain meaningful [$\alpha$/M] information by demonstrating that our model learns the $\alpha$-bimodality, without relying on stellar label correlations for stars with $T_{\rm eff} <$ 5000 K, while also being sensitive to the anomalous abundances of *Gaia*-Enceladus stars. We publicly release our trained model, codebase and data. Importantly, our stellar label independent model can be implemented for any/all XP spectra because our model performance scales with training object density, not training label density. *[Image credit: ESA/Gaia/DPAC, Creevey et al. 2022, Rene Andrea]*

Read **Laroche** & Speagle (2024) [here](https://ui.adsabs.harvard.edu/abs/2024arXiv240407316L/abstract).

----
## Data-driven modeling of carbon-enhanced metal poor stars

Under construction.

----
## Binary-stripped helium stars

Under construction.

----

# Undergraduate Research

## Constraining ultra-light dark matter with quadruply-imaged quasars
----
![image](/images/uldm_sims.png){: style="float: left; margin-right: 1em; width: 600px"}

Ultra-light dark matter (ULDM) refers to a class of theories, including ultra-light axions, in which particles with mass $m_{\psi} < 10^{-20}\, \rm{eV}$ comprise a significant fraction of the dark matter. A galactic scale de Broglie wavelength distinguishes these theories from cold dark matter (CDM), suppressing the overall abundance of structure on sub-galactic scales, and producing wave-like interference phenomena in the density profiles of halos. With the aim of constraining the particle mass, we analyze the flux ratios in a sample of eleven quadruple-image strong gravitational lenses. We account for the suppression of the halo mass function and concentration-mass relation predicted by ULDM theories, and the wave-like fluctuations in the host halo density profile, calibrating the model for the wave interference against numerical simulations of galactic-scale halos. We show that the granular structure of halo density profiles, in particular, the amplitude of the fluctuations, significantly impacts image flux ratios, and therefore inferences on the particle mass derived from these data. We infer relative likelihoods of CDM to ULDM of 8:1, 7:1, 6:1, and 4:1 for particle masses $\log_{10}(m_\psi/\rm{eV})\in[-22.5,-22.25], [-22.25,-22.0],[-22.0,-21.75], [-21.75,-21.5]$, respectively. Repeating the analysis and omitting fluctuations associated with the wave interference effects, we obtain relative likelihoods of CDM to ULDM with a particle mass in the same ranges of 98:1, 48:1, 26:1 and 18:1, highlighting the significant perturbation to image flux ratios associated with the fluctuations. Nevertheless, our results disfavor the lightest particle masses with $m_{\psi} < 10^{-21.5}\,\rm{eV}$, adding to mounting pressure on ultra-light axions as a viable dark matter candidate.

Read **Laroche** et al. (2023) [here](https://ui.adsabs.harvard.edu/abs/2022MNRAS.517.1867L/abstract).

----
## Quantifying density-ionization correlations with the 21cm power spectrum while including X-ray heating effects
----
![image](/images/eor_sims.png){: style="float: left; margin-right: 1em; width: 600px"}

Observations of the redshifted 21cm line will soon allow us to probe the physics of the early Universe at unprecedented scales.
In particular, the 21cm signal will tell us about the physics of the Epoch of Reionization (EoR), during which time the first
stars systemically ionized the intergalactic medium. Most models predict a tight correlation between the ionization and density
fields during the EoR, upon which the 21cm signal is highly dependent. We extend a parametrization for the density-ionization
correlations by including X-ray heating effects, which also significantly influence the 21cm signal. We develop forecasts for
the ability of observations to constrain these correlations while accounting for X-ray sources. We find that measurements on
the dimensionless power spectrum at redshifts $7.5 \leq z \leq 8.5$ and $13 \leq z \leq 14$ with error bars on the order of $\sim10$ mK$^2$
about our fiducial model can place strong constraints on density-ionization correlations, while accounting for X-ray heating
effects. This demonstrates that the Epoch of Heating (EoH) can also constrain density-ionization correlations. We find that the
Hydrogen Epoch of Reionization Array (HERA) will be able to significantly constrain density-ionization correlations and several
astrophysical parameters related to X-ray heating.

## Measuring the global 21cm signal
----
![image](/images/prizm.jpeg){: style="float: left; margin-right: 1em; width: 500px"}

While working as a research assistant in the McGill Radio Lab, under the supervision of [Jonathan Sievers](https://www.physics.mcgill.ca/~sievers/), I performed data selection and analysis for the [Probing Radio Intensity at high-Z from Marion (PRIZM)](https://arxiv.org/abs/1806.09531) experiment. PRIZM is a global 21cm telescope which seeks to measure the global 21cm signal during Cosmic Dawn, a loosely defined period in the Universe's history (including the EoR) when the first stars formed and 'lit up' our previously dark Universe. Clean measurements of global 21cm signal are _very_ hard to achieve. For instance, experiments must contend with radio frequency interference (RFI) and galactic foregrounds. My work involed writing code to efficiently process both on-sky spectra and antenna data. *[Image credit: AstroMcGill, Cynthia Chiang]*

----