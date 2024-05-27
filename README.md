# gdork

gdork generates dorks for all search engine

## Installation
```
git clone https://github.com/rix4uni/gdork.git
cd gdork
python3 gdork.py -h
```

## Usage
```
usage: gdork.py [-h] [-se SE] [-wl WL]

Generate search URLs with wildcard domains

options:
  -h, --help            show this help message and exit
  -se SE, --search-engines SE
                        Specify search engines separated by comma or use 'all' for all engines
  -wl WL, --wildcard-levels WL
                        Specify the number of wildcard levels to add (default is 5)
```

## Example usages

Queries:
```
site:tiltbrush.com ext:php inurl:?
site:tiltbrush.com ext:aspx inurl:?
```

Single Engine:
```
python3 gdork.py -se google -wl 5
```

Output:
```
https://www.google.com/search?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
```

Multiple Engines:
```
python3 gdork.py -se google,duckduckgo -wl 5
```

Output:
```
https://www.google.com/search?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
```

All Engines:
```
python3 gdork.py -se all -wl 5
```

Output:
```
https://www.google.com/search?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.bing.com/search?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://yandex.com/search/?text=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://search.brave.com/search?q=site:tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.bing.com/search?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://yandex.com/search/?text=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://search.brave.com/search?q=site:tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.bing.com/search?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://yandex.com/search/?text=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://search.brave.com/search?q=site:*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.bing.com/search?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://yandex.com/search/?text=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://search.brave.com/search?q=site:*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aphp%20inurl%3A%3F
https://www.google.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://www.bing.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://duckduckgo.com/?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://in.search.yahoo.com/search?p=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://yandex.com/search/?text=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
https://search.brave.com/search?q=site:*.*.*.*.*.tiltbrush.com ext%3Aaspx%20inurl%3A%3F
```
