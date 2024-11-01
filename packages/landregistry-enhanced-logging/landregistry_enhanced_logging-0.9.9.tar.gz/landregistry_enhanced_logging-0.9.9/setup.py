from setuptools import setup  # type: ignore

setup(
    name="landregistry-enhanced-logging",
    version="0.9.9",
    author="Ian Harvey",
    author_email="ian.harvey@landregistry.gov.uk",
    packages=["landregistry.enhanced_logging", "landregistry.enhanced_logging.stubs"],
    include_package_data=True,
    package_data={
        "landregistry.enhanced_logging": ["py.typed"],
    },
    description="Standardised logging configuration for HMLR applications",
    install_requires=[],
    extras_require={
        "flask": ["flask >= 2.2.0", "landregistry-trace-id >= 1.0.0"],
        "kombu": ["kombu >= 5.0.0"],
    },
    license="MIT",
    python_requires=">=3.9",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
