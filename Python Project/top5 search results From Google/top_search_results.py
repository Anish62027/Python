from googlesearch import search

query = "Data Science Slybas"
search_results = search(query, num_results=5, lang="en")

for i, result in enumerate(search_results, start=1):
    print(f"Result {i}:")
    print(result)
    print()
