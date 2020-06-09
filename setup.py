from setuptools import setup, find_packages
# version = __import__("takeaway").__version__
from takeaway.core.utils.version import  VERSION
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="startapp",
    version=VERSION,
    include_package_data=True,
    packages=['takeaway', 'takeaway.script','takeaway.core.utils','takeaway.core','takeaway.settings','takeaway.controllers','takeaway.settings.flask','takeaway.settings.fastapi'],
    author="Tural Muradov, Sabuhi Shukurov",
    author_email="tural_m@hotmail.com, sabuhi.shukurov@gmail.com",
    description="Simple startapp for fastapi and flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/marlin-dev/startapp",
    install_requires=[
        "click"
    ],
    entry_points="""
        [console_scripts]
        startapp=takeaway.script.order:cli
    """,
    classifiers=[
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3 :: Only",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
)








