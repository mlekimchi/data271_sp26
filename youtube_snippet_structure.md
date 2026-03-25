# YouTube API — `snippet` Structure
`payload['items'][0]['snippet']`

---

```
snippet{}
├── 'title'        → 'Cal Poly Humboldt'
├── 'description'  → 'Cal Poly Humboldt is where futures are found...'
├── 'customUrl'    → '@calpolyhumboldt'
├── 'publishedAt'  → '2007-05-09T18:48:38Z'
├── 'country'      → 'US'
│
├── 'thumbnails'{}
│   ├── 'default'{}          ← 88 × 88 px
│   │   ├── 'url'    → 'https://yt3.ggpht.com/...'
│   │   ├── 'width'  → 88
│   │   └── 'height' → 88
│   ├── 'medium'{}           ← 240 × 240 px
│   │   ├── 'url'    → 'https://yt3.ggpht.com/...'
│   │   ├── 'width'  → 240
│   │   └── 'height' → 240
│   └── 'high'{}             ← 800 × 800 px
│       ├── 'url'    → 'https://yt3.ggpht.com/...'
│       ├── 'width'  → 800
│       └── 'height' → 800
│
└── 'localized'{}            ← translated version of title/description
    ├── 'title'       → 'Cal Poly Humboldt'
    └── 'description' → 'Cal Poly Humboldt is where futures are found...'
```

---

## How to navigate in Python

```python
snippet = payload['items'][0]['snippet']

snippet['title']                          # channel name
snippet['publishedAt']                    # date channel was created
snippet['customUrl']                      # @ handle
snippet['thumbnails']['high']['url']      # high-res thumbnail URL
snippet['localized']['description']       # translated description
```
