---
layout: default
title: Archive
permalink: /archive/
---

# Post Archive

Here you can find all our blog posts organized chronologically.

<div class="archive">
  {% for post in site.posts %}
    {% assign currentYear = post.date | date: "%Y" %}
    {% assign previousYear = post.previous.date | date: "%Y" %}
    
    {% if currentYear != previousYear %}
      <h2>{{ currentYear }}</h2>
    {% endif %}
    
    <div class="archive-item">
      <span class="archive-date">{{ post.date | date: "%b %-d" }}</span>
      <a href="{{ post.url | relative_url }}" class="archive-link">{{ post.title }}</a>
      {% if post.categories.size > 0 %}
        <span class="archive-categories">
          {% for category in post.categories %}
            <span class="category">{{ category }}</span>
          {% endfor %}
        </span>
      {% endif %}
    </div>
  {% endfor %}
</div>

{% if site.posts.size == 0 %}
  <p>No posts yet, but stay tuned!</p>
{% endif %}

<style>
.archive {
  margin-top: 20px;
}

.archive h2 {
  border-bottom: 2px solid #e8e8e8;
  padding-bottom: 5px;
  margin-top: 30px;
  margin-bottom: 20px;
}

.archive-item {
  margin-bottom: 10px;
  padding: 8px 0;
  border-bottom: 1px solid #f0f0f0;
}

.archive-date {
  display: inline-block;
  width: 60px;
  font-size: 14px;
  color: #828282;
  font-weight: 500;
}

.archive-link {
  color: #2a7ae4;
  text-decoration: none;
  font-weight: 500;
}

.archive-link:hover {
  text-decoration: underline;
}

.archive-categories {
  margin-left: 10px;
}

.category {
  background-color: #f0f0f0;
  color: #555;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 12px;
  margin-right: 4px;
}
</style>