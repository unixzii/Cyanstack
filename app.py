from tornado.web import Application, StaticFileHandler
from tornado.ioloop import IOLoop
import settings
import handlers
import utils


if __name__ == "__main__":
    utils.set_verbose_enabled(True)

    app = Application(
        [
            (r"/", handlers.IndexHandler),
            (r"/actions/fetch_articles", handlers.FetchArticlesHandler),
            (r"/static/(.*)", StaticFileHandler, {"path": settings.APP_SETTINGS["static_path"]}),
            (r".*", handlers.NotFoundHandler),
        ],
        "",
        None,
        template_path=settings.APP_SETTINGS["template_path"],
        static_hash_cache=False,
        compiled_template_cache=False
    )
    app.listen(80)
    utils.verbose("Server started!!!")
    IOLoop.instance().start()
