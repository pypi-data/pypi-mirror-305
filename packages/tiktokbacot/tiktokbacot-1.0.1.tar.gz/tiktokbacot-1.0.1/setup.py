from setuptools import setup, find_packages

setup(
    name='tiktokbacot',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    description='Paket untuk mengubah teks menjadi suara dengan API TikTok',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tigrilminnada/tiktokbacot',
    author='masanto',
    author_email='seller.digitalocean@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)