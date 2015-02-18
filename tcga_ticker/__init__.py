from pyramid.config import Configurator
from tcga_ticker.routes import routes


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    #add routes
    routes(config)

    config.scan()
    return config.make_wsgi_app()
