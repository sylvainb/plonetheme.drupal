===============================================
plonetheme.drupal
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

plonetheme.drupal is an installable Plone Theme using `plone.app.theming`_, based on 
the default Sunburst Plone theme.

Strongly inspired by the Drupal theme `Bartik`_ (default theme in Drupal 7), this theme may help sell Plone to PHP guys ;)

**To be installed before any demonstration to an audience of Drupal followers ;) !**

Do you want to learn more about Plone versus Drupal ? Install this theme and visit *http://<your-plone-site>/@@plone-versus-drupal*

Requirements
------------

    * Tested with Plone 4.1.4 (http://plone.org/products/plone)
    
    * plone.app.theming (please configure your buildout corresponding to `plone.app.theming installation`_)

Screenshot
------------

.. image:: https://github.com/sylvainb/plonetheme.drupal/raw/master/docs/plonetheme-drupal-screenshot.png
   :height: 1039px
   :width: 1026px
   :scale: 70 %
   :alt: Plone Theme Drupal Screeshot
   :align: center

Installation
------------

Getting the theme
~~~~~~~~~~~~~~~~~~~~

Add ``plonetheme.drupal`` to your ``plone.recipe.zope2instance`` buildout section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        ...
        plonetheme.drupal

Or, you can add it as a dependency on your own product *setup.py*::

    install_requires=[
        ...
        'plonetheme.drupal',
    ],

Enabling the theme
~~~~~~~~~~~~~~~~~~~~

    Install the theme from the Add-ons control panel. That's it!

Credits
-------

    * Sylvain Boureliou [sylvainb]





.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`plone.app.theming installation`: http://pypi.python.org/pypi/plone.app.theming#installation
.. _`Bartik`: https://drupal.org/documentation/themes/bartik

