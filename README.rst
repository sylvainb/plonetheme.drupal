===============================================
plonetheme.drupal
===============================================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

plonetheme.drupal is an installable Plone Theme using `plone.app.theming`_, based on 
the default Sunburst Plone theme.

Get all the power of Drupal for Plone :)

Requirements
------------

    * Tested with Plone 4.1.4 (http://plone.org/products/plone)
    
    * plone.app.theming (*please configure your buildout corresponding to `plone.app.theming installation`_*)

Screenshots
------------

.. image:: https://lh3.googleusercontent.com/-TvpeCacVZPU/SQnO7E6d7BI/AAAAAAAAAKc/Zpbms-CylhA/s576/DSCN3602.JPG

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

