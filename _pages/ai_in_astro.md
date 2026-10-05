---
layout: archive
title: "On AI in astronomy"
permalink: /misc/ai-in-astro/
author_profile: true
---

*Written on October 5, 2026.*

I'm still forming my thoughts on this, so I thought writing them down could help. First, to be clear, I'm not against AI in astronomy. My own research uses machine learning and takes advantage of these tools. At this point, I use them every day. However, I have become increasingly concerned about generative AI making papers and proposals much faster to pump out, but no faster to read, review or verify. It is not clear to me that this "more is more" approach is a good thing for astronomy, to put it mildly. Faster analysis and writing facilitates the ability to chunkify research into least publishable units (LPUs), which could subject the field to an increasing barrage of papers that contribute little, but still take time to read, referee and cite. After all, there is only so much time in a day. Before I go on, I will give the caveat that I am speculating. I have not yet seen strong, quantitative evidence for severe AI slopification in astronomy.

## The literature

This looming problem only hit me very recently when arXiv [released its latest submission statistics](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/). In Sept. 2026, arXiv received a record ~40,000 submissions, 2x the ~20,000 in Sept. 2024 and 4x the ~10,000 in September 2016. Most notably, submissions to cs.AI have increased by a staggering 6x in just 2 years. arXiv's volunteer moderators describe a rise in ["thin papers of narrow scope"](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) (aka LPUs) and dense, AI-written papers (LPUs with extra fluff).

