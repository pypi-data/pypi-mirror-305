from setuptools import setup, find_packages

setup(
    name='financial_metrics',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Sofia',
    author_email='s.a.karpova@edu.centraluniversity.ru',
    description='Python package for calculating financial metrics.',
    url='https://github.com/your-username/financial_metrics',
    license='MIT',
    entry_points={
        'console_scripts': [
            'financial_metrics = financial_metrics.main:main',
        ],
    },
)