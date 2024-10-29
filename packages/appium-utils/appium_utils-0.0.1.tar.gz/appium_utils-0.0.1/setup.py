from setuptools import setup, find_packages

setup(
    name="appium_utils",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "selenium",
        'appium-python-client'
    ],
    author="Kim Kitae",
    author_email="daearcdo@kimkitae.com",
    description="Appium 테스트 자동화를 위한 유틸리티 패키지",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kimkitae/appium_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)

