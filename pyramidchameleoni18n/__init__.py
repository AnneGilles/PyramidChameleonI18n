from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramidchameleoni18n.models import initialize_sql


from translationstring import TranslationStringFactory
_ = TranslationStringFactory('pyramidchameleoni18n')

def translator(term):
    return get_localizer(get_current_request().translate(term))

from pyramid.events import NewRequest
from pyramid.events import subscriber

@subscriber(NewRequest)
def set_request_locale(event):
    print "DEBUG: this is __init__.set_request_locale()"
    request = event.request
    from pyramid.threadlocal import get_current_registry
    settings = get_current_registry().settings
    languages = settings['available_languages'].split()
    for lang in request.accept_language.best_matches():
        if lang in languages:
            request._LOCALE_ = lang
            break
        else:
            request._LOCALE_ = settings['default_locale_name'] 
            

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    initialize_sql(engine)
    config = Configurator(settings=settings)

#    config.add_subscriber('pyramidchameleoni18n.subscribers.add_renderer_globals',
#                          'pyramid.events.BeforeRender')
#    config.add_subscriber('pyramidchameleoni18n.subscribers.add_localizer',
#                          'pyramid.events.NewRequest')
    
    config.add_translation_dirs('pyramidchameleoni18n:locale')
    config.add_static_view('static', 'pyramidchameleoni18n:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_view('pyramidchameleoni18n.views.my_view',
                    route_name='home',
                    renderer='templates/mytemplate.pt')

    config.add_route('test_i18n', '/test')
    config.add_view('pyramidchameleoni18n.views.test_i18n_view',
                    route_name='test_i18n',
                    renderer='templates/test_i18n.pt')

    config.add_route('deform-form', '/form')
    config.add_view('pyramidchameleoni18n.views.deform_form_view',
                    route_name='deform-form',
                    renderer='templates/deform-form.pt')

    return config.make_wsgi_app()

