import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="fispkg",  # Replace with your package name
    version="1.0.0",  # Replace with your package version
    author="Baholo Mokoena",  # Replace with your name
    author_email="baholom@mindworx.co.za",  # Replace with your email
    description="This is just a nice experiment",  # Brief package description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-repo",  # Replace with your repo URL
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[],  # List dependencies here
    python_requires=">=3.8",  # Specify Python version requirement
)