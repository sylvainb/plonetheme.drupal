from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PlonethemeDrupal(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import plonetheme.drupal
        xmlconfig.file('configure.zcml',
                       plonetheme.drupal,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.drupal:default')

PLONETHEME_DRUPAL_FIXTURE = PlonethemeDrupal()
PLONETHEME_DRUPAL_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONETHEME_DRUPAL_FIXTURE, ),
                       name="PlonethemeDrupal:Integration")