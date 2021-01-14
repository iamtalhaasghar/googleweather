import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="googleweather",
    version="0.0.2",
    author="Talha Asghar",
    author_email="talhaasghar.contact@simplelogin.fr",
    description="Python CLI tool to scrap weather info from Google using http requests and custom user-agent",
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
    install_requires=["bs4", "requests"],
    scripts=["googleweather.py"]
	
)
