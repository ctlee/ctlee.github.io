---
layout: single
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
classes: wide
---

[PDF Version](/files/CTL_CV.pdf){: .btn .btn--inverse .btn--small}

<h2>Education</h2>
* **2013-2019**: Ph.D. Computational Chemistry \| _University of California, San Diego_
* **2011-2013**: M.S. Biochemistry \| _University of Virginia_
* **2007-2011**: B.S. Chemistry & B.A. Computer Science \| _University of Virginia_

<h2>Work Experience</h2>
* **2019-ongoing**: Hartwell Foundation Postdoctoral Fellow
  * Padmini Rangamani and Michael J. Holst Labs
* **2013-2019**: Graduate Research Associate
  * Rommie E. Amaro and J. Andrew McCammon Labs
  * Developed workflows to enable spatially resolved cellular and
    subcellular simulations of signaling cascades using real
    geometries from electron microscopy.
* **2011-2013**: Graduate Research Associate
  * Linda Columbus and Cameron Mura Labs
  * Experimentally characterized the biological function of a zinc
    dependent glycerol dehydrogenase from <i>Thermotoga maritima</i>
    using a variety of bespoke experimental assays.
* **2010-2011**: Undergraduate Research Associate
  * Michael Shirts Lab
  * Created the initial prototype of InterMol a molecular simulation structure,
  	topology, and parameter conversion software.

<h2>Fellowships and Competitive Funding</h2>
* **2019-2021**     Hartwell Foundation Postdoctoral Fellowship
* **2019**          Schmidt Science Fellows Finalist
* **Spring 2018**   UCSD Chem/Biochem Distinguished Graduate Fellowship
* **2017-18**       San Diego Diversity Fellowship
* **2017**          Biophysical Society Travel Award
* **2017**          Simula Computational Physiology Scholarship
* **2017**          NSF I-Corps, UCSD ($1k) Role: Co-PI
* **2014-16**       Fellow, UCSD Molecular Biophysics Training Program
* **2012**          UCSD SHORE Award
* **Summer 2011**   NBCR Summer Institute Travel Award
* **2011**          Mead Scholar, UVA Computational Biology

<h2>Honors & Awards</h2>
* **2017**  ACS CINF Scholarship for Scientific Excellence
* **2017**  Bruno Zimm Award
* **2017**  Carol & George Lattimer Award
* **2015**  MBTG Annual Retreat Best Poster, UCSD
* **2014**  Teaching Assistant Excellence Award, UCSD

<h2><a href="/publications/">Publications</a></h2>
<h3>In Preparation and Submitted</h3>
  <ul>{% for post in site.inpreps %}
    {% include cv-pub.html %}
  {% endfor %}</ul>

<h3>Peer Reviewed</h3>
{% assign sorted = site.publications | sort:'date' | reverse %}
  <ol>{% for post in sorted %}
    {% include cv-pub.html %}
  {% endfor %}</ol>

<h2>Service and Leadership</h2>
* Mentor for Amaro Lab Summer outreach program, BioChemCoRE.
  * Worked with over 30 undergraduate and high school students

<h2>Talks and Conference Contributions</h2>
  {% assign sorted = site.talks | sort:'date' | reverse %}
  <ul class="archive__list">{% for post in sorted%}
    {% include talk-list.html %}
  {% endfor %}</ul>

<h2>Teaching</h2>
  <ul class="archive__list">{% for post in site.teaching reversed %}
    {% include teaching-list.html %}
  {% endfor %}</ul>
