from html import escape


def format_article_html(title: str, publish_date: str, publisher: str, content: str) -> str:
    """
    Convert crawled government article metadata into a standardized HTML block.
    """

    safe_title = escape(title)
    safe_publish_date = escape(publish_date)
    safe_publisher = escape(publisher)
    safe_content = escape(content).replace("\n", "<br>")

    return f"""
<article class="gov-article">
    <h1>{safe_title}</h1>
    <div class="article-meta">
        <span>Publication Date: {safe_publish_date}</span>
        <span>Publisher: {safe_publisher}</span>
    </div>
    <div class="article-content">
        {safe_content}
    </div>
</article>
""".strip()