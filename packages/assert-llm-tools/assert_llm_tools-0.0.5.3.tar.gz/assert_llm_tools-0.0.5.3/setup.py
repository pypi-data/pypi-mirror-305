from setuptools import setup, find_packages

setup(
    name="assert-llm-tools",
    # ... other setup parameters ...
    packages=find_packages(),
    package_data={"": ["*.py"]},
    include_package_data=True,
)
