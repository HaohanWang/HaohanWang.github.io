#!/usr/bin/env python3
"""Build the blog from Markdown sources.

Unpublished drafts live in blog/drafts/ (gitignored, so they never reach the
public repo). To publish, move a draft into blog/posts/ and set its date.
Published posts live in blog/posts/*.md with YAML front matter:

    ---
    title: Vision should be structural
    subtitle: One-sentence summary shown in the index and search results.
    date: 2026-10-09        # or DRAFT (drafts are skipped)
    tags: [computer vision, SVG, perspective]
    slug: vision-should-be-structural   # optional; defaults to the file name
    ---

Outputs blog/<slug>.html, blog/index.html, blog/feed.xml, and refreshes the blog
block of sitemap.xml. Run from anywhere:  python3 tools/build_blog.py
Requires: pip install markdown pyyaml
"""
import datetime as dt
import html
import json
import pathlib
import re

import markdown
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
POSTS = ROOT / "blog" / "posts"
OUT = ROOT / "blog"
BASE = "https://haohanwang.ischool.illinois.edu/"
PERSON = {"@type": "Person", "@id": BASE + "#person", "name": "Haohan Wang", "url": BASE}

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>{title}</title>
	<meta name="description" content="{desc}">
	<meta name="author" content="Haohan Wang">
	<link rel="canonical" href="{url}">
	<link rel="icon" href="../favicon.ico" type="image/x-icon">
	<link rel="alternate" type="application/rss+xml" title="Haohan Wang's blog" href="{base}blog/feed.xml">
	<meta property="og:type" content="{og_type}">
	<meta property="og:site_name" content="Haohan Wang">
	<meta property="og:title" content="{og_title}">
	<meta property="og:description" content="{desc}">
	<meta property="og:url" content="{url}">
	<meta property="og:image" content="{base}img/haohanwang.jpg">
	<meta name="twitter:card" content="summary">
	<meta name="twitter:site" content="@HaohanWang">
	<meta name="twitter:creator" content="@HaohanWang">
	<script type="application/ld+json">
{ld}
	</script>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css?family=Poppins:300,400,500,600&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="../css/linearicons.css">
	<link rel="stylesheet" href="../css/bootstrap.css">
	<link rel="stylesheet" href="../css/main.css">
	<link rel="stylesheet" href="../css/site.css">
</head>
<body>
	<header id="header">
		<div class="container main-menu">
			<div class="row align-items-center justify-content-between d-flex">
				<div id="logo"><a href="../index.html" aria-label="Home"></a></div>
				<nav id="nav-menu-container" aria-label="Main">
					<ul class="nav-menu">
						<li><a href="../index.html">Home</a></li>
						<li><a href="../index.html#research">Research</a></li>
						<li><a href="../index.html#news">News</a></li>
						<li><a href="../index.html#talks">Talks</a></li>
						<li><a href="../publications.html">Publications</a></li>
						<li><a href="index.html" class="menu-active">Blog</a></li>
						<li><a href="../index.html#speaking">Speaking</a></li>
						<li><a href="../index.html#about">About</a></li>
					</ul>
				</nav>
			</div>
		</div>
	</header>
	<main class="topic-page blog-page">
		<section class="section-gap">
			<div class="container">
"""

FOOT = """			</div>
		</section>
	</main>
	<footer class="footer-area">
		<div class="container text-center">
			<p>© {year} Haohan Wang · School of Information Sciences, University of Illinois Urbana-Champaign · <a href="../index.html">Home</a> · <a href="index.html">Blog</a> · <a href="feed.xml">RSS</a></p>
		</div>
	</footer>
	<script src="../js/site.js" defer></script>
</body>
</html>
"""


def esc(s):
    return html.escape(str(s), quote=True)


def load_posts():
    posts = []
    for path in sorted(POSTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
        if not m:
            raise SystemExit(f"{path}: missing front matter")
        meta = yaml.safe_load(m.group(1)) or {}
        date = str(meta.get("date", "DRAFT"))
        if date.upper() == "DRAFT" or meta.get("draft"):
            continue
        meta["date"] = dt.date.fromisoformat(date)
        meta["slug"] = meta.get("slug") or re.sub(r"^\d+-", "", path.stem)
        meta["tags"] = meta.get("tags") or []
        # The page template already shows the title and subtitle, so drop a leading
        # "# Title" line and an italic subtitle line if the Markdown repeats them.
        body_md = re.sub(r"^\s*#\s+[^\n]*\n+(\*[^\n]*\*\s*\n+)?", "", m.group(2), count=1)
        meta["body"] = markdown.markdown(body_md, extensions=["extra", "smarty", "toc"])
        meta["words"] = len(re.findall(r"\w+", m.group(2)))
        posts.append(meta)
    return sorted(posts, key=lambda p: p["date"], reverse=True)


def render_post(p):
    url = f"{BASE}blog/{p['slug']}.html"
    ld = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p["title"],
          "description": p.get("subtitle", ""), "url": url, "mainEntityOfPage": url,
          "datePublished": p["date"].isoformat(), "dateModified": p["date"].isoformat(),
          "author": PERSON, "publisher": PERSON, "keywords": p["tags"], "wordCount": p["words"],
          "image": BASE + "img/haohanwang.jpg", "inLanguage": "en",
          "isPartOf": {"@type": "Blog", "@id": BASE + "blog/", "name": "Haohan Wang's blog"}}
    head = HEAD.format(title=esc(f"{p['title']} | Haohan Wang"), desc=esc(p.get("subtitle", "")), url=url,
                       base=BASE, og_type="article", og_title=esc(p["title"]),
                       ld=json.dumps(ld, ensure_ascii=False, indent=1))
    tags = " · ".join(esc(t) for t in p["tags"])
    body = f"""				<p class="breadcrumb-line"><a href="../index.html">Haohan Wang</a> › <a href="index.html">Blog</a></p>
				<article class="blog-post">
					<h1>{esc(p['title'])}</h1>
					<p class="post-subtitle">{esc(p.get('subtitle', ''))}</p>
					<p class="post-meta">Haohan Wang · <time datetime="{p['date'].isoformat()}">{p['date'].strftime('%B %-d, %Y')}</time>{(' · ' + tags) if tags else ''}</p>
					{p['body']}
					<p class="post-note">This post shares my personal perspective; it does not represent the views of the University of Illinois.</p>
				</article>
				<p class="related-line"><a href="index.html">← All posts</a> · <a href="feed.xml">Subscribe via RSS</a></p>
