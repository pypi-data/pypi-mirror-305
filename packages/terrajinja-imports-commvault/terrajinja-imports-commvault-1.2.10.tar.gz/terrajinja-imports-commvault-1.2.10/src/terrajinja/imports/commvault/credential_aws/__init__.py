'''
# `commvault_credential_aws`

Refer to the Terraform Registry for docs: [`commvault_credential_aws`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws).
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


class CredentialAws(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAws",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws commvault_credential_aws}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        accesskeyid: builtins.str,
        name: builtins.str,
        secretaccesskey: builtins.str,
        accounttype: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vendortype: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws commvault_credential_aws} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param accesskeyid: Access Key ID of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#accesskeyid CredentialAws#accesskeyid}
        :param name: Name of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}
        :param secretaccesskey: Secret Access Key of Credential and must be in base64 encoded format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#secretaccesskey CredentialAws#secretaccesskey}
        :param accounttype: [WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#accounttype CredentialAws#accounttype}
        :param description: Description of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#description CredentialAws#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#security CredentialAws#security}
        :param vendortype: Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#vendortype CredentialAws#vendortype}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcea87f453eb488f5becce437a7e926f76d8f6c5c0f04b2b2771eca49445f8be)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CredentialAwsConfig(
            accesskeyid=accesskeyid,
            name=name,
            secretaccesskey=secretaccesskey,
            accounttype=accounttype,
            description=description,
            id=id,
            security=security,
            vendortype=vendortype,
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
        '''Generates CDKTF code for importing a CredentialAws resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CredentialAws to import.
        :param import_from_id: The id of the existing CredentialAws that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CredentialAws to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0ed1f2749d201728e7b32836920a85e628ffdd8468d8afaf235df922885eec9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5c259e57bad16a1a48322b529875f0e7dbe7217165573f1f4888f2ebe4b19b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecurity", [value]))

    @jsii.member(jsii_name="resetAccounttype")
    def reset_accounttype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccounttype", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurity")
    def reset_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurity", []))

    @jsii.member(jsii_name="resetVendortype")
    def reset_vendortype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendortype", []))

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
    @jsii.member(jsii_name="security")
    def security(self) -> "CredentialAwsSecurityList":
        return typing.cast("CredentialAwsSecurityList", jsii.get(self, "security"))

    @builtins.property
    @jsii.member(jsii_name="accesskeyidInput")
    def accesskeyid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accesskeyidInput"))

    @builtins.property
    @jsii.member(jsii_name="accounttypeInput")
    def accounttype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accounttypeInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretaccesskeyInput")
    def secretaccesskey_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretaccesskeyInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurity"]]], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="vendortypeInput")
    def vendortype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendortypeInput"))

    @builtins.property
    @jsii.member(jsii_name="accesskeyid")
    def accesskeyid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accesskeyid"))

    @accesskeyid.setter
    def accesskeyid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d47635e39cec2a7fad9de26e39d19d1ed6170211047fb0c21688d8697439bfc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accesskeyid", value)

    @builtins.property
    @jsii.member(jsii_name="accounttype")
    def accounttype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accounttype"))

    @accounttype.setter
    def accounttype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b76588896d143226150fc86cc4a817d0a7fa02ecdc5b781e71fc6a5b28dacb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accounttype", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a93b841b3fb1a851ceda65976be6c17413955a8194bc9fd7b45be3e4ab69fb8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d3a8cf83961f6b91211b1855a3f7c38d49df09104c3986889cd9674c8fda467)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eddf656428bac2c2e011e1cd0f72be568e19880b9c0352328d08d339ef3c0171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="secretaccesskey")
    def secretaccesskey(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretaccesskey"))

    @secretaccesskey.setter
    def secretaccesskey(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbfd9960b81891e583f157c7f843f267d10886d4d0ec58118b5b6f086fea578f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretaccesskey", value)

    @builtins.property
    @jsii.member(jsii_name="vendortype")
    def vendortype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendortype"))

    @vendortype.setter
    def vendortype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78bb396a53e182dbedbd15f820c258a83a3e70fbc92d4fbea66920e0eca9ba77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendortype", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "accesskeyid": "accesskeyid",
        "name": "name",
        "secretaccesskey": "secretaccesskey",
        "accounttype": "accounttype",
        "description": "description",
        "id": "id",
        "security": "security",
        "vendortype": "vendortype",
    },
)
class CredentialAwsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        accesskeyid: builtins.str,
        name: builtins.str,
        secretaccesskey: builtins.str,
        accounttype: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vendortype: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param accesskeyid: Access Key ID of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#accesskeyid CredentialAws#accesskeyid}
        :param name: Name of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}
        :param secretaccesskey: Secret Access Key of Credential and must be in base64 encoded format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#secretaccesskey CredentialAws#secretaccesskey}
        :param accounttype: [WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#accounttype CredentialAws#accounttype}
        :param description: Description of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#description CredentialAws#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#security CredentialAws#security}
        :param vendortype: Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#vendortype CredentialAws#vendortype}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec5ebe896453bd42793fc65d198282029db149c42d57332f3d0e0c69346d3b3)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument accesskeyid", value=accesskeyid, expected_type=type_hints["accesskeyid"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument secretaccesskey", value=secretaccesskey, expected_type=type_hints["secretaccesskey"])
            check_type(argname="argument accounttype", value=accounttype, expected_type=type_hints["accounttype"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument vendortype", value=vendortype, expected_type=type_hints["vendortype"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accesskeyid": accesskeyid,
            "name": name,
            "secretaccesskey": secretaccesskey,
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
        if accounttype is not None:
            self._values["accounttype"] = accounttype
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if security is not None:
            self._values["security"] = security
        if vendortype is not None:
            self._values["vendortype"] = vendortype

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
    def accesskeyid(self) -> builtins.str:
        '''Access Key ID of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#accesskeyid CredentialAws#accesskeyid}
        '''
        result = self._values.get("accesskeyid")
        assert result is not None, "Required property 'accesskeyid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secretaccesskey(self) -> builtins.str:
        '''Secret Access Key of Credential and must be in base64 encoded format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#secretaccesskey CredentialAws#secretaccesskey}
        '''
        result = self._values.get("secretaccesskey")
        assert result is not None, "Required property 'secretaccesskey' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accounttype(self) -> typing.Optional[builtins.str]:
        '''[WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#accounttype CredentialAws#accounttype}
        '''
        result = self._values.get("accounttype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#description CredentialAws#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurity"]]]:
        '''security block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#security CredentialAws#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurity"]]], result)

    @builtins.property
    def vendortype(self) -> typing.Optional[builtins.str]:
        '''Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#vendortype CredentialAws#vendortype}
        '''
        result = self._values.get("vendortype")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurity",
    jsii_struct_bases=[],
    name_mapping={"associations": "associations", "owner": "owner"},
)
class CredentialAwsSecurity:
    def __init__(
        self,
        *,
        associations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        owner: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityOwner", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param associations: associations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#associations CredentialAws#associations}
        :param owner: owner block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#owner CredentialAws#owner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f5965c416d0861d6df8a9f698c1d69777f954c9e50fdb7356fa2f665bcef28a)
            check_type(argname="argument associations", value=associations, expected_type=type_hints["associations"])
            check_type(argname="argument owner", value=owner, expected_type=type_hints["owner"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if associations is not None:
            self._values["associations"] = associations
        if owner is not None:
            self._values["owner"] = owner

    @builtins.property
    def associations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociations"]]]:
        '''associations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#associations CredentialAws#associations}
        '''
        result = self._values.get("associations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociations"]]], result)

    @builtins.property
    def owner(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwner"]]]:
        '''owner block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#owner CredentialAws#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwner"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociations",
    jsii_struct_bases=[],
    name_mapping={
        "iscreatorassociation": "iscreatorassociation",
        "permissions": "permissions",
        "user": "user",
        "usergroup": "usergroup",
    },
)
class CredentialAwsSecurityAssociations:
    def __init__(
        self,
        *,
        iscreatorassociation: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociationsPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociationsUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociationsUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param iscreatorassociation: To check if the user/user group associated is the owner. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#iscreatorassociation CredentialAws#iscreatorassociation}
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#permissions CredentialAws#permissions}
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#user CredentialAws#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#usergroup CredentialAws#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81fa2e8172ec37637d2a867eef07b0c4da88a51e01fbf928b608ba1773162b7)
            check_type(argname="argument iscreatorassociation", value=iscreatorassociation, expected_type=type_hints["iscreatorassociation"])
            check_type(argname="argument permissions", value=permissions, expected_type=type_hints["permissions"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument usergroup", value=usergroup, expected_type=type_hints["usergroup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if iscreatorassociation is not None:
            self._values["iscreatorassociation"] = iscreatorassociation
        if permissions is not None:
            self._values["permissions"] = permissions
        if user is not None:
            self._values["user"] = user
        if usergroup is not None:
            self._values["usergroup"] = usergroup

    @builtins.property
    def iscreatorassociation(self) -> typing.Optional[builtins.str]:
        '''To check if the user/user group associated is the owner.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#iscreatorassociation CredentialAws#iscreatorassociation}
        '''
        result = self._values.get("iscreatorassociation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsPermissions"]]]:
        '''permissions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#permissions CredentialAws#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsPermissions"]]], result)

    @builtins.property
    def user(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#user CredentialAws#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#usergroup CredentialAws#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityAssociations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityAssociationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b896446e60868a279b1c19856782987f5839405aabc0667f247a8e699b4e93e0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwsSecurityAssociationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__954b68aceb3b4e6278ce15c473f4ffaff5f6deb0cf7c9b7d063e027bf8a86e9f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityAssociationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81ee82681750397f307c8f2a70e0f6915173bea1a4d728bdee782c111a8cf027)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2a822242450c3a5faa41c9d31ada3cc15fb07e5e5679422563b6bcf11dbfee6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9def051a6cea9d7377c33d4df2851ccc2f75149687eadca9a59e664c8fa7aef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__029274c6d423af79205fd1d0aee984404c24fa4683340716520b1be025026a2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityAssociationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b1a80a81ea1af058b48d25709daeda2d64207891c0beebe72e8743449352347)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociationsPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd95a8765a9d10bce0c6acfba8132eb2e055de16d69608c400feceb76c0ce9c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociationsUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e7398d2b0b55fe2ef9881b374e7c9e1f84dc25e0864e1fd66abf0d50ee35e74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityAssociationsUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa513abde08a20b3da6ccae12d996bf26f32e1fdea4ee81b47975352b7ab1040)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUsergroup", [value]))

    @jsii.member(jsii_name="resetIscreatorassociation")
    def reset_iscreatorassociation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscreatorassociation", []))

    @jsii.member(jsii_name="resetPermissions")
    def reset_permissions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissions", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="resetUsergroup")
    def reset_usergroup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsergroup", []))

    @builtins.property
    @jsii.member(jsii_name="permissions")
    def permissions(self) -> "CredentialAwsSecurityAssociationsPermissionsList":
        return typing.cast("CredentialAwsSecurityAssociationsPermissionsList", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "CredentialAwsSecurityAssociationsUserList":
        return typing.cast("CredentialAwsSecurityAssociationsUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(self) -> "CredentialAwsSecurityAssociationsUsergroupList":
        return typing.cast("CredentialAwsSecurityAssociationsUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="iscreatorassociationInput")
    def iscreatorassociation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscreatorassociationInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsPermissions"]]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityAssociationsUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="iscreatorassociation")
    def iscreatorassociation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscreatorassociation"))

    @iscreatorassociation.setter
    def iscreatorassociation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a83e0803c73d1084ad87ca4803d8d2e7429e20e8f7ee2d55309410d53393c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscreatorassociation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03b8fe3516d706d0df189ce33c0cac53434b3423f6e1aac0bbf742fb33e716f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsPermissions",
    jsii_struct_bases=[],
    name_mapping={
        "categoryid": "categoryid",
        "categoryname": "categoryname",
        "exclude": "exclude",
        "permissionid": "permissionid",
        "permissionname": "permissionname",
        "type": "type",
    },
)
class CredentialAwsSecurityAssociationsPermissions:
    def __init__(
        self,
        *,
        categoryid: typing.Optional[jsii.Number] = None,
        categoryname: typing.Optional[builtins.str] = None,
        exclude: typing.Optional[builtins.str] = None,
        permissionid: typing.Optional[jsii.Number] = None,
        permissionname: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param categoryid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#categoryid CredentialAws#categoryid}.
        :param categoryname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#categoryname CredentialAws#categoryname}.
        :param exclude: Flag to specify if this is included permission or excluded permission. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#exclude CredentialAws#exclude}
        :param permissionid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#permissionid CredentialAws#permissionid}.
        :param permissionname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#permissionname CredentialAws#permissionname}.
        :param type: Returns the type of association. [ALL_CATEGORIES, CATEGORY_ENTITY, PERMISSION_ENTITY]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#type CredentialAws#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b12bac515a55fe4eb2e39c91b8492c49ab80779b843481557e495f835cc6bd5)
            check_type(argname="argument categoryid", value=categoryid, expected_type=type_hints["categoryid"])
            check_type(argname="argument categoryname", value=categoryname, expected_type=type_hints["categoryname"])
            check_type(argname="argument exclude", value=exclude, expected_type=type_hints["exclude"])
            check_type(argname="argument permissionid", value=permissionid, expected_type=type_hints["permissionid"])
            check_type(argname="argument permissionname", value=permissionname, expected_type=type_hints["permissionname"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if categoryid is not None:
            self._values["categoryid"] = categoryid
        if categoryname is not None:
            self._values["categoryname"] = categoryname
        if exclude is not None:
            self._values["exclude"] = exclude
        if permissionid is not None:
            self._values["permissionid"] = permissionid
        if permissionname is not None:
            self._values["permissionname"] = permissionname
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def categoryid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#categoryid CredentialAws#categoryid}.'''
        result = self._values.get("categoryid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def categoryname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#categoryname CredentialAws#categoryname}.'''
        result = self._values.get("categoryname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if this is included permission or excluded permission.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#exclude CredentialAws#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissionid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#permissionid CredentialAws#permissionid}.'''
        result = self._values.get("permissionid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def permissionname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#permissionname CredentialAws#permissionname}.'''
        result = self._values.get("permissionname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Returns the type of association. [ALL_CATEGORIES, CATEGORY_ENTITY, PERMISSION_ENTITY].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#type CredentialAws#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityAssociationsPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityAssociationsPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c1b9df6e2c109a23e940256c7365a1c47b34675df6cfaa31be057fd978617a0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwsSecurityAssociationsPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d316074770ed1674a6ce729066cea6ce8644130e7b651f8ad621cc85f50d61d9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityAssociationsPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40cb27e154c0567d87cc52317732eba97ce98f3afc590ef30905a6f653d8b59e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31576cdecd7687efb1e6d558a390206b18a651e788b56168e0103b299df98a3d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7352bea496f5b6b9ab2301a345490d7e7995af38bafc74448e1ca1d63927ca36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727cf00bd781a45c5649231bd6bbccf3a401eff659a34bd1ac7957f96573f99d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityAssociationsPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa4bdb0f0c913f113a355163a1857a33c97af2786b3c1968423e365a38c31613)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCategoryid")
    def reset_categoryid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategoryid", []))

    @jsii.member(jsii_name="resetCategoryname")
    def reset_categoryname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCategoryname", []))

    @jsii.member(jsii_name="resetExclude")
    def reset_exclude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclude", []))

    @jsii.member(jsii_name="resetPermissionid")
    def reset_permissionid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissionid", []))

    @jsii.member(jsii_name="resetPermissionname")
    def reset_permissionname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPermissionname", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="categoryidInput")
    def categoryid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "categoryidInput"))

    @builtins.property
    @jsii.member(jsii_name="categorynameInput")
    def categoryname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "categorynameInput"))

    @builtins.property
    @jsii.member(jsii_name="excludeInput")
    def exclude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "excludeInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionidInput")
    def permissionid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "permissionidInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionnameInput")
    def permissionname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionnameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="categoryid")
    def categoryid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "categoryid"))

    @categoryid.setter
    def categoryid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ee5742aa0b68ae5c10cc9cf1df8929d575746af5a746058d9db12c8f89f1ed0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryid", value)

    @builtins.property
    @jsii.member(jsii_name="categoryname")
    def categoryname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "categoryname"))

    @categoryname.setter
    def categoryname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25dc7be55e2b1b0283e84f5704933e1d11db8568cdf7efe1fd6cd3700d45aa50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryname", value)

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__413336e55c755a455b0cc50ece513978ec8405ec153194477e04df8b749dfbfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="permissionid")
    def permissionid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "permissionid"))

    @permissionid.setter
    def permissionid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41898b90efd93cb08d4a233bf320fb4fc9510584127e491e107bc62498734f7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionid", value)

    @builtins.property
    @jsii.member(jsii_name="permissionname")
    def permissionname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionname"))

    @permissionname.setter
    def permissionname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde54e21365d4835d187ae01dd9233d90194714975c5d412f388f23f5a22ab54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionname", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e37dcc6cb839485cba5a856721fd219f22ab7a0044fc25db9f4b40a48c1f38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsPermissions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsPermissions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsPermissions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__724f860dd8d5ba96bc05718b4d8f691eb068c43f9748a4ad7ea69c7d3f028d2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class CredentialAwsSecurityAssociationsUser:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d89944d3d80ce0189e5c6538405d1aa2c65b48e241164f21c23a0faa0c2691b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityAssociationsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityAssociationsUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__819dba7641ec6ac0389aa7f12fe897d866288e9f066993eb66f0b89fc44670da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwsSecurityAssociationsUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94a12e270ac0c83e2c40b9869e1996bddf23631cc46d990f3205997f405b7d7e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityAssociationsUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb9390cf92a912258af073d8d5043fc384f7355e7187b95f6780cdfc613ded84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e79e1e84895c544b0c4f85d09379d85234645730714ef7ac1031775a4927289)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fcbd3b727b8d0b72e04d71ced70aca0dfac98fcb0388fdbc9e5a207587657aed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e271110a0a2e1d140c35c28cf7283a57e6f12ad154263fda66a2f5956046b8d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityAssociationsUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e770dbef57c2b4310fee47e8ce56b800fa65039c6da32da04408bf6bb44decc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a3c14cd0275f0ac9cbd0632675db1d80c05f5a9599da906713a12159629ad8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa26b6fa7f6a95e81193f7afae542f2faa84016edb1db87b85499fa768ba3504)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class CredentialAwsSecurityAssociationsUsergroup:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e066e03a72fe620354a5b2cc1d6e8a79af576ffe4dc596e0f1d3c9806fc7335a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityAssociationsUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityAssociationsUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b54dcfeef1c245c90dfc5a7cb1cc760b573102410163347e204df9259ef3b3e6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwsSecurityAssociationsUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__509bf246c61a2198889d5738b85f9613523885cbc019691d60bface773b84397)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityAssociationsUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d11ded4a41449a55d28e6ae4d82df12a283e260e24754f4fa922b91bd255cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1932cd19c08f906441b88c53941cb5ba57ff573fb09d4cdfb42d4c332fea4520)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd5384cef61aae8244b0c3570d04c18353b4ae4f583cda51013129cb06c89af5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffb753b72c524bbf3d1e15d71d480d0c0cde9ccab3dd438627615e5906641860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityAssociationsUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityAssociationsUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e00d6a94bdc7978e7a94a478bcec668b9fd7b14357dcb6cac875407ecfb2eed2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dc30e6260622ad1399311ead4c25c5e378d1e18290703fef14c3288d738a0aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8706e5811b79a9bcf8228c847aa7dca460bdb5a4e2f3b1cf54dc661d749e51c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__14ef4d5d695f0ac1c21a03aff658de0b3f97ad50d18faa22ea2a985bf6f8e11e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CredentialAwsSecurityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0cb0f5d198240985ea2f81bcceeaa59e43c0d9a35cdb03efd7b3eaf3c54d6ca)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f801bf0216ead00da1e83873b2fb693b377499017e8a95fdbf18cd85006e58)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5507665803a5f6a3dd2e6710529894220b39b8d6e6fe983a28ade44683b303d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__50b521e069d849ef5735a9acbd3658a18a16d8fe8eed5894b987f65ecafdf918)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1560294b5809866e5da94906f3d85d0359a54a760e192580cf79a7d4ae6027d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c717530ba512dc7ce796cbf39dc5ea160f628bf87316ec95d62e16cc2155408b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssociations")
    def put_associations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__993a7e8301fea942a53a3e1356e3386c02bbe6edb027cd31a33c03cbfe1d8248)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssociations", [value]))

    @jsii.member(jsii_name="putOwner")
    def put_owner(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityOwner", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd192ed148d176fb879593987c8acea0f778f45b24eae6ea29356d118f813cf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOwner", [value]))

    @jsii.member(jsii_name="resetAssociations")
    def reset_associations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociations", []))

    @jsii.member(jsii_name="resetOwner")
    def reset_owner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOwner", []))

    @builtins.property
    @jsii.member(jsii_name="associations")
    def associations(self) -> CredentialAwsSecurityAssociationsList:
        return typing.cast(CredentialAwsSecurityAssociationsList, jsii.get(self, "associations"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> "CredentialAwsSecurityOwnerList":
        return typing.cast("CredentialAwsSecurityOwnerList", jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="associationsInput")
    def associations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociations]]], jsii.get(self, "associationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwner"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwner"]]], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e9e61a96c09049e2c1cd74c8e9116d1f38b62f48152d6fc80ac999b7f96a015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwner",
    jsii_struct_bases=[],
    name_mapping={"user": "user", "usergroup": "usergroup"},
)
class CredentialAwsSecurityOwner:
    def __init__(
        self,
        *,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityOwnerUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityOwnerUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#user CredentialAws#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#usergroup CredentialAws#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10d364803d70cf6031d6f7fe520e6232b5637d9efc14088c98d515814a910b09)
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument usergroup", value=usergroup, expected_type=type_hints["usergroup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if user is not None:
            self._values["user"] = user
        if usergroup is not None:
            self._values["usergroup"] = usergroup

    @builtins.property
    def user(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#user CredentialAws#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#usergroup CredentialAws#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityOwner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityOwnerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__de473e731b91c7e56f0a83140d337ee6aa6d19f421ab4a0f6bba249555fbd4dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CredentialAwsSecurityOwnerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318162788b9efd9201d040d8d5a0c7ae895866be58420a52d60ea7aa1c2840ec)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityOwnerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5284dc0b04a817c1250b7c021216d18cc01c56eb9d6051a7a1619ab77437c1c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__43b5718a7c30bb37d70df0c463c20d9bd7623b925fc3829281923c62b182f7a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4e8e153f0d657c3410c790edc17610a00dd91894fa231a637ad3c0241adfa58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwner]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwner]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwner]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4da723136093340ea286acda2815f908fd55b803154717c7e49ca035cc917dc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityOwnerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82ec00b7f69dc288255587560b53fabfeaabc6054b6921428204e964c491a095)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityOwnerUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80857c6de625200aded068b0727442ab3ca53a2a49005cc9ac0f73d2487128be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwsSecurityOwnerUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__272859d98c81528a103af0253a71af30c150873f6020063d203072caa870c9ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUsergroup", [value]))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="resetUsergroup")
    def reset_usergroup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsergroup", []))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "CredentialAwsSecurityOwnerUserList":
        return typing.cast("CredentialAwsSecurityOwnerUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(self) -> "CredentialAwsSecurityOwnerUsergroupList":
        return typing.cast("CredentialAwsSecurityOwnerUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwsSecurityOwnerUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwner]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwner]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwner]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70e6fd90f2f5117ee4003af452cd9fb48dfaf8917eb151a835b926c7367d23e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class CredentialAwsSecurityOwnerUser:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f57626dcd7f59b3e492ea28836e9bba92a2ed639fa2404719cc1fc6c627b381)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityOwnerUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityOwnerUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce44d24b47e6965cd7878a294ed0269026a1a078de96f55470c3f485b04c5f75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwsSecurityOwnerUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5435e3a2604f9463c29e0213456141289f00c818e7bf079921e7dcd9ede185d0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityOwnerUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b418b6cdaf487436c86e0b5ca533b6e977289dd27dba8b59761a489a861f6bf0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__46c31832e46b0795334919b91919d3f223894988b9dcff2591b8b42d6dff3141)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bee9e3173b7b9f23d8d09a7f1d3aa4c3695e1d9341971db4f3ec6641d090cba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb7c5fcbf44f4f06e5544d87b0d43b069305e06ad81e65ab3e7b69c35d2f0523)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityOwnerUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3661fba40eb39de32d17e8537c667d37e9b2fe78e8a99dc1826932be4b4b1e2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0ad62cfa62c361c6d666762c1261205ac584433dad3b056439a5e989026ab6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c2750de89c876c59afef76eb9ee88e4aeac325612d729200414ca076052f541)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6305851af305b83a103cada977022cc2a7dd487f350c0bfef435de594865c334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class CredentialAwsSecurityOwnerUsergroup:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5301943d9dab3a8988cde371db8c6903997974a9458c14ebaa7d18a2da86e58)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#id CredentialAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_aws#name CredentialAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwsSecurityOwnerUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwsSecurityOwnerUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__137981d7b77fcb35eb9ac363a460d9556f2d97becc5a4d4c595183b083879ffa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwsSecurityOwnerUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e20d5d715a05b2413b709ec3b8a5fdf84e572f378becee470817ff6fb235d236)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwsSecurityOwnerUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a796019a1deaecdd836282c496667ac4157c57e92a15819371643c2ded9a1b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad08d768553131c903add2e471583468d23983b6a7d4d2522a707562e9ba8dfa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fddaed4f0c3507c4d14d437b7c96f64bcfea22ae925f1b0f45654c820795cd62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57c3fac17adaf74b350d79203f2238db51de2017defa0ebe73ebcf7438b3e370)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwsSecurityOwnerUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAws.CredentialAwsSecurityOwnerUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__33cac5580c916da078aff4164eb9a9e13673fb59156a9df649e775082d5de016)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ae2772e7c9c2c0d9cf720d1747d4a7c12be4673c125374fe744434a77333129)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fd51f302836b4b3bdbad4c1a1bca674b287b875cb36b3432f7db07f65e7a598)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae0cc8165fe6f06dcf745651ba1474aba06bdc38dca703c571ee28e3480530f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CredentialAws",
    "CredentialAwsConfig",
    "CredentialAwsSecurity",
    "CredentialAwsSecurityAssociations",
    "CredentialAwsSecurityAssociationsList",
    "CredentialAwsSecurityAssociationsOutputReference",
    "CredentialAwsSecurityAssociationsPermissions",
    "CredentialAwsSecurityAssociationsPermissionsList",
    "CredentialAwsSecurityAssociationsPermissionsOutputReference",
    "CredentialAwsSecurityAssociationsUser",
    "CredentialAwsSecurityAssociationsUserList",
    "CredentialAwsSecurityAssociationsUserOutputReference",
    "CredentialAwsSecurityAssociationsUsergroup",
    "CredentialAwsSecurityAssociationsUsergroupList",
    "CredentialAwsSecurityAssociationsUsergroupOutputReference",
    "CredentialAwsSecurityList",
    "CredentialAwsSecurityOutputReference",
    "CredentialAwsSecurityOwner",
    "CredentialAwsSecurityOwnerList",
    "CredentialAwsSecurityOwnerOutputReference",
    "CredentialAwsSecurityOwnerUser",
    "CredentialAwsSecurityOwnerUserList",
    "CredentialAwsSecurityOwnerUserOutputReference",
    "CredentialAwsSecurityOwnerUsergroup",
    "CredentialAwsSecurityOwnerUsergroupList",
    "CredentialAwsSecurityOwnerUsergroupOutputReference",
]

publication.publish()

def _typecheckingstub__bcea87f453eb488f5becce437a7e926f76d8f6c5c0f04b2b2771eca49445f8be(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    accesskeyid: builtins.str,
    name: builtins.str,
    secretaccesskey: builtins.str,
    accounttype: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vendortype: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__e0ed1f2749d201728e7b32836920a85e628ffdd8468d8afaf235df922885eec9(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c259e57bad16a1a48322b529875f0e7dbe7217165573f1f4888f2ebe4b19b0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d47635e39cec2a7fad9de26e39d19d1ed6170211047fb0c21688d8697439bfc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b76588896d143226150fc86cc4a817d0a7fa02ecdc5b781e71fc6a5b28dacb3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a93b841b3fb1a851ceda65976be6c17413955a8194bc9fd7b45be3e4ab69fb8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3a8cf83961f6b91211b1855a3f7c38d49df09104c3986889cd9674c8fda467(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eddf656428bac2c2e011e1cd0f72be568e19880b9c0352328d08d339ef3c0171(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbfd9960b81891e583f157c7f843f267d10886d4d0ec58118b5b6f086fea578f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78bb396a53e182dbedbd15f820c258a83a3e70fbc92d4fbea66920e0eca9ba77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec5ebe896453bd42793fc65d198282029db149c42d57332f3d0e0c69346d3b3(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    accesskeyid: builtins.str,
    name: builtins.str,
    secretaccesskey: builtins.str,
    accounttype: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vendortype: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f5965c416d0861d6df8a9f698c1d69777f954c9e50fdb7356fa2f665bcef28a(
    *,
    associations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    owner: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityOwner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81fa2e8172ec37637d2a867eef07b0c4da88a51e01fbf928b608ba1773162b7(
    *,
    iscreatorassociation: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociationsPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociationsUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociationsUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b896446e60868a279b1c19856782987f5839405aabc0667f247a8e699b4e93e0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__954b68aceb3b4e6278ce15c473f4ffaff5f6deb0cf7c9b7d063e027bf8a86e9f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81ee82681750397f307c8f2a70e0f6915173bea1a4d728bdee782c111a8cf027(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a822242450c3a5faa41c9d31ada3cc15fb07e5e5679422563b6bcf11dbfee6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9def051a6cea9d7377c33d4df2851ccc2f75149687eadca9a59e664c8fa7aef(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__029274c6d423af79205fd1d0aee984404c24fa4683340716520b1be025026a2c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b1a80a81ea1af058b48d25709daeda2d64207891c0beebe72e8743449352347(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd95a8765a9d10bce0c6acfba8132eb2e055de16d69608c400feceb76c0ce9c7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociationsPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e7398d2b0b55fe2ef9881b374e7c9e1f84dc25e0864e1fd66abf0d50ee35e74(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociationsUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa513abde08a20b3da6ccae12d996bf26f32e1fdea4ee81b47975352b7ab1040(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociationsUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a83e0803c73d1084ad87ca4803d8d2e7429e20e8f7ee2d55309410d53393c48(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03b8fe3516d706d0df189ce33c0cac53434b3423f6e1aac0bbf742fb33e716f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b12bac515a55fe4eb2e39c91b8492c49ab80779b843481557e495f835cc6bd5(
    *,
    categoryid: typing.Optional[jsii.Number] = None,
    categoryname: typing.Optional[builtins.str] = None,
    exclude: typing.Optional[builtins.str] = None,
    permissionid: typing.Optional[jsii.Number] = None,
    permissionname: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c1b9df6e2c109a23e940256c7365a1c47b34675df6cfaa31be057fd978617a0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d316074770ed1674a6ce729066cea6ce8644130e7b651f8ad621cc85f50d61d9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40cb27e154c0567d87cc52317732eba97ce98f3afc590ef30905a6f653d8b59e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31576cdecd7687efb1e6d558a390206b18a651e788b56168e0103b299df98a3d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7352bea496f5b6b9ab2301a345490d7e7995af38bafc74448e1ca1d63927ca36(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__727cf00bd781a45c5649231bd6bbccf3a401eff659a34bd1ac7957f96573f99d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa4bdb0f0c913f113a355163a1857a33c97af2786b3c1968423e365a38c31613(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee5742aa0b68ae5c10cc9cf1df8929d575746af5a746058d9db12c8f89f1ed0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25dc7be55e2b1b0283e84f5704933e1d11db8568cdf7efe1fd6cd3700d45aa50(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__413336e55c755a455b0cc50ece513978ec8405ec153194477e04df8b749dfbfd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41898b90efd93cb08d4a233bf320fb4fc9510584127e491e107bc62498734f7d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde54e21365d4835d187ae01dd9233d90194714975c5d412f388f23f5a22ab54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e37dcc6cb839485cba5a856721fd219f22ab7a0044fc25db9f4b40a48c1f38(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__724f860dd8d5ba96bc05718b4d8f691eb068c43f9748a4ad7ea69c7d3f028d2c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsPermissions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d89944d3d80ce0189e5c6538405d1aa2c65b48e241164f21c23a0faa0c2691b(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__819dba7641ec6ac0389aa7f12fe897d866288e9f066993eb66f0b89fc44670da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94a12e270ac0c83e2c40b9869e1996bddf23631cc46d990f3205997f405b7d7e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb9390cf92a912258af073d8d5043fc384f7355e7187b95f6780cdfc613ded84(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e79e1e84895c544b0c4f85d09379d85234645730714ef7ac1031775a4927289(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcbd3b727b8d0b72e04d71ced70aca0dfac98fcb0388fdbc9e5a207587657aed(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e271110a0a2e1d140c35c28cf7283a57e6f12ad154263fda66a2f5956046b8d6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e770dbef57c2b4310fee47e8ce56b800fa65039c6da32da04408bf6bb44decc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a3c14cd0275f0ac9cbd0632675db1d80c05f5a9599da906713a12159629ad8b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa26b6fa7f6a95e81193f7afae542f2faa84016edb1db87b85499fa768ba3504(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e066e03a72fe620354a5b2cc1d6e8a79af576ffe4dc596e0f1d3c9806fc7335a(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54dcfeef1c245c90dfc5a7cb1cc760b573102410163347e204df9259ef3b3e6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509bf246c61a2198889d5738b85f9613523885cbc019691d60bface773b84397(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d11ded4a41449a55d28e6ae4d82df12a283e260e24754f4fa922b91bd255cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1932cd19c08f906441b88c53941cb5ba57ff573fb09d4cdfb42d4c332fea4520(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd5384cef61aae8244b0c3570d04c18353b4ae4f583cda51013129cb06c89af5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffb753b72c524bbf3d1e15d71d480d0c0cde9ccab3dd438627615e5906641860(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityAssociationsUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00d6a94bdc7978e7a94a478bcec668b9fd7b14357dcb6cac875407ecfb2eed2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dc30e6260622ad1399311ead4c25c5e378d1e18290703fef14c3288d738a0aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8706e5811b79a9bcf8228c847aa7dca460bdb5a4e2f3b1cf54dc661d749e51c7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityAssociationsUsergroup]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ef4d5d695f0ac1c21a03aff658de0b3f97ad50d18faa22ea2a985bf6f8e11e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0cb0f5d198240985ea2f81bcceeaa59e43c0d9a35cdb03efd7b3eaf3c54d6ca(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f801bf0216ead00da1e83873b2fb693b377499017e8a95fdbf18cd85006e58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5507665803a5f6a3dd2e6710529894220b39b8d6e6fe983a28ade44683b303d1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b521e069d849ef5735a9acbd3658a18a16d8fe8eed5894b987f65ecafdf918(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1560294b5809866e5da94906f3d85d0359a54a760e192580cf79a7d4ae6027d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c717530ba512dc7ce796cbf39dc5ea160f628bf87316ec95d62e16cc2155408b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__993a7e8301fea942a53a3e1356e3386c02bbe6edb027cd31a33c03cbfe1d8248(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd192ed148d176fb879593987c8acea0f778f45b24eae6ea29356d118f813cf1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityOwner, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e9e61a96c09049e2c1cd74c8e9116d1f38b62f48152d6fc80ac999b7f96a015(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10d364803d70cf6031d6f7fe520e6232b5637d9efc14088c98d515814a910b09(
    *,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityOwnerUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityOwnerUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de473e731b91c7e56f0a83140d337ee6aa6d19f421ab4a0f6bba249555fbd4dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318162788b9efd9201d040d8d5a0c7ae895866be58420a52d60ea7aa1c2840ec(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5284dc0b04a817c1250b7c021216d18cc01c56eb9d6051a7a1619ab77437c1c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b5718a7c30bb37d70df0c463c20d9bd7623b925fc3829281923c62b182f7a8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e8e153f0d657c3410c790edc17610a00dd91894fa231a637ad3c0241adfa58(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da723136093340ea286acda2815f908fd55b803154717c7e49ca035cc917dc7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwner]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82ec00b7f69dc288255587560b53fabfeaabc6054b6921428204e964c491a095(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80857c6de625200aded068b0727442ab3ca53a2a49005cc9ac0f73d2487128be(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityOwnerUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__272859d98c81528a103af0253a71af30c150873f6020063d203072caa870c9ff(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwsSecurityOwnerUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e6fd90f2f5117ee4003af452cd9fb48dfaf8917eb151a835b926c7367d23e0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwner]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f57626dcd7f59b3e492ea28836e9bba92a2ed639fa2404719cc1fc6c627b381(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce44d24b47e6965cd7878a294ed0269026a1a078de96f55470c3f485b04c5f75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5435e3a2604f9463c29e0213456141289f00c818e7bf079921e7dcd9ede185d0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b418b6cdaf487436c86e0b5ca533b6e977289dd27dba8b59761a489a861f6bf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c31832e46b0795334919b91919d3f223894988b9dcff2591b8b42d6dff3141(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bee9e3173b7b9f23d8d09a7f1d3aa4c3695e1d9341971db4f3ec6641d090cba(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7c5fcbf44f4f06e5544d87b0d43b069305e06ad81e65ab3e7b69c35d2f0523(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3661fba40eb39de32d17e8537c667d37e9b2fe78e8a99dc1826932be4b4b1e2a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ad62cfa62c361c6d666762c1261205ac584433dad3b056439a5e989026ab6d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c2750de89c876c59afef76eb9ee88e4aeac325612d729200414ca076052f541(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6305851af305b83a103cada977022cc2a7dd487f350c0bfef435de594865c334(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5301943d9dab3a8988cde371db8c6903997974a9458c14ebaa7d18a2da86e58(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__137981d7b77fcb35eb9ac363a460d9556f2d97becc5a4d4c595183b083879ffa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e20d5d715a05b2413b709ec3b8a5fdf84e572f378becee470817ff6fb235d236(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a796019a1deaecdd836282c496667ac4157c57e92a15819371643c2ded9a1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad08d768553131c903add2e471583468d23983b6a7d4d2522a707562e9ba8dfa(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fddaed4f0c3507c4d14d437b7c96f64bcfea22ae925f1b0f45654c820795cd62(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57c3fac17adaf74b350d79203f2238db51de2017defa0ebe73ebcf7438b3e370(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwsSecurityOwnerUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33cac5580c916da078aff4164eb9a9e13673fb59156a9df649e775082d5de016(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae2772e7c9c2c0d9cf720d1747d4a7c12be4673c125374fe744434a77333129(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd51f302836b4b3bdbad4c1a1bca674b287b875cb36b3432f7db07f65e7a598(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae0cc8165fe6f06dcf745651ba1474aba06bdc38dca703c571ee28e3480530f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwsSecurityOwnerUsergroup]],
) -> None:
    """Type checking stubs"""
    pass
