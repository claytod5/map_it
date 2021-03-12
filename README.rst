=======
Map it!
=======


Copy an address/location to your clipboard and search it on an online map provider


* Free software: MIT license


Features
--------

* Multiple map providers supported
        * Google Maps
        * Map Quest
        * Bing Maps
* Multiple browsers supported
        * Firefox
        * Chromium

Usage
-----
::

       $ map_it --help
       usage: map_it [-h] [-p {google_maps,map_quest,bing_maps}] [-b {chromium,firefox}]

       Search an address/location you have copied to your clipboard on an online map provider

       optional arguments:
         -h, --help            show this help message and exit
         -p {google_maps,map_quest,bing_maps}, --provider {google_maps,map_quest,bing_maps}
                               An online map provider
         -b {chromium,firefox}, --browser {chromium,firefox}
                               An executable webbrowser


       

        
Installation
------------

OS: Linux

Installing with pipx from Github::

        pipx install git+https://www.github.com/claytod5/map_it

Installing with pip from Github::

        pip install git+https://www.github.com/claytod5/map_it


Recommended Setup
-----------------

To make things quick and efficient, you can set up a keyboard shortcut to invoke the program after you copy something to your clipboard. Ths avoids having to copy something, open a terminal, and invoke the command.

Using your Linux distro of choice, you can use the following command (as an example)::

        bash -i -c "map_it"

Credits
-------
This project was inspired by a project idea in "Automate the Boring Stuff with Python" by Al Sweigart.

This package was created with Cookiecutter_ and based on the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
