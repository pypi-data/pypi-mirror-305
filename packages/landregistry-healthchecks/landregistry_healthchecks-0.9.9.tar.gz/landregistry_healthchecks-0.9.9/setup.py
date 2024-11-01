from setuptools import setup  # type: ignore

setup(
    name="landregistry-healthchecks",
    version="0.9.9",
    author="Ian Harvey",
    author_email="ian.harvey@landregistry.gov.uk",
    packages=["landregistry.healthchecks"],
    package_data={
        "landregistry.healthchecks": ["py.typed"],
    },
    include_package_data=True,
    description="Standardised health endpoints for HMLR Flask applications",
    install_requires=["flask >= 2.3.0", "requests >= 2.23.0"],
    python_requires=">=3.9",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
