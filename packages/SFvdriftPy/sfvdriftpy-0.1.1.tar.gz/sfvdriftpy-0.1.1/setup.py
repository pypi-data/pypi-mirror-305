from setuptools import setup, find_packages

setup(
    name='SFvdriftPy',
    version='0.1.1',
    description="""Model for equatorial vertical drift based on paper published by Scherliess & Fejer.
                Refactored from sami2py development team.""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mateo Cardona Serrano (them)',
    author_email='mcardonaserrano@berkeley.edu',
    url='https://github.com/mcardonaserrano/SFvdriftPy',
    packages=find_packages(),
    include_package_data=True,
    package_data={'SFvdriftPy': ['data/*.txt']},
    install_requires=[
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
