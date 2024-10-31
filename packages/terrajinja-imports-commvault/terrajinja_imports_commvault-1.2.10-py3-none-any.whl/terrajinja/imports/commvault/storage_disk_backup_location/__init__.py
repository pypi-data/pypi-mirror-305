'''
# `commvault_storage_disk_backup_location`

Refer to the Terraform Registry for docs: [`commvault_storage_disk_backup_location`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class StorageDiskBackupLocation(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocation",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location commvault_storage_disk_backup_location}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        backuplocation: builtins.str,
        mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationMediaagent", typing.Dict[builtins.str, typing.Any]]]],
        storagepoolid: jsii.Number,
        access: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        savedcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationSavedcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location commvault_storage_disk_backup_location} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backuplocation: The mount path on the media agent where the data is to be backed up. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#backuplocation StorageDiskBackupLocation#backuplocation}
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#mediaagent StorageDiskBackupLocation#mediaagent}
        :param storagepoolid: Id of the disk storage to update. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#storagepoolid StorageDiskBackupLocation#storagepoolid}
        :param access: The access type for the access path can be either read (writing to path not allowed) or read and write (writing to path allowed). [READ_AND_WRITE, READ] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#access StorageDiskBackupLocation#access}
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#configuration StorageDiskBackupLocation#configuration}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#credentials StorageDiskBackupLocation#credentials}
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#enabled StorageDiskBackupLocation#enabled}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param savedcredentials: savedcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#savedcredentials StorageDiskBackupLocation#savedcredentials}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d0f076a299c4527882a3e947da8c33cea87afb085a231cbdf44e909a0946e3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageDiskBackupLocationConfig(
            backuplocation=backuplocation,
            mediaagent=mediaagent,
            storagepoolid=storagepoolid,
            access=access,
            configuration=configuration,
            credentials=credentials,
            enabled=enabled,
            id=id,
            savedcredentials=savedcredentials,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a StorageDiskBackupLocation resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the StorageDiskBackupLocation to import.
        :param import_from_id: The id of the existing StorageDiskBackupLocation that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the StorageDiskBackupLocation to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742511e5d8581b50c9d9b0cbdfe116a5e541c6969e711392b3d7afcc55515563)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationConfiguration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad3ca1bf8066d7446d029016d99e5475ee6e50e4e393bb705dcf00ff777626d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationCredentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca1d455f027da3e2bfd26bed16cd6f4fadbd417053c1e9ab07833f832cd5f45d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putMediaagent")
    def put_mediaagent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationMediaagent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af80f2eb825bfdf1882cee398d005e50a965b0e1189234b712fc4ee6eee08d37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMediaagent", [value]))

    @jsii.member(jsii_name="putSavedcredentials")
    def put_savedcredentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationSavedcredentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42bde4f7d6b6ff574e2675e4267ddd304dc599f04201540985bebd02a567ad86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSavedcredentials", [value]))

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSavedcredentials")
    def reset_savedcredentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSavedcredentials", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> "StorageDiskBackupLocationConfigurationList":
        return typing.cast("StorageDiskBackupLocationConfigurationList", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "StorageDiskBackupLocationCredentialsList":
        return typing.cast("StorageDiskBackupLocationCredentialsList", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="mediaagent")
    def mediaagent(self) -> "StorageDiskBackupLocationMediaagentList":
        return typing.cast("StorageDiskBackupLocationMediaagentList", jsii.get(self, "mediaagent"))

    @builtins.property
    @jsii.member(jsii_name="savedcredentials")
    def savedcredentials(self) -> "StorageDiskBackupLocationSavedcredentialsList":
        return typing.cast("StorageDiskBackupLocationSavedcredentialsList", jsii.get(self, "savedcredentials"))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="backuplocationInput")
    def backuplocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backuplocationInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationConfiguration"]]], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationCredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationCredentials"]]], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mediaagentInput")
    def mediaagent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationMediaagent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationMediaagent"]]], jsii.get(self, "mediaagentInput"))

    @builtins.property
    @jsii.member(jsii_name="savedcredentialsInput")
    def savedcredentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationSavedcredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationSavedcredentials"]]], jsii.get(self, "savedcredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="storagepoolidInput")
    def storagepoolid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storagepoolidInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "access"))

    @access.setter
    def access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83c528a0f3be49025fa98f66359c6b822869b5ba7f81bf6ea5604caabc156e99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="backuplocation")
    def backuplocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backuplocation"))

    @backuplocation.setter
    def backuplocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fde1d6a1eab2a79da8193746ec6748afaa3b70694bf88c886905a2c1c3d56e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backuplocation", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e5cffcf30341f374eb0dbfc93eaeef2dba0c84e002efd46c0b30dfd3eea8a5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07092ae0eddb5cfac566afbc851e522d5703a19d24a628965ce31c685e6b2e82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="storagepoolid")
    def storagepoolid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "storagepoolid"))

    @storagepoolid.setter
    def storagepoolid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85438486235cba133ab12fdfc2de01acf64441553325bcd592be9e1577fddb29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagepoolid", value)


@jsii.data_type(
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backuplocation": "backuplocation",
        "mediaagent": "mediaagent",
        "storagepoolid": "storagepoolid",
        "access": "access",
        "configuration": "configuration",
        "credentials": "credentials",
        "enabled": "enabled",
        "id": "id",
        "savedcredentials": "savedcredentials",
    },
)
class StorageDiskBackupLocationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        backuplocation: builtins.str,
        mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationMediaagent", typing.Dict[builtins.str, typing.Any]]]],
        storagepoolid: jsii.Number,
        access: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationConfiguration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        savedcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageDiskBackupLocationSavedcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backuplocation: The mount path on the media agent where the data is to be backed up. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#backuplocation StorageDiskBackupLocation#backuplocation}
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#mediaagent StorageDiskBackupLocation#mediaagent}
        :param storagepoolid: Id of the disk storage to update. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#storagepoolid StorageDiskBackupLocation#storagepoolid}
        :param access: The access type for the access path can be either read (writing to path not allowed) or read and write (writing to path allowed). [READ_AND_WRITE, READ] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#access StorageDiskBackupLocation#access}
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#configuration StorageDiskBackupLocation#configuration}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#credentials StorageDiskBackupLocation#credentials}
        :param enabled: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#enabled StorageDiskBackupLocation#enabled}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param savedcredentials: savedcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#savedcredentials StorageDiskBackupLocation#savedcredentials}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b9091e79332e18a4b3b6b798b45fc138a470a04d44a0064bcda91292e53267c)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backuplocation", value=backuplocation, expected_type=type_hints["backuplocation"])
            check_type(argname="argument mediaagent", value=mediaagent, expected_type=type_hints["mediaagent"])
            check_type(argname="argument storagepoolid", value=storagepoolid, expected_type=type_hints["storagepoolid"])
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument savedcredentials", value=savedcredentials, expected_type=type_hints["savedcredentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backuplocation": backuplocation,
            "mediaagent": mediaagent,
            "storagepoolid": storagepoolid,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if access is not None:
            self._values["access"] = access
        if configuration is not None:
            self._values["configuration"] = configuration
        if credentials is not None:
            self._values["credentials"] = credentials
        if enabled is not None:
            self._values["enabled"] = enabled
        if id is not None:
            self._values["id"] = id
        if savedcredentials is not None:
            self._values["savedcredentials"] = savedcredentials

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def backuplocation(self) -> builtins.str:
        '''The mount path on the media agent where the data is to be backed up.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#backuplocation StorageDiskBackupLocation#backuplocation}
        '''
        result = self._values.get("backuplocation")
        assert result is not None, "Required property 'backuplocation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mediaagent(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationMediaagent"]]:
        '''mediaagent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#mediaagent StorageDiskBackupLocation#mediaagent}
        '''
        result = self._values.get("mediaagent")
        assert result is not None, "Required property 'mediaagent' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationMediaagent"]], result)

    @builtins.property
    def storagepoolid(self) -> jsii.Number:
        '''Id of the disk storage to update.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#storagepoolid StorageDiskBackupLocation#storagepoolid}
        '''
        result = self._values.get("storagepoolid")
        assert result is not None, "Required property 'storagepoolid' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def access(self) -> typing.Optional[builtins.str]:
        '''The access type for the access path can be either read (writing to path not allowed) or read and write (writing to path allowed).

        [READ_AND_WRITE, READ]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#access StorageDiskBackupLocation#access}
        '''
        result = self._values.get("access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationConfiguration"]]]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#configuration StorageDiskBackupLocation#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationConfiguration"]]], result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationCredentials"]]]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#credentials StorageDiskBackupLocation#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationCredentials"]]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#enabled StorageDiskBackupLocation#enabled}.'''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def savedcredentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationSavedcredentials"]]]:
        '''savedcredentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#savedcredentials StorageDiskBackupLocation#savedcredentials}
        '''
        result = self._values.get("savedcredentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageDiskBackupLocationSavedcredentials"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageDiskBackupLocationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "disablebackuplocationforfuturebackups": "disablebackuplocationforfuturebackups",
        "enablebackuplocation": "enablebackuplocation",
        "prepareforretirement": "prepareforretirement",
    },
)
class StorageDiskBackupLocationConfiguration:
    def __init__(
        self,
        *,
        disablebackuplocationforfuturebackups: typing.Optional[builtins.str] = None,
        enablebackuplocation: typing.Optional[builtins.str] = None,
        prepareforretirement: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disablebackuplocationforfuturebackups: Used to determine if backup location has to be disabled or enabled for future backups. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#disablebackuplocationforfuturebackups StorageDiskBackupLocation#disablebackuplocationforfuturebackups}
        :param enablebackuplocation: Used to enable or disable backup location. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#enablebackuplocation StorageDiskBackupLocation#enablebackuplocation}
        :param prepareforretirement: Used to determine if the backup location has to be prepared for retirement. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#prepareforretirement StorageDiskBackupLocation#prepareforretirement}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd645b8237aeb47d0020c23b87b96337737002feb1afd0b23b576577a84e58a3)
            check_type(argname="argument disablebackuplocationforfuturebackups", value=disablebackuplocationforfuturebackups, expected_type=type_hints["disablebackuplocationforfuturebackups"])
            check_type(argname="argument enablebackuplocation", value=enablebackuplocation, expected_type=type_hints["enablebackuplocation"])
            check_type(argname="argument prepareforretirement", value=prepareforretirement, expected_type=type_hints["prepareforretirement"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disablebackuplocationforfuturebackups is not None:
            self._values["disablebackuplocationforfuturebackups"] = disablebackuplocationforfuturebackups
        if enablebackuplocation is not None:
            self._values["enablebackuplocation"] = enablebackuplocation
        if prepareforretirement is not None:
            self._values["prepareforretirement"] = prepareforretirement

    @builtins.property
    def disablebackuplocationforfuturebackups(self) -> typing.Optional[builtins.str]:
        '''Used to determine if backup location has to be disabled or enabled for future backups.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#disablebackuplocationforfuturebackups StorageDiskBackupLocation#disablebackuplocationforfuturebackups}
        '''
        result = self._values.get("disablebackuplocationforfuturebackups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enablebackuplocation(self) -> typing.Optional[builtins.str]:
        '''Used to enable or disable backup location.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#enablebackuplocation StorageDiskBackupLocation#enablebackuplocation}
        '''
        result = self._values.get("enablebackuplocation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prepareforretirement(self) -> typing.Optional[builtins.str]:
        '''Used to determine if the backup location has to be prepared for retirement.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#prepareforretirement StorageDiskBackupLocation#prepareforretirement}
        '''
        result = self._values.get("prepareforretirement")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageDiskBackupLocationConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageDiskBackupLocationConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationConfigurationList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbaba8816c7ab7700ef756e91e6082ccaaa59f146df1e8b9667612a8e69f73c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageDiskBackupLocationConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f851e02251056183932e372fc359f4d32aa5f01dd8a6d06e68d3fd652ea21008)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageDiskBackupLocationConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40f5e3b9ee2afaf4e7ccd45c36fb9edbc7c4a16c103b1a51c6fe904d656a63a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17cc28c25e7d40be462591f46c215aa33f0e4bc3188c95ef27d35dd1df5e87f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38b98d277774ccf343d3f5a847b9648ecf2bfcb6757ca3723e58fffe7e58bc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b56920e202137bdf78086cbb9ffe99096a514eef2bd8daf052534d5c13690b44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageDiskBackupLocationConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1552f415778c3182d2c7956fe7b03acd8f68b22e73c7c8d16dae254a9d32eccd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisablebackuplocationforfuturebackups")
    def reset_disablebackuplocationforfuturebackups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablebackuplocationforfuturebackups", []))

    @jsii.member(jsii_name="resetEnablebackuplocation")
    def reset_enablebackuplocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablebackuplocation", []))

    @jsii.member(jsii_name="resetPrepareforretirement")
    def reset_prepareforretirement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrepareforretirement", []))

    @builtins.property
    @jsii.member(jsii_name="disablebackuplocationforfuturebackupsInput")
    def disablebackuplocationforfuturebackups_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disablebackuplocationforfuturebackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackuplocationInput")
    def enablebackuplocation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablebackuplocationInput"))

    @builtins.property
    @jsii.member(jsii_name="prepareforretirementInput")
    def prepareforretirement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prepareforretirementInput"))

    @builtins.property
    @jsii.member(jsii_name="disablebackuplocationforfuturebackups")
    def disablebackuplocationforfuturebackups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disablebackuplocationforfuturebackups"))

    @disablebackuplocationforfuturebackups.setter
    def disablebackuplocationforfuturebackups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aabf8bd4fc0b0439c02df19ad59b9ff6e43a7404e3b5c55d8ec992b5ae77378)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablebackuplocationforfuturebackups", value)

    @builtins.property
    @jsii.member(jsii_name="enablebackuplocation")
    def enablebackuplocation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablebackuplocation"))

    @enablebackuplocation.setter
    def enablebackuplocation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0e579f278a92f04da1352bc241a80e0160f68023717c3816a5eae8c135ddc16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackuplocation", value)

    @builtins.property
    @jsii.member(jsii_name="prepareforretirement")
    def prepareforretirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prepareforretirement"))

    @prepareforretirement.setter
    def prepareforretirement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0675444948e335e919cf56f9ce452670cbdebb8172efd33dafb7135192960ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prepareforretirement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationConfiguration]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationConfiguration]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationConfiguration]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__368da41861faafcd45e629bfe55c3dddabc3a10120735cabb942ccad67a259d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationCredentials",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "password": "password"},
)
class StorageDiskBackupLocationCredentials:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: username to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#name StorageDiskBackupLocation#name}
        :param password: password to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#password StorageDiskBackupLocation#password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec45dbff5fdd124106698330460679577699b308753d21277fee5597c20a24e2)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if password is not None:
            self._values["password"] = password

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''username to access the network path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#name StorageDiskBackupLocation#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''password to access the network path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#password StorageDiskBackupLocation#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageDiskBackupLocationCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageDiskBackupLocationCredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationCredentialsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8000dc606c54c01932334e37d792d1860c9b470ad2d6009aa511bb18c90657d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageDiskBackupLocationCredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889a78866d73a58d44de03e380bdb4423a1d2c71b45a987fe61b0ef882e8f6fb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageDiskBackupLocationCredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef9f1ffb0aa2b98fe069ef0ca8f17bbb1bdc16c5b1b90c71275b62b89a808a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce61acc7d434138d11ef5f95b6adf4a06743841a641d236cb7e5bb86e77b9453)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8f38d95696187e97ed4417f624cd2b687facea0278bd1359adc74b959d684d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationCredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationCredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationCredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a1943e3356b4f4fbf0fc4c02474bad2ef16ef29d29482b538b98bcada6072ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageDiskBackupLocationCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationCredentialsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd2cb1995305cd9709839dcea8a0b23a2f5b48d4f315d94f071e6e21637f9b5c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b34daab52c2bc1322d1e3e7cc1ec92170def266cbfe57b639afddb463b74da7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c75121bb6ca886b11b1736d5cc9cdbe04aa9244b19e8142ab316da8c450bf236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationCredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationCredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationCredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de0f620cd29b52a1239dc603cc1e7880a342e881c7e5ce6c01d32129acba9d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationMediaagent",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageDiskBackupLocationMediaagent:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#name StorageDiskBackupLocation#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f5fdacc2d3afe8ad96178d34289ebdf6ca63697be13bd2fdf91c85ec0f2de7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#name StorageDiskBackupLocation#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageDiskBackupLocationMediaagent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageDiskBackupLocationMediaagentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationMediaagentList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee8e7a17ed654d792c4d6e39ae338780380327e1b4a24a8485c2aaf272248a85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageDiskBackupLocationMediaagentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52a4f730d476ee4ea6228fd39b47c89c698ef4a54da5e9ae467ca16640296486)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageDiskBackupLocationMediaagentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd74453e8a92270de6ebf39e667b7ecd57c695978f944fde47eebf3de9df3fae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c116d0c92722e2cf55dbafed4b3e7551f0121e61aeec42caacc545882d2414d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d07bf75d8a7a6e7b99ec2b385fa255f88346977116a22b92447c7eb298f28a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationMediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationMediaagent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationMediaagent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7de741c3f7895be8cd6926d59361ee09315162986c4d24fc124ac670887f395)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageDiskBackupLocationMediaagentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationMediaagentOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__745dd8e43fafaf9f7f4ce627061b56d5c7fd7ba751e4df6cef9f1dfc6894d338)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52de9fb70776165e3cc1289cc48a8736c1ae2a157b917e7f5183e287a5937339)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d8443037bab24b6e3d24a0bbcb28149d9f440c45a5f6955ce0dcdf650c349c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationMediaagent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationMediaagent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationMediaagent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__783e242392207114a45e52a1a50a43ec1d9af44ebae32363c9dccd9bff1d391b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationSavedcredentials",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageDiskBackupLocationSavedcredentials:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#name StorageDiskBackupLocation#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85545bcc29bb557d509644a663833fc5a71c44269a6b715d72375ecef7abd84c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#id StorageDiskBackupLocation#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_disk_backup_location#name StorageDiskBackupLocation#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageDiskBackupLocationSavedcredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageDiskBackupLocationSavedcredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationSavedcredentialsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9085e3e6df766c4ff4b4ff6e47b49d3120b495a7aa67b2a8eadbef2c552628f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageDiskBackupLocationSavedcredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5d4707a31a4871fed0e6f0bf16bba3fd0fafafb499d4255f197c45f018805bc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageDiskBackupLocationSavedcredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a95859a096ff96b2b5a5b765128d4707f204bc54383db45f9f7224eecfe4354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1edf02767c2e37ee127773ed8218d16b33596a9f53a2347783de2be9b20e8bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ed836c25a456a39b0e956ede759c80c8c9a8d616381a51000cb857548d3de5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationSavedcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationSavedcredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationSavedcredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c786c286576a77aecb24cf783c21c146b9db3e1f4f884e42273229adf9a46118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageDiskBackupLocationSavedcredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageDiskBackupLocation.StorageDiskBackupLocationSavedcredentialsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1125c880c4e29cd1022a2b8693389b0c0dec7bc314f8e04289d546d6009df2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2ccfaaacb0eb870570d80a61eb828c64dd5efb4b473f7803a4c89519202105d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9690e938f9c43054da2e454c84536b358e8ecc44225ef0e8a4bb9dc1f3be41d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationSavedcredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationSavedcredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationSavedcredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b718520166ee2fa75dfe1b8aef72f0c4460b82653523161dffaef6ff259009e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageDiskBackupLocation",
    "StorageDiskBackupLocationConfig",
    "StorageDiskBackupLocationConfiguration",
    "StorageDiskBackupLocationConfigurationList",
    "StorageDiskBackupLocationConfigurationOutputReference",
    "StorageDiskBackupLocationCredentials",
    "StorageDiskBackupLocationCredentialsList",
    "StorageDiskBackupLocationCredentialsOutputReference",
    "StorageDiskBackupLocationMediaagent",
    "StorageDiskBackupLocationMediaagentList",
    "StorageDiskBackupLocationMediaagentOutputReference",
    "StorageDiskBackupLocationSavedcredentials",
    "StorageDiskBackupLocationSavedcredentialsList",
    "StorageDiskBackupLocationSavedcredentialsOutputReference",
]

