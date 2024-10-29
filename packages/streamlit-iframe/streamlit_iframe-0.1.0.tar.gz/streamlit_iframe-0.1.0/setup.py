from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamlit_iframe",
    version="0.1.0",
    author="Manos Nikakis",
    author_email="scrtmanos@gmail.com",
    description="Render an HTML iframe within a Streamlit app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itdsntwork/streamlit-iframe",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ]
)
