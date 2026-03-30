"""
lab09_mock.py  —  Offline fallback for Lab 09 when the NOAA CDO API is down.

USAGE: Add the following line IMMEDIATELY after the existing imports cell:

    import lab09_mock

That's it. All requests.get() calls to the NOAA API will be intercepted and
served from the pre-fetched CSV files in this folder. The rest of the notebook
runs exactly as written.
"""

import os
import csv
import requests as _real_requests

# ── Locate CSV files (same directory as this file) ──────────────────────────
_HERE = os.path.dirname(os.path.abspath(__file__))

def _load_csv(filename):
    path = os.path.join(_HERE, filename)
    rows = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["value"] = float(row["value"])
            rows.append(row)
    return rows

_SF_DATA       = _load_csv("sf_data_oct2018.csv")
_DOWNTOWN_DATA = _load_csv("downtown_sf_data_oct2018.csv")
_EUREKA_DATA   = _load_csv("eureka_data_jan2024.csv")

# ── Mock response class ──────────────────────────────────────────────────────
class _MockResponse:
    def __init__(self, payload, status_code=200):
        self._payload = payload
        self.status_code = status_code

    def json(self):
        return self._payload

    def __repr__(self):
        return f"<MockResponse [status_code={self.status_code}]>"

# ── Pre-baked payloads for Section 2 exploration endpoints ───────────────────
_DATASETS_PAYLOAD = {
    "metadata": {"resultset": {"offset": 1, "count": 11, "limit": 25}},
    "results": [
        {"uid": "gov.noaa.ncdc:C00861", "mindate": "1763-01-01", "maxdate": "2024-10-27",
         "name": "Daily Summaries", "datacoverage": 1, "id": "GHCND"},
        {"uid": "gov.noaa.ncdc:C00946", "mindate": "1763-01-01", "maxdate": "2024-10-01",
         "name": "Global Summary of the Month", "datacoverage": 1, "id": "GSOM"},
        {"uid": "gov.noaa.ncdc:C00947", "mindate": "1763-01-01", "maxdate": "2024-01-01",
         "name": "Global Summary of the Year", "datacoverage": 1, "id": "GSOY"},
        {"uid": "gov.noaa.ncdc:C00345", "mindate": "1991-06-05", "maxdate": "2024-10-27",
         "name": "Weather Radar (Level II)", "datacoverage": 0.95, "id": "NEXRAD2"},
        {"uid": "gov.noaa.ncdc:C00708", "mindate": "1994-05-20", "maxdate": "2024-10-27",
         "name": "Weather Radar (Level III)", "datacoverage": 0.95, "id": "NEXRAD3"},
        {"uid": "gov.noaa.ncdc:C00821", "mindate": "2010-01-01", "maxdate": "2010-01-01",
         "name": "Normals Annual/Seasonal", "datacoverage": 1, "id": "NORMAL_ANN"},
        {"uid": "gov.noaa.ncdc:C00823", "mindate": "2010-01-01", "maxdate": "2010-12-01",
         "name": "Normals Daily", "datacoverage": 1, "id": "NORMAL_DLY"},
        {"uid": "gov.noaa.ncdc:C00824", "mindate": "2010-01-01", "maxdate": "2010-12-01",
         "name": "Normals Hourly", "datacoverage": 1, "id": "NORMAL_HLY"},
        {"uid": "gov.noaa.ncdc:C00822", "mindate": "2010-01-01", "maxdate": "2010-12-01",
         "name": "Normals Monthly", "datacoverage": 1, "id": "NORMAL_MLY"},
        {"uid": "gov.noaa.ncdc:C00505", "mindate": "1970-05-12", "maxdate": "2014-01-01",
         "name": "Precipitation 15 Minute", "datacoverage": 0.25, "id": "PRECIP_15"},
        {"uid": "gov.noaa.ncdc:C00313", "mindate": "1900-01-01", "maxdate": "2014-01-01",
         "name": "Precipitation Hourly", "datacoverage": 1, "id": "PRECIP_HLY"},
    ]
}