arXiv has begun to fight back. In Oct. 2025, arXiv stopped accepting computer science (CS) [review articles and position papers](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/) unless they had already passed peer review, noting that generative AI makes papers which are ["not introducing new research results"](https://blog.arxiv.org/2025/10/31/attention-authors-updated-practice-for-review-articles-and-position-papers-in-arxiv-cs-category/) fast and easy to write. In Oct. 2026, arXiv [limited every submitter](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/) to 2 submissions per month, which arXiv termed ["a stopgap while we determine what may be the new best practice"](https://blog.arxiv.org/2026/10/01/updated-rate-limit-policy/).

I do not see a reason why astronomy is immune to following in the footsteps of CS, but arXiv's own numbers do not necessarily suggest this is happening (yet). Comparing Jan.-Sept. per year, astrophysics submissions grew by 1.1x from 2022 to 2024, then by 1.3x from 2024 to 2026, or ~1.5x over four years. Over the same four years CS submissions grew by ~2.8x, and in some months of 2026 cs.AI alone received more submissions than all of astrophysics. Still, if the number of astro papers begins to grow at similar rates, I fear that it will become increasingly impossible to keep up.

<figure class="essay-fig essay-fig--dark">
<img src="/images/misc/arxiv_submissions.png" alt="Left: all arXiv submissions per month from 1991 to September 2026, rising steeply to about 40,000 in September 2026. Right: monthly submissions since 2022 for computer science, cs.AI and astrophysics, with computer science rising from about 4,000 to 18,000 per month and cs.AI overtaking astrophysics in 2026.">
<figcaption>Left: all arXiv submissions per month since 1991. Right: monthly submissions by category since 2022. Data from arXiv's <a href="https://arxiv.org/stats/monthly_submissions">monthly submission</a> and <a href="https://info.arxiv.org/about/reports/submission_category_by_year.html">category</a> statistics.</figcaption>
</figure>

## Peer review

Peer review depends on a finite number of scientists volunteering their time. More submissions means more reviews requested from the same people. A paper written in an afternoon can still take a referee days to review. If this imbalance grows, I worry that the quality of peer review will plummet for all papers, not just the heavily AI-aided ones. In the long run, I am not sure that peer review as we know it can survive. It will be interesting to see if astro journals begin to implement arXiv-esque limits.

## Proposals

Observers could soon be facing the same problem, if this hasn't occurred already. For context, JWST Cycle 5 received a [record ~2,900 proposals](https://www.stsci.edu/contents/newsletters/2026-volume-43-issue-01/jwst-cycle-5-proposal-selection) for ~8,000 hours of time, an oversubscription of roughly 12:1. STScI now requires proposers to [declare generative AI use](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-call-for-proposals-for-cycle-6/jwst-key-policies), will [disqualify proposals with hallucinated references](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-call-for-proposals-for-cycle-6/jwst-key-policies), and, in its [guidance on generative AI](https://www.stsci.edu/contents/newsletters/2026-volume-43-issue-01/jwst-cycle-5-proposal-selection), reminds proposers that (nearly) identical proposals are prohibited. STScI has looked into whether AI is driving oversubscription. As of May 2026, STScI [did not find any evidence that AI is the culprit](https://www.stsci.edu/files/live/sites/www/files/home/jwst/science-planning/user-committees/jwst-users-committee/_documents/jstuc-0526-cycle6-plans-peebles.pdf).

JWST Cycle 6 proposals were due on Sept. 30, 2026, until the APT server [crashed](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-call-for-proposals-for-cycle-6) 15 min before the deadline. As a result, STScI extended the deadline to Oct. 1. Cycle 6 is another record year for proposal submissions. STScI has not released official Cycle 6 numbers yet, but tracking proposal numbers as they were assigned in the final days before each deadline shows Cycle 6 reaching [~3,500 proposals shortly before the deadline](https://www.linkedin.com/posts/ian-crossfield-430ab4134_another-record-year-for-jwst-proposals-share-7511389802789773312--SYB/). It is worth noting that this number is incomplete relative to the ~2,900 total proposals for Cycle 5 since counts were halted before the crash. I wonder what the final Cycle 6 number will be...

<figure class="essay-fig">
<img src="/images/misc/jwst_proposals_by_cycle.png" alt="Two panels against days until the JWST proposal deadline for Cycles 1 to 6. Top: cumulative proposal number, with Cycle 6 reaching roughly 3,500 compared with about 2,900 for Cycle 5. Bottom: new submissions per minute, rising to a few per minute in the final hour.">
<figcaption>JWST proposal numbers as a function of time before the deadline, Cycles 1 to 6 (top), and the submission rate (bottom). Figure by <a href="https://crossfield.ku.edu/">Ian Crossfield</a>, from his <a href="https://www.linkedin.com/posts/ian-crossfield-430ab4134_another-record-year-for-jwst-proposals-share-7511389802789773312--SYB/">LinkedIn post</a>.</figcaption>
</figure>

The capacity of Telescope Allocation Committees (TACs) doesn't grow with the number of proposals. More proposals means more work for the TACs and simply a lower success rate. It seems obvious to me that a proposal that was easier to write is not necessarily one more worthy of observing. STScI [notes](https://www.stsci.edu/contents/newsletters/2026-volume-43-issue-01/jwst-cycle-5-proposal-selection) that, anecdotally, the PIs who submitted the most Cycle 5 proposals did not have a single one accepted. Every one of those proposals still had to be read, graded and discussed by reviewers, which is exactly the kind of burden I worry about. Still, I await STScI's analysis to determine if any evidence for AI-induced oversubscription is found.

## Where AI can help

All that aside, there are real benefits. AI models can help us work with datasets that are too large to inspect by hand, such as the ~220 million Gaia XP spectra. Building models for this kind of big data is a component of [my research](/research/). It should also be fairly obvious at this point that AI tools are particularly efficient at some of the tedious aspects of research, such as writing and debugging code, and data formatting. I used Claude to help build this website, and boy did it help. Still, I endeavour to [trust, but verify](https://en.wikipedia.org/wiki/Trust,_but_verify).

## Where I'm at (for now)

The distinction I keep coming back to is between using AI to accomplish novel, interesting work, perhaps at a faster pace, and simply using it to produce more output, for output's sake. The first could make research better. The second places an unfair burden on readers, referees and review panels, which are scarcer resources than GPUs. Additionally, how can young astronomers find meaning in an already competitive environment which AI could increasingly negatively reinforce?

A lot of the AI discussion I have come across jumps straight to productivity-maxxing and letting them cook[^cook], before asking whether it is in our best interest to, and even more fundamentally whether we should. Perhaps I am holding on to a dated, romantic perspective that the purpose of research is the process: the work contains the meaning, and the resulting paper is the proverbial cherry on top. I expect my views to change as the tools and community's norms evolve.

[^cook]: "Let them cook" is borrowed from David Hogg's white paper ["Why do we do astrophysics?"](https://arxiv.org/abs/2602.10181). I highly recommend reading it, since he addresses these questions much more thoroughly than I.
