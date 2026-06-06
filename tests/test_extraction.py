from backend.services.extractor_service import extract_article


url = input("Enter article URL: ")

text = extract_article(url)

print("\n")
print("=" * 80)
print(text[:2000])
print("\n")
print("=" * 80)
print(f"\nExtracted {len(text)} characters.")