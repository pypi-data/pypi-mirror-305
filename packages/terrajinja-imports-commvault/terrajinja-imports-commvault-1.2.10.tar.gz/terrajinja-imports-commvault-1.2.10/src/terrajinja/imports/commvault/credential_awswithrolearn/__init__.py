'''
# `commvault_credential_awswithrolearn`

Refer to the Terraform Registry for docs: [`commvault_credential_awswithrolearn`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn).
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


class CredentialAwswithrolearn(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearn",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn commvault_credential_awswithrolearn}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        rolearn: builtins.str,
        accounttype: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vendortype: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn commvault_credential_awswithrolearn} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}
        :param rolearn: Role ARN of credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#rolearn CredentialAwswithrolearn#rolearn}
        :param accounttype: [WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#accounttype CredentialAwswithrolearn#accounttype}
        :param description: Description of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#description CredentialAwswithrolearn#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Role ARN of credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#password CredentialAwswithrolearn#password}
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#security CredentialAwswithrolearn#security}
        :param vendortype: Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#vendortype CredentialAwswithrolearn#vendortype}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57517280cc2fc7b9382c1a3c7645691dcbf6a0973798986e4f692a0724384f7a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CredentialAwswithrolearnConfig(
            name=name,
            rolearn=rolearn,
            accounttype=accounttype,
            description=description,
            id=id,
            password=password,
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
        '''Generates CDKTF code for importing a CredentialAwswithrolearn resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the CredentialAwswithrolearn to import.
        :param import_from_id: The id of the existing CredentialAwswithrolearn that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the CredentialAwswithrolearn to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f888dfc95e361895b52378acb9bbf4b2be85389ad028380426f4b2547b813ad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4723e26112a6f07892d04e90d6c21119f770f2bba03dacc5860956a1672c44e)
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

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

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
    def security(self) -> "CredentialAwswithrolearnSecurityList":
        return typing.cast("CredentialAwswithrolearnSecurityList", jsii.get(self, "security"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="rolearnInput")
    def rolearn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rolearnInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurity"]]], jsii.get(self, "securityInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__759e054727815b032e871b353d386b71ab890bfd309aecad445f7717bc5b64ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accounttype", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e8021e5e1ab5d9c96e929961471b66eae74b5d54d1c2e7aba88d4bb88483e0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08be5c1c514c8014650975eff909b97a4eea0ede5c5610b5a5a42dd73cddb2eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d73e4f10f89a99eee311d4fcb78ec36d932a9b9c436fc4573e510558aa6e55cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa669c1131e511f58cb5332600b88f3d1cf4ad8c184dfb27e3002275deec11e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="rolearn")
    def rolearn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rolearn"))

    @rolearn.setter
    def rolearn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeed83720edfb18e0aafd2803586315298a0f6111e1cd76ade73c149b12c9e2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rolearn", value)

    @builtins.property
    @jsii.member(jsii_name="vendortype")
    def vendortype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendortype"))

    @vendortype.setter
    def vendortype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9de9c651ddf57c77e69b8a3fff33511e6282025bb95a28721d45348fe151a22d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendortype", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "rolearn": "rolearn",
        "accounttype": "accounttype",
        "description": "description",
        "id": "id",
        "password": "password",
        "security": "security",
        "vendortype": "vendortype",
    },
)
class CredentialAwswithrolearnConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        rolearn: builtins.str,
        accounttype: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
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
        :param name: Name of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}
        :param rolearn: Role ARN of credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#rolearn CredentialAwswithrolearn#rolearn}
        :param accounttype: [WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#accounttype CredentialAwswithrolearn#accounttype}
        :param description: Description of Credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#description CredentialAwswithrolearn#description}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Role ARN of credential. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#password CredentialAwswithrolearn#password}
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#security CredentialAwswithrolearn#security}
        :param vendortype: Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#vendortype CredentialAwswithrolearn#vendortype}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9563aa14f482363956cb20d27dfa712fc41f8499b7e6e59ef026142cf670676)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rolearn", value=rolearn, expected_type=type_hints["rolearn"])
            check_type(argname="argument accounttype", value=accounttype, expected_type=type_hints["accounttype"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument vendortype", value=vendortype, expected_type=type_hints["vendortype"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rolearn": rolearn,
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
        if password is not None:
            self._values["password"] = password
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
    def name(self) -> builtins.str:
        '''Name of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rolearn(self) -> builtins.str:
        '''Role ARN of credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#rolearn CredentialAwswithrolearn#rolearn}
        '''
        result = self._values.get("rolearn")
        assert result is not None, "Required property 'rolearn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accounttype(self) -> typing.Optional[builtins.str]:
        '''[WINDOWSACCOUNT, LINUXACCOUNT, STORAGE_ARRAY_ACCOUNT, CLOUD_ACCOUNT].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#accounttype CredentialAwswithrolearn#accounttype}
        '''
        result = self._values.get("accounttype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of Credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#description CredentialAwswithrolearn#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Role ARN of credential.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#password CredentialAwswithrolearn#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurity"]]]:
        '''security block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#security CredentialAwswithrolearn#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurity"]]], result)

    @builtins.property
    def vendortype(self) -> typing.Optional[builtins.str]:
        '''Cloud vendor types appilcable only for Cloud Account type [ALICLOUD_OSS, AMAZON_GLACIER, AMAZON, ATT_SYNAPTIC, REVERA_VAULT, CEPH_OBJECT_GATEWAY_S3, CMCC_ONEST, CLOUDIAN_HYPERSTORE, DELL_EMC_ECS_S3, EMC_ATMOS, FUJITSU_STORAGE_ETERNUS, GOOGLE_CLOUD, HDS_HCP, HITACHI_VANTARA_HCP_S3, HUAWEI_OSS, IBM_CLOUD, IBM_CLOUD_S3, INSPUR_CLOUD, IRON_MOUNTAIN_CLOUD, KINGSOFT_KS3, MICROSOFT_AZURE_TYPE, NETAPP_STORAGEGRID, NUTANIX_BUCKETS, OPENSTACK, AMPLIDATA, RACKSPACE_CLOUD_FILES, S3_COMPATIBLE, SALESFORCE_CONNECTED_APP, SCALITY_RING, TELEFONICA_OPEN_CLOUD_OBJECT_STORAGE, VERIZON_CLOUD, WASABI_HOT_CLOUD_STORAGE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#vendortype CredentialAwswithrolearn#vendortype}
        '''
        result = self._values.get("vendortype")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurity",
    jsii_struct_bases=[],
    name_mapping={"associations": "associations", "owner": "owner"},
)
class CredentialAwswithrolearnSecurity:
    def __init__(
        self,
        *,
        associations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        owner: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityOwner", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param associations: associations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#associations CredentialAwswithrolearn#associations}
        :param owner: owner block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#owner CredentialAwswithrolearn#owner}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd6c9d1135f96a9638611442b4251b8cdd1f0a233ee74b0d5750af214a512be)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociations"]]]:
        '''associations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#associations CredentialAwswithrolearn#associations}
        '''
        result = self._values.get("associations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociations"]]], result)

    @builtins.property
    def owner(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwner"]]]:
        '''owner block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#owner CredentialAwswithrolearn#owner}
        '''
        result = self._values.get("owner")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwner"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociations",
    jsii_struct_bases=[],
    name_mapping={
        "iscreatorassociation": "iscreatorassociation",
        "permissions": "permissions",
        "user": "user",
        "usergroup": "usergroup",
    },
)
class CredentialAwswithrolearnSecurityAssociations:
    def __init__(
        self,
        *,
        iscreatorassociation: typing.Optional[builtins.str] = None,
        permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociationsPermissions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociationsUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociationsUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param iscreatorassociation: To check if the user/user group associated is the owner. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#iscreatorassociation CredentialAwswithrolearn#iscreatorassociation}
        :param permissions: permissions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#permissions CredentialAwswithrolearn#permissions}
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#user CredentialAwswithrolearn#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#usergroup CredentialAwswithrolearn#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__640c9384dc3efab3b06b7b4c3e0413d8e253017b5fbdb0a28ae8c0ebbe68d7f7)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#iscreatorassociation CredentialAwswithrolearn#iscreatorassociation}
        '''
        result = self._values.get("iscreatorassociation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsPermissions"]]]:
        '''permissions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#permissions CredentialAwswithrolearn#permissions}
        '''
        result = self._values.get("permissions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsPermissions"]]], result)

    @builtins.property
    def user(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#user CredentialAwswithrolearn#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#usergroup CredentialAwswithrolearn#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnSecurityAssociations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityAssociationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cd1f33ea3e24ec26a2aef0e7a6cbbc69c28c917d86e9499999afd8421c2a141)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityAssociationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8796d27191b1a497e8eae065f688a80306cbdfb147a50798f7b3d39a29b99060)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bfabc662a878744f18bcc1ff8b126e0178101f7f35b408bae0fc092a21192c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31073c41cfaa63344ddd4c79984531bdfff181844b660e0ca6d4c999e48fd3db)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1c25d75dc3f7d2e9fd99d14ebb0e7f35ede79c2ade2b1cd00c81fedb998f8af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fa4ec8e8819a3f67f11c0d9e87f6ae06485ffcc7294fd90fbedb12c48ec7e43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityAssociationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cdafe63cd2855572c089b65d2505689f10e4fbd52747ca665271db37f06df89)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPermissions")
    def put_permissions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociationsPermissions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69a4a0e2add9d9772c4dfd64925579f691de3b17ae62c724016e3bfc3dce790e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPermissions", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociationsUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5810a8c290fe067bc0f3d60afccf9c560264086176347f5e8b745165495241fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityAssociationsUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0b50f7dacd1348b27f703b896c5ed2e4f7cc1debaecfef17f3a856ed137d698)
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
    ) -> "CredentialAwswithrolearnSecurityAssociationsPermissionsList":
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsPermissionsList", jsii.get(self, "permissions"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "CredentialAwswithrolearnSecurityAssociationsUserList":
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(self) -> "CredentialAwswithrolearnSecurityAssociationsUsergroupList":
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="iscreatorassociationInput")
    def iscreatorassociation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscreatorassociationInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionsInput")
    def permissions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsPermissions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsPermissions"]]], jsii.get(self, "permissionsInput"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityAssociationsUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="iscreatorassociation")
    def iscreatorassociation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscreatorassociation"))

    @iscreatorassociation.setter
    def iscreatorassociation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e4656c23fc1e4f4c20bc45653ff613ac229b7f476a4ccadf465e4a54e79194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscreatorassociation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f139adc36af3612e294f9e4365c788f3a399c87bac5acc01195ad19c10db1a32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsPermissions",
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
class CredentialAwswithrolearnSecurityAssociationsPermissions:
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
        :param categoryid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#categoryid CredentialAwswithrolearn#categoryid}.
        :param categoryname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#categoryname CredentialAwswithrolearn#categoryname}.
        :param exclude: Flag to specify if this is included permission or excluded permission. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#exclude CredentialAwswithrolearn#exclude}
        :param permissionid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#permissionid CredentialAwswithrolearn#permissionid}.
        :param permissionname: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#permissionname CredentialAwswithrolearn#permissionname}.
        :param type: Returns the type of association. [ALL_CATEGORIES, CATEGORY_ENTITY, PERMISSION_ENTITY]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#type CredentialAwswithrolearn#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f731d4c161d892f1897e313c3c9126ae72b98a07b16030ac4a09b9e9a29b6db)
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
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#categoryid CredentialAwswithrolearn#categoryid}.'''
        result = self._values.get("categoryid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def categoryname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#categoryname CredentialAwswithrolearn#categoryname}.'''
        result = self._values.get("categoryname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclude(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if this is included permission or excluded permission.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#exclude CredentialAwswithrolearn#exclude}
        '''
        result = self._values.get("exclude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissionid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#permissionid CredentialAwswithrolearn#permissionid}.'''
        result = self._values.get("permissionid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def permissionname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#permissionname CredentialAwswithrolearn#permissionname}.'''
        result = self._values.get("permissionname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Returns the type of association. [ALL_CATEGORIES, CATEGORY_ENTITY, PERMISSION_ENTITY].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#type CredentialAwswithrolearn#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnSecurityAssociationsPermissions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityAssociationsPermissionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsPermissionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1eac5f6d785fa17dc5d0c90fcfe75d1fc09026369811dae2f8a0be0f04ae39c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityAssociationsPermissionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a00f3f91af7da643d28123f348886daa75cb64d7d1209789684f9f4ea785d64e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsPermissionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__304a209b70ce5c0d7f761121f30dd62e3f195387b0c92c9622678f2178d902c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7bb49746e1c2a014f3c882540c0f1909dc7da49fb005deb425f73fea03c83b70)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d79064c0ca115da9ece05fa7eacfb41a8564eae42f5bc3609a30bf9c408f9e3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsPermissions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsPermissions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsPermissions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d226e61cce422ae6d5f7fe24a105e4c9cf499ba6e02b7c51d5a8bb7df5539bfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityAssociationsPermissionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsPermissionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7deb2b06c1eacad2eb3356c049afd0ba2c8d993b623601c5bee5170f62f549c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__53efa0d34d8c0b0e9046e45b6f7e1d948c4b00c90fbe43c46794ff3361a78999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryid", value)

    @builtins.property
    @jsii.member(jsii_name="categoryname")
    def categoryname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "categoryname"))

    @categoryname.setter
    def categoryname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc4625037b1498577046e3af803d6c4d868381d01e8b3b15a3ca70174d387679)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "categoryname", value)

    @builtins.property
    @jsii.member(jsii_name="exclude")
    def exclude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclude"))

    @exclude.setter
    def exclude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5460c286583920e4df4c431170c782f21e874bc9ace86f5017d4d8155217085)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclude", value)

    @builtins.property
    @jsii.member(jsii_name="permissionid")
    def permissionid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "permissionid"))

    @permissionid.setter
    def permissionid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b62df86b6b725675a3abb1a2dbe88af3b49e75185d90ef8a315f624ffb0f39f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionid", value)

    @builtins.property
    @jsii.member(jsii_name="permissionname")
    def permissionname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "permissionname"))

    @permissionname.setter
    def permissionname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40fd2ce88528ea997526974f39f4d4c826eea5ade14f5ad0167e1f2393ea3977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionname", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c6e40ceac60d19d3dd865f6febf19c9e02a23a18edfab0e5a73fb82521c6ad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsPermissions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsPermissions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsPermissions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e8ecbb2c010ca842bc67abb26c5d314e3e60e82f043ac9ecad949fcebf0f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class CredentialAwswithrolearnSecurityAssociationsUser:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2578270ee1460583caf318d840190e88484996cb092da24474e3dfc59efcc9f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}.

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
        return "CredentialAwswithrolearnSecurityAssociationsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityAssociationsUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16e2ab8b884d0b093c8f058c1ae30864147b8e90cdbbd94c7192cdec9a315b8b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityAssociationsUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11095b028086c457a9f236c32c3aa65031ff3d27aee72e5a5ae4976b17cd7216)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5300b280e2dae4e6e8100bd8fee2196b00de8940b9931db0a5396fe8fc9a921c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df9915efa77a18393c804ca7acbf82c755f11a674d09ea95571021af113442d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcdf362cd2b2d37e76bfda0f0392bd8fb8d3010b821742a883b1bcd995b18c74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b486cf85fe89d4c9e8886f8ed9f94e823c76b822d54e56098313c8dbedb47d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityAssociationsUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4226a61c74fe05c15567ded8d47c38210edaddc7fdf366487960558b4a9b4811)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0f811e4d2c04f78d4126aec160d7ef5e42260d46f0a9f72766ac1c639e55c36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f70f71290f909f5bdef69241e11afc8cd1021dfa4ac778c58a5f8fff90b1ba4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class CredentialAwswithrolearnSecurityAssociationsUsergroup:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29f32ebd1411b59b9ef29e1ddc362ec0f698c6b84b09a0e6fb3cf111a780a123)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}.

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
        return "CredentialAwswithrolearnSecurityAssociationsUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityAssociationsUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__900d3452f6eac4f6d03059b0e371a627c2c4faafe5673ee4ee001fbdcf74767d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityAssociationsUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6995f8276e4afb5aae2512ef2a41f0da4c93d21953e866f237745eedd9633561)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityAssociationsUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fe4eee9bebb4967d129d4cbcb4bfaf2af305844b078a7f16e52c23e3c33040c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dcc76e8be8e0e433227ad5e487687b581e164c3d409b26979f46556d84944ee0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c3f39c07454b09ac3f7d63b2341f954f31d4b44a750b9c2311780c0740a1c061)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59f69fe05e1c0d8a38bad8880ebf91c5fac95d6e38a4d84cbdd2fe25fc8a6b0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityAssociationsUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityAssociationsUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__caa7022075fddea27f480dc32e54711ce755a2f8c74f93a49b96194c7ed04ebb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__373ce80a66427ade8787c50fc97c42492a5a85856bae3a200366b3c7d9846dd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8fa59dcffca021e1eaf3cbb12ef640a47cacdf3226b0c6c22a663cd7a0cdcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b38a16dc53a98feaa1f1e96fc03de5fb26d87f0a92e1861c69a0bd62135684d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b4e16ea8423a046b0204172c4eb89cb12c6f3575391145d285aa754d553260)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa79ab1066977dfb0360731cfbde92abf537b70393bc7f712e4477a2cfd42d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4e0849ab11e44af5f47f6f684c6278e4fe1f20827810e71524477cc6497cf43b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1acbe058116db9e72bd19102164aa122e2fedfc0ad957418e506f031f9bd0031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2626d8f8f8af76ac6b7bf071a152eb597f257c7e6b125b357be0b524d0ca41d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1329ab3d3228ba06a6efebc3b742c7808466159d14c898bb3e374c484f70eebb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssociations")
    def put_associations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02092bff4a698d3fabf65fe1330ba7e9b825c0a77243cb4f7f5e99a9b60b5e18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssociations", [value]))

    @jsii.member(jsii_name="putOwner")
    def put_owner(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityOwner", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5bc17d6dae4646b7133ace375091cf66095697f006c064e71e19d179d24d02)
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
    def associations(self) -> CredentialAwswithrolearnSecurityAssociationsList:
        return typing.cast(CredentialAwswithrolearnSecurityAssociationsList, jsii.get(self, "associations"))

    @builtins.property
    @jsii.member(jsii_name="owner")
    def owner(self) -> "CredentialAwswithrolearnSecurityOwnerList":
        return typing.cast("CredentialAwswithrolearnSecurityOwnerList", jsii.get(self, "owner"))

    @builtins.property
    @jsii.member(jsii_name="associationsInput")
    def associations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociations]]], jsii.get(self, "associationsInput"))

    @builtins.property
    @jsii.member(jsii_name="ownerInput")
    def owner_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwner"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwner"]]], jsii.get(self, "ownerInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7633096b5e4109fc733a8f3d01513801424be6c13dec0d5f89f829c2c47cb363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwner",
    jsii_struct_bases=[],
    name_mapping={"user": "user", "usergroup": "usergroup"},
)
class CredentialAwswithrolearnSecurityOwner:
    def __init__(
        self,
        *,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityOwnerUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityOwnerUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#user CredentialAwswithrolearn#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#usergroup CredentialAwswithrolearn#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f36fb65494a964a23be7e4a0d48d654cce160475edb37029ba8eeb9aca0f64d4)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#user CredentialAwswithrolearn#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#usergroup CredentialAwswithrolearn#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnSecurityOwner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityOwnerList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8524ecf8f963e96a56a30fc4b019f4ef48bbec8023c6511c75ffd3461c96c6f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityOwnerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75cf84b3444ca53d359aca65e7e25ced7496b98b28f4bc386a880f91c47625f8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityOwnerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aa5e1a174479b9e915f597b8e7b3b62dd694def596cb897f79e512aa8b43383)
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
            type_hints = typing.get_type_hints(_typecheckingstub__82e791e8674af0182cd3ac776d0edf99c005203791dd2575f680830e735b36e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d9b6e99ce2918e0da7c3081a48818f5f7b63cf2dad98254c92ed4c447668e34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwner]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwner]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwner]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aac4e59da5118b406b4e6ee188ad3b128031a82fa313012efbfb683ddb93a8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityOwnerOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__28b2924abd93967eee5e929c65045c09a6e9794367a73e8b19e02aa46fb79821)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityOwnerUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ae6253c3869d02f2cd6e8890c3c2f329dc01ebd7bbd267613edebf1b213753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["CredentialAwswithrolearnSecurityOwnerUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60af1b3b1ded39b75d6d35239c7634e12a1bb82c4d9e1a4b4338fc35305485e)
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
    def user(self) -> "CredentialAwswithrolearnSecurityOwnerUserList":
        return typing.cast("CredentialAwswithrolearnSecurityOwnerUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(self) -> "CredentialAwswithrolearnSecurityOwnerUsergroupList":
        return typing.cast("CredentialAwswithrolearnSecurityOwnerUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["CredentialAwswithrolearnSecurityOwnerUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwner]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwner]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwner]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652dfc529ca53949299d58d7935386f8a0b30712d82b796442d4ab4e79b30571)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class CredentialAwswithrolearnSecurityOwnerUser:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5abea5d0f8e3d3500911db29bd3eb78647f7f8fd675425abd33a4c7d95b51ec2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnSecurityOwnerUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityOwnerUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__990414b4c157cdb60c31c5a2cf98ed85fc6c37989f9dd81b7e7eaab8798ad27c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityOwnerUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c24294860c73d0af78d6f45f76f8f36a31f86c64d1dca2000d804a39f8f4d3b0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityOwnerUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b84a3f5149efe2bcd85a0d187b8f1fce64c5c0bffe54064cdebd62668401ae41)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa3bed282a9bcbfe090f8cfcb9aba609889d66814cf873444c9402fff4238301)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95497162e79848f9e982c15ef9c72b045cad8d826510a713a4171b55daf5fd8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca2144484fef695089c7c9de8ccb25dc66003768c92c674a32658d218b50565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityOwnerUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2159c943a9424aa59b2abf10a6a791f58ca545e36d572442469b8e2acff94e3c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b3bb0f6afe4fb810417dc3d54c8d95a549488dc852de26b91a9f04fb3ed17a1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9581a4589224d811f9ab73e588c0759c6394beff611051829b6cc40d7952f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc9baeaa2d153f269f966a8c314081eb0f6215dee9136443065a5eea8bd7cbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class CredentialAwswithrolearnSecurityOwnerUsergroup:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31df252088a259424a63bb3401c7b7d0761904e90c77a96f40a381d47a75ca21)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#id CredentialAwswithrolearn#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/credential_awswithrolearn#name CredentialAwswithrolearn#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CredentialAwswithrolearnSecurityOwnerUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CredentialAwswithrolearnSecurityOwnerUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e9cd918f4ca66e735bfb6a55655f3b7c2544aef9a8eb1a2ebc814765b140636)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "CredentialAwswithrolearnSecurityOwnerUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e613c2a6ce25a2fd25bb13ea94c2042dddd0ae2fb6df079e79b163fe41f85637)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CredentialAwswithrolearnSecurityOwnerUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec3f1d40ae0a74a35c0755f41eea4f05d06be496910d1a7315c316ffed86e53)
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
            type_hints = typing.get_type_hints(_typecheckingstub__155d19d8566e032962bafb070a5b937b266e162770c5f1cb050e7c0a37b90b44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ae1c85cb973502aaaed2d11815f187ed46f26e7b2235875283fb3f78ad748681)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fa6898c11ca3eb1153a5be4e6cbe50dbee73b1e3d91857582bd1d2f7034ccfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CredentialAwswithrolearnSecurityOwnerUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.credentialAwswithrolearn.CredentialAwswithrolearnSecurityOwnerUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a595ad470b86b615ddb58c166310f3383c828210ab5473ecb35ba58dc447c9f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60c63b4282517fa01843f06d0e628b159efbe1293265a6847ba8c62c676d85bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb90466c410faaffc156ac7e16cefa4301f1889edb13265112363d5977baac89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86cf6fcd6fb4fad7a5a9623ebc3eb39f1e55812bedf6fa2396d8a30944b79c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CredentialAwswithrolearn",
    "CredentialAwswithrolearnConfig",
    "CredentialAwswithrolearnSecurity",
    "CredentialAwswithrolearnSecurityAssociations",
    "CredentialAwswithrolearnSecurityAssociationsList",
    "CredentialAwswithrolearnSecurityAssociationsOutputReference",
    "CredentialAwswithrolearnSecurityAssociationsPermissions",
    "CredentialAwswithrolearnSecurityAssociationsPermissionsList",
    "CredentialAwswithrolearnSecurityAssociationsPermissionsOutputReference",
    "CredentialAwswithrolearnSecurityAssociationsUser",
    "CredentialAwswithrolearnSecurityAssociationsUserList",
    "CredentialAwswithrolearnSecurityAssociationsUserOutputReference",
    "CredentialAwswithrolearnSecurityAssociationsUsergroup",
    "CredentialAwswithrolearnSecurityAssociationsUsergroupList",
    "CredentialAwswithrolearnSecurityAssociationsUsergroupOutputReference",
    "CredentialAwswithrolearnSecurityList",
    "CredentialAwswithrolearnSecurityOutputReference",
    "CredentialAwswithrolearnSecurityOwner",
    "CredentialAwswithrolearnSecurityOwnerList",
    "CredentialAwswithrolearnSecurityOwnerOutputReference",
    "CredentialAwswithrolearnSecurityOwnerUser",
    "CredentialAwswithrolearnSecurityOwnerUserList",
    "CredentialAwswithrolearnSecurityOwnerUserOutputReference",
    "CredentialAwswithrolearnSecurityOwnerUsergroup",
    "CredentialAwswithrolearnSecurityOwnerUsergroupList",
    "CredentialAwswithrolearnSecurityOwnerUsergroupOutputReference",
]

