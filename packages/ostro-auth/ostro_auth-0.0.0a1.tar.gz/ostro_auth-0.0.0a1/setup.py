from setuptools import setup, find_namespace_packages

setup(
    name="ostro-auth",  # Adjust for each package (e.g., ostro-container)
    version="0.0.0a1",  # Alpha version
    description="Auth package for the Ostro project",
    packages=find_namespace_packages(include=["ostro.*"]),
    install_requires=[],
    python_requires=">=3.6",
)
