'''
# `commvault_hypervisor_aws`

Refer to the Terraform Registry for docs: [`commvault_hypervisor_aws`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws).
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


class HypervisorAws(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAws",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws commvault_hypervisor_aws}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        accesskey: builtins.str,
        name: builtins.str,
        secretkey: builtins.str,
        useiamrole: builtins.str,
        accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsAccessnodes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrol", typing.Dict[builtins.str, typing.Any]]]]] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        displayname: typing.Optional[builtins.str] = None,
        enableawsadminaccount: typing.Optional[builtins.str] = None,
        etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsEtcdprotection", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsFbrunixmediaagent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hypervisortype: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rolearn: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        skipcredentialvalidation: typing.Optional[builtins.str] = None,
        useserviceaccount: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws commvault_hypervisor_aws} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param accesskey: Access Key of Amazon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#accesskey HypervisorAws#accesskey}
        :param name: The name of the hypervisor group being created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        :param secretkey: secret Key of Amazon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#secretkey HypervisorAws#secretkey}
        :param useiamrole: if Iam Role is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#useiamrole HypervisorAws#useiamrole}
        :param accessnodes: accessnodes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#accessnodes HypervisorAws#accessnodes}
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitycontrol HypervisorAws#activitycontrol}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#credentials HypervisorAws#credentials}
        :param displayname: The name of the hypervisor that has to be changed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#displayname HypervisorAws#displayname}
        :param enableawsadminaccount: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableawsadminaccount HypervisorAws#enableawsadminaccount}.
        :param etcdprotection: etcdprotection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#etcdprotection HypervisorAws#etcdprotection}
        :param fbrunixmediaagent: fbrunixmediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#fbrunixmediaagent HypervisorAws#fbrunixmediaagent}
        :param hypervisortype: [Amazon]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#hypervisortype HypervisorAws#hypervisortype}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: AWS region if Iam role is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#region HypervisorAws#region}
        :param rolearn: Role ARN for STS assume role with IAM policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#rolearn HypervisorAws#rolearn}
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#security HypervisorAws#security}
        :param settings: settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#settings HypervisorAws#settings}
        :param skipcredentialvalidation: if credential validation has to be skipped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#skipcredentialvalidation HypervisorAws#skipcredentialvalidation}
        :param useserviceaccount: Clientname to be used as Admin Account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#useserviceaccount HypervisorAws#useserviceaccount}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba79429b3d746a73e900e838121cc94859c11d3f5a16c5c6a38943daf397c5e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HypervisorAwsConfig(
            accesskey=accesskey,
            name=name,
            secretkey=secretkey,
            useiamrole=useiamrole,
            accessnodes=accessnodes,
            activitycontrol=activitycontrol,
            credentials=credentials,
            displayname=displayname,
            enableawsadminaccount=enableawsadminaccount,
            etcdprotection=etcdprotection,
            fbrunixmediaagent=fbrunixmediaagent,
            hypervisortype=hypervisortype,
            id=id,
            region=region,
            rolearn=rolearn,
            security=security,
            settings=settings,
            skipcredentialvalidation=skipcredentialvalidation,
            useserviceaccount=useserviceaccount,
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
        '''Generates CDKTF code for importing a HypervisorAws resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the HypervisorAws to import.
        :param import_from_id: The id of the existing HypervisorAws that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the HypervisorAws to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c758abb84ce1437a1c73cb953494923a0d0f5b62931563323ab40d87c8eb01ba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAccessnodes")
    def put_accessnodes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsAccessnodes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d94cc290b2dcd2ed97d32379b0182297e09b39a730c698016261a674a51ad4df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessnodes", [value]))

    @jsii.member(jsii_name="putActivitycontrol")
    def put_activitycontrol(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrol", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10896250b8e61f82709e8f4c65c893fb9009c4b778ad10283c082dd6c9f3c5d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActivitycontrol", [value]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsCredentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8a384a3df0912f761daab3abe44b60e3d51a1be2365e2fa7d771030a48cb0ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putEtcdprotection")
    def put_etcdprotection(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsEtcdprotection", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b1f84f9b20090b06c893c3a9fb5ca285c999e3c10b817183e203340fdb415e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEtcdprotection", [value]))

    @jsii.member(jsii_name="putFbrunixmediaagent")
    def put_fbrunixmediaagent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsFbrunixmediaagent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6f7b4bc62835758b3ea2e7c2e5477414fa0f0275619fd3772948211d2bb3303)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFbrunixmediaagent", [value]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSecurity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__735c5df166bb0de23c8df5ac794f04b5360c6173ec4e9aeb344d886f42859183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecurity", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ac675e97bc93af92b64234d1d35fcfe502fe1e8c79b09ecd00edbf6f4cb0fc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="resetAccessnodes")
    def reset_accessnodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessnodes", []))

    @jsii.member(jsii_name="resetActivitycontrol")
    def reset_activitycontrol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivitycontrol", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetDisplayname")
    def reset_displayname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayname", []))

    @jsii.member(jsii_name="resetEnableawsadminaccount")
    def reset_enableawsadminaccount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableawsadminaccount", []))

    @jsii.member(jsii_name="resetEtcdprotection")
    def reset_etcdprotection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEtcdprotection", []))

    @jsii.member(jsii_name="resetFbrunixmediaagent")
    def reset_fbrunixmediaagent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFbrunixmediaagent", []))

    @jsii.member(jsii_name="resetHypervisortype")
    def reset_hypervisortype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHypervisortype", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRolearn")
    def reset_rolearn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRolearn", []))

    @jsii.member(jsii_name="resetSecurity")
    def reset_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurity", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetSkipcredentialvalidation")
    def reset_skipcredentialvalidation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipcredentialvalidation", []))

    @jsii.member(jsii_name="resetUseserviceaccount")
    def reset_useserviceaccount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseserviceaccount", []))

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
    @jsii.member(jsii_name="accessnodes")
    def accessnodes(self) -> "HypervisorAwsAccessnodesList":
        return typing.cast("HypervisorAwsAccessnodesList", jsii.get(self, "accessnodes"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrol")
    def activitycontrol(self) -> "HypervisorAwsActivitycontrolList":
        return typing.cast("HypervisorAwsActivitycontrolList", jsii.get(self, "activitycontrol"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "HypervisorAwsCredentialsList":
        return typing.cast("HypervisorAwsCredentialsList", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="etcdprotection")
    def etcdprotection(self) -> "HypervisorAwsEtcdprotectionList":
        return typing.cast("HypervisorAwsEtcdprotectionList", jsii.get(self, "etcdprotection"))

    @builtins.property
    @jsii.member(jsii_name="fbrunixmediaagent")
    def fbrunixmediaagent(self) -> "HypervisorAwsFbrunixmediaagentList":
        return typing.cast("HypervisorAwsFbrunixmediaagentList", jsii.get(self, "fbrunixmediaagent"))

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> "HypervisorAwsSecurityList":
        return typing.cast("HypervisorAwsSecurityList", jsii.get(self, "security"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "HypervisorAwsSettingsList":
        return typing.cast("HypervisorAwsSettingsList", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="accesskeyInput")
    def accesskey_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accesskeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessnodesInput")
    def accessnodes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsAccessnodes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsAccessnodes"]]], jsii.get(self, "accessnodesInput"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrolInput")
    def activitycontrol_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrol"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrol"]]], jsii.get(self, "activitycontrolInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsCredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsCredentials"]]], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="displaynameInput")
    def displayname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displaynameInput"))

    @builtins.property
    @jsii.member(jsii_name="enableawsadminaccountInput")
    def enableawsadminaccount_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableawsadminaccountInput"))

    @builtins.property
    @jsii.member(jsii_name="etcdprotectionInput")
    def etcdprotection_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotection"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotection"]]], jsii.get(self, "etcdprotectionInput"))

    @builtins.property
    @jsii.member(jsii_name="fbrunixmediaagentInput")
    def fbrunixmediaagent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsFbrunixmediaagent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsFbrunixmediaagent"]]], jsii.get(self, "fbrunixmediaagentInput"))

    @builtins.property
    @jsii.member(jsii_name="hypervisortypeInput")
    def hypervisortype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hypervisortypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="rolearnInput")
    def rolearn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rolearnInput"))

    @builtins.property
    @jsii.member(jsii_name="secretkeyInput")
    def secretkey_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretkeyInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSecurity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSecurity"]]], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettings"]]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipcredentialvalidationInput")
    def skipcredentialvalidation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skipcredentialvalidationInput"))

    @builtins.property
    @jsii.member(jsii_name="useiamroleInput")
    def useiamrole_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useiamroleInput"))

    @builtins.property
    @jsii.member(jsii_name="useserviceaccountInput")
    def useserviceaccount_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useserviceaccountInput"))

    @builtins.property
    @jsii.member(jsii_name="accesskey")
    def accesskey(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accesskey"))

    @accesskey.setter
    def accesskey(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25072377c15de32f3234405760a62e2f08c18f82bbeea933ed924354cfe3180b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accesskey", value)

    @builtins.property
    @jsii.member(jsii_name="displayname")
    def displayname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayname"))

    @displayname.setter
    def displayname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e59e515f9279e25e87ac65ed94cb51658ba9320b1ab478d2c42d35d8846caa3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayname", value)

    @builtins.property
    @jsii.member(jsii_name="enableawsadminaccount")
    def enableawsadminaccount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableawsadminaccount"))

    @enableawsadminaccount.setter
    def enableawsadminaccount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f05236d2e1e2b9c47414f8764631838bf66591fdafc2b93f9665204d575d4a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableawsadminaccount", value)

    @builtins.property
    @jsii.member(jsii_name="hypervisortype")
    def hypervisortype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hypervisortype"))

    @hypervisortype.setter
    def hypervisortype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d3df5832328a8a5007d9ce1fcbe8697011bfe0562bfb0af322a56022a6b281b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hypervisortype", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b678faa439124f15a15387905cb3aaa0ca9bd81601b921331a2a9e3cbc696578)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__208f6b343d3b611cc91b0e9d674c624efe9cd4802caaa671d52384bc2b7adc5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51f75abeef1e463cc5a19c91aa36ae7f43201fb0778b52f8aa62d4d9a2ef1a27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="rolearn")
    def rolearn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rolearn"))

    @rolearn.setter
    def rolearn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc3158f246dfb83eec5d47d0b1e23f4ac4eb05fd927e30d272e97b5066cfc2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rolearn", value)

    @builtins.property
    @jsii.member(jsii_name="secretkey")
    def secretkey(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretkey"))

    @secretkey.setter
    def secretkey(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c720080dc876a1114d867d0ba7735ae9dd4263a0a0514334be1003f52db1d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretkey", value)

    @builtins.property
    @jsii.member(jsii_name="skipcredentialvalidation")
    def skipcredentialvalidation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skipcredentialvalidation"))

    @skipcredentialvalidation.setter
    def skipcredentialvalidation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f475c30388889a39ada8aba1cf061b143b3eda8d4e84c368fb6c46c8da2e20f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipcredentialvalidation", value)

    @builtins.property
    @jsii.member(jsii_name="useiamrole")
    def useiamrole(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useiamrole"))

    @useiamrole.setter
    def useiamrole(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634e3ebedb4712694d456e31f9f7c7901bd69341eae5833200430b18586d5f98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useiamrole", value)

    @builtins.property
    @jsii.member(jsii_name="useserviceaccount")
    def useserviceaccount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useserviceaccount"))

    @useserviceaccount.setter
    def useserviceaccount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ccadb608377f0004f7be32d37790150894666f3fbc0b527250c1b8a1ea40954)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useserviceaccount", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsAccessnodes",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class HypervisorAwsAccessnodes:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        type: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param type: Type of access node , Ex: 3 - access Node , 28 - Access Node Groups. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#type HypervisorAws#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e11f173b15cbc2e649546bb82cdde05a1d0eebdd7781f48252a6893efaf53bf6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[jsii.Number]:
        '''Type of access node , Ex: 3 - access Node , 28 - Access Node Groups.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#type HypervisorAws#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsAccessnodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsAccessnodesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsAccessnodesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__19f13f07f595615574cc49d743e6a81a954974ed465c5e856e7000eac0f8848f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsAccessnodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0c43aeab2083909ab908a60a63036213342c62be3c4dd6285bc50235bbd81b1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsAccessnodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b022b478299c5d4de664592bade71f7a7bfb4a2e64dd238ddee67f4f9a90db0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c4578cfd893a6667f53f4efe95bed1756668f109dc093896d7b232450056cbc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cafdcf2120261ee51419d6d42e743da9d55af4ffea6254c9f460c713bc8e990e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsAccessnodes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsAccessnodes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsAccessnodes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__379818b1367d886e114d9c19064040596e1b8575fe9c9b4d6fec7f872d9f222b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsAccessnodesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsAccessnodesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7d491cd13c4b77ec0d94b096ee11ccca5e8fb96216d1347e684fb1c339f4bac4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2878aec4c871630ba0c5316bfa5458d105797a7114ed74e00be7a5d51ad47cf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "type"))

    @type.setter
    def type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4dc28efe705df0afef7d6647ba323849bc91d58a8ddd3350bc6530548e4a9fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsAccessnodes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsAccessnodes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsAccessnodes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58bd37333b150917419629434cd2cc1f7161de64519608ce4e9f0c36aa54d23a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrol",
    jsii_struct_bases=[],
    name_mapping={
        "backupactivitycontroloptions": "backupactivitycontroloptions",
        "enablebackup": "enablebackup",
        "enablerestore": "enablerestore",
        "restoreactivitycontroloptions": "restoreactivitycontroloptions",
    },
)
class HypervisorAwsActivitycontrol:
    def __init__(
        self,
        *,
        backupactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolBackupactivitycontroloptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enablebackup: typing.Optional[builtins.str] = None,
        enablerestore: typing.Optional[builtins.str] = None,
        restoreactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolRestoreactivitycontroloptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backupactivitycontroloptions: backupactivitycontroloptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#backupactivitycontroloptions HypervisorAws#backupactivitycontroloptions}
        :param enablebackup: true if Backup is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enablebackup HypervisorAws#enablebackup}
        :param enablerestore: true if Restore is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enablerestore HypervisorAws#enablerestore}
        :param restoreactivitycontroloptions: restoreactivitycontroloptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#restoreactivitycontroloptions HypervisorAws#restoreactivitycontroloptions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd46c9e116e2fc30c4baaf977fb664e62c5399c15513a8cfabefc0e6473a3ecb)
            check_type(argname="argument backupactivitycontroloptions", value=backupactivitycontroloptions, expected_type=type_hints["backupactivitycontroloptions"])
            check_type(argname="argument enablebackup", value=enablebackup, expected_type=type_hints["enablebackup"])
            check_type(argname="argument enablerestore", value=enablerestore, expected_type=type_hints["enablerestore"])
            check_type(argname="argument restoreactivitycontroloptions", value=restoreactivitycontroloptions, expected_type=type_hints["restoreactivitycontroloptions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupactivitycontroloptions is not None:
            self._values["backupactivitycontroloptions"] = backupactivitycontroloptions
        if enablebackup is not None:
            self._values["enablebackup"] = enablebackup
        if enablerestore is not None:
            self._values["enablerestore"] = enablerestore
        if restoreactivitycontroloptions is not None:
            self._values["restoreactivitycontroloptions"] = restoreactivitycontroloptions

    @builtins.property
    def backupactivitycontroloptions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptions"]]]:
        '''backupactivitycontroloptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#backupactivitycontroloptions HypervisorAws#backupactivitycontroloptions}
        '''
        result = self._values.get("backupactivitycontroloptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptions"]]], result)

    @builtins.property
    def enablebackup(self) -> typing.Optional[builtins.str]:
        '''true if Backup is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enablebackup HypervisorAws#enablebackup}
        '''
        result = self._values.get("enablebackup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enablerestore(self) -> typing.Optional[builtins.str]:
        '''true if Restore is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enablerestore HypervisorAws#enablerestore}
        '''
        result = self._values.get("enablerestore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restoreactivitycontroloptions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptions"]]]:
        '''restoreactivitycontroloptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#restoreactivitycontroloptions HypervisorAws#restoreactivitycontroloptions}
        '''
        result = self._values.get("restoreactivitycontroloptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptions",
    jsii_struct_bases=[],
    name_mapping={
        "activitytype": "activitytype",
        "delaytime": "delaytime",
        "enableactivitytype": "enableactivitytype",
        "enableafteradelay": "enableafteradelay",
    },
)
class HypervisorAwsActivitycontrolBackupactivitycontroloptions:
    def __init__(
        self,
        *,
        activitytype: typing.Optional[builtins.str] = None,
        delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enableactivitytype: typing.Optional[builtins.str] = None,
        enableafteradelay: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param activitytype: denotes the activity type being considered [BACKUP, RESTORE, ONLINECI, ARCHIVEPRUNE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitytype HypervisorAws#activitytype}
        :param delaytime: delaytime block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#delaytime HypervisorAws#delaytime}
        :param enableactivitytype: True if the activity type is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableactivitytype HypervisorAws#enableactivitytype}
        :param enableafteradelay: True if the activity will be enabled after a delay time interval. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableafteradelay HypervisorAws#enableafteradelay}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d161e716ef20fc45c0e8f236f61e2ee6b94e534901916db79a88ae0a31c6f4d6)
            check_type(argname="argument activitytype", value=activitytype, expected_type=type_hints["activitytype"])
            check_type(argname="argument delaytime", value=delaytime, expected_type=type_hints["delaytime"])
            check_type(argname="argument enableactivitytype", value=enableactivitytype, expected_type=type_hints["enableactivitytype"])
            check_type(argname="argument enableafteradelay", value=enableafteradelay, expected_type=type_hints["enableafteradelay"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activitytype is not None:
            self._values["activitytype"] = activitytype
        if delaytime is not None:
            self._values["delaytime"] = delaytime
        if enableactivitytype is not None:
            self._values["enableactivitytype"] = enableactivitytype
        if enableafteradelay is not None:
            self._values["enableafteradelay"] = enableafteradelay

    @builtins.property
    def activitytype(self) -> typing.Optional[builtins.str]:
        '''denotes the activity type being considered [BACKUP, RESTORE, ONLINECI, ARCHIVEPRUNE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitytype HypervisorAws#activitytype}
        '''
        result = self._values.get("activitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delaytime(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime"]]]:
        '''delaytime block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#delaytime HypervisorAws#delaytime}
        '''
        result = self._values.get("delaytime")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime"]]], result)

    @builtins.property
    def enableactivitytype(self) -> typing.Optional[builtins.str]:
        '''True if the activity type is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableactivitytype HypervisorAws#enableactivitytype}
        '''
        result = self._values.get("enableactivitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enableafteradelay(self) -> typing.Optional[builtins.str]:
        '''True if the activity will be enabled after a delay time interval.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableafteradelay HypervisorAws#enableafteradelay}
        '''
        result = self._values.get("enableafteradelay")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrolBackupactivitycontroloptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime",
    jsii_struct_bases=[],
    name_mapping={"time": "time", "timezone": "timezone", "value": "value"},
)
class HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime:
    def __init__(
        self,
        *,
        time: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param time: delay time in unix timestamp. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#time HypervisorAws#time}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#timezone HypervisorAws#timezone}
        :param value: actual delay time value in string format according to the timezone. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#value HypervisorAws#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d04a84b6a13cbc33cd7d42929709135478c2db16164797de8d90c6a38cd16e)
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if time is not None:
            self._values["time"] = time
        if timezone is not None:
            self._values["timezone"] = timezone
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def time(self) -> typing.Optional[jsii.Number]:
        '''delay time in unix timestamp.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#time HypervisorAws#time}
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#timezone HypervisorAws#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''actual delay time value in string format according to the timezone.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#value HypervisorAws#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__160f932080e73164169ce77553fb3afe61436c114f0abbdf063dcba50c0a8139)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a21c3d3e63ae2724f2c4e048fc1b980dea02857980d3bf573acc7faf2d4261a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca5aa34af367365a83a8b6d9d0b2634a38c056d194d45f4fdbca149d7e780547)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f3fdd1a51b3e0a8fd0b8cc8d94c39e138a8ec42b8b97d8782ac64757da55f7d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b321f74afe4ebf34dd289674d268dafdf26e832cf3adc837f0adef3e448bc6e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c743fdb66570550147fcc2554b72320c338c2e47b41cd6b213151407f1d67a05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c70373ae55a49e403771c876742afbdbcff97cc5d8d005b2df5d395a48cf5c0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__948a0e8ad8c77b52950767fd73eceb30dbae5f793b53dffa4ed44643afe17434)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimezone", [value]))

    @jsii.member(jsii_name="resetTime")
    def reset_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTime", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(
        self,
    ) -> "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList":
        return typing.cast("HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "time"))

    @time.setter
    def time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e7952534460f411e219a7a121448630b5cc78b1c353d3ea6ff41ec63f56c488)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a1bf9d754f05cd0967bce31c2714206219de20e15cbd82e816a9cf9c6a93207)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9863e0770e33289771e365e9fa53aa1e6b79c86acd789c261a59c5cedc7688f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f822d6139095b60229d0ba0cfc8c579030074ae769ac780cd1400315df481207)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__408e37ce50467af9fac23f9ef6be40e292642b899237f3c838048ffef8dc4fbe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2da7d3ab9e37b6525eb5eaf7b1b6ef50ff0651bd6e1708a26a918742fc8ac8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35fb8804065bcdebd9f2c084ff56bbba64d22de3c67e2f69b60279b0ee83d612)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfc1dc5ea52384e7acd2288986106209cd6ddf54c381ad17ea6d75d4a8c8b978)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c92bc845a33ff864b39d3d258d3895362e29a0c4e2a0fde14fe26ea40901f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9502f4cc4a36180ed04a612f54efce76b194027694166914a0d068b03c082ef7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f49b9774b1fb99557d5e48fb83ef52fb710738e3236f677cecbadc5ec78ff46)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e896162934ee20e64b76cf8680fd00e1c10f160ea005710af595129482a7d00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdb5eda7678a31997b850287240306037bb72d9441f1e61f25afae31f430ce93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7563249c39314ec9526bbde65a901b4cc3a3e901a3ff274f769f7b13d4add997)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolBackupactivitycontroloptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dbfc3e8fabefd3efd6592eab3a34cd686ea870cde6af1bdcbb2aec4067fb33fe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsActivitycontrolBackupactivitycontroloptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3e8a65417f7cf5ffb716265c20ba36f4e750ccbb91a1a1e4eb3688f3d930ca)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolBackupactivitycontroloptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3118dc2dc6b0ba68de4a570bb832cf519194629695184572c4582b352830f692)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca7170166815757657849e66e5b9d3d3fb00e5e8c3c7eb80f14cbe233c08a4b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0860db6ef2ff776c0084430454f96c031103d62cb48b95cebc4834f6d3eca288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73d2023a48419b3d0ac6f5e3532b88f739d230c2b80d26e12e6f54708dcef167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolBackupactivitycontroloptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolBackupactivitycontroloptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__533eb0e919607c965225fd70c472a09ce815d4394d54b96ca35cbdfdc3054059)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDelaytime")
    def put_delaytime(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c46512f9832ffcde0af4bf9b2914b21eb7b8d09d1f6bb5cd5f1b938460da1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDelaytime", [value]))

    @jsii.member(jsii_name="resetActivitytype")
    def reset_activitytype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivitytype", []))

    @jsii.member(jsii_name="resetDelaytime")
    def reset_delaytime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelaytime", []))

    @jsii.member(jsii_name="resetEnableactivitytype")
    def reset_enableactivitytype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableactivitytype", []))

    @jsii.member(jsii_name="resetEnableafteradelay")
    def reset_enableafteradelay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableafteradelay", []))

    @builtins.property
    @jsii.member(jsii_name="delaytime")
    def delaytime(
        self,
    ) -> HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeList:
        return typing.cast(HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeList, jsii.get(self, "delaytime"))

    @builtins.property
    @jsii.member(jsii_name="activitytypeInput")
    def activitytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activitytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="delaytimeInput")
    def delaytime_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]], jsii.get(self, "delaytimeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableactivitytypeInput")
    def enableactivitytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableactivitytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableafteradelayInput")
    def enableafteradelay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableafteradelayInput"))

    @builtins.property
    @jsii.member(jsii_name="activitytype")
    def activitytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activitytype"))

    @activitytype.setter
    def activitytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d919d5f7639d57a1bd2919ead0445d26894a24271db68f35fab53ac4e1bae3ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableactivitytype")
    def enableactivitytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableactivitytype"))

    @enableactivitytype.setter
    def enableactivitytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b74c1ba5880c8fab9c689c95f62a862f659ec4a87274e06eeb3696c337440d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableactivitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableafteradelay")
    def enableafteradelay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableafteradelay"))

    @enableafteradelay.setter
    def enableafteradelay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31366641ed769f9c823db7c6d7c8bd558363443a5c4451a1a118faa2541e7953)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableafteradelay", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab0e6ca2734e744939d7ae695964881cc1a5e0f8c716c72e21e99ac3cbd0a266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4464171e0824e5c92d55b073dadb35bad06c740a7a189909105e8dd2d1dc0f91)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsActivitycontrolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceb5e1a61d937473d98f21f5d420429b11520710496f2d7af994704cb49f258f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7fb402116471943ad895a001a1e030f2c23892bd7b16f77eee1e230e4df586a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2b5a807bb7f00274f1ff909070988377af9aa276d66b2fa8e211845fa7767ea4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a4827e15f608052cae06c63b16619cf9d97ee6efe5c17f52509f8f3b700c8e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrol]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrol]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrol]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07ba26984839d5226ea70193e89c48c3e6ecd594072abe5bd28cc6e0eb3c85f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5344d31c236d1d10651ab8b36d927c2b4d5a7392eea3d44719b63cae33c94e5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackupactivitycontroloptions")
    def put_backupactivitycontroloptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc0938c728b7271f15d65d7927a067a5f9ac9d0c4e008b51b3de487584dd8b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackupactivitycontroloptions", [value]))

    @jsii.member(jsii_name="putRestoreactivitycontroloptions")
    def put_restoreactivitycontroloptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolRestoreactivitycontroloptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d7f89b928bedaddecb9ddeb2727c3c03194d6a17ba28d45994dd4044bd9cf7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRestoreactivitycontroloptions", [value]))

    @jsii.member(jsii_name="resetBackupactivitycontroloptions")
    def reset_backupactivitycontroloptions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupactivitycontroloptions", []))

    @jsii.member(jsii_name="resetEnablebackup")
    def reset_enablebackup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablebackup", []))

    @jsii.member(jsii_name="resetEnablerestore")
    def reset_enablerestore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablerestore", []))

    @jsii.member(jsii_name="resetRestoreactivitycontroloptions")
    def reset_restoreactivitycontroloptions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestoreactivitycontroloptions", []))

    @builtins.property
    @jsii.member(jsii_name="backupactivitycontroloptions")
    def backupactivitycontroloptions(
        self,
    ) -> HypervisorAwsActivitycontrolBackupactivitycontroloptionsList:
        return typing.cast(HypervisorAwsActivitycontrolBackupactivitycontroloptionsList, jsii.get(self, "backupactivitycontroloptions"))

    @builtins.property
    @jsii.member(jsii_name="restoreactivitycontroloptions")
    def restoreactivitycontroloptions(
        self,
    ) -> "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsList":
        return typing.cast("HypervisorAwsActivitycontrolRestoreactivitycontroloptionsList", jsii.get(self, "restoreactivitycontroloptions"))

    @builtins.property
    @jsii.member(jsii_name="backupactivitycontroloptionsInput")
    def backupactivitycontroloptions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptions]]], jsii.get(self, "backupactivitycontroloptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackupInput")
    def enablebackup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablebackupInput"))

    @builtins.property
    @jsii.member(jsii_name="enablerestoreInput")
    def enablerestore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablerestoreInput"))

    @builtins.property
    @jsii.member(jsii_name="restoreactivitycontroloptionsInput")
    def restoreactivitycontroloptions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptions"]]], jsii.get(self, "restoreactivitycontroloptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackup")
    def enablebackup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablebackup"))

    @enablebackup.setter
    def enablebackup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d04b5b1b3e5945545193b0dcf243ed25895f62bedc9dec7f8464962e831dfed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackup", value)

    @builtins.property
    @jsii.member(jsii_name="enablerestore")
    def enablerestore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablerestore"))

    @enablerestore.setter
    def enablerestore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ad27bbf8515c4df8b1e16fac0caa7edffef2e5d40d2ab52fbf4da7fdc388761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablerestore", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrol]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrol]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrol]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e67efc874459554b24e9d65bb3b08af4db2d560ec431adc01775c412ad4a6cd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptions",
    jsii_struct_bases=[],
    name_mapping={
        "activitytype": "activitytype",
        "delaytime": "delaytime",
        "enableactivitytype": "enableactivitytype",
        "enableafteradelay": "enableafteradelay",
    },
)
class HypervisorAwsActivitycontrolRestoreactivitycontroloptions:
    def __init__(
        self,
        *,
        activitytype: typing.Optional[builtins.str] = None,
        delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enableactivitytype: typing.Optional[builtins.str] = None,
        enableafteradelay: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param activitytype: denotes the activity type being considered [BACKUP, RESTORE, ONLINECI, ARCHIVEPRUNE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitytype HypervisorAws#activitytype}
        :param delaytime: delaytime block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#delaytime HypervisorAws#delaytime}
        :param enableactivitytype: True if the activity type is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableactivitytype HypervisorAws#enableactivitytype}
        :param enableafteradelay: True if the activity will be enabled after a delay time interval. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableafteradelay HypervisorAws#enableafteradelay}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0799ecb6a6cfe4172a9a2ec541a9ff61545cae7f55a88c6ef7c07ea086c0dac)
            check_type(argname="argument activitytype", value=activitytype, expected_type=type_hints["activitytype"])
            check_type(argname="argument delaytime", value=delaytime, expected_type=type_hints["delaytime"])
            check_type(argname="argument enableactivitytype", value=enableactivitytype, expected_type=type_hints["enableactivitytype"])
            check_type(argname="argument enableafteradelay", value=enableafteradelay, expected_type=type_hints["enableafteradelay"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if activitytype is not None:
            self._values["activitytype"] = activitytype
        if delaytime is not None:
            self._values["delaytime"] = delaytime
        if enableactivitytype is not None:
            self._values["enableactivitytype"] = enableactivitytype
        if enableafteradelay is not None:
            self._values["enableafteradelay"] = enableafteradelay

    @builtins.property
    def activitytype(self) -> typing.Optional[builtins.str]:
        '''denotes the activity type being considered [BACKUP, RESTORE, ONLINECI, ARCHIVEPRUNE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitytype HypervisorAws#activitytype}
        '''
        result = self._values.get("activitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delaytime(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime"]]]:
        '''delaytime block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#delaytime HypervisorAws#delaytime}
        '''
        result = self._values.get("delaytime")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime"]]], result)

    @builtins.property
    def enableactivitytype(self) -> typing.Optional[builtins.str]:
        '''True if the activity type is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableactivitytype HypervisorAws#enableactivitytype}
        '''
        result = self._values.get("enableactivitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enableafteradelay(self) -> typing.Optional[builtins.str]:
        '''True if the activity will be enabled after a delay time interval.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableafteradelay HypervisorAws#enableafteradelay}
        '''
        result = self._values.get("enableafteradelay")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrolRestoreactivitycontroloptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime",
    jsii_struct_bases=[],
    name_mapping={"time": "time", "timezone": "timezone", "value": "value"},
)
class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime:
    def __init__(
        self,
        *,
        time: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param time: delay time in unix timestamp. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#time HypervisorAws#time}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#timezone HypervisorAws#timezone}
        :param value: actual delay time value in string format according to the timezone. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#value HypervisorAws#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c75362cc06471b09fc815ef073a4fcff8a37706debae7e6d9079d050db96db60)
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if time is not None:
            self._values["time"] = time
        if timezone is not None:
            self._values["timezone"] = timezone
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def time(self) -> typing.Optional[jsii.Number]:
        '''delay time in unix timestamp.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#time HypervisorAws#time}
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#timezone HypervisorAws#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''actual delay time value in string format according to the timezone.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#value HypervisorAws#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea3aa595e4a9980442021dde0e020e66d44d1bec724dc79308728768fe2685dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b85600ba44083c4f8fdb666648e19493a2c75f74c5731f3c8124dc18010c476)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f140e2795713a77b2e96dff48655fb5c5be4cc8abbe4fd3c7b942444faadcb0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6293da07377afc996f0f3ba88dea10a07e5ed146914ebe6bb9e089cea6411def)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a67f2154097567964ac4b0a69ad3f164b7a2e27f211cddf5e3c5553959e988d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa8752cb485fc83b75d3677cd5dc668c6b422df4ac871cb01ef524ec93b498f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2af6785b720f29330ec7a01338aee23a512ff403c2ea53b3fa8c15a12fc033c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3505fa99518a196658f45e4ed1643755696adc3ecbf3c7072d6c66a6520d78e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimezone", [value]))

    @jsii.member(jsii_name="resetTime")
    def reset_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTime", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(
        self,
    ) -> "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList":
        return typing.cast("HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "time"))

    @time.setter
    def time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076710c23df7731796f0722d2848d6072b35ff9090211c794c7ad575f01d774f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d7f637fe0feb38ec7288b4636fc6fdd23724b10ad211e022be8a115071f2985)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4276c42c6445598003e01169712fb3157541ae813f9ae97e5c2201fe192ab190)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af67addbddee453971f4807577002b3bef94d364af69786965efadbe49b4c465)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6d1342553ac939a3e3f3b49a61d45c87d14d85030a3d08286652c3b6fdd672d6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2246a805437ddce53856755d0af6671b12930ca404b60beda15cead81a5738d2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcf69690fb04f209938ccfd90f8a634549cf09aea8f1d4f09720a90247f1d033)
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
            type_hints = typing.get_type_hints(_typecheckingstub__958056daf7176fef00725b870d7b64f9db5bd9fa29d6e00d0ac864dea140d061)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2cce85ef3dd338e9ac680330106a0a03d856561905b774b5d8fa59d4bf97326)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b8d7609ae527121ff619934cb3799be619c9a2bac1583dddf631b193b14d05f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a4d3efceee23d170d53bc0c92ead4cd4da53621606073526125610d69e20b48)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f55560d092fc6d718fa76306045672d2f11ee360d9da18d298436e0033eb067d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4355585d1600fc5bae9a37880b4973a49319d96befe7f83367937eb8bc20b8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c4dbf6764fe3fd3c9829c1712264e871c501805dcceaa12ea5485456905a210)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__425911ebcaccaacc29c19b7cea494acdf8d0b56999d3dec67ca4a600ef027c11)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fbe77e55ae46d4dbaddbbab232bab8f22dcd56e6bad3ad790951d93b24a3e50)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsActivitycontrolRestoreactivitycontroloptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf885c8496dd93eceab964ebdd11ee05adf15793e86ca4a2560fb04c40231c80)
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
            type_hints = typing.get_type_hints(_typecheckingstub__953d8cd22df82001df66a751936075907755df721af01b779d51342cdb3977b8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4d5f56e26cf3197763433372338731b7be959f1056d79868e61a28ebce4b6a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19237f6fdcf717308baa82bf61d4e8f51725215a3d8894cd87ab4af675c8e934)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsActivitycontrolRestoreactivitycontroloptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsActivitycontrolRestoreactivitycontroloptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7dff02f3aeca7f44d68ec88ba8e2450160e1329eb3ae338eda2db316d5a1c7c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDelaytime")
    def put_delaytime(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d18a6007b7ec55d913fed9a404336abee56652b1d1d326a4a3a4372cd0a85840)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDelaytime", [value]))

    @jsii.member(jsii_name="resetActivitytype")
    def reset_activitytype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivitytype", []))

    @jsii.member(jsii_name="resetDelaytime")
    def reset_delaytime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelaytime", []))

    @jsii.member(jsii_name="resetEnableactivitytype")
    def reset_enableactivitytype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableactivitytype", []))

    @jsii.member(jsii_name="resetEnableafteradelay")
    def reset_enableafteradelay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableafteradelay", []))

    @builtins.property
    @jsii.member(jsii_name="delaytime")
    def delaytime(
        self,
    ) -> HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeList:
        return typing.cast(HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeList, jsii.get(self, "delaytime"))

    @builtins.property
    @jsii.member(jsii_name="activitytypeInput")
    def activitytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activitytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="delaytimeInput")
    def delaytime_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]], jsii.get(self, "delaytimeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableactivitytypeInput")
    def enableactivitytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableactivitytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="enableafteradelayInput")
    def enableafteradelay_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableafteradelayInput"))

    @builtins.property
    @jsii.member(jsii_name="activitytype")
    def activitytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activitytype"))

    @activitytype.setter
    def activitytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb96c9e7440dd20699b986ac89c01ebdd964dcd0982a68d3020243d3b106f1ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableactivitytype")
    def enableactivitytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableactivitytype"))

    @enableactivitytype.setter
    def enableactivitytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d14d4385697612a485e28b613b42afaa71d74b5e6af0a6c0e28412db840dc17e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableactivitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableafteradelay")
    def enableafteradelay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableafteradelay"))

    @enableafteradelay.setter
    def enableafteradelay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f7be644cc9912c9dac6139b0bf2c28d17a1c9f1261f4373af7ee9aba3475710)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableafteradelay", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a537d1ad5da3d0b51c75259d316a38818e62d4b361608222890f3ff84ac93486)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "accesskey": "accesskey",
        "name": "name",
        "secretkey": "secretkey",
        "useiamrole": "useiamrole",
        "accessnodes": "accessnodes",
        "activitycontrol": "activitycontrol",
        "credentials": "credentials",
        "displayname": "displayname",
        "enableawsadminaccount": "enableawsadminaccount",
        "etcdprotection": "etcdprotection",
        "fbrunixmediaagent": "fbrunixmediaagent",
        "hypervisortype": "hypervisortype",
        "id": "id",
        "region": "region",
        "rolearn": "rolearn",
        "security": "security",
        "settings": "settings",
        "skipcredentialvalidation": "skipcredentialvalidation",
        "useserviceaccount": "useserviceaccount",
    },
)
class HypervisorAwsConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        accesskey: builtins.str,
        name: builtins.str,
        secretkey: builtins.str,
        useiamrole: builtins.str,
        accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        displayname: typing.Optional[builtins.str] = None,
        enableawsadminaccount: typing.Optional[builtins.str] = None,
        etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsEtcdprotection", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsFbrunixmediaagent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hypervisortype: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        rolearn: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        skipcredentialvalidation: typing.Optional[builtins.str] = None,
        useserviceaccount: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param accesskey: Access Key of Amazon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#accesskey HypervisorAws#accesskey}
        :param name: The name of the hypervisor group being created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        :param secretkey: secret Key of Amazon login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#secretkey HypervisorAws#secretkey}
        :param useiamrole: if Iam Role is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#useiamrole HypervisorAws#useiamrole}
        :param accessnodes: accessnodes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#accessnodes HypervisorAws#accessnodes}
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitycontrol HypervisorAws#activitycontrol}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#credentials HypervisorAws#credentials}
        :param displayname: The name of the hypervisor that has to be changed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#displayname HypervisorAws#displayname}
        :param enableawsadminaccount: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableawsadminaccount HypervisorAws#enableawsadminaccount}.
        :param etcdprotection: etcdprotection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#etcdprotection HypervisorAws#etcdprotection}
        :param fbrunixmediaagent: fbrunixmediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#fbrunixmediaagent HypervisorAws#fbrunixmediaagent}
        :param hypervisortype: [Amazon]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#hypervisortype HypervisorAws#hypervisortype}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param region: AWS region if Iam role is used. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#region HypervisorAws#region}
        :param rolearn: Role ARN for STS assume role with IAM policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#rolearn HypervisorAws#rolearn}
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#security HypervisorAws#security}
        :param settings: settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#settings HypervisorAws#settings}
        :param skipcredentialvalidation: if credential validation has to be skipped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#skipcredentialvalidation HypervisorAws#skipcredentialvalidation}
        :param useserviceaccount: Clientname to be used as Admin Account. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#useserviceaccount HypervisorAws#useserviceaccount}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__081b4659eb613b7f1353d60b0d1f88e06863de5242a53de6dbb6dd2b9e4b263e)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument accesskey", value=accesskey, expected_type=type_hints["accesskey"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument secretkey", value=secretkey, expected_type=type_hints["secretkey"])
            check_type(argname="argument useiamrole", value=useiamrole, expected_type=type_hints["useiamrole"])
            check_type(argname="argument accessnodes", value=accessnodes, expected_type=type_hints["accessnodes"])
            check_type(argname="argument activitycontrol", value=activitycontrol, expected_type=type_hints["activitycontrol"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument displayname", value=displayname, expected_type=type_hints["displayname"])
            check_type(argname="argument enableawsadminaccount", value=enableawsadminaccount, expected_type=type_hints["enableawsadminaccount"])
            check_type(argname="argument etcdprotection", value=etcdprotection, expected_type=type_hints["etcdprotection"])
            check_type(argname="argument fbrunixmediaagent", value=fbrunixmediaagent, expected_type=type_hints["fbrunixmediaagent"])
            check_type(argname="argument hypervisortype", value=hypervisortype, expected_type=type_hints["hypervisortype"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument rolearn", value=rolearn, expected_type=type_hints["rolearn"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument skipcredentialvalidation", value=skipcredentialvalidation, expected_type=type_hints["skipcredentialvalidation"])
            check_type(argname="argument useserviceaccount", value=useserviceaccount, expected_type=type_hints["useserviceaccount"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accesskey": accesskey,
            "name": name,
            "secretkey": secretkey,
            "useiamrole": useiamrole,
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
        if accessnodes is not None:
            self._values["accessnodes"] = accessnodes
        if activitycontrol is not None:
            self._values["activitycontrol"] = activitycontrol
        if credentials is not None:
            self._values["credentials"] = credentials
        if displayname is not None:
            self._values["displayname"] = displayname
        if enableawsadminaccount is not None:
            self._values["enableawsadminaccount"] = enableawsadminaccount
        if etcdprotection is not None:
            self._values["etcdprotection"] = etcdprotection
        if fbrunixmediaagent is not None:
            self._values["fbrunixmediaagent"] = fbrunixmediaagent
        if hypervisortype is not None:
            self._values["hypervisortype"] = hypervisortype
        if id is not None:
            self._values["id"] = id
        if region is not None:
            self._values["region"] = region
        if rolearn is not None:
            self._values["rolearn"] = rolearn
        if security is not None:
            self._values["security"] = security
        if settings is not None:
            self._values["settings"] = settings
        if skipcredentialvalidation is not None:
            self._values["skipcredentialvalidation"] = skipcredentialvalidation
        if useserviceaccount is not None:
            self._values["useserviceaccount"] = useserviceaccount

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
    def accesskey(self) -> builtins.str:
        '''Access Key of Amazon login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#accesskey HypervisorAws#accesskey}
        '''
        result = self._values.get("accesskey")
        assert result is not None, "Required property 'accesskey' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the hypervisor group being created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secretkey(self) -> builtins.str:
        '''secret Key of Amazon login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#secretkey HypervisorAws#secretkey}
        '''
        result = self._values.get("secretkey")
        assert result is not None, "Required property 'secretkey' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def useiamrole(self) -> builtins.str:
        '''if Iam Role is used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#useiamrole HypervisorAws#useiamrole}
        '''
        result = self._values.get("useiamrole")
        assert result is not None, "Required property 'useiamrole' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accessnodes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsAccessnodes]]]:
        '''accessnodes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#accessnodes HypervisorAws#accessnodes}
        '''
        result = self._values.get("accessnodes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsAccessnodes]]], result)

    @builtins.property
    def activitycontrol(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrol]]]:
        '''activitycontrol block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#activitycontrol HypervisorAws#activitycontrol}
        '''
        result = self._values.get("activitycontrol")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrol]]], result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsCredentials"]]]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#credentials HypervisorAws#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsCredentials"]]], result)

    @builtins.property
    def displayname(self) -> typing.Optional[builtins.str]:
        '''The name of the hypervisor that has to be changed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#displayname HypervisorAws#displayname}
        '''
        result = self._values.get("displayname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enableawsadminaccount(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enableawsadminaccount HypervisorAws#enableawsadminaccount}.'''
        result = self._values.get("enableawsadminaccount")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def etcdprotection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotection"]]]:
        '''etcdprotection block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#etcdprotection HypervisorAws#etcdprotection}
        '''
        result = self._values.get("etcdprotection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotection"]]], result)

    @builtins.property
    def fbrunixmediaagent(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsFbrunixmediaagent"]]]:
        '''fbrunixmediaagent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#fbrunixmediaagent HypervisorAws#fbrunixmediaagent}
        '''
        result = self._values.get("fbrunixmediaagent")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsFbrunixmediaagent"]]], result)

    @builtins.property
    def hypervisortype(self) -> typing.Optional[builtins.str]:
        '''[Amazon].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#hypervisortype HypervisorAws#hypervisortype}
        '''
        result = self._values.get("hypervisortype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''AWS region if Iam role is used.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#region HypervisorAws#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rolearn(self) -> typing.Optional[builtins.str]:
        '''Role ARN for STS assume role with IAM policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#rolearn HypervisorAws#rolearn}
        '''
        result = self._values.get("rolearn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSecurity"]]]:
        '''security block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#security HypervisorAws#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSecurity"]]], result)

    @builtins.property
    def settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettings"]]]:
        '''settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#settings HypervisorAws#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettings"]]], result)

    @builtins.property
    def skipcredentialvalidation(self) -> typing.Optional[builtins.str]:
        '''if credential validation has to be skipped.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#skipcredentialvalidation HypervisorAws#skipcredentialvalidation}
        '''
        result = self._values.get("skipcredentialvalidation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def useserviceaccount(self) -> typing.Optional[builtins.str]:
        '''Clientname to be used as Admin Account.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#useserviceaccount HypervisorAws#useserviceaccount}
        '''
        result = self._values.get("useserviceaccount")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsCredentials",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsCredentials:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19ae90d138fcdd700cae503db07eaedbab9258c3f732a9d33e4fbee80565e05a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsCredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsCredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b4fabdbb5b9ae507c2f07f808a2568a2c889e2635b898691bcbe6809fb59434)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsCredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd000e37795a4ae356a8de84c2e533746cca8c04d31bc78a973ffcbaede0cef)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsCredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faaeff078a587620805a6735bff7fca53d40a4698daaa9ef96ff58732d6ff635)
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
            type_hints = typing.get_type_hints(_typecheckingstub__815cf2d006ad3616ddd6128de1548ac98e5296f4cfca5df91af9761d0cd2764a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0656517beadd7515fd02a5a8b51eca5ba94cc1cf622a79ede5162f82d0842960)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsCredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsCredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsCredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c978d3ca0d7e70b0ea0efc97fda6fd9a800a1219220f7bee10d7ae8b8450d85d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5248c3e6758c0401ab53737fb558968f85eee75bd37ac136d42cfac14183382)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a16a9c85f17ac36d072384161223afee652276f5b53ba5e07280e5d294b7380a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__226ce6321cd8551b47ad5b9e653166499a8da43d83d87b90627be079f15a7386)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsCredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsCredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsCredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3888e590a83458f8304f3ab6228ebf5117e1e31be73bfcf7d9c006163d8f4f3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsEtcdprotection",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "plan": "plan"},
)
class HypervisorAwsEtcdprotection:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsEtcdprotectionPlan", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Denote if etcd protection is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enabled HypervisorAws#enabled}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#plan HypervisorAws#plan}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__672a925a28f66ee511d962ad7287354db60b8f9d9cf6b98f536767549d36a29b)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if plan is not None:
            self._values["plan"] = plan

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.str]:
        '''Denote if etcd protection is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#enabled HypervisorAws#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotectionPlan"]]]:
        '''plan block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#plan HypervisorAws#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotectionPlan"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsEtcdprotection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsEtcdprotectionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsEtcdprotectionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5a87ae464b2655c4d0d7b093edd7425c0dbe08509ae932f27577fbbb48877058)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsEtcdprotectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fee88e00b32d5e9b40c8e75c5fc49e2dee9bc5a2df0808a57e1238accee29f2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsEtcdprotectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19a81fe91bdfc6adb9f5ab9758544eb3530f4ade36165626536cbfb01b56b883)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d63f1ccb1a91d2e16c148ea13dfbbf76df27798ba6eab9644aac7b220f4c01a7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__21ab2225e9597e20784f36e193e2437b1332cf3c178c3fea4bf665dc083dc858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotection]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6299f8b0551ce68af1059e2ae4d0542d1e14ccdd8df5ee1eec31aba17b910258)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsEtcdprotectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsEtcdprotectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__70ee8fe3d9f1244097cf96ce8d312219e634614ab43c7c3ab00b087556b18541)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsEtcdprotectionPlan", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca35ec7a98eb923dc8c8bdc7eecbaf470961eca950082c3820ce968bc2a0c914)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "HypervisorAwsEtcdprotectionPlanList":
        return typing.cast("HypervisorAwsEtcdprotectionPlanList", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotectionPlan"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsEtcdprotectionPlan"]]], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b39733195d698ceb8e3a818254ccc9a7153d56fdb09f3c5068dd70f5cb352282)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotection]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotection]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotection]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea9bd7644652b05c40917468fd41deb29216aeb0a6d72c126268a25eb3a8ad8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsEtcdprotectionPlan",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsEtcdprotectionPlan:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2a458727637ca64dcbf3c03a304ba1524463d6758fabf133bdf3c0ae24560a4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsEtcdprotectionPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsEtcdprotectionPlanList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsEtcdprotectionPlanList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__807d6c57c6459c01379a6dae9fd3a516efdfebec27e22c0856821a6e80c15d65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsEtcdprotectionPlanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd5b425ba91a7e58f5c93959b9fe8da9cc1e8806e467bbfe8ed8cd1b248d533)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsEtcdprotectionPlanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a63898f564a8d6af64b2b3381942a4257c356c7a67b1d246a78d25557d37df2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ba69f6a61c9b256b17c371387b7eee3561b8fc950f1edd6295c9417de80679c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77780835210ed97e947f41686d6b386a89c5e1aa64c869f05875dd4b3605228f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotectionPlan]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotectionPlan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotectionPlan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cc9eff2c55fa480d8894a3d177ea12ced039d60af35b054d996ed023618b762)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsEtcdprotectionPlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsEtcdprotectionPlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c92138477f06224aff23a38e4204380e73e774d8b35f42d52078052847e0c7f8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98d74cdf4d1356eb3fb811205eb0d33cbd790aa031838782f44f28d88fedf16b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81aa9654c9748b80bbe492abeb92ee3857ff6003e04ccddbe1f11cb32cf15012)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotectionPlan]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotectionPlan]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotectionPlan]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a3ebfec4bbfdba14f45c829192fcc2a6d7b6353b1cc2c9d458f633e79e26e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsFbrunixmediaagent",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsFbrunixmediaagent:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ad59b785b6478fa8b7dce13232f770fabe31df892115d959df00ad3b2a40013)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsFbrunixmediaagent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsFbrunixmediaagentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsFbrunixmediaagentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdcc89d22662b816d539548cfd4da21e3b7ffa7085f5b749eff9993f1884d67f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsFbrunixmediaagentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ae237035b11d89143e39b4a0d6559a84c16f20be864f8546b0b74bfe2cf2a4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsFbrunixmediaagentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66840cd367320f74c248413e7e5b08f78e3244b2130ccc807f913b8bbaaa4460)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3601b4906aaf1521174d6a58bc173e705304f8a4903c1b8c0e11b2f3f20467d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4abe8d49abb65685e18de792126c42d414d27ae1e7bb5bbfedffee811a60f6ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsFbrunixmediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsFbrunixmediaagent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsFbrunixmediaagent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b93d8df86b73b83c1fc25bde189ad85346c9331566634e70d45bebf74f4ea64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsFbrunixmediaagentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsFbrunixmediaagentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd0babf6428adcb98ed77cd02d02592574b8cc11b00961d4320463b2e3b0cea3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b04de2ab11dcea9269ae0de0c622dcc55112e3cd627ab199170dfcad45875d4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f308f25ef18afdb161610465ea771f56e9248551f065c9c78ced6629790279c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsFbrunixmediaagent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsFbrunixmediaagent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsFbrunixmediaagent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__232efb2840eeb40938e63ca4b25e52e6cd9466f2d65a0e06b7c431ddc160f1d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSecurity",
    jsii_struct_bases=[],
    name_mapping={
        "associatedusergroups": "associatedusergroups",
        "clientowners": "clientowners",
    },
)
class HypervisorAwsSecurity:
    def __init__(
        self,
        *,
        associatedusergroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSecurityAssociatedusergroups", typing.Dict[builtins.str, typing.Any]]]]] = None,
        clientowners: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param associatedusergroups: associatedusergroups block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#associatedusergroups HypervisorAws#associatedusergroups}
        :param clientowners: Client owners for the Hypervisor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#clientowners HypervisorAws#clientowners}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7487908df2c603da5c4cb544091077424459373ba7d50a168a0a3ae96a6b5f7b)
            check_type(argname="argument associatedusergroups", value=associatedusergroups, expected_type=type_hints["associatedusergroups"])
            check_type(argname="argument clientowners", value=clientowners, expected_type=type_hints["clientowners"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if associatedusergroups is not None:
            self._values["associatedusergroups"] = associatedusergroups
        if clientowners is not None:
            self._values["clientowners"] = clientowners

    @builtins.property
    def associatedusergroups(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSecurityAssociatedusergroups"]]]:
        '''associatedusergroups block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#associatedusergroups HypervisorAws#associatedusergroups}
        '''
        result = self._values.get("associatedusergroups")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSecurityAssociatedusergroups"]]], result)

    @builtins.property
    def clientowners(self) -> typing.Optional[builtins.str]:
        '''Client owners for the Hypervisor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#clientowners HypervisorAws#clientowners}
        '''
        result = self._values.get("clientowners")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSecurityAssociatedusergroups",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class HypervisorAwsSecurityAssociatedusergroups:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75bdc4eeac3b033523526947d940ffdb27a81c0f9538fd1c6921539363e59ad1)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

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
        return "HypervisorAwsSecurityAssociatedusergroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSecurityAssociatedusergroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSecurityAssociatedusergroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47797f8b33e0d454132e14119bb38872bbfc166901931ae36da32ff1df2bd54c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSecurityAssociatedusergroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51081ce3da105f177b11458191d977802a501cbe5532cb14d7869c593daed825)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSecurityAssociatedusergroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb44f6324cc4d660e7922b3b62a7944020882d49251d9ecd126c6ec3b6b10b4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c47877783c704025b56bf71a5b1daa5b1949552d3f8fa5380b5ad14de2c1b46a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db408fbde9c4f588b3f8aa2184cfee71e45c783eb3f1b1158ad5f886af4eb36a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurityAssociatedusergroups]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurityAssociatedusergroups]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurityAssociatedusergroups]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6523ddfae184838f992a5275ed4fd7cc5b6096faa4ffc3470e120dbd6d16a33c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSecurityAssociatedusergroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSecurityAssociatedusergroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b9568f4660c1a4258e170ed583df50545a920a90448b5444bd9fb7ccc185751)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f297b4987d30be5f74f205319bcd1c1919cca9d6448f1385fe1252cb1c4f000)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurityAssociatedusergroups]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurityAssociatedusergroups]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurityAssociatedusergroups]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c14d73100dabcc507e34fddc8ffaa504c708993b8eacaff4b567b7321ac75e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSecurityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSecurityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9cbd366f4b407406b5a53809d7533b7ba6f6bcbe5ef0589bd75397a3bad193c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsSecurityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c975f7fe4fb425030a777e3d327a6a028b6d381245244cc66a2483b7fb74b8f9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSecurityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50597ad14eab04855e06cb5e9fee76111e1312898e8bd50fe2f9f497e4544c51)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51c377bd50feb69666f7636036389c28525303213fe10483c12dcb61b12605ed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__74966f42dcabdffc86b896ced0942b4cffa2d588975f9e34ee48baefe7fe82d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e84b103509d0b1efd6dcd0d2f14b0b225617e51c6b46a4ffca51b2f4749996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSecurityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSecurityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c24eb4cec4fd994492235376f8c288b858d8b91b0edf77bb316cd16d1d841a2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssociatedusergroups")
    def put_associatedusergroups(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSecurityAssociatedusergroups, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef4804953ab10cf50a6f84db68d4b256d9507181a90fb8211e62a17367446155)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssociatedusergroups", [value]))

    @jsii.member(jsii_name="resetAssociatedusergroups")
    def reset_associatedusergroups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatedusergroups", []))

    @jsii.member(jsii_name="resetClientowners")
    def reset_clientowners(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientowners", []))

    @builtins.property
    @jsii.member(jsii_name="associatedusergroups")
    def associatedusergroups(self) -> HypervisorAwsSecurityAssociatedusergroupsList:
        return typing.cast(HypervisorAwsSecurityAssociatedusergroupsList, jsii.get(self, "associatedusergroups"))

    @builtins.property
    @jsii.member(jsii_name="associatedusergroupsInput")
    def associatedusergroups_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurityAssociatedusergroups]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurityAssociatedusergroups]]], jsii.get(self, "associatedusergroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientownersInput")
    def clientowners_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientownersInput"))

    @builtins.property
    @jsii.member(jsii_name="clientowners")
    def clientowners(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientowners"))

    @clientowners.setter
    def clientowners(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b44c65d927c4cc2cd15f8cb7d3d3610ac293abcb3209d8f9cb949cad6a2c9c74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientowners", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29bfe3253887a025205a82998903a19c447e3cf85596bd4744cc964ca7aa4139)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettings",
    jsii_struct_bases=[],
    name_mapping={
        "applicationcredentials": "applicationcredentials",
        "customattributes": "customattributes",
        "guestcredentials": "guestcredentials",
        "metricsmonitoringpolicy": "metricsmonitoringpolicy",
        "mountaccessnode": "mountaccessnode",
        "regioninfo": "regioninfo",
        "timezone": "timezone",
    },
)
class HypervisorAwsSettings:
    def __init__(
        self,
        *,
        applicationcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsApplicationcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        customattributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsCustomattributes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        guestcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsGuestcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        metricsmonitoringpolicy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsMetricsmonitoringpolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mountaccessnode: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsMountaccessnode", typing.Dict[builtins.str, typing.Any]]]]] = None,
        regioninfo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsRegioninfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param applicationcredentials: applicationcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#applicationcredentials HypervisorAws#applicationcredentials}
        :param customattributes: customattributes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#customattributes HypervisorAws#customattributes}
        :param guestcredentials: guestcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#guestcredentials HypervisorAws#guestcredentials}
        :param metricsmonitoringpolicy: metricsmonitoringpolicy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#metricsmonitoringpolicy HypervisorAws#metricsmonitoringpolicy}
        :param mountaccessnode: mountaccessnode block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#mountaccessnode HypervisorAws#mountaccessnode}
        :param regioninfo: regioninfo block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#regioninfo HypervisorAws#regioninfo}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#timezone HypervisorAws#timezone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97e5a0fa6313743114cd8dc77deed7fb015326c13a014804c9f665c847a67dc7)
            check_type(argname="argument applicationcredentials", value=applicationcredentials, expected_type=type_hints["applicationcredentials"])
            check_type(argname="argument customattributes", value=customattributes, expected_type=type_hints["customattributes"])
            check_type(argname="argument guestcredentials", value=guestcredentials, expected_type=type_hints["guestcredentials"])
            check_type(argname="argument metricsmonitoringpolicy", value=metricsmonitoringpolicy, expected_type=type_hints["metricsmonitoringpolicy"])
            check_type(argname="argument mountaccessnode", value=mountaccessnode, expected_type=type_hints["mountaccessnode"])
            check_type(argname="argument regioninfo", value=regioninfo, expected_type=type_hints["regioninfo"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if applicationcredentials is not None:
            self._values["applicationcredentials"] = applicationcredentials
        if customattributes is not None:
            self._values["customattributes"] = customattributes
        if guestcredentials is not None:
            self._values["guestcredentials"] = guestcredentials
        if metricsmonitoringpolicy is not None:
            self._values["metricsmonitoringpolicy"] = metricsmonitoringpolicy
        if mountaccessnode is not None:
            self._values["mountaccessnode"] = mountaccessnode
        if regioninfo is not None:
            self._values["regioninfo"] = regioninfo
        if timezone is not None:
            self._values["timezone"] = timezone

    @builtins.property
    def applicationcredentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsApplicationcredentials"]]]:
        '''applicationcredentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#applicationcredentials HypervisorAws#applicationcredentials}
        '''
        result = self._values.get("applicationcredentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsApplicationcredentials"]]], result)

    @builtins.property
    def customattributes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsCustomattributes"]]]:
        '''customattributes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#customattributes HypervisorAws#customattributes}
        '''
        result = self._values.get("customattributes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsCustomattributes"]]], result)

    @builtins.property
    def guestcredentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsGuestcredentials"]]]:
        '''guestcredentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#guestcredentials HypervisorAws#guestcredentials}
        '''
        result = self._values.get("guestcredentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsGuestcredentials"]]], result)

    @builtins.property
    def metricsmonitoringpolicy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsMetricsmonitoringpolicy"]]]:
        '''metricsmonitoringpolicy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#metricsmonitoringpolicy HypervisorAws#metricsmonitoringpolicy}
        '''
        result = self._values.get("metricsmonitoringpolicy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsMetricsmonitoringpolicy"]]], result)

    @builtins.property
    def mountaccessnode(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsMountaccessnode"]]]:
        '''mountaccessnode block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#mountaccessnode HypervisorAws#mountaccessnode}
        '''
        result = self._values.get("mountaccessnode")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsMountaccessnode"]]], result)

    @builtins.property
    def regioninfo(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsRegioninfo"]]]:
        '''regioninfo block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#regioninfo HypervisorAws#regioninfo}
        '''
        result = self._values.get("regioninfo")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsRegioninfo"]]], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#timezone HypervisorAws#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsTimezone"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsApplicationcredentials",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "password": "password"},
)
class HypervisorAwsSettingsApplicationcredentials:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: username to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        :param password: password to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#password HypervisorAws#password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f92db4263752afe24a9be631c2bd09beeeca96c825683dcf473b28d6867211e)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''password to access the network path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#password HypervisorAws#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsApplicationcredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsApplicationcredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsApplicationcredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__acc5594c1ad73217d28b2b80e4862948766d72a50ee611632910f3e2e07efe6e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSettingsApplicationcredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__832b37a3cd73d0e772e9590bca764184467e226ed3c4a5d056086e8708166316)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsApplicationcredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb2e1aeee73ebc35c043316b7fb7d1e41d36181bababc93d9988e881350ba101)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6596e32119ac00bacf9c9682b13af69cef9925d04881975bc51262c9e1ccc89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__25951e96f8c78ed101eb2885b6b4194de14f2e2987aee0c9264c7bf39ca29b6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsApplicationcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsApplicationcredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsApplicationcredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d105909b6cbd3a67f5ee57188d5e20421379cb45a82b2f5919d47549eb74da9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsApplicationcredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsApplicationcredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c563bcec0f3a11059c9dc9d7a6b8bd2253610f5a3aeba508f2b052aa4b7af21)
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
            type_hints = typing.get_type_hints(_typecheckingstub__58379613416827f2e2578b7f2975f0b76fb2f3f6f7b2149d419003644bf6edba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a0845199ed3dea4d9f13bc254e73208f36e5c1adf333659561d6d01967a1775)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsApplicationcredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsApplicationcredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsApplicationcredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75172f05794b41abbddb38bbec25cbc2d48836e76130f2e5ae9315b32439ea94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsCustomattributes",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class HypervisorAwsSettingsCustomattributes:
    def __init__(
        self,
        *,
        type: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: client custom attribute type . Ex- 3 - For client 8- For clientGroup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#type HypervisorAws#type}
        :param value: client/Client Group custom attribute value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#value HypervisorAws#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e0fe5d8a8a948e2640488e3e51b61a6d9c47b5cc70eed7678643c38805383b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> typing.Optional[jsii.Number]:
        '''client custom attribute type . Ex- 3 - For client 8- For clientGroup.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#type HypervisorAws#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''client/Client Group custom attribute value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#value HypervisorAws#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsCustomattributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsCustomattributesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsCustomattributesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6442235783ea0a38adc8ba5a1932f24adfa0e5fa5489c1bb69e1d1d02dd40883)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSettingsCustomattributesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e775b1e0827768a5798351bbf4a06c0a8cbccff2cf0ba497e406113f7a73c90e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsCustomattributesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__170dee4c457d98460a8ab7d2aa661ee9f97fbd9b35c3428c7814bba08908385b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b3cde6206b8d53de00f59642410c239d2e596710fa75f3363e3c512a44426af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c637bdaaff68ff91a576bafdeac1b7d56346556bfe2a75caf5e4dd5d5079a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsCustomattributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsCustomattributes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsCustomattributes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__465ca62bba0c3b72f5a6c1ea8b90efadf77fb929b62774cd8458fc1e3e546e13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsCustomattributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsCustomattributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__189470d44236384d7514ecd86c8713d65ce3aeb49b7252255b50dcb2bda31ecf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "type"))

    @type.setter
    def type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c38b7b43ff75a72550bc509d80e6464cfc43d4ffccad5522adec2fda01eaae08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a259783e81b5547fbc367f2d001a1ab424718132040940a258b54f36cbb6f58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsCustomattributes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsCustomattributes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsCustomattributes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f27293138fd0e6f9222576098b68be5df5e14dcdde4bcdaa70aa366f08a2479)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsGuestcredentials",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "password": "password"},
)
class HypervisorAwsSettingsGuestcredentials:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: username to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        :param password: password to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#password HypervisorAws#password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce17bbea13486e0e85bdcbd79e4f94ac7ca3b7887efcdbd41211314bb0842a64)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''password to access the network path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#password HypervisorAws#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsGuestcredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsGuestcredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsGuestcredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7e5497c702d050524907f8147906b8c3904cc61b2295576e261b617a25853f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSettingsGuestcredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fff08b4dde713945ba077243b3d9d0ac654fb123c2607ea8e06e1cfba438161)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsGuestcredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__797c7251e457252e7328a844b751131b17743fb3decfccd78f0c96f767090394)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c9bf0c1db7d4bc472a50a3df9a180a966fff62d2a9681601f871183a1ca4712e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9c373cb74733388824685aca6ba3958086a648501dc8c1ba10ba05f31efdb1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsGuestcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsGuestcredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsGuestcredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9af304df67d83c170cd7dd5f5dcc8170e69e4313da78c92bd30d0b17486ea3b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsGuestcredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsGuestcredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecf0320638e0de928f12c2bcd35cdd6d60fa773c40efd37cdb5e6cfb565cf306)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f42f9200b7ba371395b4fc9d03cb824e371d82ba74dcca3ea173481d26d83e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d09ef5b2789c7e5edada93a1ff29e8358d39af909e6055b458a5a24efb2bdca7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsGuestcredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsGuestcredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsGuestcredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18d95b04b2412fd72b2964b6fd5e3d864a70b94f52617322b5dcfc56e1b5fb1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca0a31254c831155371ceafbeb2193ebb397f00d64940587f884cca1f3e4a898)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324632bb35e1a63cabacc4fb8c1ec26bfb395cd98a7f8de567023aa4d529f2e9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38ac831943df971f49742fc97207cd6b3ce072a9c80d2f4cded6077e142b9429)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22a3940cabb8d656bc1710e9cf6bb113adc9ee2db84a344fac2c8272b4141a7a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5c0f4a8c5be33960ffb40c83d3075122940b1cc331ba2d38686da8c25937ff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79043034267bc9d6ab0d58d9e2ab0c397e5048b4c9fa4fe932d170e3d67b9055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsMetricsmonitoringpolicy",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "isenabled": "isenabled", "name": "name"},
)
class HypervisorAwsSettingsMetricsmonitoringpolicy:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        isenabled: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Metrics Moitoring PolicyId. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param isenabled: True if Metrics Monioring policy is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#isenabled HypervisorAws#isenabled}
        :param name: Metrics Moitoring Policy Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29571947d5384725475de1fb5c6d5f871aaf1afdf4b37386dbc726ad496757c4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument isenabled", value=isenabled, expected_type=type_hints["isenabled"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if isenabled is not None:
            self._values["isenabled"] = isenabled
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Metrics Moitoring PolicyId.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def isenabled(self) -> typing.Optional[builtins.str]:
        '''True if Metrics Monioring policy is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#isenabled HypervisorAws#isenabled}
        '''
        result = self._values.get("isenabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Metrics Moitoring Policy Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsMetricsmonitoringpolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsMetricsmonitoringpolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsMetricsmonitoringpolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cab026d7e29d764e9745effdc655fecb46af25c77e7d0cfafe6765a31a8e81e7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSettingsMetricsmonitoringpolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8ce3bd128a6d213b3b1c7fef677d0262d5484902d44eb5a2f585c4e448d18a3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsMetricsmonitoringpolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c62ba7befcda53c647647af8a2369a435b0b9672353745b477dadd7b4f267785)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51f775401e193b9ed4883b2f4bec43f69b09247a0e9a8895f7f994d5d1162000)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c1d87496e00c482c09d55748d46cf9157be479f91961537fd6df790ff642ee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMetricsmonitoringpolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMetricsmonitoringpolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMetricsmonitoringpolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12d48929b0e9e56f1490c1f3747f5a9d70b79bea1e43a9429a3286ed66eff526)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsMetricsmonitoringpolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsMetricsmonitoringpolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__30f05f4f6c6a08a3f8e235cc9c4755333e55b1be4e6d525ff8d6ccfb15902bc9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsenabled")
    def reset_isenabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsenabled", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isenabledInput")
    def isenabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "isenabledInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__d3f3eabd4154e011c5fd2dbea045f75d4b2eb6ce633dea93348e1706db8fcb3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isenabled")
    def isenabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isenabled"))

    @isenabled.setter
    def isenabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27d0ab1e4e4a8269998fc78ff2309e8f523c80619f015a3c94188dee6ebb06dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isenabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3abf7eda16b5c58b681eaca7b2752de6ede652ecea22822285e8b758a1580f64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMetricsmonitoringpolicy]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMetricsmonitoringpolicy]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMetricsmonitoringpolicy]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30152551cae51f6e7072a0b40046df8996dd3cc8bcc343d78e1ed9d1a386123a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsMountaccessnode",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsSettingsMountaccessnode:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebb16ef810715dc6bc4305b2f5ecbbffc29b1afe833ac62a6881e34b9c858dac)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsMountaccessnode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsMountaccessnodeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsMountaccessnodeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b322a89ac2f10355f075ea300fdfc31ed04dd0bbffd3abe1a6b198603eaf860)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSettingsMountaccessnodeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55a17ff37f95c336f8523378a7d2f2920f22af4f863ea73058e63ed21174deae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsMountaccessnodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__508cea020d9c15fa48c0b08c7ed22b789e75d0354f581e8714721e305cf7a42a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bf741a6e0782100e5edbd0b54b9fa63252c23cf11db803e4f1a256f52967890)
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
            type_hints = typing.get_type_hints(_typecheckingstub__49871d006f41e1167768c10abee5d4d6ceab9599b601a8289aa97267c3ba6d99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMountaccessnode]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMountaccessnode]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMountaccessnode]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527c6a328fa9f2deee10a3e617a782e7bba202a30aad91f29f2d27c6947cda76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsMountaccessnodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsMountaccessnodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3df621357f0d25e0770e4c616599c582f89be6c470c3c9ddc084ee680e563c18)
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
            type_hints = typing.get_type_hints(_typecheckingstub__86257a7f4f98cb1a8e63e1214ffcf3103da504c11844366757c96f6fc82d4e8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dad4cf5e36f06a5283e44c95e157df71ad5f823024a6732798094a20339ff09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMountaccessnode]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMountaccessnode]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMountaccessnode]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b071bfb3dc70ff907a701585abeb3eb9110927711845f8f0530f7cde84ceca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__16415fee61db3c237f0b0d78154403ae355773e46bd362e191193d976f303e2e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putApplicationcredentials")
    def put_applicationcredentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsApplicationcredentials, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a176a043c36b225a69923e5d3641746c72e405bcb4c27ed01a73e6f710b0e051)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplicationcredentials", [value]))

    @jsii.member(jsii_name="putCustomattributes")
    def put_customattributes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsCustomattributes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1331726471ff12ce0a07c1008291896f0caf64f90bce8a2af055208d0b9e4f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomattributes", [value]))

    @jsii.member(jsii_name="putGuestcredentials")
    def put_guestcredentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsGuestcredentials, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86afd046218892c25129696a69654975dc73561fb75ec59e644e1d1feed75c38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestcredentials", [value]))

    @jsii.member(jsii_name="putMetricsmonitoringpolicy")
    def put_metricsmonitoringpolicy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsMetricsmonitoringpolicy, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3db4e0e251a4f41bf85dc7da4a03757fafb46220925d11bad747f3ded7f758a5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricsmonitoringpolicy", [value]))

    @jsii.member(jsii_name="putMountaccessnode")
    def put_mountaccessnode(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsMountaccessnode, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0ba6065b1528442dc014e79d2b6fd19abc1610480ed186564fd205d5a538043)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMountaccessnode", [value]))

    @jsii.member(jsii_name="putRegioninfo")
    def put_regioninfo(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsRegioninfo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b0779de617d425c0aebe13cdc13c62575b11ec59b38dabef6e5b93189efb1ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegioninfo", [value]))

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAwsSettingsTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92321d74e021c49da1564401898291433036b06d1e3387a76df41cd93976efdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimezone", [value]))

    @jsii.member(jsii_name="resetApplicationcredentials")
    def reset_applicationcredentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationcredentials", []))

    @jsii.member(jsii_name="resetCustomattributes")
    def reset_customattributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomattributes", []))

    @jsii.member(jsii_name="resetGuestcredentials")
    def reset_guestcredentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGuestcredentials", []))

    @jsii.member(jsii_name="resetMetricsmonitoringpolicy")
    def reset_metricsmonitoringpolicy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsmonitoringpolicy", []))

    @jsii.member(jsii_name="resetMountaccessnode")
    def reset_mountaccessnode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountaccessnode", []))

    @jsii.member(jsii_name="resetRegioninfo")
    def reset_regioninfo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegioninfo", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @builtins.property
    @jsii.member(jsii_name="applicationcredentials")
    def applicationcredentials(self) -> HypervisorAwsSettingsApplicationcredentialsList:
        return typing.cast(HypervisorAwsSettingsApplicationcredentialsList, jsii.get(self, "applicationcredentials"))

    @builtins.property
    @jsii.member(jsii_name="customattributes")
    def customattributes(self) -> HypervisorAwsSettingsCustomattributesList:
        return typing.cast(HypervisorAwsSettingsCustomattributesList, jsii.get(self, "customattributes"))

    @builtins.property
    @jsii.member(jsii_name="guestcredentials")
    def guestcredentials(self) -> HypervisorAwsSettingsGuestcredentialsList:
        return typing.cast(HypervisorAwsSettingsGuestcredentialsList, jsii.get(self, "guestcredentials"))

    @builtins.property
    @jsii.member(jsii_name="metricsmonitoringpolicy")
    def metricsmonitoringpolicy(
        self,
    ) -> HypervisorAwsSettingsMetricsmonitoringpolicyList:
        return typing.cast(HypervisorAwsSettingsMetricsmonitoringpolicyList, jsii.get(self, "metricsmonitoringpolicy"))

    @builtins.property
    @jsii.member(jsii_name="mountaccessnode")
    def mountaccessnode(self) -> HypervisorAwsSettingsMountaccessnodeList:
        return typing.cast(HypervisorAwsSettingsMountaccessnodeList, jsii.get(self, "mountaccessnode"))

    @builtins.property
    @jsii.member(jsii_name="regioninfo")
    def regioninfo(self) -> "HypervisorAwsSettingsRegioninfoList":
        return typing.cast("HypervisorAwsSettingsRegioninfoList", jsii.get(self, "regioninfo"))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> "HypervisorAwsSettingsTimezoneList":
        return typing.cast("HypervisorAwsSettingsTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="applicationcredentialsInput")
    def applicationcredentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsApplicationcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsApplicationcredentials]]], jsii.get(self, "applicationcredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="customattributesInput")
    def customattributes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsCustomattributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsCustomattributes]]], jsii.get(self, "customattributesInput"))

    @builtins.property
    @jsii.member(jsii_name="guestcredentialsInput")
    def guestcredentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsGuestcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsGuestcredentials]]], jsii.get(self, "guestcredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsmonitoringpolicyInput")
    def metricsmonitoringpolicy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMetricsmonitoringpolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMetricsmonitoringpolicy]]], jsii.get(self, "metricsmonitoringpolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="mountaccessnodeInput")
    def mountaccessnode_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMountaccessnode]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMountaccessnode]]], jsii.get(self, "mountaccessnodeInput"))

    @builtins.property
    @jsii.member(jsii_name="regioninfoInput")
    def regioninfo_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsRegioninfo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsRegioninfo"]]], jsii.get(self, "regioninfoInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAwsSettingsTimezone"]]], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68dd5b0eb62055ad0097282103faa38193f47cc249b1ea40c67ac2688f256a62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsRegioninfo",
    jsii_struct_bases=[],
    name_mapping={
        "displayname": "displayname",
        "id": "id",
        "latitude": "latitude",
        "longitude": "longitude",
        "name": "name",
    },
)
class HypervisorAwsSettingsRegioninfo:
    def __init__(
        self,
        *,
        displayname: typing.Optional[builtins.str] = None,
        id: typing.Optional[jsii.Number] = None,
        latitude: typing.Optional[builtins.str] = None,
        longitude: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param displayname: Display Name of Region. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#displayname HypervisorAws#displayname}
        :param id: Region Id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latitude: Geolocation Latitude. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#latitude HypervisorAws#latitude}
        :param longitude: Geolocation Longitude. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#longitude HypervisorAws#longitude}
        :param name: Region Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d25c62fef570a7963e2eb641d04d3ef215cdd336cf0c6231b3e121abd09d94ab)
            check_type(argname="argument displayname", value=displayname, expected_type=type_hints["displayname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
            check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if displayname is not None:
            self._values["displayname"] = displayname
        if id is not None:
            self._values["id"] = id
        if latitude is not None:
            self._values["latitude"] = latitude
        if longitude is not None:
            self._values["longitude"] = longitude
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def displayname(self) -> typing.Optional[builtins.str]:
        '''Display Name of Region.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#displayname HypervisorAws#displayname}
        '''
        result = self._values.get("displayname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Region Id.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def latitude(self) -> typing.Optional[builtins.str]:
        '''Geolocation Latitude.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#latitude HypervisorAws#latitude}
        '''
        result = self._values.get("latitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def longitude(self) -> typing.Optional[builtins.str]:
        '''Geolocation Longitude.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#longitude HypervisorAws#longitude}
        '''
        result = self._values.get("longitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Region Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsRegioninfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsRegioninfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsRegioninfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e7b5ea30f7b92dd26b655e706dfa342b086a16da4bfb2489c5cc5bfcdcd254c7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAwsSettingsRegioninfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c02c5c4f518820275173e8126b14274238c746bc8e53a3aef8d694308e45da1a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsRegioninfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a0ca27c57e536fc7cfa402c691ed257fb70a2080ff400bade4972e78180c3c1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4c80ca201226ca74ffc5a1b41c8ef1b7cb1dfd1b5c3ecf4076790f06c692f19)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bbe6a62bd16d82218177789bc834ab6ad29545cd4d5b32c1385034146e1b355)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsRegioninfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsRegioninfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsRegioninfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de276a6320cf37374e7810d248184f6cf6f8d66559740a6c32f17b625ed8f855)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsRegioninfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsRegioninfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ab659f08fc3e53d16db171f94bbeb3efd404416a085541570d4061aebdeaa0b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisplayname")
    def reset_displayname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayname", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLatitude")
    def reset_latitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatitude", []))

    @jsii.member(jsii_name="resetLongitude")
    def reset_longitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongitude", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="displaynameInput")
    def displayname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displaynameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="latitudeInput")
    def latitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="longitudeInput")
    def longitude_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "longitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="displayname")
    def displayname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayname"))

    @displayname.setter
    def displayname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47697df467da4f1339b5dd2b058b8e9d38e6d56a106a85dbd8341977051814d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9547b348c6ac56fe2249f5a14c8a83f8b69a073929b510bb14b27c4e0cf5180f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee416eef6b95d1308feea08c3f12d5943f253fde398c5be9abc96f0206481a39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad59252318f2b311026d1ea7994091afebd5ca896a674585c15a7754d0fea224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45cc6a9bca74a91e432076331217974e1d3b841b85ff159a23d0b26b6970b0cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsRegioninfo]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsRegioninfo]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsRegioninfo]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__319711b15a9dadf694a483589b3cf96e0d22a58ca85b8d73d1761ad9b3d4f82f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAwsSettingsTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72b47232caf2e1f5b8870d5894d8b5d71adf2d02989716c58548a36dfede9e19)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#id HypervisorAws#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_aws#name HypervisorAws#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAwsSettingsTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAwsSettingsTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bcf9438278d960fc401b4e45d4239d734c7b463a781372120a11abb5c477c4a9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAwsSettingsTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c47c3ce6deef55949d50011e129c2830b48fa1d07175892151f34cea6e6bae4)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAwsSettingsTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07e27b26cc65378035969febfcb9b01cf3577e4c77a8df117b27dffdb3736824)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f897fe828147ee5a0c242082b2b89a073b6fe8c9549f9995ca413aeb703076e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a847e3001add5b7f86948ecfdd6d0a21c6421f72f83c06865f793ef933906bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5ac75c44d3a80c44041c0c4e9338233b3e555f77d13cf112d5ce3718aeaddb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAwsSettingsTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAws.HypervisorAwsSettingsTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a548f0d57e767a503ac5d50424f95e3dc41c47d4115c7073f7042b00a6f4fd52)
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
            type_hints = typing.get_type_hints(_typecheckingstub__956964059d7428aaee362c791dba115a851dcaa5271ea183d782fb10209ba274)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f8ff3c15c50b9bf740a6e82ea4b84a877c5102ad62d09dde4e5572a3a3d3609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a80c8cafa7292263ab7e460fa252ee91b5ee129a13e5d2ba609abb72613b406)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HypervisorAws",
    "HypervisorAwsAccessnodes",
    "HypervisorAwsAccessnodesList",
    "HypervisorAwsAccessnodesOutputReference",
    "HypervisorAwsActivitycontrol",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptions",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeList",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsList",
    "HypervisorAwsActivitycontrolBackupactivitycontroloptionsOutputReference",
    "HypervisorAwsActivitycontrolList",
    "HypervisorAwsActivitycontrolOutputReference",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptions",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeList",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsList",
    "HypervisorAwsActivitycontrolRestoreactivitycontroloptionsOutputReference",
    "HypervisorAwsConfig",
    "HypervisorAwsCredentials",
    "HypervisorAwsCredentialsList",
    "HypervisorAwsCredentialsOutputReference",
    "HypervisorAwsEtcdprotection",
    "HypervisorAwsEtcdprotectionList",
    "HypervisorAwsEtcdprotectionOutputReference",
    "HypervisorAwsEtcdprotectionPlan",
    "HypervisorAwsEtcdprotectionPlanList",
    "HypervisorAwsEtcdprotectionPlanOutputReference",
    "HypervisorAwsFbrunixmediaagent",
    "HypervisorAwsFbrunixmediaagentList",
    "HypervisorAwsFbrunixmediaagentOutputReference",
    "HypervisorAwsSecurity",
    "HypervisorAwsSecurityAssociatedusergroups",
    "HypervisorAwsSecurityAssociatedusergroupsList",
    "HypervisorAwsSecurityAssociatedusergroupsOutputReference",
    "HypervisorAwsSecurityList",
    "HypervisorAwsSecurityOutputReference",
    "HypervisorAwsSettings",
    "HypervisorAwsSettingsApplicationcredentials",
    "HypervisorAwsSettingsApplicationcredentialsList",
    "HypervisorAwsSettingsApplicationcredentialsOutputReference",
    "HypervisorAwsSettingsCustomattributes",
    "HypervisorAwsSettingsCustomattributesList",
    "HypervisorAwsSettingsCustomattributesOutputReference",
    "HypervisorAwsSettingsGuestcredentials",
    "HypervisorAwsSettingsGuestcredentialsList",
    "HypervisorAwsSettingsGuestcredentialsOutputReference",
    "HypervisorAwsSettingsList",
    "HypervisorAwsSettingsMetricsmonitoringpolicy",
    "HypervisorAwsSettingsMetricsmonitoringpolicyList",
    "HypervisorAwsSettingsMetricsmonitoringpolicyOutputReference",
    "HypervisorAwsSettingsMountaccessnode",
    "HypervisorAwsSettingsMountaccessnodeList",
    "HypervisorAwsSettingsMountaccessnodeOutputReference",
    "HypervisorAwsSettingsOutputReference",
    "HypervisorAwsSettingsRegioninfo",
    "HypervisorAwsSettingsRegioninfoList",
    "HypervisorAwsSettingsRegioninfoOutputReference",
    "HypervisorAwsSettingsTimezone",
    "HypervisorAwsSettingsTimezoneList",
    "HypervisorAwsSettingsTimezoneOutputReference",
]

publication.publish()

def _typecheckingstub__ba79429b3d746a73e900e838121cc94859c11d3f5a16c5c6a38943daf397c5e7(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    accesskey: builtins.str,
    name: builtins.str,
    secretkey: builtins.str,
    useiamrole: builtins.str,
    accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    displayname: typing.Optional[builtins.str] = None,
    enableawsadminaccount: typing.Optional[builtins.str] = None,
    etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsEtcdprotection, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsFbrunixmediaagent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hypervisortype: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    rolearn: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skipcredentialvalidation: typing.Optional[builtins.str] = None,
    useserviceaccount: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__c758abb84ce1437a1c73cb953494923a0d0f5b62931563323ab40d87c8eb01ba(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94cc290b2dcd2ed97d32379b0182297e09b39a730c698016261a674a51ad4df(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsAccessnodes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10896250b8e61f82709e8f4c65c893fb9009c4b778ad10283c082dd6c9f3c5d2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrol, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8a384a3df0912f761daab3abe44b60e3d51a1be2365e2fa7d771030a48cb0ea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsCredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b1f84f9b20090b06c893c3a9fb5ca285c999e3c10b817183e203340fdb415e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsEtcdprotection, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6f7b4bc62835758b3ea2e7c2e5477414fa0f0275619fd3772948211d2bb3303(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsFbrunixmediaagent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__735c5df166bb0de23c8df5ac794f04b5360c6173ec4e9aeb344d886f42859183(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSecurity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ac675e97bc93af92b64234d1d35fcfe502fe1e8c79b09ecd00edbf6f4cb0fc5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25072377c15de32f3234405760a62e2f08c18f82bbeea933ed924354cfe3180b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59e515f9279e25e87ac65ed94cb51658ba9320b1ab478d2c42d35d8846caa3a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f05236d2e1e2b9c47414f8764631838bf66591fdafc2b93f9665204d575d4a8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d3df5832328a8a5007d9ce1fcbe8697011bfe0562bfb0af322a56022a6b281b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b678faa439124f15a15387905cb3aaa0ca9bd81601b921331a2a9e3cbc696578(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__208f6b343d3b611cc91b0e9d674c624efe9cd4802caaa671d52384bc2b7adc5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51f75abeef1e463cc5a19c91aa36ae7f43201fb0778b52f8aa62d4d9a2ef1a27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc3158f246dfb83eec5d47d0b1e23f4ac4eb05fd927e30d272e97b5066cfc2b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c720080dc876a1114d867d0ba7735ae9dd4263a0a0514334be1003f52db1d74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f475c30388889a39ada8aba1cf061b143b3eda8d4e84c368fb6c46c8da2e20f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634e3ebedb4712694d456e31f9f7c7901bd69341eae5833200430b18586d5f98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ccadb608377f0004f7be32d37790150894666f3fbc0b527250c1b8a1ea40954(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11f173b15cbc2e649546bb82cdde05a1d0eebdd7781f48252a6893efaf53bf6(
    *,
    id: typing.Optional[jsii.Number] = None,
    type: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f13f07f595615574cc49d743e6a81a954974ed465c5e856e7000eac0f8848f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c43aeab2083909ab908a60a63036213342c62be3c4dd6285bc50235bbd81b1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b022b478299c5d4de664592bade71f7a7bfb4a2e64dd238ddee67f4f9a90db0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c4578cfd893a6667f53f4efe95bed1756668f109dc093896d7b232450056cbc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cafdcf2120261ee51419d6d42e743da9d55af4ffea6254c9f460c713bc8e990e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__379818b1367d886e114d9c19064040596e1b8575fe9c9b4d6fec7f872d9f222b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsAccessnodes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d491cd13c4b77ec0d94b096ee11ccca5e8fb96216d1347e684fb1c339f4bac4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2878aec4c871630ba0c5316bfa5458d105797a7114ed74e00be7a5d51ad47cf0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4dc28efe705df0afef7d6647ba323849bc91d58a8ddd3350bc6530548e4a9fd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58bd37333b150917419629434cd2cc1f7161de64519608ce4e9f0c36aa54d23a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsAccessnodes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd46c9e116e2fc30c4baaf977fb664e62c5399c15513a8cfabefc0e6473a3ecb(
    *,
    backupactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enablebackup: typing.Optional[builtins.str] = None,
    enablerestore: typing.Optional[builtins.str] = None,
    restoreactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d161e716ef20fc45c0e8f236f61e2ee6b94e534901916db79a88ae0a31c6f4d6(
    *,
    activitytype: typing.Optional[builtins.str] = None,
    delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enableactivitytype: typing.Optional[builtins.str] = None,
    enableafteradelay: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d04a84b6a13cbc33cd7d42929709135478c2db16164797de8d90c6a38cd16e(
    *,
    time: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__160f932080e73164169ce77553fb3afe61436c114f0abbdf063dcba50c0a8139(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a21c3d3e63ae2724f2c4e048fc1b980dea02857980d3bf573acc7faf2d4261a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca5aa34af367365a83a8b6d9d0b2634a38c056d194d45f4fdbca149d7e780547(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3fdd1a51b3e0a8fd0b8cc8d94c39e138a8ec42b8b97d8782ac64757da55f7d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b321f74afe4ebf34dd289674d268dafdf26e832cf3adc837f0adef3e448bc6e1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c743fdb66570550147fcc2554b72320c338c2e47b41cd6b213151407f1d67a05(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c70373ae55a49e403771c876742afbdbcff97cc5d8d005b2df5d395a48cf5c0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__948a0e8ad8c77b52950767fd73eceb30dbae5f793b53dffa4ed44643afe17434(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e7952534460f411e219a7a121448630b5cc78b1c353d3ea6ff41ec63f56c488(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a1bf9d754f05cd0967bce31c2714206219de20e15cbd82e816a9cf9c6a93207(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9863e0770e33289771e365e9fa53aa1e6b79c86acd789c261a59c5cedc7688f3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f822d6139095b60229d0ba0cfc8c579030074ae769ac780cd1400315df481207(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__408e37ce50467af9fac23f9ef6be40e292642b899237f3c838048ffef8dc4fbe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2da7d3ab9e37b6525eb5eaf7b1b6ef50ff0651bd6e1708a26a918742fc8ac8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35fb8804065bcdebd9f2c084ff56bbba64d22de3c67e2f69b60279b0ee83d612(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfc1dc5ea52384e7acd2288986106209cd6ddf54c381ad17ea6d75d4a8c8b978(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c92bc845a33ff864b39d3d258d3895362e29a0c4e2a0fde14fe26ea40901f64(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9502f4cc4a36180ed04a612f54efce76b194027694166914a0d068b03c082ef7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f49b9774b1fb99557d5e48fb83ef52fb710738e3236f677cecbadc5ec78ff46(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e896162934ee20e64b76cf8680fd00e1c10f160ea005710af595129482a7d00(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdb5eda7678a31997b850287240306037bb72d9441f1e61f25afae31f430ce93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7563249c39314ec9526bbde65a901b4cc3a3e901a3ff274f769f7b13d4add997(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbfc3e8fabefd3efd6592eab3a34cd686ea870cde6af1bdcbb2aec4067fb33fe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3e8a65417f7cf5ffb716265c20ba36f4e750ccbb91a1a1e4eb3688f3d930ca(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3118dc2dc6b0ba68de4a570bb832cf519194629695184572c4582b352830f692(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca7170166815757657849e66e5b9d3d3fb00e5e8c3c7eb80f14cbe233c08a4b4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0860db6ef2ff776c0084430454f96c031103d62cb48b95cebc4834f6d3eca288(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73d2023a48419b3d0ac6f5e3532b88f739d230c2b80d26e12e6f54708dcef167(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolBackupactivitycontroloptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__533eb0e919607c965225fd70c472a09ce815d4394d54b96ca35cbdfdc3054059(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c46512f9832ffcde0af4bf9b2914b21eb7b8d09d1f6bb5cd5f1b938460da1d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d919d5f7639d57a1bd2919ead0445d26894a24271db68f35fab53ac4e1bae3ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b74c1ba5880c8fab9c689c95f62a862f659ec4a87274e06eeb3696c337440d98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31366641ed769f9c823db7c6d7c8bd558363443a5c4451a1a118faa2541e7953(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab0e6ca2734e744939d7ae695964881cc1a5e0f8c716c72e21e99ac3cbd0a266(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolBackupactivitycontroloptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4464171e0824e5c92d55b073dadb35bad06c740a7a189909105e8dd2d1dc0f91(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceb5e1a61d937473d98f21f5d420429b11520710496f2d7af994704cb49f258f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7fb402116471943ad895a001a1e030f2c23892bd7b16f77eee1e230e4df586a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b5a807bb7f00274f1ff909070988377af9aa276d66b2fa8e211845fa7767ea4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4827e15f608052cae06c63b16619cf9d97ee6efe5c17f52509f8f3b700c8e3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ba26984839d5226ea70193e89c48c3e6ecd594072abe5bd28cc6e0eb3c85f5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrol]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5344d31c236d1d10651ab8b36d927c2b4d5a7392eea3d44719b63cae33c94e5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc0938c728b7271f15d65d7927a067a5f9ac9d0c4e008b51b3de487584dd8b2c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolBackupactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d7f89b928bedaddecb9ddeb2727c3c03194d6a17ba28d45994dd4044bd9cf7d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d04b5b1b3e5945545193b0dcf243ed25895f62bedc9dec7f8464962e831dfed4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ad27bbf8515c4df8b1e16fac0caa7edffef2e5d40d2ab52fbf4da7fdc388761(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e67efc874459554b24e9d65bb3b08af4db2d560ec431adc01775c412ad4a6cd2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrol]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0799ecb6a6cfe4172a9a2ec541a9ff61545cae7f55a88c6ef7c07ea086c0dac(
    *,
    activitytype: typing.Optional[builtins.str] = None,
    delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enableactivitytype: typing.Optional[builtins.str] = None,
    enableafteradelay: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c75362cc06471b09fc815ef073a4fcff8a37706debae7e6d9079d050db96db60(
    *,
    time: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea3aa595e4a9980442021dde0e020e66d44d1bec724dc79308728768fe2685dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b85600ba44083c4f8fdb666648e19493a2c75f74c5731f3c8124dc18010c476(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f140e2795713a77b2e96dff48655fb5c5be4cc8abbe4fd3c7b942444faadcb0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6293da07377afc996f0f3ba88dea10a07e5ed146914ebe6bb9e089cea6411def(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a67f2154097567964ac4b0a69ad3f164b7a2e27f211cddf5e3c5553959e988d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa8752cb485fc83b75d3677cd5dc668c6b422df4ac871cb01ef524ec93b498f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2af6785b720f29330ec7a01338aee23a512ff403c2ea53b3fa8c15a12fc033c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3505fa99518a196658f45e4ed1643755696adc3ecbf3c7072d6c66a6520d78e6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076710c23df7731796f0722d2848d6072b35ff9090211c794c7ad575f01d774f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d7f637fe0feb38ec7288b4636fc6fdd23724b10ad211e022be8a115071f2985(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4276c42c6445598003e01169712fb3157541ae813f9ae97e5c2201fe192ab190(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af67addbddee453971f4807577002b3bef94d364af69786965efadbe49b4c465(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d1342553ac939a3e3f3b49a61d45c87d14d85030a3d08286652c3b6fdd672d6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2246a805437ddce53856755d0af6671b12930ca404b60beda15cead81a5738d2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcf69690fb04f209938ccfd90f8a634549cf09aea8f1d4f09720a90247f1d033(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__958056daf7176fef00725b870d7b64f9db5bd9fa29d6e00d0ac864dea140d061(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2cce85ef3dd338e9ac680330106a0a03d856561905b774b5d8fa59d4bf97326(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b8d7609ae527121ff619934cb3799be619c9a2bac1583dddf631b193b14d05f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a4d3efceee23d170d53bc0c92ead4cd4da53621606073526125610d69e20b48(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f55560d092fc6d718fa76306045672d2f11ee360d9da18d298436e0033eb067d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4355585d1600fc5bae9a37880b4973a49319d96befe7f83367937eb8bc20b8c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c4dbf6764fe3fd3c9829c1712264e871c501805dcceaa12ea5485456905a210(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__425911ebcaccaacc29c19b7cea494acdf8d0b56999d3dec67ca4a600ef027c11(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fbe77e55ae46d4dbaddbbab232bab8f22dcd56e6bad3ad790951d93b24a3e50(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf885c8496dd93eceab964ebdd11ee05adf15793e86ca4a2560fb04c40231c80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__953d8cd22df82001df66a751936075907755df721af01b779d51342cdb3977b8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4d5f56e26cf3197763433372338731b7be959f1056d79868e61a28ebce4b6a7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19237f6fdcf717308baa82bf61d4e8f51725215a3d8894cd87ab4af675c8e934(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsActivitycontrolRestoreactivitycontroloptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7dff02f3aeca7f44d68ec88ba8e2450160e1329eb3ae338eda2db316d5a1c7c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18a6007b7ec55d913fed9a404336abee56652b1d1d326a4a3a4372cd0a85840(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrolRestoreactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb96c9e7440dd20699b986ac89c01ebdd964dcd0982a68d3020243d3b106f1ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d14d4385697612a485e28b613b42afaa71d74b5e6af0a6c0e28412db840dc17e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f7be644cc9912c9dac6139b0bf2c28d17a1c9f1261f4373af7ee9aba3475710(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a537d1ad5da3d0b51c75259d316a38818e62d4b361608222890f3ff84ac93486(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsActivitycontrolRestoreactivitycontroloptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__081b4659eb613b7f1353d60b0d1f88e06863de5242a53de6dbb6dd2b9e4b263e(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    accesskey: builtins.str,
    name: builtins.str,
    secretkey: builtins.str,
    useiamrole: builtins.str,
    accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    displayname: typing.Optional[builtins.str] = None,
    enableawsadminaccount: typing.Optional[builtins.str] = None,
    etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsEtcdprotection, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsFbrunixmediaagent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hypervisortype: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    rolearn: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skipcredentialvalidation: typing.Optional[builtins.str] = None,
    useserviceaccount: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19ae90d138fcdd700cae503db07eaedbab9258c3f732a9d33e4fbee80565e05a(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4fabdbb5b9ae507c2f07f808a2568a2c889e2635b898691bcbe6809fb59434(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd000e37795a4ae356a8de84c2e533746cca8c04d31bc78a973ffcbaede0cef(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faaeff078a587620805a6735bff7fca53d40a4698daaa9ef96ff58732d6ff635(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__815cf2d006ad3616ddd6128de1548ac98e5296f4cfca5df91af9761d0cd2764a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0656517beadd7515fd02a5a8b51eca5ba94cc1cf622a79ede5162f82d0842960(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c978d3ca0d7e70b0ea0efc97fda6fd9a800a1219220f7bee10d7ae8b8450d85d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsCredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5248c3e6758c0401ab53737fb558968f85eee75bd37ac136d42cfac14183382(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16a9c85f17ac36d072384161223afee652276f5b53ba5e07280e5d294b7380a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__226ce6321cd8551b47ad5b9e653166499a8da43d83d87b90627be079f15a7386(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3888e590a83458f8304f3ab6228ebf5117e1e31be73bfcf7d9c006163d8f4f3a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsCredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__672a925a28f66ee511d962ad7287354db60b8f9d9cf6b98f536767549d36a29b(
    *,
    enabled: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsEtcdprotectionPlan, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a87ae464b2655c4d0d7b093edd7425c0dbe08509ae932f27577fbbb48877058(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fee88e00b32d5e9b40c8e75c5fc49e2dee9bc5a2df0808a57e1238accee29f2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a81fe91bdfc6adb9f5ab9758544eb3530f4ade36165626536cbfb01b56b883(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d63f1ccb1a91d2e16c148ea13dfbbf76df27798ba6eab9644aac7b220f4c01a7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ab2225e9597e20784f36e193e2437b1332cf3c178c3fea4bf665dc083dc858(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6299f8b0551ce68af1059e2ae4d0542d1e14ccdd8df5ee1eec31aba17b910258(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotection]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ee8fe3d9f1244097cf96ce8d312219e634614ab43c7c3ab00b087556b18541(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca35ec7a98eb923dc8c8bdc7eecbaf470961eca950082c3820ce968bc2a0c914(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsEtcdprotectionPlan, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b39733195d698ceb8e3a818254ccc9a7153d56fdb09f3c5068dd70f5cb352282(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea9bd7644652b05c40917468fd41deb29216aeb0a6d72c126268a25eb3a8ad8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotection]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2a458727637ca64dcbf3c03a304ba1524463d6758fabf133bdf3c0ae24560a4(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__807d6c57c6459c01379a6dae9fd3a516efdfebec27e22c0856821a6e80c15d65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd5b425ba91a7e58f5c93959b9fe8da9cc1e8806e467bbfe8ed8cd1b248d533(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a63898f564a8d6af64b2b3381942a4257c356c7a67b1d246a78d25557d37df2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ba69f6a61c9b256b17c371387b7eee3561b8fc950f1edd6295c9417de80679c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77780835210ed97e947f41686d6b386a89c5e1aa64c869f05875dd4b3605228f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc9eff2c55fa480d8894a3d177ea12ced039d60af35b054d996ed023618b762(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsEtcdprotectionPlan]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92138477f06224aff23a38e4204380e73e774d8b35f42d52078052847e0c7f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d74cdf4d1356eb3fb811205eb0d33cbd790aa031838782f44f28d88fedf16b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81aa9654c9748b80bbe492abeb92ee3857ff6003e04ccddbe1f11cb32cf15012(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a3ebfec4bbfdba14f45c829192fcc2a6d7b6353b1cc2c9d458f633e79e26e5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsEtcdprotectionPlan]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ad59b785b6478fa8b7dce13232f770fabe31df892115d959df00ad3b2a40013(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdcc89d22662b816d539548cfd4da21e3b7ffa7085f5b749eff9993f1884d67f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ae237035b11d89143e39b4a0d6559a84c16f20be864f8546b0b74bfe2cf2a4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66840cd367320f74c248413e7e5b08f78e3244b2130ccc807f913b8bbaaa4460(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3601b4906aaf1521174d6a58bc173e705304f8a4903c1b8c0e11b2f3f20467d1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4abe8d49abb65685e18de792126c42d414d27ae1e7bb5bbfedffee811a60f6ef(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b93d8df86b73b83c1fc25bde189ad85346c9331566634e70d45bebf74f4ea64(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsFbrunixmediaagent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd0babf6428adcb98ed77cd02d02592574b8cc11b00961d4320463b2e3b0cea3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b04de2ab11dcea9269ae0de0c622dcc55112e3cd627ab199170dfcad45875d4c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f308f25ef18afdb161610465ea771f56e9248551f065c9c78ced6629790279c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232efb2840eeb40938e63ca4b25e52e6cd9466f2d65a0e06b7c431ddc160f1d0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsFbrunixmediaagent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7487908df2c603da5c4cb544091077424459373ba7d50a168a0a3ae96a6b5f7b(
    *,
    associatedusergroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSecurityAssociatedusergroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
    clientowners: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75bdc4eeac3b033523526947d940ffdb27a81c0f9538fd1c6921539363e59ad1(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47797f8b33e0d454132e14119bb38872bbfc166901931ae36da32ff1df2bd54c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51081ce3da105f177b11458191d977802a501cbe5532cb14d7869c593daed825(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb44f6324cc4d660e7922b3b62a7944020882d49251d9ecd126c6ec3b6b10b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47877783c704025b56bf71a5b1daa5b1949552d3f8fa5380b5ad14de2c1b46a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db408fbde9c4f588b3f8aa2184cfee71e45c783eb3f1b1158ad5f886af4eb36a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6523ddfae184838f992a5275ed4fd7cc5b6096faa4ffc3470e120dbd6d16a33c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurityAssociatedusergroups]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9568f4660c1a4258e170ed583df50545a920a90448b5444bd9fb7ccc185751(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f297b4987d30be5f74f205319bcd1c1919cca9d6448f1385fe1252cb1c4f000(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c14d73100dabcc507e34fddc8ffaa504c708993b8eacaff4b567b7321ac75e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurityAssociatedusergroups]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9cbd366f4b407406b5a53809d7533b7ba6f6bcbe5ef0589bd75397a3bad193c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c975f7fe4fb425030a777e3d327a6a028b6d381245244cc66a2483b7fb74b8f9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50597ad14eab04855e06cb5e9fee76111e1312898e8bd50fe2f9f497e4544c51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51c377bd50feb69666f7636036389c28525303213fe10483c12dcb61b12605ed(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74966f42dcabdffc86b896ced0942b4cffa2d588975f9e34ee48baefe7fe82d7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e84b103509d0b1efd6dcd0d2f14b0b225617e51c6b46a4ffca51b2f4749996(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSecurity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c24eb4cec4fd994492235376f8c288b858d8b91b0edf77bb316cd16d1d841a2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef4804953ab10cf50a6f84db68d4b256d9507181a90fb8211e62a17367446155(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSecurityAssociatedusergroups, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b44c65d927c4cc2cd15f8cb7d3d3610ac293abcb3209d8f9cb949cad6a2c9c74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29bfe3253887a025205a82998903a19c447e3cf85596bd4744cc964ca7aa4139(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSecurity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97e5a0fa6313743114cd8dc77deed7fb015326c13a014804c9f665c847a67dc7(
    *,
    applicationcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsApplicationcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    customattributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsCustomattributes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    guestcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsGuestcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metricsmonitoringpolicy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsMetricsmonitoringpolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mountaccessnode: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsMountaccessnode, typing.Dict[builtins.str, typing.Any]]]]] = None,
    regioninfo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsRegioninfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f92db4263752afe24a9be631c2bd09beeeca96c825683dcf473b28d6867211e(
    *,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acc5594c1ad73217d28b2b80e4862948766d72a50ee611632910f3e2e07efe6e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__832b37a3cd73d0e772e9590bca764184467e226ed3c4a5d056086e8708166316(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb2e1aeee73ebc35c043316b7fb7d1e41d36181bababc93d9988e881350ba101(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6596e32119ac00bacf9c9682b13af69cef9925d04881975bc51262c9e1ccc89(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25951e96f8c78ed101eb2885b6b4194de14f2e2987aee0c9264c7bf39ca29b6c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d105909b6cbd3a67f5ee57188d5e20421379cb45a82b2f5919d47549eb74da9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsApplicationcredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c563bcec0f3a11059c9dc9d7a6b8bd2253610f5a3aeba508f2b052aa4b7af21(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58379613416827f2e2578b7f2975f0b76fb2f3f6f7b2149d419003644bf6edba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a0845199ed3dea4d9f13bc254e73208f36e5c1adf333659561d6d01967a1775(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75172f05794b41abbddb38bbec25cbc2d48836e76130f2e5ae9315b32439ea94(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsApplicationcredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e0fe5d8a8a948e2640488e3e51b61a6d9c47b5cc70eed7678643c38805383b(
    *,
    type: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6442235783ea0a38adc8ba5a1932f24adfa0e5fa5489c1bb69e1d1d02dd40883(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e775b1e0827768a5798351bbf4a06c0a8cbccff2cf0ba497e406113f7a73c90e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170dee4c457d98460a8ab7d2aa661ee9f97fbd9b35c3428c7814bba08908385b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3cde6206b8d53de00f59642410c239d2e596710fa75f3363e3c512a44426af(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c637bdaaff68ff91a576bafdeac1b7d56346556bfe2a75caf5e4dd5d5079a1f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__465ca62bba0c3b72f5a6c1ea8b90efadf77fb929b62774cd8458fc1e3e546e13(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsCustomattributes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189470d44236384d7514ecd86c8713d65ce3aeb49b7252255b50dcb2bda31ecf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c38b7b43ff75a72550bc509d80e6464cfc43d4ffccad5522adec2fda01eaae08(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a259783e81b5547fbc367f2d001a1ab424718132040940a258b54f36cbb6f58(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f27293138fd0e6f9222576098b68be5df5e14dcdde4bcdaa70aa366f08a2479(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsCustomattributes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce17bbea13486e0e85bdcbd79e4f94ac7ca3b7887efcdbd41211314bb0842a64(
    *,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7e5497c702d050524907f8147906b8c3904cc61b2295576e261b617a25853f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fff08b4dde713945ba077243b3d9d0ac654fb123c2607ea8e06e1cfba438161(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797c7251e457252e7328a844b751131b17743fb3decfccd78f0c96f767090394(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9bf0c1db7d4bc472a50a3df9a180a966fff62d2a9681601f871183a1ca4712e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9c373cb74733388824685aca6ba3958086a648501dc8c1ba10ba05f31efdb1d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9af304df67d83c170cd7dd5f5dcc8170e69e4313da78c92bd30d0b17486ea3b7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsGuestcredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf0320638e0de928f12c2bcd35cdd6d60fa773c40efd37cdb5e6cfb565cf306(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f42f9200b7ba371395b4fc9d03cb824e371d82ba74dcca3ea173481d26d83e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d09ef5b2789c7e5edada93a1ff29e8358d39af909e6055b458a5a24efb2bdca7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d95b04b2412fd72b2964b6fd5e3d864a70b94f52617322b5dcfc56e1b5fb1d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsGuestcredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca0a31254c831155371ceafbeb2193ebb397f00d64940587f884cca1f3e4a898(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324632bb35e1a63cabacc4fb8c1ec26bfb395cd98a7f8de567023aa4d529f2e9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38ac831943df971f49742fc97207cd6b3ce072a9c80d2f4cded6077e142b9429(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a3940cabb8d656bc1710e9cf6bb113adc9ee2db84a344fac2c8272b4141a7a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5c0f4a8c5be33960ffb40c83d3075122940b1cc331ba2d38686da8c25937ff5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79043034267bc9d6ab0d58d9e2ab0c397e5048b4c9fa4fe932d170e3d67b9055(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29571947d5384725475de1fb5c6d5f871aaf1afdf4b37386dbc726ad496757c4(
    *,
    id: typing.Optional[jsii.Number] = None,
    isenabled: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cab026d7e29d764e9745effdc655fecb46af25c77e7d0cfafe6765a31a8e81e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8ce3bd128a6d213b3b1c7fef677d0262d5484902d44eb5a2f585c4e448d18a3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c62ba7befcda53c647647af8a2369a435b0b9672353745b477dadd7b4f267785(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51f775401e193b9ed4883b2f4bec43f69b09247a0e9a8895f7f994d5d1162000(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c1d87496e00c482c09d55748d46cf9157be479f91961537fd6df790ff642ee8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12d48929b0e9e56f1490c1f3747f5a9d70b79bea1e43a9429a3286ed66eff526(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMetricsmonitoringpolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f05f4f6c6a08a3f8e235cc9c4755333e55b1be4e6d525ff8d6ccfb15902bc9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f3eabd4154e011c5fd2dbea045f75d4b2eb6ce633dea93348e1706db8fcb3f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27d0ab1e4e4a8269998fc78ff2309e8f523c80619f015a3c94188dee6ebb06dc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3abf7eda16b5c58b681eaca7b2752de6ede652ecea22822285e8b758a1580f64(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30152551cae51f6e7072a0b40046df8996dd3cc8bcc343d78e1ed9d1a386123a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMetricsmonitoringpolicy]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebb16ef810715dc6bc4305b2f5ecbbffc29b1afe833ac62a6881e34b9c858dac(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b322a89ac2f10355f075ea300fdfc31ed04dd0bbffd3abe1a6b198603eaf860(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55a17ff37f95c336f8523378a7d2f2920f22af4f863ea73058e63ed21174deae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__508cea020d9c15fa48c0b08c7ed22b789e75d0354f581e8714721e305cf7a42a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf741a6e0782100e5edbd0b54b9fa63252c23cf11db803e4f1a256f52967890(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49871d006f41e1167768c10abee5d4d6ceab9599b601a8289aa97267c3ba6d99(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527c6a328fa9f2deee10a3e617a782e7bba202a30aad91f29f2d27c6947cda76(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsMountaccessnode]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df621357f0d25e0770e4c616599c582f89be6c470c3c9ddc084ee680e563c18(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86257a7f4f98cb1a8e63e1214ffcf3103da504c11844366757c96f6fc82d4e8e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dad4cf5e36f06a5283e44c95e157df71ad5f823024a6732798094a20339ff09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b071bfb3dc70ff907a701585abeb3eb9110927711845f8f0530f7cde84ceca(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsMountaccessnode]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16415fee61db3c237f0b0d78154403ae355773e46bd362e191193d976f303e2e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a176a043c36b225a69923e5d3641746c72e405bcb4c27ed01a73e6f710b0e051(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsApplicationcredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1331726471ff12ce0a07c1008291896f0caf64f90bce8a2af055208d0b9e4f0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsCustomattributes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86afd046218892c25129696a69654975dc73561fb75ec59e644e1d1feed75c38(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsGuestcredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3db4e0e251a4f41bf85dc7da4a03757fafb46220925d11bad747f3ded7f758a5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsMetricsmonitoringpolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0ba6065b1528442dc014e79d2b6fd19abc1610480ed186564fd205d5a538043(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsMountaccessnode, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b0779de617d425c0aebe13cdc13c62575b11ec59b38dabef6e5b93189efb1ee(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsRegioninfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92321d74e021c49da1564401898291433036b06d1e3387a76df41cd93976efdf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAwsSettingsTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68dd5b0eb62055ad0097282103faa38193f47cc249b1ea40c67ac2688f256a62(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d25c62fef570a7963e2eb641d04d3ef215cdd336cf0c6231b3e121abd09d94ab(
    *,
    displayname: typing.Optional[builtins.str] = None,
    id: typing.Optional[jsii.Number] = None,
    latitude: typing.Optional[builtins.str] = None,
    longitude: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b5ea30f7b92dd26b655e706dfa342b086a16da4bfb2489c5cc5bfcdcd254c7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c02c5c4f518820275173e8126b14274238c746bc8e53a3aef8d694308e45da1a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0ca27c57e536fc7cfa402c691ed257fb70a2080ff400bade4972e78180c3c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c80ca201226ca74ffc5a1b41c8ef1b7cb1dfd1b5c3ecf4076790f06c692f19(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bbe6a62bd16d82218177789bc834ab6ad29545cd4d5b32c1385034146e1b355(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de276a6320cf37374e7810d248184f6cf6f8d66559740a6c32f17b625ed8f855(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsRegioninfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ab659f08fc3e53d16db171f94bbeb3efd404416a085541570d4061aebdeaa0b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47697df467da4f1339b5dd2b058b8e9d38e6d56a106a85dbd8341977051814d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9547b348c6ac56fe2249f5a14c8a83f8b69a073929b510bb14b27c4e0cf5180f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee416eef6b95d1308feea08c3f12d5943f253fde398c5be9abc96f0206481a39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad59252318f2b311026d1ea7994091afebd5ca896a674585c15a7754d0fea224(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45cc6a9bca74a91e432076331217974e1d3b841b85ff159a23d0b26b6970b0cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__319711b15a9dadf694a483589b3cf96e0d22a58ca85b8d73d1761ad9b3d4f82f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsRegioninfo]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72b47232caf2e1f5b8870d5894d8b5d71adf2d02989716c58548a36dfede9e19(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf9438278d960fc401b4e45d4239d734c7b463a781372120a11abb5c477c4a9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c47c3ce6deef55949d50011e129c2830b48fa1d07175892151f34cea6e6bae4(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e27b26cc65378035969febfcb9b01cf3577e4c77a8df117b27dffdb3736824(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f897fe828147ee5a0c242082b2b89a073b6fe8c9549f9995ca413aeb703076e2(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a847e3001add5b7f86948ecfdd6d0a21c6421f72f83c06865f793ef933906bb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5ac75c44d3a80c44041c0c4e9338233b3e555f77d13cf112d5ce3718aeaddb1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAwsSettingsTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a548f0d57e767a503ac5d50424f95e3dc41c47d4115c7073f7042b00a6f4fd52(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__956964059d7428aaee362c791dba115a851dcaa5271ea183d782fb10209ba274(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f8ff3c15c50b9bf740a6e82ea4b84a877c5102ad62d09dde4e5572a3a3d3609(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a80c8cafa7292263ab7e460fa252ee91b5ee129a13e5d2ba609abb72613b406(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAwsSettingsTimezone]],
) -> None:
    """Type checking stubs"""
    pass
