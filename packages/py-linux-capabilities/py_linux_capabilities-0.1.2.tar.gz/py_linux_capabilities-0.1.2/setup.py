from setuptools import setup, find_packages

setup(
    name="linux_capabilities",
    version="0.1.2",
    description="A Python library providing an enumeration of Linux capabilities.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="damwiw",
    license="MIT",
    packages=find_packages(),
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    install_requires=[],
    url="https://github.com/damwiw/py-linux-capabilities",
)
