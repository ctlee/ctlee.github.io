---
title: "News and Updates"
permalink: /news/
layout: archive
author_profile: true
classes: wide
---

<ul style="list-style: none;">
	{% assign sorted = site.news | sort:'date' | reverse %}
	{% for post in sorted %}
		<div class="{{ include.type | default: "list" }}__item">
		  <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
		    <li>
		      <h3 class="archive__item-title" itemprop="headline">
		          {{ post.date | date: "%B %d, %Y"}} | {{ post.title }}
		      </h3>
		      {% if post.excerpt %}
		        <p class="archive__item-excerpt" itemprop="description">{{ post.excerpt }}</p> 
		      {% endif %}
		    </li>
		 </article>
		</div>
	{% endfor %}
</ul>