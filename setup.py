from distutils.core import setup
import version


setup(name='color_helpers',
      version=version.getVersion(),
      description='Utility functions and classes for color maps.',
      keywords='color colormap',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='http://github.com/cfobel/color_helpers.git',
      license='GPL',
      packages=['color_helpers'])
