from setuptools import setup  # type: ignore[import]

setup(
    name="landregistry-exception-handlers",
    version="0.9.9",
    author="Ian Harvey",
    author_email="ian.harvey@landregistry.gov.uk",
    packages=["landregistry.exceptions"],
    include_package_data=True,
    package_data={
        "landregistry.exceptions": ["py.typed"],
    },
    description="Standardised exception handlers for HMLR Flask applications",
    install_requires=["flask >= 2.3.0", "werkzeug >= 2.3.0"],
    python_requires=">=3.9",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
