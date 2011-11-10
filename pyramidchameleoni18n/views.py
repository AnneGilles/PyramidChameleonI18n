from pyramidchameleoni18n.models import DBSession
from pyramidchameleoni18n.models import MyModel

def my_view(request):
    dbsession = DBSession()
    root = dbsession.query(MyModel).filter(MyModel.name==u'root').first()
    return {'root':root, 'project':'PyramidChameleonI18n'}
