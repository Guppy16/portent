MAX_CAT = 5


tags_meta = {
    "Stock Market": [
        "Bank of England Interest Rate Decrease",
        "U.S. Consumer Price Index (CPI) rises",
        "U.S. Stock Market Crash",
        "U.S. Stock Market Boom",
        "Major sanctions imposed China",
    ],
    "Natural Disasters": [
        "Earthquake",
        "Flood",
        "Hurricane",
        "Tornado",
        "Wildfire",
        "Volcanic Eruption",
    ],
    "Other": [
        "Peace Treaty Signed",
        "New trade bloc launched",
        "Pandemic emerges",
        "Government-mandated lockdowns",
    ],
}


def get_tags():
    event_tags = []
    for key in tags_meta:
        event_tags.extend(tags_meta[key])
    return event_tags, MAX_CAT
