from backend.services.extractor_service import extract_article
from backend.services.summarizer_service import summarize_article


def summarize_from_url(url: str) -> dict:
    """
    Extract article text from a URL and generate a summary.

    Returns:
        dict containing article text and summary.
    """

    article_text = extract_article(url)

    summary = summarize_article(article_text)

    return {
        "article": article_text,
        "summary": summary,
    }