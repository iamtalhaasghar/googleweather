import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.5"
setuptools.setup(
    name="googleweather",
    version=__version__,
    author="Talha Asghar",
    author_email="talhaasghar.contact@simplelogin.fr",
    description="A simple Python CLI tool using which you can see current weather of any city (in the world) in your Terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamtalhaasghar/googleweather",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[i for i in open('requirements.txt').readlines() if len(i) != 0],
    entry_points={'console_scripts': ['gw = googleweather:googleweather.main']}
	
)
