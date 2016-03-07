import web
import feedReader

urls = ("/feeds", "feeds")
app = web.application(urls, globals())


class feeds:
    def GET(self):
        return feedReader.getNYTFeed()

if __name__ == "__main__":
    app.run()
