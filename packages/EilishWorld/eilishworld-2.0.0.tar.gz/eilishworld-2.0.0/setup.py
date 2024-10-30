import setuptools
 
with open("README.md", "r") as f:
    long_description = f.read()
 
setuptools.setup(
    name="EilishWorld",  # Replace with your package name
    version="2.0.0",  # Replace with your package version
    author="Mbali Phama",  # Replace with your name
    author_email="mbaliphama8@gmail.com",  # Replace with your email
    description="This is just a nice experiment. And it works well.",  # Brief package description
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