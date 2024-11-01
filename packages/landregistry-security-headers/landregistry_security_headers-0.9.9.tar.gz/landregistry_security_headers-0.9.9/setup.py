from setuptools import setup  # type: ignore

setup(
    name="landregistry-security-headers",
    version="0.9.9",
    author="Ian Harvey",
    author_email="ian.harvey@landregistry.gov.uk",
    packages=["landregistry.security_headers"],
    include_package_data=True,
    package_data={
        "landregistry.security_headers": ["py.typed"],
    },
    description="Standardised exception security related HTTP headers for HMLR Flask applications",
    install_requires=["flask >= 2.2.0"],
    python_requires=">=3.9",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
