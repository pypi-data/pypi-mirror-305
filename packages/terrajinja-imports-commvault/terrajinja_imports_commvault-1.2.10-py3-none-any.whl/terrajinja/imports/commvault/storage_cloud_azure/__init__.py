'''
# `commvault_storage_cloud_azure`

Refer to the Terraform Registry for docs: [`commvault_storage_cloud_azure`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure).
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


class StorageCloudAzure(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzure",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure commvault_storage_cloud_azure}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        authentication: builtins.str,
        container: builtins.str,
        mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureMediaagent", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        storageclass: builtins.str,
        accountname: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        deduplicationdblocation: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureDeduplicationdblocation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        encryption: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureEncryption", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        servicehost: typing.Optional[builtins.str] = None,
        usededuplication: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure commvault_storage_cloud_azure} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication: Authentication type for the cloud storage server. Only Access & Account Name and IAM AD require credentials. [Access and secret keys, IAM VM role assignment, IAM AD application role assignment (Credential Manager)] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#authentication StorageCloudAzure#authentication}
        :param container: Name of container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#container StorageCloudAzure#container}
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#mediaagent StorageCloudAzure#mediaagent}
        :param name: Name of the cloud storage library. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}
        :param storageclass: Appropriate storage class for your account [Container's default, Hot, Cool, Archive, Hot/Archive (Combined Storage Tiers), Cool/Archive (Combined Storage Tiers)]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#storageclass StorageCloudAzure#storageclass}
        :param accountname: Only for IAM VM and IAM AD. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#accountname StorageCloudAzure#accountname}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#credentials StorageCloudAzure#credentials}
        :param deduplicationdblocation: deduplicationdblocation block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#deduplicationdblocation StorageCloudAzure#deduplicationdblocation}
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#encryption StorageCloudAzure#encryption}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#security StorageCloudAzure#security}
        :param servicehost: IP address or fully qualified domain name or URL for the cloud library based on cloud vendor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#servicehost StorageCloudAzure#servicehost}
        :param usededuplication: Enables or disables deduplication on the storage. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#usededuplication StorageCloudAzure#usededuplication}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52fd31619b2a5f0880d407bbc630a47c99178fa4e3bd6b5dd62f67d082c9fb70)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageCloudAzureConfig(
            authentication=authentication,
            container=container,
            mediaagent=mediaagent,
            name=name,
            storageclass=storageclass,
            accountname=accountname,
            credentials=credentials,
            deduplicationdblocation=deduplicationdblocation,
            encryption=encryption,
            id=id,
            security=security,
            servicehost=servicehost,
            usededuplication=usededuplication,
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
        '''Generates CDKTF code for importing a StorageCloudAzure resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the StorageCloudAzure to import.
        :param import_from_id: The id of the existing StorageCloudAzure that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the StorageCloudAzure to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f6b10da71b61b3aefaa5bdef5a0e7d2b208b61c55f12aa750a05befdb31535b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureCredentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c23cac1dd6fe15828c23d3a7ef6b886ed62d09df6057ac559e31da537b126c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putDeduplicationdblocation")
    def put_deduplicationdblocation(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureDeduplicationdblocation", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18d56609900ff65e8e251a44346f41417479d8c094dc5948433e62de6e40676e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeduplicationdblocation", [value]))

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureEncryption", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20caba3f77b60eb8dd682c9f927e1710b3a2a04bbf637263d30e59c004d7b013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="putMediaagent")
    def put_mediaagent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureMediaagent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf02d8bee817759071137b82350f2ffa26910b5cd195f18e37061c0621bc217c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMediaagent", [value]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d071135b1d11ab858d6db6be2c18f0a0370b39e235d3ccc2d84ff48e15080443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecurity", [value]))

    @jsii.member(jsii_name="resetAccountname")
    def reset_accountname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountname", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetDeduplicationdblocation")
    def reset_deduplicationdblocation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeduplicationdblocation", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSecurity")
    def reset_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurity", []))

    @jsii.member(jsii_name="resetServicehost")
    def reset_servicehost(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicehost", []))

    @jsii.member(jsii_name="resetUsededuplication")
    def reset_usededuplication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsededuplication", []))

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
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "StorageCloudAzureCredentialsList":
        return typing.cast("StorageCloudAzureCredentialsList", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="deduplicationdblocation")
    def deduplicationdblocation(self) -> "StorageCloudAzureDeduplicationdblocationList":
        return typing.cast("StorageCloudAzureDeduplicationdblocationList", jsii.get(self, "deduplicationdblocation"))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> "StorageCloudAzureEncryptionList":
        return typing.cast("StorageCloudAzureEncryptionList", jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="mediaagent")
    def mediaagent(self) -> "StorageCloudAzureMediaagentList":
        return typing.cast("StorageCloudAzureMediaagentList", jsii.get(self, "mediaagent"))

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> "StorageCloudAzureSecurityList":
        return typing.cast("StorageCloudAzureSecurityList", jsii.get(self, "security"))

    @builtins.property
    @jsii.member(jsii_name="accountnameInput")
    def accountname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountnameInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureCredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureCredentials"]]], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="deduplicationdblocationInput")
    def deduplicationdblocation_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureDeduplicationdblocation"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureDeduplicationdblocation"]]], jsii.get(self, "deduplicationdblocationInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureEncryption"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureEncryption"]]], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mediaagentInput")
    def mediaagent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureMediaagent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureMediaagent"]]], jsii.get(self, "mediaagentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurity"]]], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="servicehostInput")
    def servicehost_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicehostInput"))

    @builtins.property
    @jsii.member(jsii_name="storageclassInput")
    def storageclass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageclassInput"))

    @builtins.property
    @jsii.member(jsii_name="usededuplicationInput")
    def usededuplication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usededuplicationInput"))

    @builtins.property
    @jsii.member(jsii_name="accountname")
    def accountname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountname"))

    @accountname.setter
    def accountname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e63801ddd47e44669af013d9494ff008bc09bbf59e54cdd0fedd2353f2a7591)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountname", value)

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authentication"))

    @authentication.setter
    def authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dab606bd33324a1f387a02dbb8942eff2cf292b2a9086700d431055d57168dd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authentication", value)

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ea03ff4d0ccae9859bdc1e46640719171d153f99a6d6a5ec47ea826eae0516)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a1e3a0882330d3431a0fab80671c11abd73536e3714413cfc50d25b05f32b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd563e74a11c682be9ea6f29f8e052c3d91ef24209f8f077a26076304f999db2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="servicehost")
    def servicehost(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicehost"))

    @servicehost.setter
    def servicehost(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7d45461afedf59b78111fd3d4ba9c5bb2e351ecca24389592bf186c32b56e9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicehost", value)

    @builtins.property
    @jsii.member(jsii_name="storageclass")
    def storageclass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageclass"))

    @storageclass.setter
    def storageclass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8d5f8efb462ce3e93606c65e5c1cc080c0f289ba2e8959ef8fbfa6ea838596)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageclass", value)

    @builtins.property
    @jsii.member(jsii_name="usededuplication")
    def usededuplication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usededuplication"))

    @usededuplication.setter
    def usededuplication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126f81b0946368381c014d924a4a5e690743d34065b24d8ec38a83e2e5eea2f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usededuplication", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication": "authentication",
        "container": "container",
        "mediaagent": "mediaagent",
        "name": "name",
        "storageclass": "storageclass",
        "accountname": "accountname",
        "credentials": "credentials",
        "deduplicationdblocation": "deduplicationdblocation",
        "encryption": "encryption",
        "id": "id",
        "security": "security",
        "servicehost": "servicehost",
        "usededuplication": "usededuplication",
    },
)
class StorageCloudAzureConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        authentication: builtins.str,
        container: builtins.str,
        mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureMediaagent", typing.Dict[builtins.str, typing.Any]]]],
        name: builtins.str,
        storageclass: builtins.str,
        accountname: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        deduplicationdblocation: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureDeduplicationdblocation", typing.Dict[builtins.str, typing.Any]]]]] = None,
        encryption: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureEncryption", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        servicehost: typing.Optional[builtins.str] = None,
        usededuplication: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication: Authentication type for the cloud storage server. Only Access & Account Name and IAM AD require credentials. [Access and secret keys, IAM VM role assignment, IAM AD application role assignment (Credential Manager)] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#authentication StorageCloudAzure#authentication}
        :param container: Name of container. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#container StorageCloudAzure#container}
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#mediaagent StorageCloudAzure#mediaagent}
        :param name: Name of the cloud storage library. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}
        :param storageclass: Appropriate storage class for your account [Container's default, Hot, Cool, Archive, Hot/Archive (Combined Storage Tiers), Cool/Archive (Combined Storage Tiers)]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#storageclass StorageCloudAzure#storageclass}
        :param accountname: Only for IAM VM and IAM AD. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#accountname StorageCloudAzure#accountname}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#credentials StorageCloudAzure#credentials}
        :param deduplicationdblocation: deduplicationdblocation block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#deduplicationdblocation StorageCloudAzure#deduplicationdblocation}
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#encryption StorageCloudAzure#encryption}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#security StorageCloudAzure#security}
        :param servicehost: IP address or fully qualified domain name or URL for the cloud library based on cloud vendor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#servicehost StorageCloudAzure#servicehost}
        :param usededuplication: Enables or disables deduplication on the storage. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#usededuplication StorageCloudAzure#usededuplication}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d3151b4b4d2c7baba6e57b658ce5d387975bf8eb51afec4e24647e3a8cc8df)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument mediaagent", value=mediaagent, expected_type=type_hints["mediaagent"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument storageclass", value=storageclass, expected_type=type_hints["storageclass"])
            check_type(argname="argument accountname", value=accountname, expected_type=type_hints["accountname"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument deduplicationdblocation", value=deduplicationdblocation, expected_type=type_hints["deduplicationdblocation"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument servicehost", value=servicehost, expected_type=type_hints["servicehost"])
            check_type(argname="argument usededuplication", value=usededuplication, expected_type=type_hints["usededuplication"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication": authentication,
            "container": container,
            "mediaagent": mediaagent,
            "name": name,
            "storageclass": storageclass,
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
        if accountname is not None:
            self._values["accountname"] = accountname
        if credentials is not None:
            self._values["credentials"] = credentials
        if deduplicationdblocation is not None:
            self._values["deduplicationdblocation"] = deduplicationdblocation
        if encryption is not None:
            self._values["encryption"] = encryption
        if id is not None:
            self._values["id"] = id
        if security is not None:
            self._values["security"] = security
        if servicehost is not None:
            self._values["servicehost"] = servicehost
        if usededuplication is not None:
            self._values["usededuplication"] = usededuplication

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
    def authentication(self) -> builtins.str:
        '''Authentication type for the cloud storage server.

        Only Access & Account Name and IAM AD require credentials. [Access and secret keys, IAM VM role assignment, IAM AD application role assignment (Credential Manager)]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#authentication StorageCloudAzure#authentication}
        '''
        result = self._values.get("authentication")
        assert result is not None, "Required property 'authentication' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container(self) -> builtins.str:
        '''Name of container.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#container StorageCloudAzure#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mediaagent(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureMediaagent"]]:
        '''mediaagent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#mediaagent StorageCloudAzure#mediaagent}
        '''
        result = self._values.get("mediaagent")
        assert result is not None, "Required property 'mediaagent' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureMediaagent"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the cloud storage library.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storageclass(self) -> builtins.str:
        '''Appropriate storage class for your account [Container's default, Hot, Cool, Archive, Hot/Archive (Combined Storage Tiers), Cool/Archive (Combined Storage Tiers)].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#storageclass StorageCloudAzure#storageclass}
        '''
        result = self._values.get("storageclass")
        assert result is not None, "Required property 'storageclass' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accountname(self) -> typing.Optional[builtins.str]:
        '''Only for IAM VM and IAM AD.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#accountname StorageCloudAzure#accountname}
        '''
        result = self._values.get("accountname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureCredentials"]]]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#credentials StorageCloudAzure#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureCredentials"]]], result)

    @builtins.property
    def deduplicationdblocation(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureDeduplicationdblocation"]]]:
        '''deduplicationdblocation block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#deduplicationdblocation StorageCloudAzure#deduplicationdblocation}
        '''
        result = self._values.get("deduplicationdblocation")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureDeduplicationdblocation"]]], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureEncryption"]]]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#encryption StorageCloudAzure#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureEncryption"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurity"]]]:
        '''security block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#security StorageCloudAzure#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurity"]]], result)

    @builtins.property
    def servicehost(self) -> typing.Optional[builtins.str]:
        '''IP address or fully qualified domain name or URL for the cloud library based on cloud vendor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#servicehost StorageCloudAzure#servicehost}
        '''
        result = self._values.get("servicehost")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usededuplication(self) -> typing.Optional[builtins.str]:
        '''Enables or disables deduplication on the storage.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#usededuplication StorageCloudAzure#usededuplication}
        '''
        result = self._values.get("usededuplication")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureCredentials",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudAzureCredentials:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32cb9ecb26719f2da692f6cf4111d869b4041aca4f53448ad865fafc3f701223)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureCredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureCredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57e55e6f1897797b0a47ea49ed563958a61afab5a7aee0969e770afdc5ac7f0a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageCloudAzureCredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29319920541ccbb007ec6bb055c7ce90574dc0d618cd392d61515163e66a173)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureCredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa5ff791b3ad81cf7cdaa0c0cbb146b319009ff47bf3afed37ba9fcc4bf56a97)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ca03256b3ae2873a1c4f294819dff6806ad08868deeca5b14b2023109240ab8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a8e6be2f46cdeaeb958559cf77f0880e02faf72d51bf9dba96570b24ed6efca4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureCredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureCredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureCredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b7879c0d669a6a2023a1e90a88793fee7a530ea9530eeb2a7f0addfdd63f112)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__498b41340dab61988ae96c388efd9b8bf34566597d37094baf000050c9f773f0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f2ae1bd61ee06364e04635372bae7cfa407a72b13bac554920cf5c8642c83d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__476b9d32ed9b691fbcb8d558aa4b2a89b3b26948c803d95f8cdbf8b1933a3b33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureCredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureCredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureCredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64dbeffba08fc53091a4b2ed2ac9c1ff6fe4d9fb903c2b0c40e87a09d394de6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureDeduplicationdblocation",
    jsii_struct_bases=[],
    name_mapping={"mediaagent": "mediaagent", "path": "path"},
)
class StorageCloudAzureDeduplicationdblocation:
    def __init__(
        self,
        *,
        mediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureDeduplicationdblocationMediaagent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#mediaagent StorageCloudAzure#mediaagent}
        :param path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#path StorageCloudAzure#path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dde537d8635a038c9b182a9b2a2f1a6952d639d83d4894229a4162556624dec)
            check_type(argname="argument mediaagent", value=mediaagent, expected_type=type_hints["mediaagent"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if mediaagent is not None:
            self._values["mediaagent"] = mediaagent
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def mediaagent(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureDeduplicationdblocationMediaagent"]]]:
        '''mediaagent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#mediaagent StorageCloudAzure#mediaagent}
        '''
        result = self._values.get("mediaagent")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureDeduplicationdblocationMediaagent"]]], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#path StorageCloudAzure#path}.'''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureDeduplicationdblocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureDeduplicationdblocationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureDeduplicationdblocationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5eceb53aef05700e2f4686398909633d04fbacf1b56ea9a15e67f9f7474f1ce6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudAzureDeduplicationdblocationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b2c4300149a68991767da0440d6d46a8eee1e25ecc4fbcd79211fcb3b8fd363)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureDeduplicationdblocationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48316706e105990f8ad3bc2b2c58416fac27895a177c72c48c3640b734363e29)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f3a9e9bd059f46623cdc0ed05544ed587b0df8e828eddf3b4de4c139d1f70e3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__746e2c20400325b99a9cd351ed6bdffafdcd1e3e268782a8240fc3c998be2e03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocation]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocation]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocation]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__950b5e6e0976f23e445b54078f9cc35e70f32b7b692a60a36d8158417dae9a16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureDeduplicationdblocationMediaagent",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudAzureDeduplicationdblocationMediaagent:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a6c666ada02d0a6165862d73824ed3f6a167901157722a95f8bd35a878a0443)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureDeduplicationdblocationMediaagent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureDeduplicationdblocationMediaagentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureDeduplicationdblocationMediaagentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4be8a85bb1b8c881842109e0e051841967a79199c30df3611471494447cff304)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudAzureDeduplicationdblocationMediaagentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e2bd3157dba5871240c6c435901281a475649daa2588d0b25f72e408b159898)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureDeduplicationdblocationMediaagentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e1f9a37cb0ebdb9d52ea6a801caa39c0e0a225d502bdff29d8a0a54cfb58993)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3959dc18ccf6151482331b7db5c2890e7be86fdc4fd43bb46f42a902764c7b39)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f76c85976939d96dadfae39d7dc8af3a3174ad8d5edf4e1badcc302369b19e73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocationMediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocationMediaagent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocationMediaagent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3be99194508122147afbd1f4109157ebb02101e86a01052481a9134ca24ab4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureDeduplicationdblocationMediaagentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureDeduplicationdblocationMediaagentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9335d758025e4debd997bc09c14949a79f58b85368f7a8aa6aa48fef0a1bae5c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__932a7ebbf8b1263b9340b0eb1d313a1370383c189fa7991e6e36bb0b7b89949e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e52c470ef36fb0346cde31c8e8fba12c0f48877b252ff7ccfa9f9122b194c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocationMediaagent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocationMediaagent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocationMediaagent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e82535cedd6066a3694fc75c44d9c104f95a7c6c376a7316ee4f537a90288fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureDeduplicationdblocationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureDeduplicationdblocationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9410ab26e446bddebe3b7d7781c9e439e6ac22a7928677c17c03ad84560ddbf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMediaagent")
    def put_mediaagent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureDeduplicationdblocationMediaagent, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b88c2a15247021691c57ba574dc88f2a8c8c9d991c712758db52d55f2ad8c874)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMediaagent", [value]))

    @jsii.member(jsii_name="resetMediaagent")
    def reset_mediaagent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMediaagent", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="mediaagent")
    def mediaagent(self) -> StorageCloudAzureDeduplicationdblocationMediaagentList:
        return typing.cast(StorageCloudAzureDeduplicationdblocationMediaagentList, jsii.get(self, "mediaagent"))

    @builtins.property
    @jsii.member(jsii_name="mediaagentInput")
    def mediaagent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocationMediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocationMediaagent]]], jsii.get(self, "mediaagentInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a0cabe5c5876ab406191f09572a54956b3d55d93b87aecd6f17f05c2ad9571c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocation]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocation]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocation]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f2a802ef979b4e25385b42843ed4c1b7483b1f75a885d2a39d5e08a474b7a33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureEncryption",
    jsii_struct_bases=[],
    name_mapping={
        "cipher": "cipher",
        "encrypt": "encrypt",
        "keylength": "keylength",
        "keyprovider": "keyprovider",
    },
)
class StorageCloudAzureEncryption:
    def __init__(
        self,
        *,
        cipher: typing.Optional[builtins.str] = None,
        encrypt: typing.Optional[builtins.str] = None,
        keylength: typing.Optional[jsii.Number] = None,
        keyprovider: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureEncryptionKeyprovider", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param cipher: The different types of encryption keys that can be used for encrypting the data. The values are case sensitive [BlowFish, AES, DES3, GOST, Serpent, Twofish] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#cipher StorageCloudAzure#cipher}
        :param encrypt: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#encrypt StorageCloudAzure#encrypt}.
        :param keylength: Different keylengths are present for different kinds of ciphers. Blowfish,Twofish,AES and Serpent all accept both 128 and 256. DES3 accepts only 192. GOST accepts only 256. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#keylength StorageCloudAzure#keylength}
        :param keyprovider: keyprovider block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#keyprovider StorageCloudAzure#keyprovider}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d2c9759df130c56e8ce9591661c70ee6d28bc6159999a76b43e7baf07e916bb)
            check_type(argname="argument cipher", value=cipher, expected_type=type_hints["cipher"])
            check_type(argname="argument encrypt", value=encrypt, expected_type=type_hints["encrypt"])
            check_type(argname="argument keylength", value=keylength, expected_type=type_hints["keylength"])
            check_type(argname="argument keyprovider", value=keyprovider, expected_type=type_hints["keyprovider"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cipher is not None:
            self._values["cipher"] = cipher
        if encrypt is not None:
            self._values["encrypt"] = encrypt
        if keylength is not None:
            self._values["keylength"] = keylength
        if keyprovider is not None:
            self._values["keyprovider"] = keyprovider

    @builtins.property
    def cipher(self) -> typing.Optional[builtins.str]:
        '''The different types of encryption keys that can be used for encrypting the data.

        The values are case sensitive [BlowFish, AES, DES3, GOST, Serpent, Twofish]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#cipher StorageCloudAzure#cipher}
        '''
        result = self._values.get("cipher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encrypt(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#encrypt StorageCloudAzure#encrypt}.'''
        result = self._values.get("encrypt")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keylength(self) -> typing.Optional[jsii.Number]:
        '''Different keylengths are present for different kinds of ciphers.

        Blowfish,Twofish,AES and Serpent all accept both 128 and 256. DES3 accepts only 192. GOST accepts only 256.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#keylength StorageCloudAzure#keylength}
        '''
        result = self._values.get("keylength")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keyprovider(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureEncryptionKeyprovider"]]]:
        '''keyprovider block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#keyprovider StorageCloudAzure#keyprovider}
        '''
        result = self._values.get("keyprovider")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureEncryptionKeyprovider"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureEncryptionKeyprovider",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudAzureEncryptionKeyprovider:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0305abe2c078f99352515b315384108ed127f7b9a3f9d23158db16e3c1729846)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureEncryptionKeyprovider(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureEncryptionKeyproviderList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureEncryptionKeyproviderList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0b3d32eaa07155d5e2515a2d0ca505c49e1cad4ea1a41d8ddf38f7da68df3533)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudAzureEncryptionKeyproviderOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d203a226ff3c71be7c327c1dc82f27e558803459990c6c137eb8b5ab4ee5b7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureEncryptionKeyproviderOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f7fe6cc280db41f07638f38d18f70afd21b2240a252804a17f240e4a0e77d2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90c7a3a78f6fd783c3cc2f86df3c2380e100ce3d8028b91af10a933523e8170a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c4a7cd299a26d64d8ca9ef8ec688693417ab77916206961c27b509c625c1b59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryptionKeyprovider]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryptionKeyprovider]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryptionKeyprovider]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9bea4acf78cf3f6a3a24c7e73062e1ffdaff488449fe2530222c4cfa41057df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureEncryptionKeyproviderOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureEncryptionKeyproviderOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7ea7c01102ecabfc9b2bdd96f29f4b911bc1af4e3afc6ecd0132b17e8add67b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3fe38f0b6b74b7023717f824658de1f367c181e402c62f61b86124c0d98a4ca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc6408423cf79a57733f76e5d0fe5e992bbeb4bff194725d7249f97323ebf4cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryptionKeyprovider]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryptionKeyprovider]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryptionKeyprovider]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f28a0523ab967bb3725ff47e1532ff832c7a3e5a5f13b5c4440ead2981056eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureEncryptionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureEncryptionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb64cebb0689344f644fc889fbe74db926c9428e174abed2f68f50eaecf4ae79)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageCloudAzureEncryptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06e5363c425918dc84c66a40894acf8c796c6e0b7c1a29c8d167c423bc6bc7eb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureEncryptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ba6f3db76647111eeb29525f3ba269f9f7ca1a0f71861b5cb7369eb3a3b2280)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77d40b86da6c9885ab48c5965205373609c4555a33643d493bcadb0b0bfa6325)
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
            type_hints = typing.get_type_hints(_typecheckingstub__79465de5c5a295b55b24667f952fd3967370eefdf0b29d3c2a6283b0a9e1bcf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryption]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__572f38846b7d145b0dd026820192255a69f74c61095e4bb75d7b08724135a77c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureEncryptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d2d15a9095b229f646a117ec445a60737e6da0997d021da1df7107f2ce0bf78a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putKeyprovider")
    def put_keyprovider(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureEncryptionKeyprovider, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d04c9d03cebc05a027a137c1dd26bca49ecaa4f46f55b46cc6041d4ef3fe1a8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKeyprovider", [value]))

    @jsii.member(jsii_name="resetCipher")
    def reset_cipher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCipher", []))

    @jsii.member(jsii_name="resetEncrypt")
    def reset_encrypt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncrypt", []))

    @jsii.member(jsii_name="resetKeylength")
    def reset_keylength(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeylength", []))

    @jsii.member(jsii_name="resetKeyprovider")
    def reset_keyprovider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyprovider", []))

    @builtins.property
    @jsii.member(jsii_name="keyprovider")
    def keyprovider(self) -> StorageCloudAzureEncryptionKeyproviderList:
        return typing.cast(StorageCloudAzureEncryptionKeyproviderList, jsii.get(self, "keyprovider"))

    @builtins.property
    @jsii.member(jsii_name="cipherInput")
    def cipher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cipherInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptInput")
    def encrypt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptInput"))

    @builtins.property
    @jsii.member(jsii_name="keylengthInput")
    def keylength_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keylengthInput"))

    @builtins.property
    @jsii.member(jsii_name="keyproviderInput")
    def keyprovider_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryptionKeyprovider]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryptionKeyprovider]]], jsii.get(self, "keyproviderInput"))

    @builtins.property
    @jsii.member(jsii_name="cipher")
    def cipher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cipher"))

    @cipher.setter
    def cipher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e087c7614a9046ef4eaec2dc594568554ca19e81fc9e24fbc1b11b6136acdcbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cipher", value)

    @builtins.property
    @jsii.member(jsii_name="encrypt")
    def encrypt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encrypt"))

    @encrypt.setter
    def encrypt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c01709bc2ed3104708bee400b6925863c438377366e4aa2399c1f6c6b1615684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encrypt", value)

    @builtins.property
    @jsii.member(jsii_name="keylength")
    def keylength(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keylength"))

    @keylength.setter
    def keylength(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbcb376f398c8a4c1053060edc6dae2f31e32e3fb0a5ad6d23b158bb5e655210)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keylength", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryption]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryption]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryption]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e82721ad29a33d8940db0e642a357859ac30376f24b58f5c4f049cb919672c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureMediaagent",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudAzureMediaagent:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8e73ab99eff40e5fb3f633edb0728125053a85de7a3d2a1eab5d2f393bf7223)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#name StorageCloudAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureMediaagent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureMediaagentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureMediaagentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86e23a24a4b57c89a6255ea148aad495e71e06a349979d824d6c0a87cffb3940)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageCloudAzureMediaagentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e43a60f067b8309d8dd590f40eeeda59bfc8e2694ddd4f96ac2e87297342c972)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureMediaagentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b63696d78bf7e90fdd0da8ee26950427485ee2d348fd9999658544298eb2128e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4adbdf0c6da9182b5bb09ac7dd4260b7f31336c72ff37c37a9982288c5f8d0b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e587c4fff01814399c903411ac1c7b7d4611d959209b424f17fb10a5a1acea85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureMediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureMediaagent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureMediaagent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2fe1e264d5324cd8e8d1e165a7368ba52a5c7fe142f291956ce0af8c0118d65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureMediaagentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureMediaagentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3ff5f5693c46df539ec9c40fd70aec43e28fa69523758c7eff73bdefa7c5718)
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
            type_hints = typing.get_type_hints(_typecheckingstub__74a6b822b9a76458a6480d960b4bed5c911510332f49e3dd1110af089047a4aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b57fbc75bc1f15e9c9053328579083f30a799a514b627ec19e9bb1ceeb2286a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureMediaagent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureMediaagent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureMediaagent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03989cb167dfd8c79ebf9defeb34edbf85f9a4dc07b511503bc31ac5355e23e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurity",
    jsii_struct_bases=[],
    name_mapping={"role": "role", "user": "user", "usergroup": "usergroup"},
)
class StorageCloudAzureSecurity:
    def __init__(
        self,
        *,
        role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurityRole", typing.Dict[builtins.str, typing.Any]]]]] = None,
        user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurityUser", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurityUsergroup", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param role: role block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#role StorageCloudAzure#role}
        :param user: user block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#user StorageCloudAzure#user}
        :param usergroup: usergroup block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#usergroup StorageCloudAzure#usergroup}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30a01fa0430afbcbedc45762b9aa8e7f8df450e471c58f34a1a4dc1722a23427)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
            check_type(argname="argument usergroup", value=usergroup, expected_type=type_hints["usergroup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role
        if user is not None:
            self._values["user"] = user
        if usergroup is not None:
            self._values["usergroup"] = usergroup

    @builtins.property
    def role(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityRole"]]]:
        '''role block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#role StorageCloudAzure#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityRole"]]], result)

    @builtins.property
    def user(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUser"]]]:
        '''user block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#user StorageCloudAzure#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUser"]]], result)

    @builtins.property
    def usergroup(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUsergroup"]]]:
        '''usergroup block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#usergroup StorageCloudAzure#usergroup}
        '''
        result = self._values.get("usergroup")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUsergroup"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudAzureSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureSecurityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b54bd8a6e284e768d3196f67f1dce4d5eca4019e2c3e2d8c7fbe83fc4b8eae86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageCloudAzureSecurityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c810b1242a6e2e2962b8e1848a8a9b57c0547951cd4d20ab5658d1a3481f6201)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureSecurityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b337de2c89d11aeb1018766a776308e74531b5a3afca49c0aca347466cc00b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__430ed6ecd09b5e5c3a4f6500ecfbbba1ee24e3491ec98a6fe615aa397320e6d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__295fa83b0b9e5da05addd47fb0ba6ed1fea9cd510584ca01f4278134e2398f37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12adadbf9265bb3a37b5082c247bb2e6c74dffb43f037875c4dfb355e5cf61d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureSecurityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ad4c7b84f99d4b9a0994a5218e146765e64434870abff2f3ca8c09b88c7c15a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRole")
    def put_role(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurityRole", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78d239d0d161de02e39399267d4f583c362fb4f91fa1a7c14e798138c22699d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRole", [value]))

    @jsii.member(jsii_name="putUser")
    def put_user(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurityUser", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af07fac55e29eb96b53251928cb8dbab60e04a313e8800d3c575492c1352d5b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUser", [value]))

    @jsii.member(jsii_name="putUsergroup")
    def put_usergroup(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudAzureSecurityUsergroup", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf51d0e07aae77ce244c0f7c30fe3a3b008f61f2ffd28a46483dc4ecd2a8a50e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUsergroup", [value]))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @jsii.member(jsii_name="resetUsergroup")
    def reset_usergroup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsergroup", []))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> "StorageCloudAzureSecurityRoleList":
        return typing.cast("StorageCloudAzureSecurityRoleList", jsii.get(self, "role"))

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> "StorageCloudAzureSecurityUserList":
        return typing.cast("StorageCloudAzureSecurityUserList", jsii.get(self, "user"))

    @builtins.property
    @jsii.member(jsii_name="usergroup")
    def usergroup(self) -> "StorageCloudAzureSecurityUsergroupList":
        return typing.cast("StorageCloudAzureSecurityUsergroupList", jsii.get(self, "usergroup"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityRole"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityRole"]]], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="usergroupInput")
    def usergroup_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUsergroup"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUsergroup"]]], jsii.get(self, "usergroupInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUser"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudAzureSecurityUser"]]], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96329fdb485e7e869aa6c5ef550734d68245961bcf7676772b64aee7cbf69edf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityRole",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class StorageCloudAzureSecurityRole:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6073c5cce64501513bd2d8f70dff3c492c9191a0c91e4cd9bb3b7c0930b89c03)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

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
        return "StorageCloudAzureSecurityRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureSecurityRoleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityRoleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3190c3e652886b2d0acebdfe51a818c88949b511d665b73dd2c2ddbaf8df97af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageCloudAzureSecurityRoleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8d8a5768665e24f3f0b3105830098a41985a663fe3a620d4cfd8e76aa8dbfb)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureSecurityRoleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b76c23ab709a64b180c0f67bedd8949b81d16feacd30954592d3234a42219715)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa48038e4101dc5d95786b9f5f4a6185a9687a2568e8c6e2b57fc2e3fe584f5a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81ca56823cc17344085fd548b93159eba3c97faab4a60b64d6e24e516db6d2d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityRole]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityRole]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityRole]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__136532c247735567939b227c4a61f5d19059305c1896d4c020a7652f41d52d05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureSecurityRoleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityRoleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__73798ffb9ea35ac29578e7ff88141d7df0c39429d3e41d334156622a3ea51e1e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad7a344019479a6fcfd63a5ca280c3309bd3bd9253d6ba3c83c36dab00f07267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityRole]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityRole]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityRole]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665dd205611ade069ff1abae0e77a753d4877f558fbc97fc396a1b2bc13ecdcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityUser",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class StorageCloudAzureSecurityUser:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63351e44ee10dd15492b96a15211807ad2e2d306f92c3c1c38cf68d10deb75f7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

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
        return "StorageCloudAzureSecurityUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureSecurityUserList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityUserList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6964bc130581a0763ca550ae0835e84a89507884cb3013520ac8304ea9e97a13)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "StorageCloudAzureSecurityUserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a78cd8af8848b77a8f4e5d40f1721d2a4364ed047d21a81b547dc1b8961043b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureSecurityUserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa7d7ba8cc140b2aad06cd138693e40da2437800caa1ecdca6c95383af6966ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b78b3626651c68e9dfc64bfe0c7e3c4745f09697ca319878652eab93ace7c81f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8db58161918fc19c6169b943a5469af83a305a596799facaf30480ae059fb79e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUser]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1456a3f0f10e01d8ecbda13dcb7a2bda6de95699aba423d59b8b2758ed9323a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureSecurityUserOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityUserOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__65f53fbffb86d5d9fc14e4996a71e3a495d58d42308342d2d5b1c206fb4f6726)
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
            type_hints = typing.get_type_hints(_typecheckingstub__156f46685de2180ee9d0ec95c8a3d952ad19493fd35e6496e9fef8738165fb67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUser]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUser]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUser]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67c07821a67232f2f6c8f6253119ede36507c18d01cdf7a592563cafaa75ba40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityUsergroup",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class StorageCloudAzureSecurityUsergroup:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__317a045939a6eb0d29232865b3b1eb308b18c945e7ffa869f93c693c9fdf0841)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_azure#id StorageCloudAzure#id}.

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
        return "StorageCloudAzureSecurityUsergroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudAzureSecurityUsergroupList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityUsergroupList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c37cef4bdfe398d307f8dfc712ed1d2ad954420d96a919f441fc139a80d13084)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudAzureSecurityUsergroupOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__804028ec57b0d3159497207e44c214695a559b03c4aa420ee7231a71a1668d78)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudAzureSecurityUsergroupOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f92dac41f6dd1e30501ca8b7191e94b312d35cd772b705074b64983f592f4a45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9c9618e9f4b78fa3107046a38d120e5c0e584a81785a23de4c0e3d2cbc7e397)
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
            type_hints = typing.get_type_hints(_typecheckingstub__be9696441b3f37a5a5ce01a74c554926712fdc2677daf4436ce9a98871586ea1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUsergroup]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUsergroup]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUsergroup]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4c0909db8bdef38ba838682076142c40a171dba0f074b109e36f0d0ac38e153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudAzureSecurityUsergroupOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudAzure.StorageCloudAzureSecurityUsergroupOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea7d3b1ae4d15831055453b442b660438845237112350a2aff06bc7bef4bf172)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b3ab3f8d703f093b7cf96a21f9b961cdec33c505229eb7b2618f028f76b19b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUsergroup]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUsergroup]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUsergroup]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a277a2a96f692c53a4bacc3ad5c8a25143808e7a40a2ab5efa4912f04c2dcfd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageCloudAzure",
    "StorageCloudAzureConfig",
    "StorageCloudAzureCredentials",
    "StorageCloudAzureCredentialsList",
    "StorageCloudAzureCredentialsOutputReference",
    "StorageCloudAzureDeduplicationdblocation",
    "StorageCloudAzureDeduplicationdblocationList",
    "StorageCloudAzureDeduplicationdblocationMediaagent",
    "StorageCloudAzureDeduplicationdblocationMediaagentList",
    "StorageCloudAzureDeduplicationdblocationMediaagentOutputReference",
    "StorageCloudAzureDeduplicationdblocationOutputReference",
    "StorageCloudAzureEncryption",
    "StorageCloudAzureEncryptionKeyprovider",
    "StorageCloudAzureEncryptionKeyproviderList",
    "StorageCloudAzureEncryptionKeyproviderOutputReference",
    "StorageCloudAzureEncryptionList",
    "StorageCloudAzureEncryptionOutputReference",
    "StorageCloudAzureMediaagent",
    "StorageCloudAzureMediaagentList",
    "StorageCloudAzureMediaagentOutputReference",
    "StorageCloudAzureSecurity",
    "StorageCloudAzureSecurityList",
    "StorageCloudAzureSecurityOutputReference",
    "StorageCloudAzureSecurityRole",
    "StorageCloudAzureSecurityRoleList",
    "StorageCloudAzureSecurityRoleOutputReference",
    "StorageCloudAzureSecurityUser",
    "StorageCloudAzureSecurityUserList",
    "StorageCloudAzureSecurityUserOutputReference",
    "StorageCloudAzureSecurityUsergroup",
    "StorageCloudAzureSecurityUsergroupList",
    "StorageCloudAzureSecurityUsergroupOutputReference",
]

