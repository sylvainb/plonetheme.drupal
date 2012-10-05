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

    * I have tested this release with Plone 4.3a1, Plone 4.2.1.1 and Plone 4.1.6 (http://plone.org/products/plone).
    
    * For Plone 4.1.6 : plone.app.theming 1.0 (please configure your buildout corresponding to `plone.app.theming installation`_)

Screenshot
------------

.. image:: https://github.com/sylvainb/plonetheme.drupal/raw/master/docs/plonetheme-drupal-screenshot.png
   :height: 1039px
   :width: 1026px
   :scale: 70 %
   :alt: Plone Theme Drupal Screenshot
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

Quickly test ?
~~~~~~~~~~~~~~~~~~~~

Download plonetheme.drupal and use virtualenv and buildout to test the theme::

	easy_install virtualenv
	cd plonetheme.drupal
	virtualenv .
	source bin/activate
	(plonetheme.drupal) easy_install zc.buildout 
    !!! check the buildout config file ``test-plone-base.cfg`` before running !!!
    (plonetheme.drupal) ln -s test-plone-4.2.x.cfg buildout.cfg 
    (plonetheme.drupal) python bootstrap.py
	(plonetheme.drupal) bin/buildout
	[...] be patient... [...]
	(plonetheme.drupal) ./bin/instance fg

Go to http://localhost:8080, add a new Plone Site and install plonetheme.drupal

Launch tests::

	(plonetheme.drupal) ./bin/test -s plonetheme.drupal

Launch code coverage::

    (plonetheme.drupal) bin/coverage
    (plonetheme.drupal) bin/report
    And open with a browser htmlcov/index.html

Credits
-------

    * Sylvain Boureliou [sylvainb] - `GitHub <https://github.com/sylvainb>`_ - `Website <http://www.asilax.fr/>`_


Source code
-----------

`Source code <https://github.com/sylvainb/plonetheme.drupal>`_ is hosted on Github.

How to contribute and submit a patch ?
--------------------------------------

`Source code <https://github.com/sylvainb/plonetheme.drupal>`_ and an `issue tracker <https://github.com/sylvainb/plonetheme.drupal/issues>`_ is hosted on Github.



.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`plone.app.theming installation`: http://pypi.python.org/pypi/plone.app.theming/1.0#installation
.. _`Bartik`: https://drupal.org/documentation/themes/bartik

