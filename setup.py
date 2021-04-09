import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DoggoMenus",
    version="1.0.0",
    author="Doggotaco",
    author_email="taromaruyuki@gmail.com",
    description="A basic console menu system for Python!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Taromaruu/WaifuLabs",
    install_requires=["py-getch"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)