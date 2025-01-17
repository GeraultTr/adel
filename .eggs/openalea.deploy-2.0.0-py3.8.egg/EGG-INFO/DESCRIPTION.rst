========================
openalea.deploy
========================

.. {# pkglts, doc


.. image:: https://badge.fury.io/py/openalea.deploy.svg
    :alt: PyPI version
    :target: https://badge.fury.io/py/openalea.deploy

.. #}

OpenAlea.Deploy support the installation of OpenAlea packages via the network and manage their dependencies. It is an extension of Setuptools. 

**Authors** : S. Dufour-Kowalski, C. Pradal

**Contributors** : OpenAlea Consortium

**Institutes** : INRIA/CIRAD/INRA

**Type** : Pure Python package

**Status** : Devel

**License** : CeCILL-C


About
------

OpenAlea.Deploy support the installation of OpenAlea packages via the network and manage
their dependencies .
It is an extension of Setuptools_.



**Additional Features** :
   * Discover and manage packages in EGG format
   * Declare shared libraries directory and include directories
   * Call SCons scripts
   * Create namespaces if necessary
   * Support post_install scripts
   * Support 'develop' command
   * OpenAlea GForge upload

It doesn't include any GUI interface (See [[packages:compilation_installation:deploygui:deploygui|OpenAlea.DeployGui]] for that).

Requirements
-------------

  * Python_ <= 2.7
  * Setuptools_

Download
---------

See the [[:download|Download page]].

Installation
-------------

  python setup.py install

.. note::

  OpenAlea.Deploy can be automatically installed with the *alea_setup.py* script.


.. _Setuptools: http://pythonhosted.org/setuptools
.. _Python: http://www.python.org


Developper Documentation
-------------------------

To distribute your package with OpenAlea.Deploy, you need to write a setup.py script
as you do with setuptools.

  * have a look to the Setuptools_ developer's guide.
  * OpenAlea.Deploy add a numerous of keywords and commands

Setup keywords
###############

  * create_namespace = [True|False] : if **True** create the namespaces in *namespace_packages*
  * scons_scripts = [list of Scons scripts] : if not empty, call scons to build extensions
  * scons_parameters = [list of Scons parameters] : such as ``build_prefix=...``
  * postinstall_scripts = [list of strings] : Each string corresponds to a python module to execute at installation time. The module may contain a install function ``def install():``.
  * inc_dirs = {dict of dest_dir:src_dir} : Dictionary to map the directory containing the header files.
  * lib_dirs = {dict of dest_dir:src_dir} : Dictionary to map the directory containing the dynamic libraries to share.
  * share_dirs = {dict of dest_dir:src_dir} : Dictionary to map the directory containing shared data.

Additional setup.py commands
#############################

   * *create_namespace* : create_namespace declared in *namespace_packages*, usage : ``python setup.py create_namespace``.
   * *scons* : call scons scripts, usage : ``python setup.py scons``.
   * *alea_install* : wrap easy_install command, usage : ``python setup.py alea_install``.
   * *alea_upload* : upload distribution forge on the openalea gforge

For more information see : ``python setup.py --help-commands``

Setup.py example
#################

::

    import sys
    import os
    from setuptools import setup, find_packages
    from os.path import join as pj

    build_prefix = "build-scons"

    # Setup function
    setup(
        name = "OpenAlea.FakePackage",
        version = "0.1",
        author = "Me",
        author_email = "me@example.com",
        description = "This is an Example Package",
        license = 'GPL',
        keywords = 'fake',
        url = 'http://myurl.com',

        # Scons
        scons_scripts = ["SConstruct"],
        scons_parameters = ["build_prefix=%s"%(build_prefix)],

        # Packages
        namespace_packages = ["openalea"],
        create_namespaces = True,
        packages = ['openalea.fakepackage', ],

        package_dir = {
                    'openalea.fakepackage':  pj('src','fakepackage'),
                    '' : 'src',  # necessary to use develop command
                      },
        include_package_data = True,
        zip_safe= False,

        # Specific options of openalea.deploy
        lib_dirs = { 'lib' : pj(build_prefix, 'lib'), },
        inc_dirs = { 'include' : pj(build_prefix, 'include') },
        share_dirs = { 'share' : 'share' },
        postinstall_scripts = ['openalea.fakepackage.postinstall',],

        # Scripts
        entry_points = { 'console_scripts': [
                               'fake_script = openalea.fakepackage.amodule:console_script', ],
                         'gui_scripts': [
                               'fake_gui = openalea.fakepackage.amodule:gui_script',]},

        # Dependencies
        setup_requires = ['openalea.deploy'],
        dependency_links = ['http://openalea.gforge.inria.fr/pi'],
        #install_requires = [],

    )








OpenAlea.Deploy 2.0.0
---------------------

- add VirtualEnv and Conda compatibility and detection

OpenAlea.Deploy 0.9.0
---------------------

- add bdist_rpm  options

OpenAlea.Deploy 0.8.0
---------------------

**Revision 2194**

- add add_plat_name option in setuptools
- Add Sphinx documentation in ./doc and update the setup.cfg accordingly

OpenAlea.Deploy 0.7.0
---------------------

**Revision xxxx**

- add pylint option in setuptools
- add sphinx_upload option in setuptools
- add DYLD_LIBRARY_PATH to deploy config file
- update documentation
	- Fixes docstrings to make them compatible with sphinx, or have a nicer output
	- fixes indentation issues in binary_deps and gforge_utils
	- fixes coding conventions
	- a few typos
	- remove some warnings
	- Fixed bad indentation

OpenAlea.Deploy 0.6.2
---------------------

**Revision 1575**

- add clean command to incorporate scons into setup.py
- Port to Mac
- Fix documentation (docstrings) to remove warnings in epydoc:
	http://openalea.gforge.inria.fr/doc/deploy-0.6.0/
- Fix tests
- Upgrade setuptools to 0.6c9
- Fix PATH problem on Windows to take into account OpenAlea libraries.
- Version are now compared with pkg_resources

OpenAlea.Deploy 0.4.12
----------------------
- Fix PATH problem on Windows to take into account OpenAlea libraries.

OpenAlea.Deploy 0.4.11
----------------------
- Fix version comparison by using parse_version rather than lexical cmp.

OpenAlea.Deploy 0.4.9
---------------------
- add binary dependency declaration in binray_deps.py

OpenAlea.Deploy 0.4.8
---------------------
- Fix upload for big files

OpenAlea.Deploy 0.4.7
---------------------
- Add remove_package and remove_release in gforge.py

OpenAlea.Deploy 0.4.6
---------------------
- Add get_metainfo function

OpenAlea.Deploy 0.4.5
---------------------
- Fix alea_clean Bug (remove all site-package)

OpenAlea.Deploy 0.4.4
---------------------
- Fix bug with os.environ['PATH'] under windows

OpenAlea.Deploy 0.4.3
---------------------
- Fix bug with namespace creation and complex __init__.py

OpenAlea.Deploy 0.4.2
---------------------
- Add <alea_upload> command (GForge upload)
- Add gforge module (SOAP communication)
- Fix dyn-lib bug with virtual env and with relative path
- Add option to alea_config to print dyn-lib

OpenAlea.Deploy 0.4.1
---------------------
- Fix bug with <develop> command and namespaces

OpenAlea.Deploy 0.4.0
---------------------
- Improve <develop> command : manage namespace and environment variables
- Reinstall shared libraries if they are missing (but not egm)
- Add shell command : alea_clean, alea_config and alea_update
- Based on setuptools-0.6c8

OpenAlea.Deploy 0.3.8
---------------------
- Adapt develop command for lib_dir and bin_dir

OpenAlea.Deploy 0.3.7
---------------------
- Simplify the warning message for environment variable on Linux

OpenAlea.Deploy 0.3.6
---------------------
- add get_recommended_pkg functions

OpenAlea.Deploy 0.3.5
---------------------
- add alea_clean and alea_update_all scripts

OpenAlea.Deploy 0.3.4a
----------------------
- Fix platform detection for darwin

OpenAlea.Deploy 0.3.3
---------------------
- Execute build_ext before build_py

OpenAlea.Deploy 0.3.2
---------------------
- Manage a list of web repository

OpenAlea.Deploy 0.3
-------------------
- Manage a directory of shared lib



