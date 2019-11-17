# hnclone API

This document lists the implemented resources on the API

## List of Contents
* [Articles](##Articles)
* [Crawlers](##Crawlers)

## Articles
Article here refers to the news article as a dictionary.

### Adding Articles to the Datastore
Using the client

    from client import Client
    c = Client(api_token='...', api_url='...')
    article = {'..':'..'} # The structure of the article should be as follows.
    c.update(article)

or

    POST /add
    Content-Type: application/json

    {
        "source": "...",
        "source_url": "...",
        "headline":"...",
        "story_url":"...",
        "short_desc":"...",
        "category":"...",
        "updated_on":"..."
    } 

    HTTP/1.1 201 Created
    Content-Type: application/json
    {
        "message": "article added"
    }
    ---
    HTTP/1.1 412 Precondition Failed
    If any of the keys among 'headline', 'source', 'source_url', 'story_url' turns out to be empty/missing


### Fetching Articles

    GET /news
    ---
    HTTP/1.1 200 OK
    Content-Type: application/json

    [
        {
            "source": "hn",
            "source_url": "xyx.com",
            "headline":"alpha beta gamma ",
            "story_url":"alpha.betagama",
            "short_desc":"q delta",
            "category":"science",
            "updated_on":"..."

        }
        {
            "source": "ab",
            .....
        }
    ]
    
    POST /news
    Content-Type: application/json
    {
        "source": 'abc'
        ....
    }

    HTTP/1.1 200 OK
    Content-Type: application/json
    [
        {
            "source" : 'abc',
            ...
        }
        {
            "source" : 'abc',
            ...
        }
    ]




## Crawlers
    #TODO