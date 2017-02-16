"""
Package config for selfie bot
"""
import setuptools

setuptools.setup(
    name='trans_girls_rule_the_world',
    version='3.0.1',
    description='A tumblr bot to reblog trans girl\'s selfies',
    url='https://github.com/Deafjams/trans_girls_rule_the_world',
    author='Emma Foster',
    license='Public Domain',
    install_requires=[
        'pytumblr>=0.0.6,<0.1.0',
        'emoji>=0.3,<1.0',
        'plan>=0.5,<1.0'
    ],
    package_dir={
        'trans_girls_rule_the_world': 'trans_girls_rule_the_world'
    },
    packages=setuptools.find_packages(),
    classifiers=(
        "Development Status :: 5 - Production",
        "License :: Public Domain",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7"
    )
)
