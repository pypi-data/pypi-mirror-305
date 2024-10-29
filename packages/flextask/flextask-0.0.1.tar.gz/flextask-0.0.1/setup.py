import os
import sys
import re

from setuptools import find_packages, setup

try:
    from setuptools.command.install import install
except ImportError:
    from distutils.command.install import install

# Get version
current_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(current_path, "flextask", "__init__.py"), encoding="utf-8") as f:
    output = re.search(r'__version__ = ["\']([^"\']+)', f.read())

    if not output:
        raise ValueError("Error: can't find version in flextask/__init__.py")

    version = output.group(1)

class custom_install(install):
    def run(self):
        global dir_install_script

        install.run(self)

        # Check if this version is deprecated or has vulnerabilities! 
        import flextask.net

        r = flextask.net.request(
            {'get': {'action': 'get-flextask-version-notes-setup', 'version': version}})
        notes = r.get('dict', {}).get('notes','')
        if notes !='':
            print (notes)


############################################################
# Add all directories in "automations" to the distribution

root = 'flextask'

setup(
    name="flextask",

    author="Grigori Fursin",
    author_email="",

    version=version,

    description="TBD",

    license="Apache 2.0",

    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",

    url="",

    python_requires="", # do not force for testing

    packages=['flextask'],

    include_package_data=False,

    cmdclass={
        'install': custom_install
    },

    install_requires=['requests', 'setuptools'],

    entry_points={"console_scripts": [
                      "flextask = flextask.cli:run_flex_task",
                      "ft = flextask.cli:run_flex_task"
                     ]},

    zip_safe=False,

    keywords="flextask,ft,cli"
)
