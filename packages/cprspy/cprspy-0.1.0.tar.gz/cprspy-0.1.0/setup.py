from setuptools import setup, find_packages

setup(
    name='cprspy',
    version='0.1.0',
    description='Circle-Point-Round Source Pure Python Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='lbylzkx',
    author_email='lbylzkx@outlook.com',
    url='https://github.com/lbylzkx/Circle-Point-Round',
    packages=find_packages(),  # 自动找到项目中的所有包
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # 支持的 Python 版本
    install_requires=['numpy', 'matplotlib'],  # 如果有依赖库，列在这里
)
