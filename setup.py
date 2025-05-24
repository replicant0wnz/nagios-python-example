import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="http_cluster",
    version=os.environ['BUILD_VERSION'],
    author="Glenn E. Bailey III",
    author_email="glenn@dronemusic.co",
    description="Example Nagios plugin",
    install_requires=[''],
    license_files=['LICENSE'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/replicant0wnz/nagios-python-example",
    project_urls={
        "Bug Tracker": "https://github.com/replicant0wnz/nagios-python-example/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
