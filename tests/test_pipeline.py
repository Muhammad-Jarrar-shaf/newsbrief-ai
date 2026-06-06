from backend.services.pipeline_service import summarize_from_url


url = input("Enter article URL: ")

result = summarize_from_url(url)

print("\n")
print("=" * 80)
print("SUMMARY")
print("=" * 80)

print(result["summary"])

print("\n")
print("=" * 80)
print(f"Article Length: {len(result['article'])} characters")