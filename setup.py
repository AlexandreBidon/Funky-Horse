from distutils.core import setup
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'funky_horse',         # How you named your package folder (MyLib)
  packages = ['funky_horse'],   # Chose the same as "name"
  version = '1.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python-based fun avatar generator',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Alexandre Bidon',                   # Type in your name
  author_email = 'alexandre.bidon.44@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/AlexandreBidon/Funky-Horse',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/AlexandreBidon/Funky-Horse/archive/refs/tags/1.0.0.tar.gz',    # I explain this later on
  keywords = ['Funky', 'Horse', 'Avatar','svg','png','Generator','Vector'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'cairosvg',
      ],
  packages=setuptools.find_packages(),
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  include_package_data=True,
    package_data={
        setuptools.find_packages()[0]: ['assets/*.svg', 'assets/**/*.svg', 'assets/**/**/*.svg']
    },
)