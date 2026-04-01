# Python Datetime Format Reference

## Common Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | `2025` |
| `%y` | 2-digit year | `25` |
| `%m` | Month as zero-padded number | `04` |
| `%B` | Full month name | `April` |
| `%b` | Abbreviated month name | `Apr` |
| `%d` | Day of month, zero-padded | `05` |
| `%H` | Hour (24-hour clock), zero-padded | `14` |
| `%I` | Hour (12-hour clock), zero-padded | `02` |
| `%M` | Minute, zero-padded | `30` |
| `%S` | Second, zero-padded | `09` |
| `%p` | AM or PM | `PM` |
| `%j` | Day of the year | `095` |
| `%A` | Full weekday name | `Tuesday` |
| `%a` | Abbreviated weekday name | `Tue` |
| `%Z` | Timezone name | `UTC` |

## Lecture 27 Examples

| String | Format string |
|--------|--------------|
| `'April 5, 2025'` | `'%B %d, %Y'` |
| `'Apr 5, 2025'` | `'%b %d, %Y'` |
| `'4/5/25'` | `'%m/%d/%y'` |
| `'5-4-25'` | `'%d-%m-%y'` |
| `'4-5-2025'` | `'%m-%d-%Y'` |

Full reference: [Python strftime/strptime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
