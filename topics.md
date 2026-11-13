---
layout: page
title: 주제별 글 모음
description: "부천 화접몽한의원 박서연 한의사가 답하는 편평사마귀, 모공각화증, 지루성피부염·모낭염, 건선, 여드름·여드름흉터 질문과 답변을 주제별로 모았습니다."
permalink: /topics/
---

부천 화접몽한의원 박서연 한의사가 진료실에서 자주 받는 피부 질문에 답한 글을 주제별로 모았습니다.

{% assign topics = "편평사마귀|flat-wart,모공각화증|keratosis,지루성피부염·모낭염|seborrheic;folliculitis,건선|psoriasis,여드름·여드름흉터|teen-acne;acne-scar,아토피·습진·한포진|atopy;eczema;dyshidrotic,원형탈모|alopecia,손발 사마귀|warts-hands-feet,등·가슴 피부|chest-back" | split: "," %}
{% for t in topics %}
{% assign parts = t | split: "|" %}
{% assign keys = parts[1] | split: ";" %}
## {{ parts[0] }}

<ul>
{% for post in site.posts %}
{% assign hit = false %}
{% for k in keys %}{% if post.url contains k %}{% assign hit = true %}{% endif %}{% endfor %}
{% if hit %}<li><a href="{{ post.url | relative_url }}">{{ post.title }}</a></li>{% endif %}
{% endfor %}
</ul>
{% endfor %}

[홈으로]({{ '/' | relative_url }}) · [글쓴이 소개]({{ '/about/' | relative_url }})
