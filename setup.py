import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wordtoken",
    version="0.0.1",
    author="Lemuel Uhuru",
    author_email="hello@wordtoken.com",
    description="Conversational Analytics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wordtoken/wordtoken",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)