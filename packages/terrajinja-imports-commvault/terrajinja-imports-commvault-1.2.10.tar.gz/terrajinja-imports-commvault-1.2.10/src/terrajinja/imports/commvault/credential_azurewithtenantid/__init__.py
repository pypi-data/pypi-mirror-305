'''
# `commvault_credential_azurewithtenantid`

Refer to the Terraform Registry for docs: [`commvault_credential_azurewithtenantid`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid).
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


class CredentialAzurewithtenantid(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantid",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid commvault_credential_azurewithtenantid}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        applicationid: builtins.str,
        applicationsecret: builtins.str,
        environment: builtins.str,
        name: builtins.str,
        tenantid: builtins.str,
        accounttype: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidEndpoints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vendortype: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid commvault_credential_azurewithtenantid} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param applicationid: Unique Azure application ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#applicationid CredentialAzurewithtenantid#applicationid}
        :param applicationsecret: Application secret of Credential and must be in base64 encoded format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#applicationsecret CredentialAzurewithtenantid#applicationsecret}
        :param environment: Azure cloud deployed region [AZURE_CLOUD, AZURE_USGOV, AZURE_GERMANCLOUD, AZURE_CHINACLOUD, AZURE_STACK]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#environment CredentialAzurewithtenantid#environment}
        :param name: Name of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}
        :param tenantid: Unique Azure active directory ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#tenantid CredentialAzurewithtenantid#tenantid}
        :param accounttype: [WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#accounttype CredentialAzurewithtenantid#accounttype}
        :param description: Description of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#description CredentialAzurewithtenantid#description}
        :param endpoints: endpoints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#endpoints CredentialAzurewithtenantid#endpoints}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#security CredentialAzurewithtenantid#security}
        :param vendortype: Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#vendortype CredentialAzurewithtenantid#vendortype}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fee9a11d45d38d94f187426148aa368b1d8bd576f100af39d376d9264926e6b1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CredentialAzurewithtenantidConfig(
            applicationid=applicationid,
            applicationsecret=applicationsecret,
            environment=environment,
            name=name,
            tenantid=tenantid,
            accounttype=accounttype,
            description=description,
            endpoints=endpoints,
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
        '''Generates CDKTF code for importing a CredentialAzurewithtenantid resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CredentialAzurewithtenantid to import.
        :param import_from_id: The id of the existing CredentialAzurewithtenantid that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CredentialAzurewithtenantid to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e57ae1e60e02f1f07743a979434aff30a297500473d2a87e94f7684bd3cce2b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putEndpoints")
    def put_endpoints(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidEndpoints", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71c2fbd67eb3f5d63b778041b1dc9a9b856a2311feb2dbe51699c76ee13cee00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEndpoints", [value]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9145e02031b75ec42d02579daf38de0b0e16e910555f16952f0e1e20a5e67781)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecurity", [value]))

    @jsii.member(jsii_name="resetAccounttype")
    def reset_accounttype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccounttype", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEndpoints")
    def reset_endpoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoints", []))

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
    @jsii.member(jsii_name="endpoints")
    def endpoints(self) -> "CredentialAzurewithtenantidEndpointsList":
        return typing.cast("CredentialAzurewithtenantidEndpointsList", jsii.get(self, "endpoints"))

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> "CredentialAzurewithtenantidSecurityList":
        return typing.cast("CredentialAzurewithtenantidSecurityList", jsii.get(self, "security"))

    @builtins.property
    @jsii.member(jsii_name="accounttypeInput")
    def accounttype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accounttypeInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationidInput")
    def applicationid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationidInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationsecretInput")
    def applicationsecret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationsecretInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsInput")
    def endpoints_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidEndpoints"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidEndpoints"]]], jsii.get(self, "endpointsInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurity"]]], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantidInput")
    def tenantid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantidInput"))

    @builtins.property
    @jsii.member(jsii_name="vendortypeInput")
    def vendortype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendortypeInput"))

    @builtins.property
    @jsii.member(jsii_name="accounttype")
    def accounttype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accounttype"))

    @accounttype.setter
    def accounttype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8b0522438621a76c9b3ff65367a927582ab645516aefad9088a0459cc42168f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accounttype", value)

    @builtins.property
    @jsii.member(jsii_name="applicationid")
    def applicationid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationid"))

    @applicationid.setter
    def applicationid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35fa72cffba46511d13525217247a9c9aeaac4cd30ae6ee1c3df84f366ba5100)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationid", value)

    @builtins.property
    @jsii.member(jsii_name="applicationsecret")
    def applicationsecret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationsecret"))

    @applicationsecret.setter
    def applicationsecret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5492ee2147d6cdf0931d03375b992120f6e225096f82dfdf7222cb9a2f0bb5fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationsecret", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce7e2c03100eca697d7b9e11c3beb8f977044e8472387c83587436e98951962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__756ee78e8a699f88686384b594f6e3cb5956e2ce789fe688578583bd33cc40d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e204d882cdedaa97f54cff18e5276e610537881d0ba37024a094aed807a3b7a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6817f2184c1315100e2a4c27ab346af6236ac5873755d66a2e76b38d1d23927)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tenantid")
    def tenantid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantid"))

    @tenantid.setter
    def tenantid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6732bebd5d9c81ce85ab7aae4bfcb5ff2692e15ee2ac228ef0cdf0907e7a98e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantid", value)

    @builtins.property
    @jsii.member(jsii_name="vendortype")
    def vendortype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendortype"))

    @vendortype.setter
    def vendortype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97f87a3b50a422cc0fc35350f58d0f23022bf7cb984d3e90028d377c8ea4bed5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendortype", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "applicationid": "applicationid",
        "applicationsecret": "applicationsecret",
        "environment": "environment",
        "name": "name",
        "tenantid": "tenantid",
        "accounttype": "accounttype",
        "description": "description",
        "endpoints": "endpoints",
        "id": "id",
        "security": "security",
        "vendortype": "vendortype",
    },
)
class CredentialAzurewithtenantidConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        applicationid: builtins.str,
        applicationsecret: builtins.str,
        environment: builtins.str,
        name: builtins.str,
        tenantid: builtins.str,
        accounttype: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidEndpoints", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param applicationid: Unique Azure application ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#applicationid CredentialAzurewithtenantid#applicationid}
        :param applicationsecret: Application secret of Credential and must be in base64 encoded format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#applicationsecret CredentialAzurewithtenantid#applicationsecret}
        :param environment: Azure cloud deployed region [AZURE_CLOUD, AZURE_USGOV, AZURE_GERMANCLOUD, AZURE_CHINACLOUD, AZURE_STACK]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#environment CredentialAzurewithtenantid#environment}
        :param name: Name of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}
        :param tenantid: Unique Azure active directory ID. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#tenantid CredentialAzurewithtenantid#tenantid}
        :param accounttype: [WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#accounttype CredentialAzurewithtenantid#accounttype}
        :param description: Description of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#description CredentialAzurewithtenantid#description}
        :param endpoints: endpoints block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#endpoints CredentialAzurewithtenantid#endpoints}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#security CredentialAzurewithtenantid#security}
        :param vendortype: Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#vendortype CredentialAzurewithtenantid#vendortype}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bdda5c7ac00dfef2f933db6a51474af2110171497ef4a304a7f3fbaef2de619)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument applicationid", value=applicationid, expected_type=type_hints["applicationid"])
            check_type(argname="argument applicationsecret", value=applicationsecret, expected_type=type_hints["applicationsecret"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tenantid", value=tenantid, expected_type=type_hints["tenantid"])
            check_type(argname="argument accounttype", value=accounttype, expected_type=type_hints["accounttype"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument endpoints", value=endpoints, expected_type=type_hints["endpoints"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument vendortype", value=vendortype, expected_type=type_hints["vendortype"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "applicationid": applicationid,
            "applicationsecret": applicationsecret,
            "environment": environment,
            "name": name,
            "tenantid": tenantid,
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
        if endpoints is not None:
            self._values["endpoints"] = endpoints
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
    def applicationid(self) -> builtins.str:
        '''Unique Azure application ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#applicationid CredentialAzurewithtenantid#applicationid}
        '''
        result = self._values.get("applicationid")
        assert result is not None, "Required property 'applicationid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def applicationsecret(self) -> builtins.str:
        '''Application secret of Credential and must be in base64 encoded format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#applicationsecret CredentialAzurewithtenantid#applicationsecret}
        '''
        result = self._values.get("applicationsecret")
        assert result is not None, "Required property 'applicationsecret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment(self) -> builtins.str:
        '''Azure cloud deployed region [AZURE_CLOUD, AZURE_USGOV, AZURE_GERMANCLOUD, AZURE_CHINACLOUD, AZURE_STACK].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#environment CredentialAzurewithtenantid#environment}
        '''
        result = self._values.get("environment")
        assert result is not None, "Required property 'environment' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenantid(self) -> builtins.str:
        '''Unique Azure active directory ID.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#tenantid CredentialAzurewithtenantid#tenantid}
        '''
        result = self._values.get("tenantid")
        assert result is not None, "Required property 'tenantid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accounttype(self) -> typing.Optional[builtins.str]:
        '''[WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#accounttype CredentialAzurewithtenantid#accounttype}
        '''
        result = self._values.get("accounttype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#description CredentialAzurewithtenantid#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoints(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidEndpoints"]]]:
        '''endpoints block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#endpoints CredentialAzurewithtenantid#endpoints}
        '''
        result = self._values.get("endpoints")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidEndpoints"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurity"]]]:
        '''security block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#security CredentialAzurewithtenantid#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurity"]]], result)

    @builtins.property
    def vendortype(self) -> typing.Optional[builtins.str]:
        '''Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#vendortype CredentialAzurewithtenantid#vendortype}
        '''
        result = self._values.get("vendortype")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidEndpoints",
    jsii_struct_bases=[],
    name_mapping={
        "activedirectory": "activedirectory",
        "resourcemanager": "resourcemanager",
        "storage": "storage",
    },
)
class CredentialAzurewithtenantidEndpoints:
    def __init__(
        self,
        *,
        activedirectory: typing.Optional[builtins.str] = None,
        resourcemanager: typing.Optional[builtins.str] = None,
        storage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param activedirectory: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#activedirectory CredentialAzurewithtenantid#activedirectory}.
        :param resourcemanager: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#resourcemanager CredentialAzurewithtenantid#resourcemanager}.
        :param storage: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#storage CredentialAzurewithtenantid#storage}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__019f2af318a8140963e621432cfb592cf39128d2e8e381fd56903ca6b8033b19)
            check_type(argname="argument activedirectory", value=activedirectory, expected_type=type_hints["activedirectory"])
            check_type(argname="argument resourcemanager", value=resourcemanager, expected_type=type_hints["resourcemanager"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activedirectory is not None:
            self._values["activedirectory"] = activedirectory
        if resourcemanager is not None:
            self._values["resourcemanager"] = resourcemanager
        if storage is not None:
            self._values["storage"] = storage

    @builtins.property
    def activedirectory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#activedirectory CredentialAzurewithtenantid#activedirectory}.'''
        result = self._values.get("activedirectory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resourcemanager(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#resourcemanager CredentialAzurewithtenantid#resourcemanager}.'''
        result = self._values.get("resourcemanager")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#storage CredentialAzurewithtenantid#storage}.'''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidEndpoints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidEndpointsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidEndpointsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8031da8156694df65bdc402479cb70a0a4ba586a1f1f3df07c813b808681757)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidEndpointsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cbc72785dd9f3e69b081591e72d3311a38ccb1b5f230a4bbc89e4394a830c7b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidEndpointsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__262d035d2e3ce23bdb5baacc737b2d1326a3054b6b60fc968e483aac61f2684d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__842d4edd6b29901db1bfcd86223c8e4d3ce206c3dc825a1ead4c574468c929a2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7007e7b6a3e058493a6462957418fb887aeb9b70a61c1949d61d1f400d57f551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidEndpoints]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidEndpoints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidEndpoints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b727ef1a10a8cf541c0c77079a940c3363e745f5863eff163d744f6ec884a156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidEndpointsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidEndpointsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f5d793b9751998f5f788d4656e79a3d300a7479119ef8d4aefbd087f8222a60)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetActivedirectory")
    def reset_activedirectory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivedirectory", []))

    @jsii.member(jsii_name="resetResourcemanager")
    def reset_resourcemanager(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourcemanager", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

    @builtins.property
    @jsii.member(jsii_name="activedirectoryInput")
    def activedirectory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activedirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcemanagerInput")
    def resourcemanager_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourcemanagerInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="activedirectory")
    def activedirectory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activedirectory"))

    @activedirectory.setter
    def activedirectory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71dc6911cc15eb9c65e5aa7df2e704a0ef6aa83ac3ed9b2369562c94c1a7af08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activedirectory", value)

    @builtins.property
    @jsii.member(jsii_name="resourcemanager")
    def resourcemanager(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourcemanager"))

    @resourcemanager.setter
    def resourcemanager(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b13dd378d89a3e539af0b2f2ae5b9cb869298ab936d4d9e14f71f670d4b5451f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourcemanager", value)

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storage"))

    @storage.setter
    def storage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d46a874285ff0f5807222a958caa95c3210b22db99185e4428991f974179004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidEndpoints]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidEndpoints]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidEndpoints]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f663c4754f285c7d4b1821a4f560f8616c81bc243ce3a3430f168039f77c515)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurity",
    jsii_struct_bases=[],
    name_mapping={"associations": "associations", "owner": "owner"},
)
class CredentialAzurewithtenantidSecurity:
    def __init__(
        self,
        *,
        associations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        owner: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityOwner", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param associations: associations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#associations CredentialAzurewithtenantid#associations}
        :param owner: owner block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#owner CredentialAzurewithtenantid#owner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6360b6fab0ebedfea7f92604436b03b48e67cf14e5ccaf4758663d8bbd74d734)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociations"]]]:
        '''associations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#associations CredentialAzurewithtenantid#associations}
        '''
        result = self._values.get("associations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociations"]]], result)

    @builtins.property
    def owner(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwner"]]]:
        '''owner block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#owner CredentialAzurewithtenantid#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwner"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociations",
    jsii_struct_bases=[],
    name_mapping={
        "iscreatorassociation": "iscreatorassociation",
        "permissions": "permissions",
        "user": "user",
        "usergroup": "usergroup",
    },
)
class CredentialAzurewithtenantidSecurityAssociations:
    def __init__(
        self,
        *,
        iscreatorassociation: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociationsPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociationsUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociationsUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param iscreatorassociation: To check if the user/user group associated is the owner. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#iscreatorassociation CredentialAzurewithtenantid#iscreatorassociation}
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#permissions CredentialAzurewithtenantid#permissions}
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#user CredentialAzurewithtenantid#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#usergroup CredentialAzurewithtenantid#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__882ce2a79e8062cb3bd60a17d47242d6747d383b42aa4d6ef8561fe06076b11c)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#iscreatorassociation CredentialAzurewithtenantid#iscreatorassociation}
        '''
        result = self._values.get("iscreatorassociation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsPermissions"]]]:
        '''permissions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#permissions CredentialAzurewithtenantid#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsPermissions"]]], result)

    @builtins.property
    def user(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#user CredentialAzurewithtenantid#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#usergroup CredentialAzurewithtenantid#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidSecurityAssociations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityAssociationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__062c757d1444433e41c1902bb7d58ce30e6fabbad94d494828fdf7c494796a51)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityAssociationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2d80bcc8849d02b2030cabe5ab66b2b7ef6a527d09e0d47a8caeaca288d7998)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8976f185279923cac83c101e2418c299216d0db14c4cfc70cf00f2c71f72a1c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__00895e73cf043ebaefa3cd5d450f625e5e51ccc7cfec986ca2503d99833028b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__009784602e1d218b10d1b52b7d92f7f93748a365dcc46d117af3abb1734a47fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cbb02f3ab742a9a2f75017145a997ddcd3f975b93a4df7738159dd057800b6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityAssociationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a3898dcca8eb7552a1d2e79e67576cd857cf9dd3eae97dc00b9c47aaf15861d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociationsPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa3887c725fdd332b6c26723043c9ec4db4fb33ecdf1f897c9f87b471bd4194f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociationsUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b12efebb0d18c4dcbbe74cb0b45171ab28e51143a183f672410bd43a3ecc5fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityAssociationsUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__989a559a5092141515a7f7352ff071eeebbe340f571c20dc73202026d80bd18b)
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
    def permissions(
        self,
    ) -> "CredentialAzurewithtenantidSecurityAssociationsPermissionsList":
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsPermissionsList", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "CredentialAzurewithtenantidSecurityAssociationsUserList":
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(
        self,
    ) -> "CredentialAzurewithtenantidSecurityAssociationsUsergroupList":
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="iscreatorassociationInput")
    def iscreatorassociation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscreatorassociationInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsPermissions"]]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityAssociationsUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="iscreatorassociation")
    def iscreatorassociation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscreatorassociation"))

    @iscreatorassociation.setter
    def iscreatorassociation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cfa504683c3883d4ce6ef01091d7acb35785fd4f66cbd344eea9ce2311aad21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscreatorassociation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61f989b4fd1958ea111a00ba9d69bc128c080bbe03ac7e1ecee558ddcbee9834)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsPermissions",
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
class CredentialAzurewithtenantidSecurityAssociationsPermissions:
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
        :param categoryid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#categoryid CredentialAzurewithtenantid#categoryid}.
        :param categoryname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#categoryname CredentialAzurewithtenantid#categoryname}.
        :param exclude: Flag to specify if this is included permission or excluded permission. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#exclude CredentialAzurewithtenantid#exclude}
        :param permissionid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#permissionid CredentialAzurewithtenantid#permissionid}.
        :param permissionname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#permissionname CredentialAzurewithtenantid#permissionname}.
        :param type: Returns the type of association. [ALL_CATEGORIES, CATEGORY_ENTITY, PERMISSION_ENTITY]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#type CredentialAzurewithtenantid#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b81885881ae19c1dd15b048709139762fbe8eeecd5b484141e481c47660fd4c9)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#categoryid CredentialAzurewithtenantid#categoryid}.'''
        result = self._values.get("categoryid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def categoryname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#categoryname CredentialAzurewithtenantid#categoryname}.'''
        result = self._values.get("categoryname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if this is included permission or excluded permission.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#exclude CredentialAzurewithtenantid#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissionid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#permissionid CredentialAzurewithtenantid#permissionid}.'''
        result = self._values.get("permissionid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def permissionname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#permissionname CredentialAzurewithtenantid#permissionname}.'''
        result = self._values.get("permissionname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Returns the type of association. [ALL_CATEGORIES, CATEGORY_ENTITY, PERMISSION_ENTITY].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#type CredentialAzurewithtenantid#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidSecurityAssociationsPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityAssociationsPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__efd36c2ab9ab90749207add97c6430f79bc9d111bd0489c22d91f00ab63b43da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityAssociationsPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df07cfd7567ceb165c4da2e146faa5bb20d27c784efd0388cf1e8adf438419b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7278d5834e7301ae9d23437086c8e73ff7b5468708b3f0a93098f749707d253b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4451f32752ae9cbdc88ddc8ef67bbe03587d47377b86850789df2a5b3c0c521f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22492ec5a5c24e4bb828fdb405e2f7a6edad6a9615d760cf6616eca69432b3fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32c832905ddce2e01bd4ce2ce91d4e1800df735beaf6d73f8948fef14d41f9c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityAssociationsPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f45f7f003f052bd1e34c5f1c5d2b068c232b138c387e686e3f839c331033311b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__63476482b502b2da6ad063a0d19c405ee9111ed66f52faffd08cba9c14ff7158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryid", value)

    @builtins.property
    @jsii.member(jsii_name="categoryname")
    def categoryname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "categoryname"))

    @categoryname.setter
    def categoryname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25530e332dcd5897f39c5730906290a96f6b68b687d3b1892862881baa8e6483)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryname", value)

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d072b5d2a78fd51914acbc624227a1b9087e4b131b3342d43554a2d56e3a2ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="permissionid")
    def permissionid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "permissionid"))

    @permissionid.setter
    def permissionid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9489ad3e9f82fde46ae7e3f4780eccc06ccf995fe34751ff6685c9ca36d6c47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionid", value)

    @builtins.property
    @jsii.member(jsii_name="permissionname")
    def permissionname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionname"))

    @permissionname.setter
    def permissionname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__257dcf9ed9466ffb69fd3b48e711e28c3b8f796dc90004400793ac2bf2b73731)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionname", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cefc5de2c9c61db75f79203aea134e7bd099aa6712770a4b9d1d6c6c758fbf3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsPermissions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsPermissions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsPermissions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde32370c046d5fcf462b639a7c8f61ebf916263abb8ff3770308634a95b6f72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class CredentialAzurewithtenantidSecurityAssociationsUser:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57dc2f23ab4afc8394f6acf4e338f92302aaec3e5a25947f624193208dd2768c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}.

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
        return "CredentialAzurewithtenantidSecurityAssociationsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityAssociationsUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1941fb1deb8a1257733baf170b189acd2b46c16a78e2108f5ee2b51c468fd269)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityAssociationsUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be527d08268b24a6f9ac42305ad77a164c95008ff237a65c47d66747facca886)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a402f950b40b05e689f74804080afaa0287b029390da5e8bc95f20a8b9429a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__58d329399eb97ed9c1db45fc6eb7994e7b42071709014c4f5aacf7bd07ee45be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3a6325301460668eeb49c1bde9fef3e4174f3e5743c9ffec633c24c6cb6d2e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4ea2371ae3635a3e5a10cd133a6203c613083b532f56cb23dd4202733d9db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityAssociationsUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f85bc05d903d5e25667db5a96dd0423671f067fc439b235ef8b42fbc81d5399d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3d6e9fa98be70a0214e78e5b74e8e3d50d1b6f605809f5f4eb62ded62ae3da2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f50148180609b845c1a2bdfe1a852d427b380ca98bb2acada57ff3bd185c3073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class CredentialAzurewithtenantidSecurityAssociationsUsergroup:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7b1f05dd4c3d564f736445048e09a33eb18acfdf4ee89d6e15ee015a3deef90)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}.

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
        return "CredentialAzurewithtenantidSecurityAssociationsUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityAssociationsUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7724a02df04cc09e2410b4dc45c0825bbee71f226c560f9bb729dc5bfb019a5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityAssociationsUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1863495c8b92848415f9c1f6423ad18146458502a34ad131806fffb63d7fa6e1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityAssociationsUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0053520e2a8ca7be0a28d362ac1f2cfa69ef07f85d95075e3d3276802b7a0193)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b58ff8e5eb23ca2cb02e1c448875be795a06c6681b25bf4f3ca27b177aebc746)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e77359ce69f2162a4525060740b8c89f7e0b1e65dd63c80852519fece90f9ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a487452ecd21136e6cdd7d64c32d1bfc6128830d71e65a2386956093a7a98566)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityAssociationsUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityAssociationsUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__32b246698fe63e247b1df5d5dfb588171b15875abec21d358439164499fd039f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4da1421db91749031959b2e81daba006703ee4ffdd389e754c6c6ff996b98c89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20625883c213ba5aa58d628486b365b2d67b431d0c4c33551bfa0ae0c3230a47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9cbe68b260c908c78dbdda08fc46c7f9eb0689b9ec79b5ebfd371b43f6472633)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da829103b82bf9f0c7ace858ee5f1f7b29e6d4a0cff02062cdc77f5c78f37a07)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e7aeeb1f97aafb750926f9a109194fc36968f77f83e205fcbfaa8f4c66a653d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__246c044a540f87bfb2ef3e79c697d990f9ae8924dae2eb05453e3b58f7ac5b50)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c01128fe7ce98d288b9ad5ba31ab17404d5b812a1b7bcc8b70dd568c8a8d888a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88c1e17c2e29790c2decea028605b85b597c89ccba15bd567b7584c6cf23c61c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__879f55d9796a2cb6cda6b9e002de3619678a68bc9331c4576b5f32b0783dc5ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssociations")
    def put_associations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a42f8c57b5a0434fe437956b806a5f55032648ebe06fb801dc557573daae8fa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssociations", [value]))

    @jsii.member(jsii_name="putOwner")
    def put_owner(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityOwner", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f06f6f7605c418d883b2ce590edd766e5fbf1464946454580b203048a5690182)
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
    def associations(self) -> CredentialAzurewithtenantidSecurityAssociationsList:
        return typing.cast(CredentialAzurewithtenantidSecurityAssociationsList, jsii.get(self, "associations"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> "CredentialAzurewithtenantidSecurityOwnerList":
        return typing.cast("CredentialAzurewithtenantidSecurityOwnerList", jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="associationsInput")
    def associations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociations]]], jsii.get(self, "associationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwner"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwner"]]], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1489fcb56dd27613ee21f22005b41a6456c027ad93ab402f6252eaf10a0419fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwner",
    jsii_struct_bases=[],
    name_mapping={"user": "user", "usergroup": "usergroup"},
)
class CredentialAzurewithtenantidSecurityOwner:
    def __init__(
        self,
        *,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityOwnerUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityOwnerUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#user CredentialAzurewithtenantid#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#usergroup CredentialAzurewithtenantid#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ed4116060a4bd134f6d9af0dcbcbe7366ebb6da54aa4b7b59b4e7751eb86271)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#user CredentialAzurewithtenantid#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#usergroup CredentialAzurewithtenantid#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidSecurityOwner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityOwnerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b584c57966e3a1384971f2b130f4a4b5d0daeb127cac14fd0ff71ce585eea6ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityOwnerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa97d2be3d06718bdc7e85c384b362eb74a208839624e3788bb0f66ccdf3b155)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityOwnerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__363232a3c06be0a8cfa0cc441b99e9933af4c1f4d8d81939a4865a61336756cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__525f012a54e8ecab4b7cfd794b2fc262f9dbf48feef3de16f9b137503c244ba7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90572a48e4e91febffe5003e2e62f429405e09bdd46bc1ecaaba2b6e5145fd34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwner]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwner]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwner]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a01f3942103f8ca338a1e958c59be63727eabb9448ce6a9b476f87acd7cf429e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityOwnerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1ff72f9c7a3f2153909b13a27dd265fa23eb36bfb3af0b02c71197d7b9133b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityOwnerUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8049f8688b3088387a3580c0f71e280854b869f05f53b79af1d9acafff2896)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAzurewithtenantidSecurityOwnerUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aafa7a26c9955b1b1b24c779f7db689688ae05fc76f6d08f0ad35795b7f2a88)
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
    def user(self) -> "CredentialAzurewithtenantidSecurityOwnerUserList":
        return typing.cast("CredentialAzurewithtenantidSecurityOwnerUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(self) -> "CredentialAzurewithtenantidSecurityOwnerUsergroupList":
        return typing.cast("CredentialAzurewithtenantidSecurityOwnerUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAzurewithtenantidSecurityOwnerUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwner]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwner]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwner]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6b3867642ac19bbb5a8b6c9e69fbc8939153dd1c0f4175591ce7a08a1a45965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class CredentialAzurewithtenantidSecurityOwnerUser:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa3b9212380b58100cba6ea14e911b4662a1a0e31cec5dcaa00bb4724b622f83)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidSecurityOwnerUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityOwnerUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0e23559f48bb6f832ff42ea723982dfde997a09ee917cdc4c422fac2269def6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityOwnerUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbcd7d6962403b1beb33c8c05aabcd3056bf271b09b282cc6a258bed443687a9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityOwnerUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__090437c104d245eb37cf9338d15e68d674c53b8821819c7bd9b8446ef57241c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3f706a25a87bf01c6f6ee88b00133258dd3b728cb566a0570f6804e4fbf0a49)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ee6e0b46ea111fb70acaa7325ffff28491917581b43158225704e3f0f219e034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58a60e01043e0c129cb0b4be967b55248ce8fb28247ae100c7680340327e9577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityOwnerUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f0865ae77afca2120208668c601fd00d69aa2e9fd2dbb34258c13c8106508b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce26e5a040e656941306864e283b86040c8eb596f27a05d630bed0933d99e8bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d321f7cea15ed56744071fb70f37cc7b3fc2428cde36177709db95a08055fe0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a3f0c21305fa90f2101d72cc8d661c11d0a6bf7548d2569518d0115536c6bcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class CredentialAzurewithtenantidSecurityOwnerUsergroup:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240a795d7189b2d9f2271040ef8f4664716c4752d8d26e55978f4aff5f79f112)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#id CredentialAzurewithtenantid#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_azurewithtenantid#name CredentialAzurewithtenantid#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAzurewithtenantidSecurityOwnerUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAzurewithtenantidSecurityOwnerUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc695a993d4731c8570370917bfaad745c8f6bf2662e57eb9a447cd5728d02b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAzurewithtenantidSecurityOwnerUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01eb3a42dad22a41cdebda9a29ec2b6027a37f14c7772100b4091c1ae20c50ef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAzurewithtenantidSecurityOwnerUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc9b8a16b663c804b57a9c5fa5f87e3c8ca364c0d2e0783f1701cb46a1fae517)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d190d3471ef184faca0d93aa676fe0f860749d45e1a372317b44e55f10ac2e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b69ac8076c2f73d0e071885087837e10e977e080fe6e5fad316140a58c41bf48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__781b8ec1e6f58393865fd2802513ab172fa29366cfcb38249d1a3de1f0a50b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAzurewithtenantidSecurityOwnerUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAzurewithtenantid.CredentialAzurewithtenantidSecurityOwnerUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f742f811c37c123aea037741ef24508dc26cfc7853a7fae0f3f2ce4f160c1a8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__766ba316708ff5b360550bd91e94b3cbbf3441845d56cc252b99f42771febc28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0f9d1450d37715846616db43aef8e39e370171d9459c065c04c7e18ae4dad7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b733d97aff4c9d1059036fe8acebb9ed3d6da603c94ce604357fb5cd2cf5b895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CredentialAzurewithtenantid",
    "CredentialAzurewithtenantidConfig",
    "CredentialAzurewithtenantidEndpoints",
    "CredentialAzurewithtenantidEndpointsList",
    "CredentialAzurewithtenantidEndpointsOutputReference",
    "CredentialAzurewithtenantidSecurity",
    "CredentialAzurewithtenantidSecurityAssociations",
    "CredentialAzurewithtenantidSecurityAssociationsList",
    "CredentialAzurewithtenantidSecurityAssociationsOutputReference",
    "CredentialAzurewithtenantidSecurityAssociationsPermissions",
    "CredentialAzurewithtenantidSecurityAssociationsPermissionsList",
    "CredentialAzurewithtenantidSecurityAssociationsPermissionsOutputReference",
    "CredentialAzurewithtenantidSecurityAssociationsUser",
    "CredentialAzurewithtenantidSecurityAssociationsUserList",
    "CredentialAzurewithtenantidSecurityAssociationsUserOutputReference",
    "CredentialAzurewithtenantidSecurityAssociationsUsergroup",
    "CredentialAzurewithtenantidSecurityAssociationsUsergroupList",
    "CredentialAzurewithtenantidSecurityAssociationsUsergroupOutputReference",
    "CredentialAzurewithtenantidSecurityList",
    "CredentialAzurewithtenantidSecurityOutputReference",
    "CredentialAzurewithtenantidSecurityOwner",
    "CredentialAzurewithtenantidSecurityOwnerList",
    "CredentialAzurewithtenantidSecurityOwnerOutputReference",
    "CredentialAzurewithtenantidSecurityOwnerUser",
    "CredentialAzurewithtenantidSecurityOwnerUserList",
    "CredentialAzurewithtenantidSecurityOwnerUserOutputReference",
    "CredentialAzurewithtenantidSecurityOwnerUsergroup",
    "CredentialAzurewithtenantidSecurityOwnerUsergroupList",
    "CredentialAzurewithtenantidSecurityOwnerUsergroupOutputReference",
]

publication.publish()

def _typecheckingstub__fee9a11d45d38d94f187426148aa368b1d8bd576f100af39d376d9264926e6b1(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    applicationid: builtins.str,
    applicationsecret: builtins.str,
    environment: builtins.str,
    name: builtins.str,
    tenantid: builtins.str,
    accounttype: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__4e57ae1e60e02f1f07743a979434aff30a297500473d2a87e94f7684bd3cce2b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c2fbd67eb3f5d63b778041b1dc9a9b856a2311feb2dbe51699c76ee13cee00(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidEndpoints, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9145e02031b75ec42d02579daf38de0b0e16e910555f16952f0e1e20a5e67781(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8b0522438621a76c9b3ff65367a927582ab645516aefad9088a0459cc42168f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35fa72cffba46511d13525217247a9c9aeaac4cd30ae6ee1c3df84f366ba5100(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5492ee2147d6cdf0931d03375b992120f6e225096f82dfdf7222cb9a2f0bb5fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce7e2c03100eca697d7b9e11c3beb8f977044e8472387c83587436e98951962(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756ee78e8a699f88686384b594f6e3cb5956e2ce789fe688578583bd33cc40d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e204d882cdedaa97f54cff18e5276e610537881d0ba37024a094aed807a3b7a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6817f2184c1315100e2a4c27ab346af6236ac5873755d66a2e76b38d1d23927(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6732bebd5d9c81ce85ab7aae4bfcb5ff2692e15ee2ac228ef0cdf0907e7a98e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97f87a3b50a422cc0fc35350f58d0f23022bf7cb984d3e90028d377c8ea4bed5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bdda5c7ac00dfef2f933db6a51474af2110171497ef4a304a7f3fbaef2de619(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    applicationid: builtins.str,
    applicationsecret: builtins.str,
    environment: builtins.str,
    name: builtins.str,
    tenantid: builtins.str,
    accounttype: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    endpoints: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidEndpoints, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vendortype: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__019f2af318a8140963e621432cfb592cf39128d2e8e381fd56903ca6b8033b19(
    *,
    activedirectory: typing.Optional[builtins.str] = None,
    resourcemanager: typing.Optional[builtins.str] = None,
    storage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8031da8156694df65bdc402479cb70a0a4ba586a1f1f3df07c813b808681757(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cbc72785dd9f3e69b081591e72d3311a38ccb1b5f230a4bbc89e4394a830c7b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__262d035d2e3ce23bdb5baacc737b2d1326a3054b6b60fc968e483aac61f2684d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__842d4edd6b29901db1bfcd86223c8e4d3ce206c3dc825a1ead4c574468c929a2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7007e7b6a3e058493a6462957418fb887aeb9b70a61c1949d61d1f400d57f551(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b727ef1a10a8cf541c0c77079a940c3363e745f5863eff163d744f6ec884a156(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidEndpoints]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f5d793b9751998f5f788d4656e79a3d300a7479119ef8d4aefbd087f8222a60(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71dc6911cc15eb9c65e5aa7df2e704a0ef6aa83ac3ed9b2369562c94c1a7af08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b13dd378d89a3e539af0b2f2ae5b9cb869298ab936d4d9e14f71f670d4b5451f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d46a874285ff0f5807222a958caa95c3210b22db99185e4428991f974179004(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f663c4754f285c7d4b1821a4f560f8616c81bc243ce3a3430f168039f77c515(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidEndpoints]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6360b6fab0ebedfea7f92604436b03b48e67cf14e5ccaf4758663d8bbd74d734(
    *,
    associations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    owner: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityOwner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__882ce2a79e8062cb3bd60a17d47242d6747d383b42aa4d6ef8561fe06076b11c(
    *,
    iscreatorassociation: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociationsPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociationsUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociationsUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__062c757d1444433e41c1902bb7d58ce30e6fabbad94d494828fdf7c494796a51(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2d80bcc8849d02b2030cabe5ab66b2b7ef6a527d09e0d47a8caeaca288d7998(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8976f185279923cac83c101e2418c299216d0db14c4cfc70cf00f2c71f72a1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00895e73cf043ebaefa3cd5d450f625e5e51ccc7cfec986ca2503d99833028b8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009784602e1d218b10d1b52b7d92f7f93748a365dcc46d117af3abb1734a47fc(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cbb02f3ab742a9a2f75017145a997ddcd3f975b93a4df7738159dd057800b6f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a3898dcca8eb7552a1d2e79e67576cd857cf9dd3eae97dc00b9c47aaf15861d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa3887c725fdd332b6c26723043c9ec4db4fb33ecdf1f897c9f87b471bd4194f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociationsPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b12efebb0d18c4dcbbe74cb0b45171ab28e51143a183f672410bd43a3ecc5fa(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociationsUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__989a559a5092141515a7f7352ff071eeebbe340f571c20dc73202026d80bd18b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociationsUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cfa504683c3883d4ce6ef01091d7acb35785fd4f66cbd344eea9ce2311aad21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61f989b4fd1958ea111a00ba9d69bc128c080bbe03ac7e1ecee558ddcbee9834(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b81885881ae19c1dd15b048709139762fbe8eeecd5b484141e481c47660fd4c9(
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

def _typecheckingstub__efd36c2ab9ab90749207add97c6430f79bc9d111bd0489c22d91f00ab63b43da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df07cfd7567ceb165c4da2e146faa5bb20d27c784efd0388cf1e8adf438419b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7278d5834e7301ae9d23437086c8e73ff7b5468708b3f0a93098f749707d253b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4451f32752ae9cbdc88ddc8ef67bbe03587d47377b86850789df2a5b3c0c521f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22492ec5a5c24e4bb828fdb405e2f7a6edad6a9615d760cf6616eca69432b3fe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32c832905ddce2e01bd4ce2ce91d4e1800df735beaf6d73f8948fef14d41f9c1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f45f7f003f052bd1e34c5f1c5d2b068c232b138c387e686e3f839c331033311b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63476482b502b2da6ad063a0d19c405ee9111ed66f52faffd08cba9c14ff7158(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25530e332dcd5897f39c5730906290a96f6b68b687d3b1892862881baa8e6483(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d072b5d2a78fd51914acbc624227a1b9087e4b131b3342d43554a2d56e3a2ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9489ad3e9f82fde46ae7e3f4780eccc06ccf995fe34751ff6685c9ca36d6c47(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257dcf9ed9466ffb69fd3b48e711e28c3b8f796dc90004400793ac2bf2b73731(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cefc5de2c9c61db75f79203aea134e7bd099aa6712770a4b9d1d6c6c758fbf3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde32370c046d5fcf462b639a7c8f61ebf916263abb8ff3770308634a95b6f72(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsPermissions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57dc2f23ab4afc8394f6acf4e338f92302aaec3e5a25947f624193208dd2768c(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1941fb1deb8a1257733baf170b189acd2b46c16a78e2108f5ee2b51c468fd269(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be527d08268b24a6f9ac42305ad77a164c95008ff237a65c47d66747facca886(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a402f950b40b05e689f74804080afaa0287b029390da5e8bc95f20a8b9429a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d329399eb97ed9c1db45fc6eb7994e7b42071709014c4f5aacf7bd07ee45be(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3a6325301460668eeb49c1bde9fef3e4174f3e5743c9ffec633c24c6cb6d2e4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4ea2371ae3635a3e5a10cd133a6203c613083b532f56cb23dd4202733d9db4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85bc05d903d5e25667db5a96dd0423671f067fc439b235ef8b42fbc81d5399d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d6e9fa98be70a0214e78e5b74e8e3d50d1b6f605809f5f4eb62ded62ae3da2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f50148180609b845c1a2bdfe1a852d427b380ca98bb2acada57ff3bd185c3073(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b1f05dd4c3d564f736445048e09a33eb18acfdf4ee89d6e15ee015a3deef90(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7724a02df04cc09e2410b4dc45c0825bbee71f226c560f9bb729dc5bfb019a5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1863495c8b92848415f9c1f6423ad18146458502a34ad131806fffb63d7fa6e1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0053520e2a8ca7be0a28d362ac1f2cfa69ef07f85d95075e3d3276802b7a0193(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b58ff8e5eb23ca2cb02e1c448875be795a06c6681b25bf4f3ca27b177aebc746(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e77359ce69f2162a4525060740b8c89f7e0b1e65dd63c80852519fece90f9ee(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a487452ecd21136e6cdd7d64c32d1bfc6128830d71e65a2386956093a7a98566(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityAssociationsUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b246698fe63e247b1df5d5dfb588171b15875abec21d358439164499fd039f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4da1421db91749031959b2e81daba006703ee4ffdd389e754c6c6ff996b98c89(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20625883c213ba5aa58d628486b365b2d67b431d0c4c33551bfa0ae0c3230a47(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityAssociationsUsergroup]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cbe68b260c908c78dbdda08fc46c7f9eb0689b9ec79b5ebfd371b43f6472633(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da829103b82bf9f0c7ace858ee5f1f7b29e6d4a0cff02062cdc77f5c78f37a07(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7aeeb1f97aafb750926f9a109194fc36968f77f83e205fcbfaa8f4c66a653d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__246c044a540f87bfb2ef3e79c697d990f9ae8924dae2eb05453e3b58f7ac5b50(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01128fe7ce98d288b9ad5ba31ab17404d5b812a1b7bcc8b70dd568c8a8d888a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88c1e17c2e29790c2decea028605b85b597c89ccba15bd567b7584c6cf23c61c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__879f55d9796a2cb6cda6b9e002de3619678a68bc9331c4576b5f32b0783dc5ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42f8c57b5a0434fe437956b806a5f55032648ebe06fb801dc557573daae8fa0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f06f6f7605c418d883b2ce590edd766e5fbf1464946454580b203048a5690182(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityOwner, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1489fcb56dd27613ee21f22005b41a6456c027ad93ab402f6252eaf10a0419fa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ed4116060a4bd134f6d9af0dcbcbe7366ebb6da54aa4b7b59b4e7751eb86271(
    *,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityOwnerUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityOwnerUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b584c57966e3a1384971f2b130f4a4b5d0daeb127cac14fd0ff71ce585eea6ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa97d2be3d06718bdc7e85c384b362eb74a208839624e3788bb0f66ccdf3b155(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363232a3c06be0a8cfa0cc441b99e9933af4c1f4d8d81939a4865a61336756cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__525f012a54e8ecab4b7cfd794b2fc262f9dbf48feef3de16f9b137503c244ba7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90572a48e4e91febffe5003e2e62f429405e09bdd46bc1ecaaba2b6e5145fd34(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a01f3942103f8ca338a1e958c59be63727eabb9448ce6a9b476f87acd7cf429e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwner]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ff72f9c7a3f2153909b13a27dd265fa23eb36bfb3af0b02c71197d7b9133b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8049f8688b3088387a3580c0f71e280854b869f05f53b79af1d9acafff2896(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityOwnerUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aafa7a26c9955b1b1b24c779f7db689688ae05fc76f6d08f0ad35795b7f2a88(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAzurewithtenantidSecurityOwnerUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6b3867642ac19bbb5a8b6c9e69fbc8939153dd1c0f4175591ce7a08a1a45965(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwner]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa3b9212380b58100cba6ea14e911b4662a1a0e31cec5dcaa00bb4724b622f83(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e23559f48bb6f832ff42ea723982dfde997a09ee917cdc4c422fac2269def6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbcd7d6962403b1beb33c8c05aabcd3056bf271b09b282cc6a258bed443687a9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__090437c104d245eb37cf9338d15e68d674c53b8821819c7bd9b8446ef57241c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3f706a25a87bf01c6f6ee88b00133258dd3b728cb566a0570f6804e4fbf0a49(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6e0b46ea111fb70acaa7325ffff28491917581b43158225704e3f0f219e034(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a60e01043e0c129cb0b4be967b55248ce8fb28247ae100c7680340327e9577(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f0865ae77afca2120208668c601fd00d69aa2e9fd2dbb34258c13c8106508b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce26e5a040e656941306864e283b86040c8eb596f27a05d630bed0933d99e8bd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d321f7cea15ed56744071fb70f37cc7b3fc2428cde36177709db95a08055fe0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3f0c21305fa90f2101d72cc8d661c11d0a6bf7548d2569518d0115536c6bcd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240a795d7189b2d9f2271040ef8f4664716c4752d8d26e55978f4aff5f79f112(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc695a993d4731c8570370917bfaad745c8f6bf2662e57eb9a447cd5728d02b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01eb3a42dad22a41cdebda9a29ec2b6027a37f14c7772100b4091c1ae20c50ef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9b8a16b663c804b57a9c5fa5f87e3c8ca364c0d2e0783f1701cb46a1fae517(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d190d3471ef184faca0d93aa676fe0f860749d45e1a372317b44e55f10ac2e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69ac8076c2f73d0e071885087837e10e977e080fe6e5fad316140a58c41bf48(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__781b8ec1e6f58393865fd2802513ab172fa29366cfcb38249d1a3de1f0a50b09(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAzurewithtenantidSecurityOwnerUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f742f811c37c123aea037741ef24508dc26cfc7853a7fae0f3f2ce4f160c1a8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766ba316708ff5b360550bd91e94b3cbbf3441845d56cc252b99f42771febc28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0f9d1450d37715846616db43aef8e39e370171d9459c065c04c7e18ae4dad7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b733d97aff4c9d1059036fe8acebb9ed3d6da603c94ce604357fb5cd2cf5b895(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAzurewithtenantidSecurityOwnerUsergroup]],
) -> None:
    """Type checking stubs"""
    pass