publication.publish()

def _typecheckingstub__57517280cc2fc7b9382c1a3c7645691dcbf6a0973798986e4f692a0724384f7a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    rolearn: builtins.str,
    accounttype: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__8f888dfc95e361895b52378acb9bbf4b2be85389ad028380426f4b2547b813ad(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4723e26112a6f07892d04e90d6c21119f770f2bba03dacc5860956a1672c44e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759e054727815b032e871b353d386b71ab890bfd309aecad445f7717bc5b64ef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e8021e5e1ab5d9c96e929961471b66eae74b5d54d1c2e7aba88d4bb88483e0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08be5c1c514c8014650975eff909b97a4eea0ede5c5610b5a5a42dd73cddb2eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73e4f10f89a99eee311d4fcb78ec36d932a9b9c436fc4573e510558aa6e55cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa669c1131e511f58cb5332600b88f3d1cf4ad8c184dfb27e3002275deec11e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeed83720edfb18e0aafd2803586315298a0f6111e1cd76ade73c149b12c9e2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9de9c651ddf57c77e69b8a3fff33511e6282025bb95a28721d45348fe151a22d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9563aa14f482363956cb20d27dfa712fc41f8499b7e6e59ef026142cf670676(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    rolearn: builtins.str,
    accounttype: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vendortype: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd6c9d1135f96a9638611442b4251b8cdd1f0a233ee74b0d5750af214a512be(
    *,
    associations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    owner: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityOwner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640c9384dc3efab3b06b7b4c3e0413d8e253017b5fbdb0a28ae8c0ebbe68d7f7(
    *,
    iscreatorassociation: typing.Optional[builtins.str] = None,
    permissions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociationsPermissions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociationsUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociationsUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cd1f33ea3e24ec26a2aef0e7a6cbbc69c28c917d86e9499999afd8421c2a141(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8796d27191b1a497e8eae065f688a80306cbdfb147a50798f7b3d39a29b99060(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0bfabc662a878744f18bcc1ff8b126e0178101f7f35b408bae0fc092a21192c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31073c41cfaa63344ddd4c79984531bdfff181844b660e0ca6d4c999e48fd3db(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c25d75dc3f7d2e9fd99d14ebb0e7f35ede79c2ade2b1cd00c81fedb998f8af(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa4ec8e8819a3f67f11c0d9e87f6ae06485ffcc7294fd90fbedb12c48ec7e43(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cdafe63cd2855572c089b65d2505689f10e4fbd52747ca665271db37f06df89(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69a4a0e2add9d9772c4dfd64925579f691de3b17ae62c724016e3bfc3dce790e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociationsPermissions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5810a8c290fe067bc0f3d60afccf9c560264086176347f5e8b745165495241fc(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociationsUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0b50f7dacd1348b27f703b896c5ed2e4f7cc1debaecfef17f3a856ed137d698(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociationsUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e4656c23fc1e4f4c20bc45653ff613ac229b7f476a4ccadf465e4a54e79194(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f139adc36af3612e294f9e4365c788f3a399c87bac5acc01195ad19c10db1a32(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f731d4c161d892f1897e313c3c9126ae72b98a07b16030ac4a09b9e9a29b6db(
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

def _typecheckingstub__1eac5f6d785fa17dc5d0c90fcfe75d1fc09026369811dae2f8a0be0f04ae39c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a00f3f91af7da643d28123f348886daa75cb64d7d1209789684f9f4ea785d64e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__304a209b70ce5c0d7f761121f30dd62e3f195387b0c92c9622678f2178d902c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb49746e1c2a014f3c882540c0f1909dc7da49fb005deb425f73fea03c83b70(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d79064c0ca115da9ece05fa7eacfb41a8564eae42f5bc3609a30bf9c408f9e3b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d226e61cce422ae6d5f7fe24a105e4c9cf499ba6e02b7c51d5a8bb7df5539bfe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsPermissions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7deb2b06c1eacad2eb3356c049afd0ba2c8d993b623601c5bee5170f62f549c1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53efa0d34d8c0b0e9046e45b6f7e1d948c4b00c90fbe43c46794ff3361a78999(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc4625037b1498577046e3af803d6c4d868381d01e8b3b15a3ca70174d387679(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5460c286583920e4df4c431170c782f21e874bc9ace86f5017d4d8155217085(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b62df86b6b725675a3abb1a2dbe88af3b49e75185d90ef8a315f624ffb0f39f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40fd2ce88528ea997526974f39f4d4c826eea5ade14f5ad0167e1f2393ea3977(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c6e40ceac60d19d3dd865f6febf19c9e02a23a18edfab0e5a73fb82521c6ad1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e8ecbb2c010ca842bc67abb26c5d314e3e60e82f043ac9ecad949fcebf0f1a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsPermissions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2578270ee1460583caf318d840190e88484996cb092da24474e3dfc59efcc9f(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e2ab8b884d0b093c8f058c1ae30864147b8e90cdbbd94c7192cdec9a315b8b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11095b028086c457a9f236c32c3aa65031ff3d27aee72e5a5ae4976b17cd7216(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5300b280e2dae4e6e8100bd8fee2196b00de8940b9931db0a5396fe8fc9a921c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df9915efa77a18393c804ca7acbf82c755f11a674d09ea95571021af113442d3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcdf362cd2b2d37e76bfda0f0392bd8fb8d3010b821742a883b1bcd995b18c74(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b486cf85fe89d4c9e8886f8ed9f94e823c76b822d54e56098313c8dbedb47d6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4226a61c74fe05c15567ded8d47c38210edaddc7fdf366487960558b4a9b4811(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0f811e4d2c04f78d4126aec160d7ef5e42260d46f0a9f72766ac1c639e55c36(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f70f71290f909f5bdef69241e11afc8cd1021dfa4ac778c58a5f8fff90b1ba4a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f32ebd1411b59b9ef29e1ddc362ec0f698c6b84b09a0e6fb3cf111a780a123(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__900d3452f6eac4f6d03059b0e371a627c2c4faafe5673ee4ee001fbdcf74767d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6995f8276e4afb5aae2512ef2a41f0da4c93d21953e866f237745eedd9633561(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fe4eee9bebb4967d129d4cbcb4bfaf2af305844b078a7f16e52c23e3c33040c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc76e8be8e0e433227ad5e487687b581e164c3d409b26979f46556d84944ee0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3f39c07454b09ac3f7d63b2341f954f31d4b44a750b9c2311780c0740a1c061(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f69fe05e1c0d8a38bad8880ebf91c5fac95d6e38a4d84cbdd2fe25fc8a6b0b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityAssociationsUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caa7022075fddea27f480dc32e54711ce755a2f8c74f93a49b96194c7ed04ebb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__373ce80a66427ade8787c50fc97c42492a5a85856bae3a200366b3c7d9846dd4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8fa59dcffca021e1eaf3cbb12ef640a47cacdf3226b0c6c22a663cd7a0cdcf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityAssociationsUsergroup]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38a16dc53a98feaa1f1e96fc03de5fb26d87f0a92e1861c69a0bd62135684d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b4e16ea8423a046b0204172c4eb89cb12c6f3575391145d285aa754d553260(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa79ab1066977dfb0360731cfbde92abf537b70393bc7f712e4477a2cfd42d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0849ab11e44af5f47f6f684c6278e4fe1f20827810e71524477cc6497cf43b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1acbe058116db9e72bd19102164aa122e2fedfc0ad957418e506f031f9bd0031(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2626d8f8f8af76ac6b7bf071a152eb597f257c7e6b125b357be0b524d0ca41d7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1329ab3d3228ba06a6efebc3b742c7808466159d14c898bb3e374c484f70eebb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02092bff4a698d3fabf65fe1330ba7e9b825c0a77243cb4f7f5e99a9b60b5e18(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityAssociations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5bc17d6dae4646b7133ace375091cf66095697f006c064e71e19d179d24d02(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityOwner, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7633096b5e4109fc733a8f3d01513801424be6c13dec0d5f89f829c2c47cb363(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36fb65494a964a23be7e4a0d48d654cce160475edb37029ba8eeb9aca0f64d4(
    *,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityOwnerUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityOwnerUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8524ecf8f963e96a56a30fc4b019f4ef48bbec8023c6511c75ffd3461c96c6f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75cf84b3444ca53d359aca65e7e25ced7496b98b28f4bc386a880f91c47625f8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aa5e1a174479b9e915f597b8e7b3b62dd694def596cb897f79e512aa8b43383(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82e791e8674af0182cd3ac776d0edf99c005203791dd2575f680830e735b36e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9b6e99ce2918e0da7c3081a48818f5f7b63cf2dad98254c92ed4c447668e34(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aac4e59da5118b406b4e6ee188ad3b128031a82fa313012efbfb683ddb93a8c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwner]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28b2924abd93967eee5e929c65045c09a6e9794367a73e8b19e02aa46fb79821(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ae6253c3869d02f2cd6e8890c3c2f329dc01ebd7bbd267613edebf1b213753(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityOwnerUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60af1b3b1ded39b75d6d35239c7634e12a1bb82c4d9e1a4b4338fc35305485e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[CredentialAwswithrolearnSecurityOwnerUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652dfc529ca53949299d58d7935386f8a0b30712d82b796442d4ab4e79b30571(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwner]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5abea5d0f8e3d3500911db29bd3eb78647f7f8fd675425abd33a4c7d95b51ec2(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990414b4c157cdb60c31c5a2cf98ed85fc6c37989f9dd81b7e7eaab8798ad27c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24294860c73d0af78d6f45f76f8f36a31f86c64d1dca2000d804a39f8f4d3b0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b84a3f5149efe2bcd85a0d187b8f1fce64c5c0bffe54064cdebd62668401ae41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa3bed282a9bcbfe090f8cfcb9aba609889d66814cf873444c9402fff4238301(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95497162e79848f9e982c15ef9c72b045cad8d826510a713a4171b55daf5fd8d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca2144484fef695089c7c9de8ccb25dc66003768c92c674a32658d218b50565(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2159c943a9424aa59b2abf10a6a791f58ca545e36d572442469b8e2acff94e3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3bb0f6afe4fb810417dc3d54c8d95a549488dc852de26b91a9f04fb3ed17a1a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9581a4589224d811f9ab73e588c0759c6394beff611051829b6cc40d7952f30(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc9baeaa2d153f269f966a8c314081eb0f6215dee9136443065a5eea8bd7cbe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31df252088a259424a63bb3401c7b7d0761904e90c77a96f40a381d47a75ca21(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9cd918f4ca66e735bfb6a55655f3b7c2544aef9a8eb1a2ebc814765b140636(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e613c2a6ce25a2fd25bb13ea94c2042dddd0ae2fb6df079e79b163fe41f85637(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec3f1d40ae0a74a35c0755f41eea4f05d06be496910d1a7315c316ffed86e53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__155d19d8566e032962bafb070a5b937b266e162770c5f1cb050e7c0a37b90b44(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae1c85cb973502aaaed2d11815f187ed46f26e7b2235875283fb3f78ad748681(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa6898c11ca3eb1153a5be4e6cbe50dbee73b1e3d91857582bd1d2f7034ccfa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[CredentialAwswithrolearnSecurityOwnerUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a595ad470b86b615ddb58c166310f3383c828210ab5473ecb35ba58dc447c9f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60c63b4282517fa01843f06d0e628b159efbe1293265a6847ba8c62c676d85bf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb90466c410faaffc156ac7e16cefa4301f1889edb13265112363d5977baac89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86cf6fcd6fb4fad7a5a9623ebc3eb39f1e55812bedf6fa2396d8a30944b79c2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, CredentialAwswithrolearnSecurityOwnerUsergroup]],
) -> None:
    """Type checking stubs"""
    pass
