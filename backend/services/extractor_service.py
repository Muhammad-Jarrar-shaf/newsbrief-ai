from newspaper import Article
import trafilatura


class ArticleExtractionError(Exception):
    pass


def extract_with_newspaper(url: str) -> str:
    article = Article(url)

    article.download()
    article.parse()

    text = article.text.strip()

    if len(text) < 3000:
        raise ValueError("Article too short.")

    return text


def extract_with_trafilatura(url: str) -> str:
    downloaded = trafilatura.fetch_url(url)

    if downloaded is None:
        raise ValueError("Failed to download page.")

    text = trafilatura.extract(downloaded)

    if text is None or len(text.strip()) < 3000:
        raise ValueError("Extracted text too short.")

    return text.strip()


def extract_article(url: str) -> str:
    try:
        print("Trying newspaper3k...")
        return extract_with_newspaper(url)

    except Exception as e:
        print(f"newspaper3k failed: {e}")

    try:
        print("Trying trafilatura...")
        return extract_with_trafilatura(url)

    except Exception as e:
        print(f"trafilatura failed: {e}")

    raise ArticleExtractionError(
        "Failed to extract article using all available methods."
    )