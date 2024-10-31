r'''
DESC

# P6Stack

## LICENSE

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

## Other

![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod) ![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=p6m7g8_p6-template-cdk-construct-eslint-npm-ts-flatfile&metric=alert_status) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/p6m7g8/p6-template-cdk-construct-eslint-npm-ts-flatfile) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/p6m7g8/p6-template-cdk-construct-eslint-npm-ts-flatfile)

## Usage

```python
...
import { P6Stack } from 'p6-cdk-stack';

new P6Stack(this, 'P6Stack', {
});
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


@jsii.interface(jsii_type="p6-cdk-name.IP6Props")
class IP6Props(typing_extensions.Protocol):
    pass


class _IP6PropsProxy:
    __jsii_type__: typing.ClassVar[str] = "p6-cdk-name.IP6Props"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IP6Props).__jsii_proxy_class__ = lambda : _IP6PropsProxy


class P6Stack(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="p6-cdk-name.P6Stack",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        _props: IP6Props,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param _props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3914cca4370e359aae271890cc563911fcfcc0d1f965ba1bf3dc7d2f57552dbd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument _props", value=_props, expected_type=type_hints["_props"])
        jsii.create(self.__class__, self, [scope, id, _props])


__all__ = [
    "IP6Props",
    "P6Stack",
]

publication.publish()

def _typecheckingstub__3914cca4370e359aae271890cc563911fcfcc0d1f965ba1bf3dc7d2f57552dbd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    _props: IP6Props,
) -> None:
    """Type checking stubs"""
    pass
