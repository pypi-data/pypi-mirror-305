import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easypythdb",  # Unikalna nazwa pakietu na PyPI
    version="0.1.0",  # Wersja Twojej biblioteki
    author="kserafin17",
    author_email="twoj.email@example.com",
    description="A super simple database manager with powerful features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/twoj-uzytkownik/easypydb",  # Link do repozytorium
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Zmień w zależności od wybranej licencji
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],  # Wymień zależności, jeśli istnieją
    include_package_data=True,  # Uwzględnij pliki z MANIFEST.in
)
