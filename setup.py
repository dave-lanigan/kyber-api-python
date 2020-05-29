from setuptools import setup 

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    url="https://github.com/dave-lanigan/kyber-api-python",
    author="Daithi",
    author_email="dav.lanigan@gmail.com",
    name="kybernet",
    version="0.0.1",
    description="Unofficial python wrapper for Kyber Network API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["client"],
    packages=["kybernet"],
    classifiers=["Development Status :: 2 - Pre-Alpha",
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License"],
    python_requires=">=3.6",
    install_requires=["requests"],
    extras_require = {"dev": ["pytest>=3.5"]}
    )
