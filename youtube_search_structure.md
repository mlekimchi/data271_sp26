# YouTube API — Search Response Structure
`search` endpoint · `part=snippet` · `channelId=UCg7...` · `maxResults=50`

---

```
payload{}
├── 'kind'           → 'youtube#searchListResponse'
├── 'etag'           → 'AMaPoe4I...'
├── 'nextPageToken'  → 'CDIQAA'              ← pass as pageToken= to get next 50 videos
├── 'regionCode'     → 'US'
│
├── 'pageInfo'{}
│   ├── 'totalResults'    → 265              ← total videos on channel
│   └── 'resultsPerPage'  → 50              ← videos returned this request
│
└── 'items'[]                                ← list of 50 videos, one dict per video
    │
    ├── [0]{}                                ← first video  · payload['items'][0]
    │   ├── 'kind'   → 'youtube#searchResult'
    │   ├── 'etag'   → 'TwmZfvR_...'
    │   │
    │   ├── 'id'{}
    │   │   ├── 'kind'    → 'youtube#video'
    │   │   └── 'videoId' → 'sjYJVCOuX-o'   ← use this to get video stats
    │   │
    │   └── 'snippet'{}
    │       ├── 'publishedAt'        → '2026-03-23T23:53:16Z'
    │       ├── 'channelId'          → 'UCg7Fdhrmwi8ZqakqiO3xPkg'
    │       ├── 'title'              → 'Housing at Cal Poly Humboldt'
    │       ├── 'description'        → 'Thinking of living on campus?...'
    │       ├── 'channelTitle'       → 'Cal Poly Humboldt'
    │       ├── 'liveBroadcastContent' → 'none'
    │       ├── 'publishTime'        → '2026-03-23T23:53:16Z'
    │       │
    │       └── 'thumbnails'{}
    │           ├── 'default'{}      ← 120 × 90 px
    │           │   ├── 'url'    → 'https://i.ytimg.com/...'
    │           │   ├── 'width'  → 120
    │           │   └── 'height' → 90
    │           ├── 'medium'{}       ← 320 × 180 px
    │           │   ├── 'url'    → 'https://i.ytimg.com/...'
    │           │   ├── 'width'  → 320
    │           │   └── 'height' → 180
    │           └── 'high'{}         ← 480 × 360 px
    │               ├── 'url'    → 'https://i.ytimg.com/...'
    │               ├── 'width'  → 480
    │               └── 'height' → 360
    │
    ├── [1]{}                                ← second video · same structure as [0]
    ├── [2]{}
    ├── ...
    └── [49]{}                               ← 50th video  · payload['items'][49]
```

---

## How to navigate in Python

```python
# Access one video
payload['items'][0]['id']['videoId']             # video ID  ← use for stats request
payload['items'][0]['snippet']['title']          # video title
payload['items'][0]['snippet']['publishedAt']    # publish date

# Access ALL videos with a list comprehension
[item['id']['videoId'] for item in payload['items']]          # all 50 video IDs
[item['snippet']['title'] for item in payload['items']]       # all 50 titles
[item['snippet']['publishedAt'] for item in payload['items']] # all 50 dates

# Get the next 50 videos
parameters['pageToken'] = payload['nextPageToken']   # 'CDIQAA'
next_response = requests.get(search_url, params=parameters)
```
