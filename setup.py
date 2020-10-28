# coding=utf-8
import setuptools
from setuptools import setup
 
setup(
    name='trump_db_pgsql',  # 应用名
    version='2.0.1',  # 版本号
    author="kangkang",
    author_email="kangkang0517@gmail.com",
    description="trump 的 PostgreSQL 支持",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="GPL",
    url="http://git.io.gsjna.com/jna/trump_db_pgsql",
    packages=setuptools.find_packages(),
    install_requires=[
        "asyncpg",
        "pytz",
    ],
    classifiers=[
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
)
