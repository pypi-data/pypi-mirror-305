r'''
AWS CDK: A real-time S3 Protector

# P6CDKS3Protector

## LICENSE

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

## Other

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/p6m7g8/p6-cdk-s3-protector) ![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=p6m7g8_p6-cdk-s3-protector&metric=alert_status) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/p6m7g8/p6-cdk-s3-protector) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/p6m7g8/p6-cdk-s3-protector)

## Usage

```python
...
import { P6CDKS3Protector } from 'p6-cdk-s3-protector'

new P6CDKS3Protector(this, 'p6CDKS3Protector')
```

## Architecture

![./assets/diagram.png](./assets/diagram.png)

## Author

Philip M. Gollucci [pgollucci@p6m7g8.com](mailto:pgollucci@p6m7g8.com)
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class P6CDKS3Protector(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="p6-cdk-s3-protector.P6CDKS3Protector",
):
    def __init__(self, scope: _constructs_77d1e7e8.Construct, id: builtins.str) -> None:
        '''
        :param scope: -
        :param id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce547414fa284803b3db057f6ab48ad700c6434e37d461d01de2328612b013dd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [scope, id])


__all__ = [
    "P6CDKS3Protector",
]

publication.publish()

def _typecheckingstub__ce547414fa284803b3db057f6ab48ad700c6434e37d461d01de2328612b013dd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
