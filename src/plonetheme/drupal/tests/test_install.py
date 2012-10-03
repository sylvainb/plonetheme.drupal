import string
import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from zope.component import getUtility

from plonetheme.drupal.testing import PLONETHEME_DRUPAL_INTEGRATION_TESTING


class TestInstall(unittest.TestCase):

    layer = PLONETHEME_DRUPAL_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_product_is_installed(self):
        """ Validate that our products GS profile has been run and the product 
            installed
        """
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(portal_quickinstaller.isProductInstalled('plonetheme.drupal'),
                        'package appears not to have been installed')

    def test_skins(self):
        """ Validate that the skin directories are installed in the portal_skins tool
            (not added in the "Plone Default" skin) """
        portal_skins = getToolByName(self.portal, 'portal_skins')
        self.assertEqual("plonetheme_drupal_custom" in portal_skins.objectIds(), True)

    def test_css_in_registry(self):
        """ Validate our css are registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_css')
        installedStylesheetIds = portal_css.getResourceIds()
        expected = ['++theme++plonetheme.drupal/css/theme.css',
                    '++theme++plonetheme.drupal/css/ie-fixes.css', ]
        for e in expected:
            self.assertTrue(e in installedStylesheetIds, e)

    def test_js_in_registry(self):
        """ Validate our js are registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_javascripts')
        installedJavaScriptIds = portal_css.getResourceIds()
        expected = ['++theme++plonetheme.drupal/js/theme.js', ]
        for e in expected:
            self.assertTrue(e in installedJavaScriptIds, e)

    def test_browser_layer(self):
        """ Validate our browser layer is registered """
        from plone.browserlayer.utils import registered_layers
        from plonetheme.drupal.browser.interfaces import IThemeSpecific
        self.assertTrue(IThemeSpecific in registered_layers())
    
    def test_diazo_theme_available(self):
        from plone.app.theming.utils import getCurrentTheme
        self.assertTrue(getCurrentTheme() == u'plonetheme.drupal')

class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_DRUPAL_INTEGRATION_TESTING
    
    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        
        # Remove the product using the Quick Installer tool
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        portal_quickinstaller.uninstallProducts( ('plonetheme.drupal',) )

    def test_product_is_not_installed(self):
        """ Validate that our products is not yet installed
        """
        portal_quickinstaller = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(portal_quickinstaller.isProductInstalled('plonetheme.drupal'),
                        'package appears to be already installed')

    def test_not_in_skins(self):
        """ Validate that the skin directories is removed from the portal_skins tool """
        portal_skins = getToolByName(self.portal, 'portal_skins')
        self.assertNotEqual("plonetheme.drupal" in portal_skins.objectIds(), True)

    def test_css_not_in_registry(self):
        """ Validate our css are no longer registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_css')
        installedStylesheetIds = portal_css.getResourceIds()
        not_expected = ['++theme++plonetheme.drupal/css/theme.css',
                        '++theme++plonetheme.drupal/css/ie-fixes.css', ]
        for e in not_expected:
            self.assertFalse(e in installedStylesheetIds, e)

    def test_js_not_in_registry(self):
        """ Validate our js are no longer registered in portal_css """
        portal_css = getToolByName(self.portal, 'portal_javascripts')
        installedJavaScriptIds = portal_css.getResourceIds()
        not_expected = ['++theme++plonetheme.drupal/js/theme.js', ]
        for e in not_expected:
            self.assertFalse(e in installedJavaScriptIds, e)

    def test_browser_layer(self):
        """ Validate our browser layer is no longer registered """
        from plone.browserlayer.utils import registered_layers
        from plonetheme.drupal.browser.interfaces import IThemeSpecific
        self.assertFalse(IThemeSpecific in registered_layers())
    
    def test_diazo_theme_not_available(self):
        pass
        # A bug ? the theme is always selected (but inactive) in the plone.app.theming control panel
        #from plone.app.theming.utils import getCurrentTheme
        #self.assertFalse(getCurrentTheme() == u'plonetheme.drupal')

