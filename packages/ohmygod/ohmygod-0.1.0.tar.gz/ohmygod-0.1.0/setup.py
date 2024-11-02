from setuptools import setup, find_packages

setup(
    name="ohmygod",
    version="0.1.0",
    description="Rich CLI tool powered by Buddha",
    author="aintbe",
    author_email="aint.imsorry@gmail.com",
    url="https://github.com/aintbe/ohmygod",
    install_requires=["rich", "colorama", "readchar"],
    packages=find_packages(exclude=[]),
    keywords=["ohmygod", "buddha", "cli", "console", "terminal", "rich"],
    python_requires=">=3.6",
    package_data={},
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