_DATACATEGORIES_PAYLOAD = {
    "metadata": {"resultset": {"offset": 1, "count": 10, "limit": 25}},
    "results": [
        {"name": "Air Temperature",  "id": "TEMP"},
        {"name": "Precipitation",    "id": "PRCP"},
        {"name": "Snow",             "id": "SNOW"},
        {"name": "Sky cover & clouds","id": "SKY"},
        {"name": "Sunshine",         "id": "SUN"},
        {"name": "Wind",             "id": "WIND"},
        {"name": "Weather Type",     "id": "WXTYPE"},
        {"name": "Degree Days",      "id": "DEGREE"},
        {"name": "Pressure",         "id": "PRES"},
        {"name": "Evaporation",      "id": "EVAP"},
    ]
}

_DATATYPES_PAYLOAD = {
    "metadata": {"resultset": {"offset": 1, "count": 8, "limit": 100}},
    "results": [
        {"mindate": "1763-01-01", "maxdate": "2024-10-27", "name": "Maximum temperature",                    "datacoverage": 1,   "id": "TMAX"},
        {"mindate": "1763-01-01", "maxdate": "2024-10-27", "name": "Minimum temperature",                    "datacoverage": 1,   "id": "TMIN"},
        {"mindate": "1763-01-01", "maxdate": "2024-10-27", "name": "Average Temperature",                    "datacoverage": 1,   "id": "TAVG"},
        {"mindate": "2002-01-01", "maxdate": "2024-10-27", "name": "Temperature at the time of observation", "datacoverage": 0.8, "id": "TOBS"},
        {"mindate": "1895-01-01", "maxdate": "2024-10-27", "name": "Cooling Degree Days",                    "datacoverage": 1,   "id": "CDSD"},
        {"mindate": "1895-01-01", "maxdate": "2024-10-27", "name": "Heating Degree Days",                    "datacoverage": 1,   "id": "HDSD"},
        {"mindate": "1895-01-01", "maxdate": "2024-10-27", "name": "Maximum soil temperature",               "datacoverage": 0.3, "id": "MXST"},
        {"mindate": "1895-01-01", "maxdate": "2024-10-27", "name": "Minimum soil temperature",               "datacoverage": 0.3, "id": "MNST"},
    ]
}

_LOCATIONCATEGORIES_PAYLOAD = {
    "metadata": {"resultset": {"offset": 1, "count": 12, "limit": 25}},
    "results": [
        {"name": "City",                              "id": "CITY"},
        {"name": "Climate Division",                  "id": "CLIM_DIV"},
        {"name": "Climate Region",                    "id": "CLIM_REG"},
        {"name": "Country",                           "id": "CNTRY"},
        {"name": "County",                            "id": "CNTY"},
        {"name": "Hydrological Accounting Unit",      "id": "HYD_ACC"},
        {"name": "Hydrological Cataloging Unit",      "id": "HYD_CAT"},
        {"name": "Hydrological Region",               "id": "HYD_REG"},
        {"name": "Hydrological Subregion",            "id": "HYD_SUB"},
        {"name": "State",                             "id": "ST"},
        {"name": "US Territory",                      "id": "US_TERR"},
        {"name": "Zip Code",                          "id": "ZIP"},
    ]
}

# Offset=1000 query — used by q2_11 to find SF city ID
_LOCATIONS_OFFSET1000_PAYLOAD = {
    "metadata": {"resultset": {"offset": 1001, "count": 2000, "limit": 1000}},
    "results": [
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "San Francisco, CA US", "datacoverage": 1, "id": "CITY:US060031"},
        {"mindate": "1871-01-01", "maxdate": "2024-10-27", "name": "Sacramento, CA US",     "datacoverage": 1, "id": "CITY:US060029"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "San Jose, CA US",       "datacoverage": 1, "id": "CITY:US060033"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Oakland, CA US",        "datacoverage": 1, "id": "CITY:US060023"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Los Angeles, CA US",    "datacoverage": 1, "id": "CITY:US060019"},
        {"mindate": "1938-01-01", "maxdate": "2024-10-27", "name": "San Diego, CA US",      "datacoverage": 1, "id": "CITY:US060030"},
        {"mindate": "1874-01-01", "maxdate": "2024-10-27", "name": "Fresno, CA US",         "datacoverage": 1, "id": "CITY:US060013"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Eureka, CA US",         "datacoverage": 1, "id": "CITY:US060009"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Redding, CA US",        "datacoverage": 1, "id": "CITY:US060027"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Santa Barbara, CA US",  "datacoverage": 1, "id": "CITY:US060036"},
    ]
}

