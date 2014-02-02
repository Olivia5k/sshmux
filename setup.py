from setuptools import setup


setup(
    name='sshmux',
    version='0.0.1',
    author='Lowe Thiderman',
    author_email='lowe.thiderman@gmail.com',
    url='https://github.com/thiderman/sshmux',
    description='Quickfast tools for tmux and ssh',
    long_description=open('README.md').read(),
    packages=['sshmux'],
    zip_safe=False,
    license='MIT',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'sshmux = sshmux:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
)
