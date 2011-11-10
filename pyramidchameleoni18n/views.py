from pyramidchameleoni18n.models import DBSession
from pyramidchameleoni18n.models import MyModel

from pyramid.i18n import get_locale_name

def my_view(request):
    locale_name = get_locale_name(request)
    print "DEBUG: locale_name is " + str(locale_name)
    
    dbsession = DBSession()
    root = dbsession.query(MyModel).filter(MyModel.name==u'root').first()
    return {'root':root, 'project':'PyramidChameleonI18n'}
