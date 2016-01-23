from tornado.web import RequestHandler
from tornado.template import Template, Loader
from tornado import escape
import settings

class BaseHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):
        expl = "um, it\'s hard to explain."
        if status_code == 404:
            expl = "that means what you want is not existed or moved."
        if status_code == 403 or status_code == 405:
            expl = "it wants you to stop doing it, it\'s forbidden."
        if status_code == 500:
            expl = "maybe you did something server don\'t like."

        self.render("server_error.html", code=status_code, expl=expl)


class NotFoundHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.write_error(404)


class IndexHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.render("index.html")


class FetchArticlesHandler(BaseHandler):

    def get(self, *args, **kwargs):
        page = int(self.get_query_argument("page", 1))
        nav_type = 2
        hint = "To be continued"
        if page < 1 or page > 10:
            page = 1
        if page == 1:
            nav_type = 1
        if page == 10:
            hint = "EOF"
            nav_type = -1
        loader = Loader(settings.APP_SETTINGS["template_path"])
        article_item_t = loader.load("article_item.html")
        article_item_htmls = []
        for i in range(1, page + 1):
            article_item_htmls.append(escape.json_encode(article_item_t.generate(
                title="This is the title",
                author="Cyandev",
                pub_date="Jul. 16, 2010",
                preview="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                tag="Fusion",
                id=i
            )))
        self.set_header('Content-Type', 'text/plain')
        self.write(loader.load("fetch_articles.js").generate(htmls=article_item_htmls, hint=hint, nav_type=nav_type, page=page))