publication.publish()

def _typecheckingstub__b0d0f076a299c4527882a3e947da8c33cea87afb085a231cbdf44e909a0946e3(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    backuplocation: builtins.str,
    mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationMediaagent, typing.Dict[builtins.str, typing.Any]]]],
    storagepoolid: jsii.Number,
    access: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    savedcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationSavedcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742511e5d8581b50c9d9b0cbdfe116a5e541c6969e711392b3d7afcc55515563(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad3ca1bf8066d7446d029016d99e5475ee6e50e4e393bb705dcf00ff777626d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationConfiguration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca1d455f027da3e2bfd26bed16cd6f4fadbd417053c1e9ab07833f832cd5f45d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationCredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af80f2eb825bfdf1882cee398d005e50a965b0e1189234b712fc4ee6eee08d37(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationMediaagent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42bde4f7d6b6ff574e2675e4267ddd304dc599f04201540985bebd02a567ad86(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationSavedcredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83c528a0f3be49025fa98f66359c6b822869b5ba7f81bf6ea5604caabc156e99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fde1d6a1eab2a79da8193746ec6748afaa3b70694bf88c886905a2c1c3d56e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e5cffcf30341f374eb0dbfc93eaeef2dba0c84e002efd46c0b30dfd3eea8a5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07092ae0eddb5cfac566afbc851e522d5703a19d24a628965ce31c685e6b2e82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85438486235cba133ab12fdfc2de01acf64441553325bcd592be9e1577fddb29(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b9091e79332e18a4b3b6b798b45fc138a470a04d44a0064bcda91292e53267c(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backuplocation: builtins.str,
    mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationMediaagent, typing.Dict[builtins.str, typing.Any]]]],
    storagepoolid: jsii.Number,
    access: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationConfiguration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    savedcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageDiskBackupLocationSavedcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd645b8237aeb47d0020c23b87b96337737002feb1afd0b23b576577a84e58a3(
    *,
    disablebackuplocationforfuturebackups: typing.Optional[builtins.str] = None,
    enablebackuplocation: typing.Optional[builtins.str] = None,
    prepareforretirement: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbaba8816c7ab7700ef756e91e6082ccaaa59f146df1e8b9667612a8e69f73c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f851e02251056183932e372fc359f4d32aa5f01dd8a6d06e68d3fd652ea21008(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40f5e3b9ee2afaf4e7ccd45c36fb9edbc7c4a16c103b1a51c6fe904d656a63a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17cc28c25e7d40be462591f46c215aa33f0e4bc3188c95ef27d35dd1df5e87f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38b98d277774ccf343d3f5a847b9648ecf2bfcb6757ca3723e58fffe7e58bc5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56920e202137bdf78086cbb9ffe99096a514eef2bd8daf052534d5c13690b44(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationConfiguration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1552f415778c3182d2c7956fe7b03acd8f68b22e73c7c8d16dae254a9d32eccd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aabf8bd4fc0b0439c02df19ad59b9ff6e43a7404e3b5c55d8ec992b5ae77378(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0e579f278a92f04da1352bc241a80e0160f68023717c3816a5eae8c135ddc16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0675444948e335e919cf56f9ce452670cbdebb8172efd33dafb7135192960ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__368da41861faafcd45e629bfe55c3dddabc3a10120735cabb942ccad67a259d7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationConfiguration]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec45dbff5fdd124106698330460679577699b308753d21277fee5597c20a24e2(
    *,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8000dc606c54c01932334e37d792d1860c9b470ad2d6009aa511bb18c90657d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889a78866d73a58d44de03e380bdb4423a1d2c71b45a987fe61b0ef882e8f6fb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef9f1ffb0aa2b98fe069ef0ca8f17bbb1bdc16c5b1b90c71275b62b89a808a5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce61acc7d434138d11ef5f95b6adf4a06743841a641d236cb7e5bb86e77b9453(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8f38d95696187e97ed4417f624cd2b687facea0278bd1359adc74b959d684d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1943e3356b4f4fbf0fc4c02474bad2ef16ef29d29482b538b98bcada6072ed(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationCredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2cb1995305cd9709839dcea8a0b23a2f5b48d4f315d94f071e6e21637f9b5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b34daab52c2bc1322d1e3e7cc1ec92170def266cbfe57b639afddb463b74da7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75121bb6ca886b11b1736d5cc9cdbe04aa9244b19e8142ab316da8c450bf236(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de0f620cd29b52a1239dc603cc1e7880a342e881c7e5ce6c01d32129acba9d4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationCredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f5fdacc2d3afe8ad96178d34289ebdf6ca63697be13bd2fdf91c85ec0f2de7(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee8e7a17ed654d792c4d6e39ae338780380327e1b4a24a8485c2aaf272248a85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52a4f730d476ee4ea6228fd39b47c89c698ef4a54da5e9ae467ca16640296486(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd74453e8a92270de6ebf39e667b7ecd57c695978f944fde47eebf3de9df3fae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c116d0c92722e2cf55dbafed4b3e7551f0121e61aeec42caacc545882d2414d5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d07bf75d8a7a6e7b99ec2b385fa255f88346977116a22b92447c7eb298f28a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7de741c3f7895be8cd6926d59361ee09315162986c4d24fc124ac670887f395(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationMediaagent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__745dd8e43fafaf9f7f4ce627061b56d5c7fd7ba751e4df6cef9f1dfc6894d338(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52de9fb70776165e3cc1289cc48a8736c1ae2a157b917e7f5183e287a5937339(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d8443037bab24b6e3d24a0bbcb28149d9f440c45a5f6955ce0dcdf650c349c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__783e242392207114a45e52a1a50a43ec1d9af44ebae32363c9dccd9bff1d391b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationMediaagent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85545bcc29bb557d509644a663833fc5a71c44269a6b715d72375ecef7abd84c(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9085e3e6df766c4ff4b4ff6e47b49d3120b495a7aa67b2a8eadbef2c552628f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5d4707a31a4871fed0e6f0bf16bba3fd0fafafb499d4255f197c45f018805bc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a95859a096ff96b2b5a5b765128d4707f204bc54383db45f9f7224eecfe4354(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1edf02767c2e37ee127773ed8218d16b33596a9f53a2347783de2be9b20e8bf(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed836c25a456a39b0e956ede759c80c8c9a8d616381a51000cb857548d3de5e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c786c286576a77aecb24cf783c21c146b9db3e1f4f884e42273229adf9a46118(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageDiskBackupLocationSavedcredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1125c880c4e29cd1022a2b8693389b0c0dec7bc314f8e04289d546d6009df2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ccfaaacb0eb870570d80a61eb828c64dd5efb4b473f7803a4c89519202105d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9690e938f9c43054da2e454c84536b358e8ecc44225ef0e8a4bb9dc1f3be41d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b718520166ee2fa75dfe1b8aef72f0c4460b82653523161dffaef6ff259009e9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageDiskBackupLocationSavedcredentials]],
) -> None:
    """Type checking stubs"""
    pass
