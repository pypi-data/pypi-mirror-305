from setuptools import setup, find_packages

setup(
    name="cpp_source_extractor",
    version="0.1",
    packages=find_packages(),
    author="Wenxuan Shi",
    author_email="wenxuan.shi@northwestern.edu",
    description="A python library for extracting C++ function implementations from source code",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/whexy/cpp_source_extractor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["libclang"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="tests",
)
