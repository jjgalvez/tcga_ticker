__author__ = 'jc'

def routes(config):
    '''
    Add your routes here
    '''
    # static routes
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Application dynamic routes
    config.add_route('default', '/')
