from setuptools import setup  # type: ignore

setup(
    name="landregistry-trace-id",
    version="0.9.9",
    author="Ian Harvey",
    author_email="ian.harvey@landregistry.gov.uk",
    packages=["landregistry.trace_id"],
    include_package_data=True,
    package_data={
        "landregistry.trace_id": ["py.typed"],
    },
    description="Tracability for HMLR applications",
    install_requires=["flask >= 2.2.2"],
    extras_require={},
    license="MIT",
    python_requires=">=3.9",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
