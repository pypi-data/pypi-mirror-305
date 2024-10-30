from setuptools import setup, find_packages

setup(
    name='grz',
    version='1.2.0',
    description='This is a widget designed for openGauss Database inspection Tool!',
    author='RuiXu',
    author_email='ruixu@std.uestc.edu.cn',
    license='Mulan PSL v2',  # 或其他许可证
    packages=find_packages(where='src'),  # 查找 src 目录中的包
    package_dir={'': 'src'},  # 指定包的根目录
    entry_points={
        'console_scripts': [
            'grz=grz.grz:main',  # 将命令 `orz` 映射到 `orz/orz.py` 中的 `main` 函数
        ],
    },
    python_requires='>=3.6',  # Python 版本要求
)