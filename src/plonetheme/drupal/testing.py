from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from Products.CMFCore.utils import getToolByName

from plonetheme.drupal.tests.utils import PLONE_VERSION

class PlonethemeDrupal(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML, install the products and call its initialize() function 
        
        # Load ZCML for this package
        import plonetheme.drupal
        self.loadZCML(package=plonetheme.drupal)
        z2.installProduct(app, 'plonetheme.drupal')

    def setUpPloneSite(self, portal):
        # Configure the products using the Quick Installer tool 
        portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        
        portal_quickinstaller.installProducts( ('plonetheme.drupal',) )

    def tearDownZope(self, app):
        # Uninstall products
        z2.uninstallProduct(app, 'plonetheme.drupal')

    def tearDownPloneSite(self, portal):
        # Unconfigure the products using the Quick Installer tool
        portal_quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        portal_quickinstaller.uninstallProducts( ('plonetheme.drupal',) )

PLONETHEME_DRUPAL_FIXTURE = PlonethemeDrupal()
PLONETHEME_DRUPAL_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(PLONETHEME_DRUPAL_FIXTURE, ),
                       name="plonetheme.drupal:Integration")
PLONETHEME_DRUPAL_FUNCTIONNAL_TESTING = \
    FunctionalTesting(bases=(PLONETHEME_DRUPAL_FIXTURE, ),
                      name="plonetheme.drupal:Integration")
