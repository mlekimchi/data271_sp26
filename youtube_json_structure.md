# YouTube API — JSON Response Structure
`channels` endpoint · `part=snippet` · `forHandle=CalPolyHumboldt`

---

```
payload{}
├── 'kind'          → 'youtube#channelListResponse'
├── 'etag'          → 'NANAf4I7...'
├── 'pageInfo'{}
│   ├── 'totalResults'    → 1
│   └── 'resultsPerPage'  → 5
│
└── 'items'[]                          ← list, use [0] to access first item
    └── [0]{}
        ├── 'kind'    → 'youtube#channel'
        ├── 'etag'    → 'Ha1NwOtB...'
        ├── 'id'      → 'UCg7Fdhrmwi8ZqakqiO3xPkg'  ← channel_id for next request
        │
        └── 'snippet'{}                              ← returned because part='snippet'
            ├── 'title'        → 'Cal Poly Humboldt'
            ├── 'description'  → 'Cal Poly Humboldt is where...'
            ├── 'customUrl'    → '@calpolyhumboldt'
            ├── 'publishedAt'  → '2007-05-09T18:48:38Z'
            ├── 'country'      → 'US'
            │
            ├── 'thumbnails'{}
            │   ├── 'default'{}
            │   │   ├── 'url'    → 'https://yt3.ggpht.com/...'
            │   │   ├── 'width'  → 88
            │   │   └── 'height' → 88
            │   ├── 'medium'{}
            │   │   ├── 'url'    → 'https://yt3.ggpht.com/...'
            │   │   ├── 'width'  → 240
            │   │   └── 'height' → 240
            │   └── 'high'{}
            │       ├── 'url'    → 'https://yt3.ggpht.com/...'
            │       ├── 'width'  → 800
            │       └── 'height' → 800
            │
            └── 'localized'{}
                ├── 'title'       → 'Cal Poly Humboldt'
                └── 'description' → 'Cal Poly Humboldt is where...'
```

---

## How to navigate in Python

```python
payload['items'][0]['id']                                    # channel ID
payload['items'][0]['snippet']['title']                      # channel name
payload['items'][0]['snippet']['publishedAt']                # date created
payload['items'][0]['snippet']['thumbnails']['high']['url']  # thumbnail URL
```
