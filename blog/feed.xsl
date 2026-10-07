<?xml version="1.0" encoding="UTF-8"?>
<!-- Renders blog/feed.xml as a readable page when opened in a browser. Feed readers ignore this. -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/rss/channel">
<html lang="en">
<head>
	<meta charset="UTF-8"/>
	<meta name="viewport" content="width=device-width, initial-scale=1"/>
	<meta name="robots" content="noindex"/>
	<title>RSS feed · <xsl:value-of select="title"/></title>
	<style>
		body { font-family: Poppins, -apple-system, Segoe UI, Arial, sans-serif; background: #f9f9ff; color: #444; margin: 0; padding: 48px 16px; }
		main { max-width: 760px; margin: 0 auto; }
		h1 { color: #222; font-size: 28px; margin: 0 0 8px; }
		.note { background: #fff; border-left: 3px solid #8490ff; padding: 14px 18px; margin: 18px 0 28px; }
		code { background: #eef0ff; padding: 2px 6px; border-radius: 4px; word-break: break-all; }
		a { color: #5b67e8; }
		.item { border-bottom: 1px solid #e6e6ef; padding: 16px 0; }
		.item h2 { font-size: 20px; margin: 0 0 4px; }
		.date { font-size: 13px; color: #999; }
	</style>
</head>
<body>
<main>
	<h1><xsl:value-of select="title"/></h1>
	<p><xsl:value-of select="description"/></p>
	<div class="note">
		<strong>This is an RSS feed.</strong> To get new posts automatically, copy this address into a feed reader such as Feedly, Inoreader, or NetNewsWire:<br/>
		<code>https://haohanwang.ischool.illinois.edu/blog/feed.xml</code>
	</div>
	<p><a href="./">← Back to the blog</a></p>
	<xsl:for-each select="item">
		<div class="item">
			<h2><a href="{link}"><xsl:value-of select="title"/></a></h2>
			<div class="date"><xsl:value-of select="substring(pubDate, 6, 11)"/></div>
			<p><xsl:value-of select="description"/></p>
		</div>
	</xsl:for-each>
</main>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
