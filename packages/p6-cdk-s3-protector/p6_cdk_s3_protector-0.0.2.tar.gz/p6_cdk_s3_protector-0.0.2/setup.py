import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "p6-cdk-s3-protector",
    "version": "0.0.2",
    "description": "AWS CDK: A Real-Time S3 Protector",
    "license": "Apache-2.0",
    "url": "https://github.com/p6m7g8/p6-cdk-s3-protector.git",
    "long_description_content_type": "text/markdown",
    "author": "Philip M. Gollucci<pgollucci@p6m7g8.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/p6m7g8/p6-cdk-s3-protector.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "p6_cdk_s3_protector",
        "p6_cdk_s3_protector._jsii"
    ],
    "package_data": {
        "p6_cdk_s3_protector._jsii": [
            "p6-cdk-s3-protector@0.0.2.jsii.tgz"
        ],
        "p6_cdk_s3_protector": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib==2.164.1",
        "constructs>=10.4.2, <11.0.0",
        "jsii>=1.104.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard>=2.13.3,<4.3.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
