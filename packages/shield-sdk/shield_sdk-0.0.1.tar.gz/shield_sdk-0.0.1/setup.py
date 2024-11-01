from setuptools import setup, find_namespace_packages

setup(
    name="shield_sdk",
    version="0.0.1",
    author="Shield Team",
    author_email="cybersecurity.svc@bugcrowd.com",
    description="Namespace reservation package",
    long_description="This package reserves the namespace on PyPI",
    long_description_content_type="text/markdown",
    packages=['shield-sdk'],
    python_requires=">=3.9",
)