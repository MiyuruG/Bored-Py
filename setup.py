from setuptools import setup, find_packages

setup(
    name='bored_activities',
    version='0.1.0',
    description='A package to fetch and display activities for when you are bored.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    url='http://panel2.mcboss.top:25569',
    packages=find_packages(),
    install_requires=[
        'requests',
        'discord.py'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
