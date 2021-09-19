"""
    Bundesagentur für Arbeit: Jobsuche API

    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. <br><br> Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:<br><br> **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a <br> **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "jobsuche"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Bundesagentur für Arbeit: Jobsuche API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Bundesagentur für Arbeit: Jobsuche API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    Die größte Stellendatenbank Deutschlands durchsuchen, Details zu Stellenanzeigen und Informationen über Arbeitgeber abrufen. &lt;br&gt;&lt;br&gt; Die Authentifizierung funktioniert per OAuth 2 Client Credentials mit JWTs. Folgende Client-Credentials können dafür verwendet werden:&lt;br&gt;&lt;br&gt; **ClientID:** c003a37f-024f-462a-b36d-b001be4cd24a &lt;br&gt; **ClientSecret:** 32a39620-32b3-4307-9aa1-511e3d7f48a8  # noqa: E501
    """
)
