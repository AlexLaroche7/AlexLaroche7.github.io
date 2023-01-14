---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% include base_path %}

**My research is focused on developing interpretable, generative models for stellar spectra.** Careful analysis of the decomposition of light from a star into its constituent wavelengths can inform us about its properties (aka stellar labels), such as temperature, surface gravity and metallicity. In the past, these analyses have largely been undertaken with computationally expensive stellar evolution models and time intensive high-resolution spectroscopy, i.e. a model-driven approach. With the increasingly gigantic datasets from large scale surveys, commonly termed the era of big data, astronomers have recently begun to implement data-driven approaches with the help of machine learning (ML) techniques. These ML techniques can be broadly classified into (i) predictive learning; training a model to _predict_ stellar labels from stellar spectra and (ii) generative learning; training a model to _generate_ spectra from labels.

The main advantage of generative learning over predictive learning is the interpretability of the model. It is possible to interpret what a generative model is doing 'under the hood,' which in turn can aid us in discovering new astrophysics without computer models. Generative learning models for stellar specta have thus far been focused on higher resolution spectroscopic surveys, such as [APOGEE](https://arxiv.org/abs/1501.07604), whose spectra are very detailed. In contrast, low-resolution spectra sacrifice detail but typically have far larger datasets as opposed to their high-resolution counterparts. The new [_Gaia_ DR3](https://arxiv.org/abs/2012.01533) includes 220+ million low-resolution BP/RP spectra, which presents an incredibly exciting opportunity to extend the successes of generative learning to extremly low-resolutions. I am currently working on developing one of the first generative models for BP/RP spectra, which will be soon applied to an unprecented number of stars, giving us an unparalleled chemical picture of our Galaxy. Morevoer, my modeling efforts will be applicable to future low-resolution surveys, such as [SPHEREx](https://spherex.caltech.edu/), and informative for future large scale surveys such as [Vera Rubin](https://www.lsst.org/). 

# Undergraduate Research

**My undergraduate research primarily involved using a combination of simulations and statistics to investigate the nature of dark matter and Cosmic Dawn (the 'teenage' years of our Universe).** Specifically, I was involved in projects working on dark matter constraints via strong gravitational lensing and 21cm cosmology, both theory and experiment. These projects are summarized below:

## Dark matter and strong gravitational lensing
----

Four decades after Vera Rubin discovered overwhelming evidence for the existence of dark matter, astrophysicists are still grappling with the question: what is dark matter made of? This is especially concerning since dark matter is thought to be five times more abundant than ordinary matter! While cold dark matter (CDM) can explain observations of large-scale structure in our Universe, small-scale challenges to CDM have motivated a variety of alternative dark matter theories.

In recent years, strong gravitational lensing has emerged as an effective tool for constraining dark matter models. When the light from a distant quasar is lensed by an intervening galaxy, the original image of the quasar can sometimes be split into four lensed images. Hence, we often refer to these systems as 'quadruply-imaged quasars'. The relative brightnesses of these quad images (flux ratios) are extremely sensitive to the dark matter content in the lensing galaxy. This is particularly useful since many alternative dark matter models only deviate from cold dark matter (CDM) on sub-galactic scales.

### Constraining ultra-light dark matter with quadruply-imaged quasars
----
Ultra-light dark matter (ULDM) is a dark matter canditate made of ultra-light bosons, such as axions, in which particles have a mass $m<10^{-20}$ eV. These particles are so light that quantum mechanical effects can manifest on galactic scales. The kpc-scale de Broglie wavelength of ULDM particles creates wave-like density fluctuations in the density profiles of ULDM halos. Under the supervision of [Daniel Gilman](https://www.astro.utoronto.ca/~gilman/) and [Jo Bovy](https://astro.utoronto.ca/~bovy/), I developed the first strong lensing ULDM model to account for these fluctuations. In our paper [_Quantum fluctuations masquerade as halos: Bounds on ultra-light dark matter from quadruply-imaged quasars_](https://arxiv.org/abs/2206.11269), we demonstrated that fluctuations in ULDM can significantly impact image flux ratios, and present lower bounds on the ultra-light boson mass.

<center>
  <figure style="width:800px">
	  <img src="/images/uldm_sims.png" alt="ULDM simulations">
	  <figcaption>2-D simulations of ultra-light dark matter halo substructure for different ultra-light boson masses. Credit: <a href="https://ui.adsabs.harvard.edu/abs/2022arXiv220611269L/abstract">Laroche et al. (2022)</a>.</figcaption>
      </figure>
        </center>

## 21cm cosmology
----
Observations of the redshifted 21cm line have the potential to revolutionize our understanding of the early Universe. When a neutral hydrogen atom undergoes a spin-flip transiton, it emits a photon with a wavelength of roughly 21cm. The 21cm signal can therefore be used to map out the ionization history of the Universe. 21cm cosmologists are primarily interested in measuring (i) 21cm intensity maps; the 21cm photon distribution as a function of space and time, and (ii) the 21cm global signal; an all-sky measurement of the 21cm line. 

### Constraining density-ionization correlations during the Epoch of Reionization
----
I completed my undergraduate thesis, titled "Quantifying Density-Ionization Correlations with the 21cm Power Spectrum While Including X-ray Heating Effects," under the supervision of [Adrian Liu](http://www.physics.mcgill.ca/~acliu/). My thesis investigated the Epoch of Reionization (EoR); a period in the Universe's history when neutral hydrogen was systematically ionized. Reionization did not occur uniformly throughout Universe. Rather, small ionized bubbles formed and grew to eventually ionize the entire intergalactic medium. The relationship between these ionized bubbles (the ionization field) and the matter density field during the EoR can be understood with 21cm intensity mapping, but has yet to be constrained by experiments. My thesis showed that upcoming measurements of the 21cm power spectrum with the [Hydrogen Epoch of Reionization Array (HERA)](https://reionization.org/) will be able to constrain density-ionization correlations, while incorporating X-ray heating effects.

<center>
  <figure style="width:800px">
	  <img src="/images/eor_sims.png" alt="ULDM simulations">
	  <figcaption>Simulations of the ionization, matter density, spin temperature and 21cm brightness temperature fields during the EoR, for two different density-ionization correlations (top: correlated, bottom: anti-correlated). Credit: Laroche & Banghal (2021).</figcaption>
      </figure>
        </center>

### Measuring the global 21cm signal with PRIZM
----
While working as a research assistant in the McGill Radio Lab, under the supervision of [Jonathan Sievers](https://www.physics.mcgill.ca/~sievers/), I performed data selection and analysis for the [Probing Radio Intensity at high-Z from Marion (PRIZM)](https://arxiv.org/abs/1806.09531) experiment. PRIZM is a global 21cm telescope which seeks to measure the global 21cm signal during Cosmic Dawn, a loosely defined period in the Universe's history (including the EoR) when the first stars formed and 'lit up' our previously dark Universe. Clean measurements of global 21cm signal are _very_ hard to achieve. For instance, experiments must contend with radio frequency interference (RFI) and galactic foregrounds. My work involed writing code to efficiently process both on-sky spectra and antenna data.
