import client

sections = ['home', 'world', 'national',
            'politics', 'nyregion', 'business',
            'opinion', 'technology', 'science',
            'health', 'sports', 'arts',
            'fashion', 'dining', 'travel',
            'magazine', 'realestate']


def isDuplicate(feeds, feed):
    for section in feeds:
        for sectionFeed in section:
            if sectionFeed['title'] == feed['title']:
                return True
            if sectionFeed['abstract'] == feed['abstract']:
                return True
            if sectionFeed['url'] == feed['url']:
                return True
    return False


def getNYTFeed():
    feeds = {}
    for section in sections:
        feedJSON = client.getTopFeeds(section)
        feedResult = feedJSON['results']
        feeds[section] = []

        for result in feedResult:
            if not isDuplicate(result, feeds):
                feeds[section].append({'title': result['title'], 'abstract': result[
                                      'abstract'], 'url': result['url']})

    return feeds
