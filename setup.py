import setuptools

setuptools.setup(
    name='amalgam_python_sdk',
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
        'pyjwt',
        'requests',
        'cryptography',
        'kazoo',
        'PyYAML==5.3'
    ],
    entry_points={
        'console_scripts': [
            'sentry = sentry:cli',
        ],
    },
    version='0.2',
    author="Yeremia Andi Irawan",
    author_email="yeremia.ai@gmail.com",
    description="AccelByte Amalgam Python SDK",
    url="https://github.com/accelbyte/amalgam-python-sdk",
    classifiers=[],
)
