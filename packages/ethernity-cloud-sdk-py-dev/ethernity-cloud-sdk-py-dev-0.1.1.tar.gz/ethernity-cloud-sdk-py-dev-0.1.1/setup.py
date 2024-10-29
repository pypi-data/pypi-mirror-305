from setuptools import setup, find_packages

setup(
    name="ethernity-cloud-sdk-py-dev",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "ethernity_cloud_sdk_py.templates": ["src/**/*", "public/**/*"],
    },
    install_requires=[
        "requests",
        "python-dotenv",
        "ipfshttpclient",
        "tqdm",
        "pyopenssl",
        "ethernity-cloud-runner-py-dev",
        # Add other dependencies here
    ],
    entry_points={
        "console_scripts": [
            "ecld-init=ethernity_cloud_sdk_py.cli:main_init",
            "ecld-build=ethernity_cloud_sdk_py.cli:main_build",
            "ecld-publish=ethernity_cloud_sdk_py.cli:main_publish",
        ],
    },
)
