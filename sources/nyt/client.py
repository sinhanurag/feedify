import requests
import json

with open('./config.json') as configFile:
    config = json.load(configFile)

def getTopFeeds(section):
    sectionData = section + '.json'
    requestEndpoint = str(config['baseUrl']) + '/' + \
        str(config['apis']['topStories']['path']) + sectionData
    payload = {'api-key': config['apiKey']}
    feeds = requests.get(requestEndpoint, params=payload)
    return feeds.json()
