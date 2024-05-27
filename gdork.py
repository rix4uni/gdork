import argparse
import urllib.parse

# Define the base URLs for each search engine
search_engines = {
    "google": "https://www.google.com/search?q=",
    "bing": "https://www.bing.com/search?q=",
    "duckduckgo": "https://duckduckgo.com/?q=",
    "yahoo": "https://in.search.yahoo.com/search?p=",
    "yandex": "https://yandex.com/search/?text=",
    "brave": "https://search.brave.com/search?q="
}

# Function to generate search URLs
def generate_search_urls(queries, engines, wildcard_levels):
    for level in range(wildcard_levels + 1):  # From 0 to wildcard_levels
        for query in queries:
            query = query.strip()  # Remove any leading/trailing whitespace
            if query:  # Check if the line is not empty
                wildcard_prefix = '*.' * level  # Create wildcard prefix
                parts = query.split(' ')
                modified_query = f"site:{wildcard_prefix}{parts[0].split(':')[1]}"
                remaining_query = ' '.join(parts[1:])
                encoded_query = f"{modified_query} {urllib.parse.quote(remaining_query)}"
                for engine in engines:
                    base_url = search_engines.get(engine)
                    if base_url:
                        search_url = base_url + encoded_query
                        print(search_url)

def main():
    parser = argparse.ArgumentParser(description="Generate search URLs with wildcard domains")
    parser.add_argument("-se", "--search-engines", metavar="SE", type=str, default="all",
                        help="Specify search engines separated by comma or use 'all' for all engines")
    parser.add_argument("-wl", "--wildcard-levels", metavar="WL", type=int, default=5,
                        help="Specify the number of wildcard levels to add (default is 5)")
    
    args = parser.parse_args()

    if args.search_engines.lower() == "all":
        engines = list(search_engines.keys())
    else:
        engines = [engine.strip() for engine in args.search_engines.split(',')]

    queries = []
    with open('queries.txt', 'r') as file:
        queries = file.readlines()

    generate_search_urls(queries, engines, args.wildcard_levels)

if __name__ == "__main__":
    main()
