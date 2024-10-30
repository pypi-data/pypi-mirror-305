from setuptools import setup, find_packages

setup(
    name='pytimeliner',
    version='0.4.1.3',
    packages=find_packages(),
    install_requires=["googletrans==4.0.0-rc1"],
    author='nowte',
    author_email='developerahmet31@gmail.com',
    description='Create a timeline by listing events with multilingual support.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nowte/PyTimeliner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
