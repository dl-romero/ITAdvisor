import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="itadvisor-dromero",
    version="0.0.1",
    author="David Romero",
    author_email="dl_romero@outlook.com",
    description="Schneider Electric's ITAdvisor API Client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dromero.dev/index.php",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)