from pyramidchameleoni18n.models import DBSession
from pyramidchameleoni18n.models import MyModel

from pyramid.i18n import get_locale_name
from pyramid.i18n import get_localizer
from babel.core import Locale

import deform
from deform import Form
from deform import ValidationFailure
import colander

from pyramid.i18n import TranslationStringFactory
_ = TranslationStringFactory('PyramidChameleonI18n')

def translator(term):
    return get_localizer(get_current_request()).translate(term)

from pkg_resources import resource_filename
deform_template_dir = resource_filename('pyramidchameleoni18n', 'templates/')

zpt_renderer = deform.ZPTRendererFactory(
    [deform_template_dir], translator=translator)


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
    form.set_default_renderer(zpt_renderer)

    if 'submit' in request.POST:
        # the form was submitted
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
