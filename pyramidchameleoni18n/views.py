from pyramidchameleoni18n.models import DBSession
from pyramidchameleoni18n.models import MyModel

from pyramid.i18n import get_locale_name
from babel.core import Locale
#from pyramid.i18n import TranslationString

from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('PyramidChameleonI18n')

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


import deform
from deform import Form
from deform import ValidationFailure
import colander

def deform_form_view(request):
    locale_name = get_locale_name(request)
    print "DEBUG: locale_name: " + str(locale_name)

    class TestFormSchema(colander.MappingSchema):
        name = colander.SchemaNode(colander.String(),
                                   title = _('Your Name'))
        email = colander.SchemaNode(colander.String(),
                                    title = _('Email-Address'),
                                    validator = colander.Email())
        _LOCALE_ = colander.SchemaNode(colander.String(),
                                       widget = deform.widget.HiddenWidget(),
                                       default=locale_name)

    schema = TestFormSchema()
    form = deform.Form(schema,
                       buttons=[deform.Button('submit', _('Submit'))])

    if 'submit' in request.POST:
        controls = request.POST.items()
        try:
            appstruct = form.validate(controls)
            print "the controls: " + str(controls)
            print "the appstruct: " + str(appstruct)
        except ValidationFailure, e:
            return{'form': e.render()}
        print "OK: " + str(dir(form))
        return {'form':'OK'}

    return {'form': form.render()}
