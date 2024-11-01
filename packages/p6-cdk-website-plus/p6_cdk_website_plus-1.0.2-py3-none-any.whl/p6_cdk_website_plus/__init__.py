r'''
AWS CDK: R53 -> CF -> S3

# P6CDKWebsitePlus

## LICENSE

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

## Other

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/p6m7g8/p6-cdk-website-plus) ![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=p6m7g8_p6-cdk-website-plus&metric=alert_status) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/p6m7g8/p6-cdk-website-plus) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/p6m7g8/p6-cdk-website-plus)

## Usage

```python
...
import { P6CDKWebsitePlus } from 'p6-cdk-website-plus';

new P6CDKWebsitePlus(this, 'WebsiteName', {
  hostedZoneName: 'gollucci.com',
  verifyEmail: 'pgollucci@p6m7g8.com',
  cloudfrontRecordName: 'www.gollucci.com',
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


@jsii.interface(jsii_type="p6-cdk-website-plus.IP6CDKWebsiteProps")
class IP6CDKWebsiteProps(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="cloudfrontRecordName")
    def cloudfront_record_name(self) -> builtins.str:
        ...

    @cloudfront_record_name.setter
    def cloudfront_record_name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> builtins.str:
        ...

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="verifyEmail")
    def verify_email(self) -> builtins.str:
        ...

    @verify_email.setter
    def verify_email(self, value: builtins.str) -> None:
        ...


class _IP6CDKWebsitePropsProxy:
    __jsii_type__: typing.ClassVar[str] = "p6-cdk-website-plus.IP6CDKWebsiteProps"

    @builtins.property
    @jsii.member(jsii_name="cloudfrontRecordName")
    def cloudfront_record_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cloudfrontRecordName"))

    @cloudfront_record_name.setter
    def cloudfront_record_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0d57a114cdba39939c7a16ad9eaee8acaa8c932f9f5418cc33d2659c404962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudfrontRecordName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneName"))

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6baa456ea90b3f639a7901f57bf31afb56eb2e43781dfe4bc2250d714fa0b7c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="verifyEmail")
    def verify_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verifyEmail"))

    @verify_email.setter
    def verify_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3c8a929e50db03bcddb1c26e29efe3b74e97399271ac3a96597c8ff47b9dd12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifyEmail", value) # pyright: ignore[reportArgumentType]

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IP6CDKWebsiteProps).__jsii_proxy_class__ = lambda : _IP6CDKWebsitePropsProxy


class P6CDKWebsitePlus(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="p6-cdk-website-plus.P6CDKWebsitePlus",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: IP6CDKWebsiteProps,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40d8d151df2a9a330d70ded3d9afc8fb6100746acb7220be196cf1a799ddc50c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [scope, id, props])


__all__ = [
    "IP6CDKWebsiteProps",
    "P6CDKWebsitePlus",
]

publication.publish()

def _typecheckingstub__3a0d57a114cdba39939c7a16ad9eaee8acaa8c932f9f5418cc33d2659c404962(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6baa456ea90b3f639a7901f57bf31afb56eb2e43781dfe4bc2250d714fa0b7c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c8a929e50db03bcddb1c26e29efe3b74e97399271ac3a96597c8ff47b9dd12(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d8d151df2a9a330d70ded3d9afc8fb6100746acb7220be196cf1a799ddc50c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: IP6CDKWebsiteProps,
) -> None:
    """Type checking stubs"""
    pass
