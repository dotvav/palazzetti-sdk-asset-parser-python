import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="palazzetti_sdk_asset_parser",
    version="1.0.2",
    author="Palazzetti Lelio Spa",
    author_email="info@palazzetti.it",
    description="IoT Device Capability Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/palazzetti/palazzetti-sdk-asset-parser-python",
    packages=setuptools.find_packages(),
    install_requires=[
        'protobuf',
        'semver',
        'six'
    ],
    python_requires='>=3.6',
    data_files=[('data', ['palazzetti_sdk_asset_parser/data/asset_parser.json'])]
)