"""
    (OUT / f"{p['slug']}.html").write_text(head + body + FOOT.format(year=p["date"].year), encoding="utf-8")


def render_index(posts):
    url = BASE + "blog/"
    ld = {"@context": "https://schema.org", "@type": "Blog", "@id": url, "url": url,
          "name": "Haohan Wang's blog", "author": PERSON, "inLanguage": "en",
          "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f"{BASE}blog/{p['slug']}.html",
                        "datePublished": p["date"].isoformat()} for p in posts]}
    desc = "Personal perspectives from Haohan Wang (UIUC) on AI research, trustworthy AI, AI for science, and teaching."
    head = HEAD.format(title="Blog | Haohan Wang – Perspectives on AI Research and Teaching", desc=esc(desc),
                       url=url, base=BASE, og_type="website", og_title="Haohan Wang's blog",
                       ld=json.dumps(ld, ensure_ascii=False, indent=1))
    items = "".join(f"""
					<li>
						<h2><a href="{p['slug']}.html">{esc(p['title'])}</a></h2>
						<p class="post-meta"><time datetime="{p['date'].isoformat()}">{p['date'].strftime('%B %-d, %Y')}</time></p>
						<p>{esc(p.get('subtitle', ''))}</p>
					</li>""" for p in posts) or "\n\t\t\t\t\t<li><p>The first posts are coming soon.</p></li>"
    body = f"""				<h1>Blog</h1>
				<p class="lead-summary">Personal perspectives on AI research, trustworthy AI, AI for science, and teaching. For research write-ups, see the <a href="../index.html#research">research pages</a> and the <a href="https://dream.ischool.illinois.edu/blogs.html" target="_blank" rel="noopener">DREAM Lab blog</a>.</p>
				<ul class="post-list">{items}
				</ul>
"""
    (OUT / "index.html").write_text(head + body + FOOT.format(year=dt.date.today().year), encoding="utf-8")


def render_feed(posts):
    items = "".join(f"""
  <item>
    <title>{esc(p['title'])}</title>
    <link>{BASE}blog/{p['slug']}.html</link>
    <guid>{BASE}blog/{p['slug']}.html</guid>
    <pubDate>{dt.datetime.combine(p['date'], dt.time(12)).strftime('%a, %d %b %Y %H:%M:%S -0500')}</pubDate>
    <description>{esc(p.get('subtitle', ''))}</description>
  </item>""" for p in posts)
    (OUT / "feed.xml").write_text(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>Haohan Wang's blog</title>
  <link>{BASE}blog/</link>
  <description>Personal perspectives on AI research, trustworthy AI, AI for science, and teaching.</description>
  <language>en</language>{items}
</channel>
</rss>
""", encoding="utf-8")


def update_sitemap(posts):
    path = ROOT / "sitemap.xml"
    s = path.read_text(encoding="utf-8")
    s = re.sub(r"  <!-- blog:start -->.*?<!-- blog:end -->\n", "", s, flags=re.S)
    today = dt.date.today().isoformat()
    lines = [f"  <url><loc>{BASE}blog/</loc><lastmod>{(posts[0]['date'].isoformat() if posts else today)}</lastmod><priority>0.7</priority></url>"]
    lines += [f"  <url><loc>{BASE}blog/{p['slug']}.html</loc><lastmod>{p['date'].isoformat()}</lastmod><priority>0.6</priority></url>" for p in posts]
    block = "  <!-- blog:start -->\n" + "\n".join(lines) + "\n  <!-- blog:end -->\n"
    path.write_text(s.replace("</urlset>", block + "</urlset>"), encoding="utf-8")


def main():
    posts = load_posts()
    for p in posts:
        render_post(p)
    render_index(posts)
    render_feed(posts)
    update_sitemap(posts)
    print(f"Built {len(posts)} post(s).")


if __name__ == "__main__":
    main()
