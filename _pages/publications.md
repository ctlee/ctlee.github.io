---
title: "Publications"
layout: archive
permalink: /publications/
author_profile: true
classes: wide
---

<p><sup>&dagger;</sup> denotes joint authorship. <sup>$</sup> denotes corresponding author.
{% if site.author.googlescholar %}
  You can also find a more updated list on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}
</p>
[Sorted by year]({{ base_path }}by-year/){: .btn .btn--inverse .btn--small}


<h2>Submitted and In Preparation</h2>
<ul>
	{% for post in site.inpreps reversed %}
	  {% include inprep-pub-item.html %}
	{% endfor %}
</ul>

<h2>Peer Reviewed and In Press</h2>
<ol>
	{% assign sorted = site.publications | sort:'date' | reverse %}
	{% for post in sorted %}
	  {% include num-pub.html %}
	{% endfor %}
</ol>