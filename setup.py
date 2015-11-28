# Copyright (C) 2015 Bitquant Research Laboratories (Asia) Limited
# Released under the Simplified BSD License

from setuptools import (
    setup,
    find_packages,
    )

setup(
    name="ethercalc-python",
    version = "0.0.3",
    author="Joseph C Wang",
    author_email='joequant@gmail.com',
    url="https://github.com/joequant/ethercalc-python",
    description="A python API to ethercalc",
    long_description="""A python wrapper around ethercalc API""",
    license="BSD",
    packages=['ethercalc'],
    install_requires = ['requests'],
    use_2to3 = True
)
                                