# Offset=0 query — used by dessert section to search for Eureka
_LOCATIONS_OFFSET0_PAYLOAD = {
    "metadata": {"resultset": {"offset": 1, "count": 2000, "limit": 1000}},
    "results": [
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Abilene, TX US",       "datacoverage": 1, "id": "CITY:US480001"},
        {"mindate": "1874-01-01", "maxdate": "2024-10-27", "name": "Akron, OH US",         "datacoverage": 1, "id": "CITY:US390001"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Albany, NY US",        "datacoverage": 1, "id": "CITY:US360001"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Albuquerque, NM US",   "datacoverage": 1, "id": "CITY:US350001"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Eureka, CA US",        "datacoverage": 1, "id": "CITY:US060009"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Eureka, NV US",        "datacoverage": 1, "id": "CITY:US320003"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "San Francisco, CA US", "datacoverage": 1, "id": "CITY:US060031"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Sacramento, CA US",    "datacoverage": 1, "id": "CITY:US060029"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Los Angeles, CA US",   "datacoverage": 1, "id": "CITY:US060019"},
        {"mindate": "1893-01-01", "maxdate": "2024-10-27", "name": "Seattle, WA US",       "datacoverage": 1, "id": "CITY:US530018"},
    ]
}

# ── URL router ───────────────────────────────────────────────────────────────
_BASE = "https://www.ncei.noaa.gov/cdo-web/api/v2/"

def _mock_get(url, headers=None, params=None, **kwargs):
    params = params or {}

    if not url.startswith(_BASE):
        return _real_requests.get(url, headers=headers, params=params, **kwargs)

    endpoint = url[len(_BASE):]

    if endpoint == "datasets":
        return _MockResponse(_DATASETS_PAYLOAD)

    if endpoint == "datacategories":
        return _MockResponse(_DATACATEGORIES_PAYLOAD)

    if endpoint == "datatypes":
        return _MockResponse(_DATATYPES_PAYLOAD)

    if endpoint == "locationcategories":
        return _MockResponse(_LOCATIONCATEGORIES_PAYLOAD)

    if endpoint == "locations":
        offset = int(params.get("offset", 1))
        if offset == 0:
            return _MockResponse(_LOCATIONS_OFFSET0_PAYLOAD)
        return _MockResponse(_LOCATIONS_OFFSET1000_PAYLOAD)

    if endpoint == "data":
        station = params.get("stationid", "")
        location = str(params.get("locationid", ""))
        startdate = str(params.get("startdate", ""))

        # Eureka Jan 2024
        if "US060009" in location or "2024" in startdate:
            return _MockResponse({
                "metadata": {"resultset": {"offset": 1, "count": len(_EUREKA_DATA), "limit": 1000}},
                "results": _EUREKA_DATA
            })

        # Downtown SF only (single station)
        if "USW00023272" in str(station):
            return _MockResponse({
                "metadata": {"resultset": {"offset": 1, "count": len(_DOWNTOWN_DATA), "limit": 1000}},
                "results": _DOWNTOWN_DATA
            })

        # City-wide SF
        return _MockResponse({
            "metadata": {"resultset": {"offset": 1, "count": len(_SF_DATA), "limit": 1000}},
            "results": _SF_DATA
        })

    return _MockResponse({"message": "Not Found"}, status_code=404)


# ── Patch requests.get ───────────────────────────────────────────────────────
import requests
requests.get = _mock_get

print("lab09_mock loaded — NOAA API calls are served from pre-fetched CSV files.")
print("Proceed with the lab as normal.")
