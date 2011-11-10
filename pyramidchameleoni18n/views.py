from pyramidchameleoni18n.models import DBSession
from pyramidchameleoni18n.models import MyModel

from pyramid.i18n import get_locale_name
from babel.core import Locale
#from pyramid.i18n import TranslationString

def my_view(request):
    locale_name = get_locale_name(request)
    print "DEBUG: locale_name is " + str(locale_name)

    locale = Locale(locale_name)
    print "DEBUG: babel locale is " + str(locale)

#    _ = request.translate

    
    dbsession = DBSession()
    root = dbsession.query(MyModel).filter(MyModel.name==u'root').first()
    return {'root':root, 'project':'PyramidChameleonI18n'}



def test_i18n_view(request):
    locale_name = get_locale_name(request)
    print "DEBUG: locale_name is " + str(locale_name)

    locale = Locale(locale_name)
    print "DEBUG: babel locale is " + str(locale)
    locale_name = get_locale_name(request)
    print "DEBUG: locale_name is " + str(locale_name)

    locale = Locale(locale_name)
    print "DEBUG: babel locale is " + str(locale)


    return {'project':'myapp',
            'name':'Foo Bar',
            'country_of_birth':'Baz'} 
