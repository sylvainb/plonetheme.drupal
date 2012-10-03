import unittest
import doctest

from plone.testing import layered

from plonetheme.drupal.testing import PLONETHEME_DRUPAL_FUNCTIONNAL_TESTING


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite('doctests.rst',
                                     optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                                                 doctest.NORMALIZE_WHITESPACE | 
                                                 doctest.ELLIPSIS), 
                layer=PLONETHEME_DRUPAL_FUNCTIONNAL_TESTING),
    ])
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')