from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import pathlib

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        subprocess.run(["python", "install.py"])

# 读取 README 文件内容
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.MD').read_text(encoding='utf-8')

setup(
    name='PandoraBox',
    version='1.2.0',
    packages=find_packages(),
    description='Pandora Box Is All You Need. You Can Create Python Environment, Execute Python, Close Python Environment Freely and Easily.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='pydaxing',
    author_email='pydaxing@gmail.com',
    url='https://github.com/pydaxing/PandoraBox',
    python_requires='>=3.6',  # 指定支持的最低 Python 版本
    entry_points={
        'console_scripts': [
            'pbox=pbox.app:main'
        ],
    },
    install_requires=[
        'requests',
        'anyio',
        'h11',
        'fastapi',
        'uvicorn',
        'pydantic',
        'jupyter-client',
        'ipython',
        'ipykernel',
        'pandas',
        'numpy',
        'matplotlib',
        'jsonlines',
    ],
    cmdclass={
        'install': CustomInstallCommand,
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