publication.publish()

def _typecheckingstub__52fd31619b2a5f0880d407bbc630a47c99178fa4e3bd6b5dd62f67d082c9fb70(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    authentication: builtins.str,
    container: builtins.str,
    mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureMediaagent, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    storageclass: builtins.str,
    accountname: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    deduplicationdblocation: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureDeduplicationdblocation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    encryption: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureEncryption, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    servicehost: typing.Optional[builtins.str] = None,
    usededuplication: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__9f6b10da71b61b3aefaa5bdef5a0e7d2b208b61c55f12aa750a05befdb31535b(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c23cac1dd6fe15828c23d3a7ef6b886ed62d09df6057ac559e31da537b126c1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureCredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d56609900ff65e8e251a44346f41417479d8c094dc5948433e62de6e40676e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureDeduplicationdblocation, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20caba3f77b60eb8dd682c9f927e1710b3a2a04bbf637263d30e59c004d7b013(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureEncryption, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf02d8bee817759071137b82350f2ffa26910b5cd195f18e37061c0621bc217c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureMediaagent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d071135b1d11ab858d6db6be2c18f0a0370b39e235d3ccc2d84ff48e15080443(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e63801ddd47e44669af013d9494ff008bc09bbf59e54cdd0fedd2353f2a7591(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dab606bd33324a1f387a02dbb8942eff2cf292b2a9086700d431055d57168dd4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ea03ff4d0ccae9859bdc1e46640719171d153f99a6d6a5ec47ea826eae0516(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7a1e3a0882330d3431a0fab80671c11abd73536e3714413cfc50d25b05f32b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd563e74a11c682be9ea6f29f8e052c3d91ef24209f8f077a26076304f999db2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d45461afedf59b78111fd3d4ba9c5bb2e351ecca24389592bf186c32b56e9a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8d5f8efb462ce3e93606c65e5c1cc080c0f289ba2e8959ef8fbfa6ea838596(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126f81b0946368381c014d924a4a5e690743d34065b24d8ec38a83e2e5eea2f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d3151b4b4d2c7baba6e57b658ce5d387975bf8eb51afec4e24647e3a8cc8df(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    authentication: builtins.str,
    container: builtins.str,
    mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureMediaagent, typing.Dict[builtins.str, typing.Any]]]],
    name: builtins.str,
    storageclass: builtins.str,
    accountname: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    deduplicationdblocation: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureDeduplicationdblocation, typing.Dict[builtins.str, typing.Any]]]]] = None,
    encryption: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureEncryption, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    servicehost: typing.Optional[builtins.str] = None,
    usededuplication: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32cb9ecb26719f2da692f6cf4111d869b4041aca4f53448ad865fafc3f701223(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57e55e6f1897797b0a47ea49ed563958a61afab5a7aee0969e770afdc5ac7f0a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29319920541ccbb007ec6bb055c7ce90574dc0d618cd392d61515163e66a173(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa5ff791b3ad81cf7cdaa0c0cbb146b319009ff47bf3afed37ba9fcc4bf56a97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ca03256b3ae2873a1c4f294819dff6806ad08868deeca5b14b2023109240ab8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8e6be2f46cdeaeb958559cf77f0880e02faf72d51bf9dba96570b24ed6efca4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7879c0d669a6a2023a1e90a88793fee7a530ea9530eeb2a7f0addfdd63f112(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureCredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__498b41340dab61988ae96c388efd9b8bf34566597d37094baf000050c9f773f0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2ae1bd61ee06364e04635372bae7cfa407a72b13bac554920cf5c8642c83d52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__476b9d32ed9b691fbcb8d558aa4b2a89b3b26948c803d95f8cdbf8b1933a3b33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64dbeffba08fc53091a4b2ed2ac9c1ff6fe4d9fb903c2b0c40e87a09d394de6c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureCredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dde537d8635a038c9b182a9b2a2f1a6952d639d83d4894229a4162556624dec(
    *,
    mediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureDeduplicationdblocationMediaagent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5eceb53aef05700e2f4686398909633d04fbacf1b56ea9a15e67f9f7474f1ce6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b2c4300149a68991767da0440d6d46a8eee1e25ecc4fbcd79211fcb3b8fd363(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48316706e105990f8ad3bc2b2c58416fac27895a177c72c48c3640b734363e29(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3a9e9bd059f46623cdc0ed05544ed587b0df8e828eddf3b4de4c139d1f70e3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__746e2c20400325b99a9cd351ed6bdffafdcd1e3e268782a8240fc3c998be2e03(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__950b5e6e0976f23e445b54078f9cc35e70f32b7b692a60a36d8158417dae9a16(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocation]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a6c666ada02d0a6165862d73824ed3f6a167901157722a95f8bd35a878a0443(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be8a85bb1b8c881842109e0e051841967a79199c30df3611471494447cff304(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e2bd3157dba5871240c6c435901281a475649daa2588d0b25f72e408b159898(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1f9a37cb0ebdb9d52ea6a801caa39c0e0a225d502bdff29d8a0a54cfb58993(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3959dc18ccf6151482331b7db5c2890e7be86fdc4fd43bb46f42a902764c7b39(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f76c85976939d96dadfae39d7dc8af3a3174ad8d5edf4e1badcc302369b19e73(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3be99194508122147afbd1f4109157ebb02101e86a01052481a9134ca24ab4f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureDeduplicationdblocationMediaagent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9335d758025e4debd997bc09c14949a79f58b85368f7a8aa6aa48fef0a1bae5c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932a7ebbf8b1263b9340b0eb1d313a1370383c189fa7991e6e36bb0b7b89949e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e52c470ef36fb0346cde31c8e8fba12c0f48877b252ff7ccfa9f9122b194c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e82535cedd6066a3694fc75c44d9c104f95a7c6c376a7316ee4f537a90288fb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocationMediaagent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9410ab26e446bddebe3b7d7781c9e439e6ac22a7928677c17c03ad84560ddbf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88c2a15247021691c57ba574dc88f2a8c8c9d991c712758db52d55f2ad8c874(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureDeduplicationdblocationMediaagent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a0cabe5c5876ab406191f09572a54956b3d55d93b87aecd6f17f05c2ad9571c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2a802ef979b4e25385b42843ed4c1b7483b1f75a885d2a39d5e08a474b7a33(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureDeduplicationdblocation]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d2c9759df130c56e8ce9591661c70ee6d28bc6159999a76b43e7baf07e916bb(
    *,
    cipher: typing.Optional[builtins.str] = None,
    encrypt: typing.Optional[builtins.str] = None,
    keylength: typing.Optional[jsii.Number] = None,
    keyprovider: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureEncryptionKeyprovider, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0305abe2c078f99352515b315384108ed127f7b9a3f9d23158db16e3c1729846(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b3d32eaa07155d5e2515a2d0ca505c49e1cad4ea1a41d8ddf38f7da68df3533(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d203a226ff3c71be7c327c1dc82f27e558803459990c6c137eb8b5ab4ee5b7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f7fe6cc280db41f07638f38d18f70afd21b2240a252804a17f240e4a0e77d2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c7a3a78f6fd783c3cc2f86df3c2380e100ce3d8028b91af10a933523e8170a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4a7cd299a26d64d8ca9ef8ec688693417ab77916206961c27b509c625c1b59(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9bea4acf78cf3f6a3a24c7e73062e1ffdaff488449fe2530222c4cfa41057df(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryptionKeyprovider]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ea7c01102ecabfc9b2bdd96f29f4b911bc1af4e3afc6ecd0132b17e8add67b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fe38f0b6b74b7023717f824658de1f367c181e402c62f61b86124c0d98a4ca5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6408423cf79a57733f76e5d0fe5e992bbeb4bff194725d7249f97323ebf4cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f28a0523ab967bb3725ff47e1532ff832c7a3e5a5f13b5c4440ead2981056eb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryptionKeyprovider]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb64cebb0689344f644fc889fbe74db926c9428e174abed2f68f50eaecf4ae79(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06e5363c425918dc84c66a40894acf8c796c6e0b7c1a29c8d167c423bc6bc7eb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ba6f3db76647111eeb29525f3ba269f9f7ca1a0f71861b5cb7369eb3a3b2280(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d40b86da6c9885ab48c5965205373609c4555a33643d493bcadb0b0bfa6325(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79465de5c5a295b55b24667f952fd3967370eefdf0b29d3c2a6283b0a9e1bcf5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__572f38846b7d145b0dd026820192255a69f74c61095e4bb75d7b08724135a77c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureEncryption]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d15a9095b229f646a117ec445a60737e6da0997d021da1df7107f2ce0bf78a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d04c9d03cebc05a027a137c1dd26bca49ecaa4f46f55b46cc6041d4ef3fe1a8d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureEncryptionKeyprovider, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e087c7614a9046ef4eaec2dc594568554ca19e81fc9e24fbc1b11b6136acdcbc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c01709bc2ed3104708bee400b6925863c438377366e4aa2399c1f6c6b1615684(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbcb376f398c8a4c1053060edc6dae2f31e32e3fb0a5ad6d23b158bb5e655210(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e82721ad29a33d8940db0e642a357859ac30376f24b58f5c4f049cb919672c3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureEncryption]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8e73ab99eff40e5fb3f633edb0728125053a85de7a3d2a1eab5d2f393bf7223(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86e23a24a4b57c89a6255ea148aad495e71e06a349979d824d6c0a87cffb3940(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e43a60f067b8309d8dd590f40eeeda59bfc8e2694ddd4f96ac2e87297342c972(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b63696d78bf7e90fdd0da8ee26950427485ee2d348fd9999658544298eb2128e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4adbdf0c6da9182b5bb09ac7dd4260b7f31336c72ff37c37a9982288c5f8d0b1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e587c4fff01814399c903411ac1c7b7d4611d959209b424f17fb10a5a1acea85(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2fe1e264d5324cd8e8d1e165a7368ba52a5c7fe142f291956ce0af8c0118d65(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureMediaagent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ff5f5693c46df539ec9c40fd70aec43e28fa69523758c7eff73bdefa7c5718(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74a6b822b9a76458a6480d960b4bed5c911510332f49e3dd1110af089047a4aa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b57fbc75bc1f15e9c9053328579083f30a799a514b627ec19e9bb1ceeb2286a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03989cb167dfd8c79ebf9defeb34edbf85f9a4dc07b511503bc31ac5355e23e0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureMediaagent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a01fa0430afbcbedc45762b9aa8e7f8df450e471c58f34a1a4dc1722a23427(
    *,
    role: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurityRole, typing.Dict[builtins.str, typing.Any]]]]] = None,
    user: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurityUser, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usergroup: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurityUsergroup, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54bd8a6e284e768d3196f67f1dce4d5eca4019e2c3e2d8c7fbe83fc4b8eae86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c810b1242a6e2e2962b8e1848a8a9b57c0547951cd4d20ab5658d1a3481f6201(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b337de2c89d11aeb1018766a776308e74531b5a3afca49c0aca347466cc00b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430ed6ecd09b5e5c3a4f6500ecfbbba1ee24e3491ec98a6fe615aa397320e6d9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__295fa83b0b9e5da05addd47fb0ba6ed1fea9cd510584ca01f4278134e2398f37(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12adadbf9265bb3a37b5082c247bb2e6c74dffb43f037875c4dfb355e5cf61d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad4c7b84f99d4b9a0994a5218e146765e64434870abff2f3ca8c09b88c7c15a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78d239d0d161de02e39399267d4f583c362fb4f91fa1a7c14e798138c22699d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurityRole, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af07fac55e29eb96b53251928cb8dbab60e04a313e8800d3c575492c1352d5b9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurityUser, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf51d0e07aae77ce244c0f7c30fe3a3b008f61f2ffd28a46483dc4ecd2a8a50e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudAzureSecurityUsergroup, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96329fdb485e7e869aa6c5ef550734d68245961bcf7676772b64aee7cbf69edf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6073c5cce64501513bd2d8f70dff3c492c9191a0c91e4cd9bb3b7c0930b89c03(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3190c3e652886b2d0acebdfe51a818c88949b511d665b73dd2c2ddbaf8df97af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8d8a5768665e24f3f0b3105830098a41985a663fe3a620d4cfd8e76aa8dbfb(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76c23ab709a64b180c0f67bedd8949b81d16feacd30954592d3234a42219715(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa48038e4101dc5d95786b9f5f4a6185a9687a2568e8c6e2b57fc2e3fe584f5a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81ca56823cc17344085fd548b93159eba3c97faab4a60b64d6e24e516db6d2d5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136532c247735567939b227c4a61f5d19059305c1896d4c020a7652f41d52d05(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityRole]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73798ffb9ea35ac29578e7ff88141d7df0c39429d3e41d334156622a3ea51e1e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad7a344019479a6fcfd63a5ca280c3309bd3bd9253d6ba3c83c36dab00f07267(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665dd205611ade069ff1abae0e77a753d4877f558fbc97fc396a1b2bc13ecdcd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityRole]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63351e44ee10dd15492b96a15211807ad2e2d306f92c3c1c38cf68d10deb75f7(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6964bc130581a0763ca550ae0835e84a89507884cb3013520ac8304ea9e97a13(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a78cd8af8848b77a8f4e5d40f1721d2a4364ed047d21a81b547dc1b8961043b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa7d7ba8cc140b2aad06cd138693e40da2437800caa1ecdca6c95383af6966ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b78b3626651c68e9dfc64bfe0c7e3c4745f09697ca319878652eab93ace7c81f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db58161918fc19c6169b943a5469af83a305a596799facaf30480ae059fb79e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1456a3f0f10e01d8ecbda13dcb7a2bda6de95699aba423d59b8b2758ed9323a1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUser]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65f53fbffb86d5d9fc14e4996a71e3a495d58d42308342d2d5b1c206fb4f6726(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156f46685de2180ee9d0ec95c8a3d952ad19493fd35e6496e9fef8738165fb67(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67c07821a67232f2f6c8f6253119ede36507c18d01cdf7a592563cafaa75ba40(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUser]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__317a045939a6eb0d29232865b3b1eb308b18c945e7ffa869f93c693c9fdf0841(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37cef4bdfe398d307f8dfc712ed1d2ad954420d96a919f441fc139a80d13084(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804028ec57b0d3159497207e44c214695a559b03c4aa420ee7231a71a1668d78(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f92dac41f6dd1e30501ca8b7191e94b312d35cd772b705074b64983f592f4a45(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c9618e9f4b78fa3107046a38d120e5c0e584a81785a23de4c0e3d2cbc7e397(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be9696441b3f37a5a5ce01a74c554926712fdc2677daf4436ce9a98871586ea1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4c0909db8bdef38ba838682076142c40a171dba0f074b109e36f0d0ac38e153(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudAzureSecurityUsergroup]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea7d3b1ae4d15831055453b442b660438845237112350a2aff06bc7bef4bf172(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3ab3f8d703f093b7cf96a21f9b961cdec33c505229eb7b2618f028f76b19b3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a277a2a96f692c53a4bacc3ad5c8a25143808e7a40a2ab5efa4912f04c2dcfd7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudAzureSecurityUsergroup]],
) -> None:
    """Type checking stubs"""
    pass
