---
layout: single
title: "All About Chris"
excerpt: "Homepage"
author_profile: true
permalink: /
twitter: true
---

Chris's research focuses on the development of computational multiscale models to
investigate emergent system behaviors in biology.
Using his training in both biochemistry and computer science, he develops and applies new algorithms and
softwares to model and study the complexity of life.
He is currently studying phenomena such as the regulation of synaptic plasticity and learning in dendritic spines.

<h1>Latest Posts</h1>
{% assign sorted = site.posts | sort:'date' | reverse %}
<ul>
{% for post in sorted limit:3%}
	<div class="{{ include.type | default: "list" }}__item">
	  <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
	    <li>
	      <h3 class="archive__item-title" itemprop="headline">
			 	  <a href="{{ root_url }}{{ post.url }}">{{ post.title }}</a>
	      </h3>
        <p class="archive__item-excerpt" itemprop="description">{{post.excerpt}}</p>
	    </li>
	 </article>
	</div>
{% endfor %}
<ul>
<a href="/blog/" class="back-to-top">More posts &rarr;</a>

