from backend.services.summarizer_service import summarize_article

text = input("Enter text:\n")

summary = summarize_article(text)

print("\n")
print("=" * 80)

print(summary)

print("=" * 80)