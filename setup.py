from setuptools import setup, find_packages

setup(
    name="gdork",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gdork=gdork.gdork:main',  # Adjust the import path for main
        ],
    },
    install_requires=[],  # Add any dependencies if needed
)
