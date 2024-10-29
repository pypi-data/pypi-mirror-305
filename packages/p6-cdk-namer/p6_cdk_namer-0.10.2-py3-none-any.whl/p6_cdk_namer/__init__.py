r'''
AWS CDK setups up a Custom Resource via Cloud Formation which sets the AWS IAM Account Alias

# P6Namer

## LICENSE

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

## Other

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/p6m7g8/p6-cdk-namer) ![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=p6m7g8_p6-cdk-namer&metric=alert_status) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/p6m7g8/p6-cdk-namer) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/p6m7g8/p6-cdk-namer)

## Usage

```python
...
import { P6Namer } from 'p6-cdk-namer';

new P6Namer(this, 'AccountAlias', {
  accountAlias: 'THE-ALIAS',
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


@jsii.interface(jsii_type="p6-cdk-namer.IP6NamerProps")
class IP6NamerProps(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="accountAlias")
    def account_alias(self) -> builtins.str:
        ...

    @account_alias.setter
    def account_alias(self, value: builtins.str) -> None:
        ...


class _IP6NamerPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "p6-cdk-namer.IP6NamerProps"

    @builtins.property
    @jsii.member(jsii_name="accountAlias")
    def account_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountAlias"))

    @account_alias.setter
    def account_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8a15ea187b2068c1581f9a7c6d837f0af19b386bb5a857f5041bb935df7ae32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountAlias", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IP6NamerProps).__jsii_proxy_class__ = lambda : _IP6NamerPropsProxy


class P6Namer(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="p6-cdk-namer.P6Namer",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: IP6NamerProps,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4322bd430d1c04062c0f00fed42f484077e7f11eb93e07f9a5739bc8d2a702d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [scope, id, props])


__all__ = [
    "IP6NamerProps",
    "P6Namer",
]

publication.publish()

def _typecheckingstub__d8a15ea187b2068c1581f9a7c6d837f0af19b386bb5a857f5041bb935df7ae32(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4322bd430d1c04062c0f00fed42f484077e7f11eb93e07f9a5739bc8d2a702d4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: IP6NamerProps,
) -> None:
    """Type checking stubs"""
    pass
