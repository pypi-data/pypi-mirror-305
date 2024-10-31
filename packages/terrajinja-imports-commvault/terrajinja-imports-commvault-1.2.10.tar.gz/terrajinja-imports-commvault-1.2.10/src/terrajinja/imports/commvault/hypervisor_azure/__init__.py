'''
# `commvault_hypervisor_azure`

Refer to the Terraform Registry for docs: [`commvault_hypervisor_azure`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure).
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


class HypervisorAzure(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzure",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure commvault_hypervisor_azure}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        subscriptionid: builtins.str,
        tenantid: builtins.str,
        accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureAccessnodes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrol", typing.Dict[builtins.str, typing.Any]]]]] = None,
        applicationid: typing.Optional[builtins.str] = None,
        applicationpassword: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        displayname: typing.Optional[builtins.str] = None,
        etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureEtcdprotection", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureFbrunixmediaagent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hypervisortype: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        servername: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        skipcredentialvalidation: typing.Optional[builtins.str] = None,
        usemanagedidentity: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        workloadregion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureWorkloadregion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure commvault_hypervisor_azure} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the hypervisor group being created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        :param subscriptionid: subscription id of Azure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#subscriptionid HypervisorAzure#subscriptionid}
        :param tenantid: Tenant id of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#tenantid HypervisorAzure#tenantid}
        :param accessnodes: accessnodes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#accessnodes HypervisorAzure#accessnodes}
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitycontrol HypervisorAzure#activitycontrol}
        :param applicationid: Application id of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationid HypervisorAzure#applicationid}
        :param applicationpassword: Application Password of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationpassword HypervisorAzure#applicationpassword}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#credentials HypervisorAzure#credentials}
        :param displayname: The name of the hypervisor that has to be changed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#displayname HypervisorAzure#displayname}
        :param etcdprotection: etcdprotection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#etcdprotection HypervisorAzure#etcdprotection}
        :param fbrunixmediaagent: fbrunixmediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#fbrunixmediaagent HypervisorAzure#fbrunixmediaagent}
        :param hypervisortype: [Azure_V2]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#hypervisortype HypervisorAzure#hypervisortype}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Application Password of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#security HypervisorAzure#security}
        :param servername: Client Name to Update. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#servername HypervisorAzure#servername}
        :param settings: settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#settings HypervisorAzure#settings}
        :param skipcredentialvalidation: if credential validation has to be skipped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#skipcredentialvalidation HypervisorAzure#skipcredentialvalidation}
        :param usemanagedidentity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#usemanagedidentity HypervisorAzure#usemanagedidentity}.
        :param username: Application id of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#username HypervisorAzure#username}
        :param workloadregion: workloadregion block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#workloadregion HypervisorAzure#workloadregion}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3481eb1ecf65bdf7575d1535f13c9031e61896855bfd9f3719c08a8f221558d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HypervisorAzureConfig(
            name=name,
            subscriptionid=subscriptionid,
            tenantid=tenantid,
            accessnodes=accessnodes,
            activitycontrol=activitycontrol,
            applicationid=applicationid,
            applicationpassword=applicationpassword,
            credentials=credentials,
            displayname=displayname,
            etcdprotection=etcdprotection,
            fbrunixmediaagent=fbrunixmediaagent,
            hypervisortype=hypervisortype,
            id=id,
            password=password,
            security=security,
            servername=servername,
            settings=settings,
            skipcredentialvalidation=skipcredentialvalidation,
            usemanagedidentity=usemanagedidentity,
            username=username,
            workloadregion=workloadregion,
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
        '''Generates CDKTF code for importing a HypervisorAzure resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the HypervisorAzure to import.
        :param import_from_id: The id of the existing HypervisorAzure that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the HypervisorAzure to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f41d5e0da942d91dac227208f19a60ee2d2de3e3a89b1f9acbc67506178f467d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAccessnodes")
    def put_accessnodes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureAccessnodes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1e98bc81e62b5a1fac87cc55916e07acfa3fef77501cf639dd6241304bed7a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessnodes", [value]))

    @jsii.member(jsii_name="putActivitycontrol")
    def put_activitycontrol(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrol", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a5340c586de1a94d5c91e4d1f146c6de0db28b7f10791b60bb97d99e6d8e986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActivitycontrol", [value]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureCredentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d5bea7d341a7b9aa85572a89fb07e0d3a889611122f3e72f425b13fe9084a53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putEtcdprotection")
    def put_etcdprotection(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureEtcdprotection", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4543300df08a3fb044744e19abc2ceec28b9dcf6e66c6fbbf6ab46355e069ee1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEtcdprotection", [value]))

    @jsii.member(jsii_name="putFbrunixmediaagent")
    def put_fbrunixmediaagent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureFbrunixmediaagent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62e41f38538cb9c6ccd9c9363be043b6edce5a1dcf069cf41e082d8df8e5db7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFbrunixmediaagent", [value]))

    @jsii.member(jsii_name="putSecurity")
    def put_security(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSecurity", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__664696d879eaa01dddacbe3fe5b84ee277c80f8ce8ac9f15d79d2f19cfd628d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecurity", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3eb5ffacec544e98429c47f1d71a9a09bdeab4ebefd7092dd7a2b95893798b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="putWorkloadregion")
    def put_workloadregion(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureWorkloadregion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__787cce75c9628d69871125ffd7b4d9a1bed6989420e6a7e96885f476227fb7e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWorkloadregion", [value]))

    @jsii.member(jsii_name="resetAccessnodes")
    def reset_accessnodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessnodes", []))

    @jsii.member(jsii_name="resetActivitycontrol")
    def reset_activitycontrol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivitycontrol", []))

    @jsii.member(jsii_name="resetApplicationid")
    def reset_applicationid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationid", []))

    @jsii.member(jsii_name="resetApplicationpassword")
    def reset_applicationpassword(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplicationpassword", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetDisplayname")
    def reset_displayname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayname", []))

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

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSecurity")
    def reset_security(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurity", []))

    @jsii.member(jsii_name="resetServername")
    def reset_servername(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServername", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetSkipcredentialvalidation")
    def reset_skipcredentialvalidation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipcredentialvalidation", []))

    @jsii.member(jsii_name="resetUsemanagedidentity")
    def reset_usemanagedidentity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsemanagedidentity", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @jsii.member(jsii_name="resetWorkloadregion")
    def reset_workloadregion(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadregion", []))

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
    def accessnodes(self) -> "HypervisorAzureAccessnodesList":
        return typing.cast("HypervisorAzureAccessnodesList", jsii.get(self, "accessnodes"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrol")
    def activitycontrol(self) -> "HypervisorAzureActivitycontrolList":
        return typing.cast("HypervisorAzureActivitycontrolList", jsii.get(self, "activitycontrol"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "HypervisorAzureCredentialsList":
        return typing.cast("HypervisorAzureCredentialsList", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="etcdprotection")
    def etcdprotection(self) -> "HypervisorAzureEtcdprotectionList":
        return typing.cast("HypervisorAzureEtcdprotectionList", jsii.get(self, "etcdprotection"))

    @builtins.property
    @jsii.member(jsii_name="fbrunixmediaagent")
    def fbrunixmediaagent(self) -> "HypervisorAzureFbrunixmediaagentList":
        return typing.cast("HypervisorAzureFbrunixmediaagentList", jsii.get(self, "fbrunixmediaagent"))

    @builtins.property
    @jsii.member(jsii_name="security")
    def security(self) -> "HypervisorAzureSecurityList":
        return typing.cast("HypervisorAzureSecurityList", jsii.get(self, "security"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "HypervisorAzureSettingsList":
        return typing.cast("HypervisorAzureSettingsList", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="workloadregion")
    def workloadregion(self) -> "HypervisorAzureWorkloadregionList":
        return typing.cast("HypervisorAzureWorkloadregionList", jsii.get(self, "workloadregion"))

    @builtins.property
    @jsii.member(jsii_name="accessnodesInput")
    def accessnodes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureAccessnodes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureAccessnodes"]]], jsii.get(self, "accessnodesInput"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrolInput")
    def activitycontrol_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrol"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrol"]]], jsii.get(self, "activitycontrolInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationidInput")
    def applicationid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationidInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationpasswordInput")
    def applicationpassword_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationpasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureCredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureCredentials"]]], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="displaynameInput")
    def displayname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displaynameInput"))

    @builtins.property
    @jsii.member(jsii_name="etcdprotectionInput")
    def etcdprotection_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotection"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotection"]]], jsii.get(self, "etcdprotectionInput"))

    @builtins.property
    @jsii.member(jsii_name="fbrunixmediaagentInput")
    def fbrunixmediaagent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureFbrunixmediaagent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureFbrunixmediaagent"]]], jsii.get(self, "fbrunixmediaagentInput"))

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
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="securityInput")
    def security_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSecurity"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSecurity"]]], jsii.get(self, "securityInput"))

    @builtins.property
    @jsii.member(jsii_name="servernameInput")
    def servername_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servernameInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettings"]]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipcredentialvalidationInput")
    def skipcredentialvalidation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skipcredentialvalidationInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionidInput")
    def subscriptionid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionidInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantidInput")
    def tenantid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantidInput"))

    @builtins.property
    @jsii.member(jsii_name="usemanagedidentityInput")
    def usemanagedidentity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usemanagedidentityInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadregionInput")
    def workloadregion_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureWorkloadregion"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureWorkloadregion"]]], jsii.get(self, "workloadregionInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationid")
    def applicationid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationid"))

    @applicationid.setter
    def applicationid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4526ab33118e90ebcaa543f6b1031b009c0d7bcbd7a0165b0f47eeeaa7848183)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationid", value)

    @builtins.property
    @jsii.member(jsii_name="applicationpassword")
    def applicationpassword(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationpassword"))

    @applicationpassword.setter
    def applicationpassword(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cabb2931428159c38873bb6dcc39e5dd9964e83e71fbac882ad491fff301c51c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationpassword", value)

    @builtins.property
    @jsii.member(jsii_name="displayname")
    def displayname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayname"))

    @displayname.setter
    def displayname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__905c013392d92239a807550f6ffa44d40f45395f374776489d70ad9e46dd2cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayname", value)

    @builtins.property
    @jsii.member(jsii_name="hypervisortype")
    def hypervisortype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hypervisortype"))

    @hypervisortype.setter
    def hypervisortype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a589449532880f21cc10ea66e62b67d6f89d45a02781d225dd78e1687e4022c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hypervisortype", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e401586edb7e26fae6afc2e1358f4674546e70760cdda635e3e48e9905693962)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1c0d56e2501bb15323090d4867b1e34b03acbb178c1a02d22d0352b7d0e588)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c85e41daf00b10901d03d382bc0d4014257bcc4d8a6df5294e932ccf8136f751)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="servername")
    def servername(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servername"))

    @servername.setter
    def servername(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd24e129dfe88e7be6281edb4acaec3efb7da1c291a3d2fd077a01551caeaba0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servername", value)

    @builtins.property
    @jsii.member(jsii_name="skipcredentialvalidation")
    def skipcredentialvalidation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skipcredentialvalidation"))

    @skipcredentialvalidation.setter
    def skipcredentialvalidation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__123fd17e219cc0b4656dd9f500bedea6c4ce12eef3b8191619ab14583a1ae456)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipcredentialvalidation", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionid")
    def subscriptionid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionid"))

    @subscriptionid.setter
    def subscriptionid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d161b4369ccf695cee5225087370a2b74cc175f3353be0d6273b9b1ac0e32ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionid", value)

    @builtins.property
    @jsii.member(jsii_name="tenantid")
    def tenantid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantid"))

    @tenantid.setter
    def tenantid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225a6253d7ed90d702e70e2b01663c09d7072084a674dc799752a156f9367fe3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantid", value)

    @builtins.property
    @jsii.member(jsii_name="usemanagedidentity")
    def usemanagedidentity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usemanagedidentity"))

    @usemanagedidentity.setter
    def usemanagedidentity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2265727007d857a211810f44092505ead749d5314465aad911a9e905eb859618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usemanagedidentity", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d561310f9ce1d4f0e9458b194a931d66cdb56c2e04ea7c405b8cf31ecb009d28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureAccessnodes",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class HypervisorAzureAccessnodes:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        type: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param type: Type of access node , Ex: 3 - access Node , 28 - Access Node Groups. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#type HypervisorAzure#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7419c61850434fc1fcfd530009b3b362465ec595bc0bce6c916ed4df2b3301ea)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[jsii.Number]:
        '''Type of access node , Ex: 3 - access Node , 28 - Access Node Groups.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#type HypervisorAzure#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureAccessnodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureAccessnodesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureAccessnodesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57affcaac0606e0041684388295fc34c5ed0a6516589dee1e8362681bd138dc1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAzureAccessnodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0e7eaa0008655531d76c7cf0df3fceaa2f4eadacf4dc8e49b7c0a84dff99731)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureAccessnodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bea2e11d7361a965c6a640b6283e6feddeb71ea042e37c0323be9b24d649595)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a99a709a541e96859b46276db9c8d01e4266fbf02ee2db34b60c889253963fc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__110e193cc16bf72c3077b56b4cacca20e5eada215542ebfd9e1aa940d7b407d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureAccessnodes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureAccessnodes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureAccessnodes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0958a0b9a5a8d9a3a72abe170f935dd1046ed22a89df41f54c3ce29811080460)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureAccessnodesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureAccessnodesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__07ec1abb7d117ba17ddbd545b3dbe5ab83217f58251eec5b186e2ce01a58d999)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4798f07cf92fe4cbad4f063d5f2d1ede327647f65cf23f6cc314edd5d53506cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "type"))

    @type.setter
    def type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b6ecfe1fea5c96d4dc09cdf7f29ecba153dee63bcce0353ec515bb3ce56bbb0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureAccessnodes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureAccessnodes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureAccessnodes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4365db920387aada43e4e3dfed4928829f987b9dc534a9652a4feea674201107)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrol",
    jsii_struct_bases=[],
    name_mapping={
        "backupactivitycontroloptions": "backupactivitycontroloptions",
        "enablebackup": "enablebackup",
        "enablerestore": "enablerestore",
        "restoreactivitycontroloptions": "restoreactivitycontroloptions",
    },
)
class HypervisorAzureActivitycontrol:
    def __init__(
        self,
        *,
        backupactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolBackupactivitycontroloptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enablebackup: typing.Optional[builtins.str] = None,
        enablerestore: typing.Optional[builtins.str] = None,
        restoreactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolRestoreactivitycontroloptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backupactivitycontroloptions: backupactivitycontroloptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#backupactivitycontroloptions HypervisorAzure#backupactivitycontroloptions}
        :param enablebackup: true if Backup is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enablebackup HypervisorAzure#enablebackup}
        :param enablerestore: true if Restore is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enablerestore HypervisorAzure#enablerestore}
        :param restoreactivitycontroloptions: restoreactivitycontroloptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#restoreactivitycontroloptions HypervisorAzure#restoreactivitycontroloptions}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2590c4685eadab13bc258028cfc98499ecfe8cb1c5917def1919753691f50f2)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptions"]]]:
        '''backupactivitycontroloptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#backupactivitycontroloptions HypervisorAzure#backupactivitycontroloptions}
        '''
        result = self._values.get("backupactivitycontroloptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptions"]]], result)

    @builtins.property
    def enablebackup(self) -> typing.Optional[builtins.str]:
        '''true if Backup is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enablebackup HypervisorAzure#enablebackup}
        '''
        result = self._values.get("enablebackup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enablerestore(self) -> typing.Optional[builtins.str]:
        '''true if Restore is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enablerestore HypervisorAzure#enablerestore}
        '''
        result = self._values.get("enablerestore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restoreactivitycontroloptions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptions"]]]:
        '''restoreactivitycontroloptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#restoreactivitycontroloptions HypervisorAzure#restoreactivitycontroloptions}
        '''
        result = self._values.get("restoreactivitycontroloptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptions",
    jsii_struct_bases=[],
    name_mapping={
        "activitytype": "activitytype",
        "delaytime": "delaytime",
        "enableactivitytype": "enableactivitytype",
        "enableafteradelay": "enableafteradelay",
    },
)
class HypervisorAzureActivitycontrolBackupactivitycontroloptions:
    def __init__(
        self,
        *,
        activitytype: typing.Optional[builtins.str] = None,
        delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enableactivitytype: typing.Optional[builtins.str] = None,
        enableafteradelay: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param activitytype: denotes the activity type being considered [BACKUP, RESTORE, ONLINECI, ARCHIVEPRUNE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitytype HypervisorAzure#activitytype}
        :param delaytime: delaytime block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#delaytime HypervisorAzure#delaytime}
        :param enableactivitytype: True if the activity type is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableactivitytype HypervisorAzure#enableactivitytype}
        :param enableafteradelay: True if the activity will be enabled after a delay time interval. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableafteradelay HypervisorAzure#enableafteradelay}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f29695ddbe2e13079416eed7b8e55b8a84390ec9976a21eef89e61d79951da)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitytype HypervisorAzure#activitytype}
        '''
        result = self._values.get("activitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delaytime(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime"]]]:
        '''delaytime block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#delaytime HypervisorAzure#delaytime}
        '''
        result = self._values.get("delaytime")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime"]]], result)

    @builtins.property
    def enableactivitytype(self) -> typing.Optional[builtins.str]:
        '''True if the activity type is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableactivitytype HypervisorAzure#enableactivitytype}
        '''
        result = self._values.get("enableactivitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enableafteradelay(self) -> typing.Optional[builtins.str]:
        '''True if the activity will be enabled after a delay time interval.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableafteradelay HypervisorAzure#enableafteradelay}
        '''
        result = self._values.get("enableafteradelay")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrolBackupactivitycontroloptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime",
    jsii_struct_bases=[],
    name_mapping={"time": "time", "timezone": "timezone", "value": "value"},
)
class HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime:
    def __init__(
        self,
        *,
        time: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param time: delay time in unix timestamp. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#time HypervisorAzure#time}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#timezone HypervisorAzure#timezone}
        :param value: actual delay time value in string format according to the timezone. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#value HypervisorAzure#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91b0d522625f7b2746e8824a45a5a364bff30ec92dff16596a1c1651e0c3fc3f)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#time HypervisorAzure#time}
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#timezone HypervisorAzure#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''actual delay time value in string format according to the timezone.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#value HypervisorAzure#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44c9e28487f9680cb2aaef81130c8d729183fe24588fa7c1d9017ccd98523e6b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d50003a68046323971b3f8f84e447f3fb0ff09982f8a1655bde0cf5e227cd7f9)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__655324293e1266153c10e00a506f3279916e35e73afec1aee604bdc63b809684)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07fe71a8f8f4d5e29b702b6b38d11d163a4015635b8500051f5b2058eaf035d7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6654b8412e1123006f4d883edcbcedc981489f28225e7769811ec564663f366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb3582b75ee86b6d206d3b47316a97f5afe300c5e5caa656d4e6d0f6cbeaeb9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7fecc3d590284a399e18b548488cef52c2ecef5b6417ea086a1531b86ba483ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c4b827c6366d59aba64ddf438752c07fc66f5b35831a7608ab1f038ee15280)
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
    ) -> "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList":
        return typing.cast("HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone"]]], jsii.get(self, "timezoneInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__fb8c9f94593ceae8f95984ff72fdad0695a883e214028e8e3f9feda6535b418c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc403fe334e4aff9e85c0ca2e5cd5396689ca69b867de33d29e165a53c68ae5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233ecf73547ebb901a1c66eae9cf99f92a624439e521d5f5117d263bd6de22a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__187e096926c0988a6570936dd5127fffd4870bb18aecba43cae737ccad627389)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__467a6099b015e569f647fd0efb418c55a478a0dbf01877367233b1bd5677c5ed)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ead1f0c2d656da511145de6b931edb2dd030d6751e95c7b7738f60a67202f46)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5342b3b65c74dcdd1055c3fe9171da29a26a1be29dd516240a59582e49d255f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42c9157f5fda45cf30311a392c571b3d99094ce3541c34fa502df36f1f53ab28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ff693bb4c7e3b8e393aee68edb86ef99e261149b7275653cf5b805433f1d1ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__021c1f081ce8e526559865f9923f65f80926bb62ddc7d76ee49ebbe6053e62d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0257ab90acdf976eb743aef89514f0917104911bf42737e66ba344ddc678e32)
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
            type_hints = typing.get_type_hints(_typecheckingstub__24a94cf74053fa4700a63e7f519d6e29cc3f90e3cc55ff051e80c2519e3077e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d6941850ac5c219aaf2aa818b761723eafd6df6226d9c4e56d9f1bb884ee11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcd76b13684bb7d74fc7fa7a7486dc6257ea28c9034a6f0a54d34e015d9eb306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolBackupactivitycontroloptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64f78747605cff5eb4f091a41903f0da75ec94a03f53f068e827024deb0e83bf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolBackupactivitycontroloptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f794b5015c78409acdc9f54adbf681d2316495f8db6a37933b639e42e14c169)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolBackupactivitycontroloptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb9153939048baba37e27828b1a494a6c27c2e4df733c0c5b7fa0d922ef9b5de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cf5cb8779d5390c9203dcbb6561cf5d044db5557f4ccd6eb69c4821fd74507b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dc619d458f5f027f96e03cb378bced3054e3d0a74e53fff4cc0d0b2221b68ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__483e2a8e68e6a0ca9afd5a1616904688bfef99c650df783b01d73837e2b7fd24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolBackupactivitycontroloptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolBackupactivitycontroloptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__295fd9a40c196dde391cbc18a7362b2e14b2bc87f6174a037e40ae0ad69cb9ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDelaytime")
    def put_delaytime(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f6372e55a60641446146911646d61f5423914e78108df9369abf38a3b65258)
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
    ) -> HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeList:
        return typing.cast(HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeList, jsii.get(self, "delaytime"))

    @builtins.property
    @jsii.member(jsii_name="activitytypeInput")
    def activitytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activitytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="delaytimeInput")
    def delaytime_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]], jsii.get(self, "delaytimeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__38378b8ed46b58573c7c8b3d070bf4d07074b9ecf185a1eeb06dce37a9c5feb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableactivitytype")
    def enableactivitytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableactivitytype"))

    @enableactivitytype.setter
    def enableactivitytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ca4c6ee34091721eacc57f587cbbfe94b02dfb30b9011dd5c0d0cd0a8dc9dba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableactivitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableafteradelay")
    def enableafteradelay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableafteradelay"))

    @enableafteradelay.setter
    def enableafteradelay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__334fb4ec0f7bea817ecc0f551215fc923a1b12fdca6daed20af6c46abf79c8cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableafteradelay", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9de5bc260d1b719193b373404652a056339321704b203823ebbb995ecd918d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__20cc355fef8a5cab05f132c24b97a4e449f2fc758f4063294b7362f97d3bb171)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846006b896dfa48d1e8c44d2b4653bc44b44939ba79266c19f49333465853a74)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79a718ee7c493f26402b5fb441c05c3894ee01fa22843c28940772196459bf13)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adb7232ddc63064bea2e906f190a8b82d403d4b169c7e9c56041e19491c3a907)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20fc971336091521d4f39e0caa08ca009264eda56f7fafa81a21604b47054e80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrol]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrol]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrol]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ecebd237bb25a11a9cc113f68bbd2eecc5f7ccf96e4c378c00a1506281c0b8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__86cd21d206930e2254314ef440e45598e884f7228a66e02147b0b55eca7595b4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackupactivitycontroloptions")
    def put_backupactivitycontroloptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3d12978f1e5ef1381ad6a441c57491b6113b650c3e90997ce700f820d52500)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackupactivitycontroloptions", [value]))

    @jsii.member(jsii_name="putRestoreactivitycontroloptions")
    def put_restoreactivitycontroloptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolRestoreactivitycontroloptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c43c62bec18b53784899d1405dd1155234ef135ad815331fd44eb33607dd54e2)
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
    ) -> HypervisorAzureActivitycontrolBackupactivitycontroloptionsList:
        return typing.cast(HypervisorAzureActivitycontrolBackupactivitycontroloptionsList, jsii.get(self, "backupactivitycontroloptions"))

    @builtins.property
    @jsii.member(jsii_name="restoreactivitycontroloptions")
    def restoreactivitycontroloptions(
        self,
    ) -> "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsList":
        return typing.cast("HypervisorAzureActivitycontrolRestoreactivitycontroloptionsList", jsii.get(self, "restoreactivitycontroloptions"))

    @builtins.property
    @jsii.member(jsii_name="backupactivitycontroloptionsInput")
    def backupactivitycontroloptions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptions]]], jsii.get(self, "backupactivitycontroloptionsInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptions"]]], jsii.get(self, "restoreactivitycontroloptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackup")
    def enablebackup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablebackup"))

    @enablebackup.setter
    def enablebackup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e85f6addbfbb0d4c0e784ee19454c5951a7aac442b85eb6f974084a3404b56b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackup", value)

    @builtins.property
    @jsii.member(jsii_name="enablerestore")
    def enablerestore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablerestore"))

    @enablerestore.setter
    def enablerestore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f3ecb5bde9ed26a020112f7415a408902c334bf60f7f7bc2c2a8dbf538bbf8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablerestore", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrol]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrol]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrol]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a88821b1cc841ab4cd1c20d0b6c0a50765bdeeefa8a898ebe2e54c37c45ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptions",
    jsii_struct_bases=[],
    name_mapping={
        "activitytype": "activitytype",
        "delaytime": "delaytime",
        "enableactivitytype": "enableactivitytype",
        "enableafteradelay": "enableafteradelay",
    },
)
class HypervisorAzureActivitycontrolRestoreactivitycontroloptions:
    def __init__(
        self,
        *,
        activitytype: typing.Optional[builtins.str] = None,
        delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enableactivitytype: typing.Optional[builtins.str] = None,
        enableafteradelay: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param activitytype: denotes the activity type being considered [BACKUP, RESTORE, ONLINECI, ARCHIVEPRUNE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitytype HypervisorAzure#activitytype}
        :param delaytime: delaytime block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#delaytime HypervisorAzure#delaytime}
        :param enableactivitytype: True if the activity type is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableactivitytype HypervisorAzure#enableactivitytype}
        :param enableafteradelay: True if the activity will be enabled after a delay time interval. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableafteradelay HypervisorAzure#enableafteradelay}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac1ef34f65e0463d94483d30b489fd88677ca58055be062c2c1eeb5a225f0e2)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitytype HypervisorAzure#activitytype}
        '''
        result = self._values.get("activitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delaytime(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime"]]]:
        '''delaytime block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#delaytime HypervisorAzure#delaytime}
        '''
        result = self._values.get("delaytime")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime"]]], result)

    @builtins.property
    def enableactivitytype(self) -> typing.Optional[builtins.str]:
        '''True if the activity type is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableactivitytype HypervisorAzure#enableactivitytype}
        '''
        result = self._values.get("enableactivitytype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enableafteradelay(self) -> typing.Optional[builtins.str]:
        '''True if the activity will be enabled after a delay time interval.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enableafteradelay HypervisorAzure#enableafteradelay}
        '''
        result = self._values.get("enableafteradelay")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrolRestoreactivitycontroloptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime",
    jsii_struct_bases=[],
    name_mapping={"time": "time", "timezone": "timezone", "value": "value"},
)
class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime:
    def __init__(
        self,
        *,
        time: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param time: delay time in unix timestamp. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#time HypervisorAzure#time}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#timezone HypervisorAzure#timezone}
        :param value: actual delay time value in string format according to the timezone. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#value HypervisorAzure#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c7e04cd96f91dd9ab48fd1855e10e288d7ab483ecd5b5dad6a1719171834dfb)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#time HypervisorAzure#time}
        '''
        result = self._values.get("time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#timezone HypervisorAzure#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''actual delay time value in string format according to the timezone.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#value HypervisorAzure#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb0f7965b7ef01d2a6e18f9468555e3fa0f7e4315e5dbda5ec9f19a000835d68)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be629157b35613f44d3b50a7ebb73a806ea3fb4205ee7e76f23e3b018df37b54)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ab84980c82bf1d4eb9a5532ce4f02c44ee9ef26c23e9adc276f8d97bbc1ffe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0617c0ba066b101209fd83b740f1860da8a11ead627b5602526cc50fa251455b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7de86527be857d0f0edebef75b5b850396dfed3cd2ea334d014493a461584f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06870c7965b6bc8c0fa77d1029ccdd0e2764e4505da90661fd25fdf521f43a5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__655e99cb37e692428bcee0f74efcbd33ad4c5e85eaa4478bcac7ec4ed30de506)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__711375de0edb7566c4d0498731a7dd267b11815ba27ffa0bdf97f21213f05f1e)
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
    ) -> "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList":
        return typing.cast("HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone"]]], jsii.get(self, "timezoneInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__645104a8dad5ffbac4ef1273f1ba12c6c76f72c816d4337dd7f7b0481f9b7430)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01f831f4736c147806c9d935119f036a791352e34d71d005581086c81cdc6a99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c1881561308b5a45a1712698c5cb761dcb7cd5d49fa9ce6e249caa1b3091c9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94399e25e378bcfe11e2d1b078e665de3cc1e3ffbc1846e376b6a7adb55db64e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__04b257a763d6ecb8f64b0cb99b583a8893f57a20295759adc83cb731bd15e908)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdb8faf40fa42dc893d8f1d866f370004483b1fda4e831f934eb738870877b80)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b38f226485722910705681154202dfe37c6e27bbc3f1f414272e91a6e3ae8e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d24ffd615427b5bc3fca6dbbcae928f69b2735a42466028adda2d2981f38767c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b86c1d3c6210a3ceb3bad3c6f9071e104ebca16c03c9239426c78e87e0e07d66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6b8b2d1fef5757a03a51f0eae37ac5c13228cce48486f0ff4609ab0ca6f2f84)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b15d4a10edd3b495093d7f548d2a65f52a7ee283602fcb87752c7646b5e0c219)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7b8a2e377f7605edb0f7cda64a880e79c3112fa01151b5fe49aed2ae970210e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06baf72c0d80b7b2b56ecb4e1a6c4ddc617afa620983c9a6b641d0a7794c6cbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d1d1f0560acb23ef0c4b512893b19f6111ae117b74cbb3c78ff03c3f8ce853d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__69e3fd19bc58c2675a244c8671c3301b758e89b1f8e05505d7d3d44a26c55d9c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__714eefffe289378dc8db459c6abc7b9dcc86dff1b417d2622fb86455c02113d1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureActivitycontrolRestoreactivitycontroloptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a49080121c182263b3eaa9f38f10e2276cf3fa76cf4530079a66659ab7358a4f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ff59a350bf6913cf3e6805bbe28c8f6e3a811ad272d028d77bcbff90d8a4255)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a82dd47ae9f9f395291bc958766d8e226665612d30924abcd3cc1d305c78bfae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61e25bde1d4c9d371e8d1db6f1017fc4671b62ef25523bb5807035b09be232e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureActivitycontrolRestoreactivitycontroloptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureActivitycontrolRestoreactivitycontroloptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__780537017ebde6c4ac8579310bd21fd26c2ac3647778378ea802f6ca9f652596)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDelaytime")
    def put_delaytime(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c692719205d14c2510b49a84c4b152d4ea288bca88990158a4a5d47676b60f0b)
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
    ) -> HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeList:
        return typing.cast(HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeList, jsii.get(self, "delaytime"))

    @builtins.property
    @jsii.member(jsii_name="activitytypeInput")
    def activitytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activitytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="delaytimeInput")
    def delaytime_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]], jsii.get(self, "delaytimeInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__33a3005d101cac693c9d465d65e7bd0cd3d979f6147d9bed32beb4ce0cdb8a75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableactivitytype")
    def enableactivitytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableactivitytype"))

    @enableactivitytype.setter
    def enableactivitytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26648c0b36592bfe4d52afaa4742a284a6202e95741820c5feca9e0b71d7fe21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableactivitytype", value)

    @builtins.property
    @jsii.member(jsii_name="enableafteradelay")
    def enableafteradelay(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableafteradelay"))

    @enableafteradelay.setter
    def enableafteradelay(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f51bb169f57aa7a6ddf624484d9f258ec10d3ceffccffcfdf3b178d7184b55d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableafteradelay", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8fa79bc613cab9c48484be252f18fbc7e49e4bbfcd244691c2dc786e41236df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureConfig",
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
        "subscriptionid": "subscriptionid",
        "tenantid": "tenantid",
        "accessnodes": "accessnodes",
        "activitycontrol": "activitycontrol",
        "applicationid": "applicationid",
        "applicationpassword": "applicationpassword",
        "credentials": "credentials",
        "displayname": "displayname",
        "etcdprotection": "etcdprotection",
        "fbrunixmediaagent": "fbrunixmediaagent",
        "hypervisortype": "hypervisortype",
        "id": "id",
        "password": "password",
        "security": "security",
        "servername": "servername",
        "settings": "settings",
        "skipcredentialvalidation": "skipcredentialvalidation",
        "usemanagedidentity": "usemanagedidentity",
        "username": "username",
        "workloadregion": "workloadregion",
    },
)
class HypervisorAzureConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        subscriptionid: builtins.str,
        tenantid: builtins.str,
        accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
        applicationid: typing.Optional[builtins.str] = None,
        applicationpassword: typing.Optional[builtins.str] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureCredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        displayname: typing.Optional[builtins.str] = None,
        etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureEtcdprotection", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureFbrunixmediaagent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        hypervisortype: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSecurity", typing.Dict[builtins.str, typing.Any]]]]] = None,
        servername: typing.Optional[builtins.str] = None,
        settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        skipcredentialvalidation: typing.Optional[builtins.str] = None,
        usemanagedidentity: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        workloadregion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureWorkloadregion", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the hypervisor group being created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        :param subscriptionid: subscription id of Azure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#subscriptionid HypervisorAzure#subscriptionid}
        :param tenantid: Tenant id of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#tenantid HypervisorAzure#tenantid}
        :param accessnodes: accessnodes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#accessnodes HypervisorAzure#accessnodes}
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitycontrol HypervisorAzure#activitycontrol}
        :param applicationid: Application id of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationid HypervisorAzure#applicationid}
        :param applicationpassword: Application Password of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationpassword HypervisorAzure#applicationpassword}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#credentials HypervisorAzure#credentials}
        :param displayname: The name of the hypervisor that has to be changed. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#displayname HypervisorAzure#displayname}
        :param etcdprotection: etcdprotection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#etcdprotection HypervisorAzure#etcdprotection}
        :param fbrunixmediaagent: fbrunixmediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#fbrunixmediaagent HypervisorAzure#fbrunixmediaagent}
        :param hypervisortype: [Azure_V2]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#hypervisortype HypervisorAzure#hypervisortype}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Application Password of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        :param security: security block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#security HypervisorAzure#security}
        :param servername: Client Name to Update. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#servername HypervisorAzure#servername}
        :param settings: settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#settings HypervisorAzure#settings}
        :param skipcredentialvalidation: if credential validation has to be skipped. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#skipcredentialvalidation HypervisorAzure#skipcredentialvalidation}
        :param usemanagedidentity: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#usemanagedidentity HypervisorAzure#usemanagedidentity}.
        :param username: Application id of Azure login Application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#username HypervisorAzure#username}
        :param workloadregion: workloadregion block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#workloadregion HypervisorAzure#workloadregion}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d96bab74861774e2a9a9d3c7a8fc7fdc4cc7a0d3ea55bcfd9e5c6e31eb3c4c16)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subscriptionid", value=subscriptionid, expected_type=type_hints["subscriptionid"])
            check_type(argname="argument tenantid", value=tenantid, expected_type=type_hints["tenantid"])
            check_type(argname="argument accessnodes", value=accessnodes, expected_type=type_hints["accessnodes"])
            check_type(argname="argument activitycontrol", value=activitycontrol, expected_type=type_hints["activitycontrol"])
            check_type(argname="argument applicationid", value=applicationid, expected_type=type_hints["applicationid"])
            check_type(argname="argument applicationpassword", value=applicationpassword, expected_type=type_hints["applicationpassword"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument displayname", value=displayname, expected_type=type_hints["displayname"])
            check_type(argname="argument etcdprotection", value=etcdprotection, expected_type=type_hints["etcdprotection"])
            check_type(argname="argument fbrunixmediaagent", value=fbrunixmediaagent, expected_type=type_hints["fbrunixmediaagent"])
            check_type(argname="argument hypervisortype", value=hypervisortype, expected_type=type_hints["hypervisortype"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument security", value=security, expected_type=type_hints["security"])
            check_type(argname="argument servername", value=servername, expected_type=type_hints["servername"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument skipcredentialvalidation", value=skipcredentialvalidation, expected_type=type_hints["skipcredentialvalidation"])
            check_type(argname="argument usemanagedidentity", value=usemanagedidentity, expected_type=type_hints["usemanagedidentity"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument workloadregion", value=workloadregion, expected_type=type_hints["workloadregion"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "subscriptionid": subscriptionid,
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
        if accessnodes is not None:
            self._values["accessnodes"] = accessnodes
        if activitycontrol is not None:
            self._values["activitycontrol"] = activitycontrol
        if applicationid is not None:
            self._values["applicationid"] = applicationid
        if applicationpassword is not None:
            self._values["applicationpassword"] = applicationpassword
        if credentials is not None:
            self._values["credentials"] = credentials
        if displayname is not None:
            self._values["displayname"] = displayname
        if etcdprotection is not None:
            self._values["etcdprotection"] = etcdprotection
        if fbrunixmediaagent is not None:
            self._values["fbrunixmediaagent"] = fbrunixmediaagent
        if hypervisortype is not None:
            self._values["hypervisortype"] = hypervisortype
        if id is not None:
            self._values["id"] = id
        if password is not None:
            self._values["password"] = password
        if security is not None:
            self._values["security"] = security
        if servername is not None:
            self._values["servername"] = servername
        if settings is not None:
            self._values["settings"] = settings
        if skipcredentialvalidation is not None:
            self._values["skipcredentialvalidation"] = skipcredentialvalidation
        if usemanagedidentity is not None:
            self._values["usemanagedidentity"] = usemanagedidentity
        if username is not None:
            self._values["username"] = username
        if workloadregion is not None:
            self._values["workloadregion"] = workloadregion

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
        '''The name of the hypervisor group being created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscriptionid(self) -> builtins.str:
        '''subscription id of Azure.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#subscriptionid HypervisorAzure#subscriptionid}
        '''
        result = self._values.get("subscriptionid")
        assert result is not None, "Required property 'subscriptionid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenantid(self) -> builtins.str:
        '''Tenant id of Azure login Application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#tenantid HypervisorAzure#tenantid}
        '''
        result = self._values.get("tenantid")
        assert result is not None, "Required property 'tenantid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accessnodes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureAccessnodes]]]:
        '''accessnodes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#accessnodes HypervisorAzure#accessnodes}
        '''
        result = self._values.get("accessnodes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureAccessnodes]]], result)

    @builtins.property
    def activitycontrol(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrol]]]:
        '''activitycontrol block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#activitycontrol HypervisorAzure#activitycontrol}
        '''
        result = self._values.get("activitycontrol")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrol]]], result)

    @builtins.property
    def applicationid(self) -> typing.Optional[builtins.str]:
        '''Application id of Azure login Application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationid HypervisorAzure#applicationid}
        '''
        result = self._values.get("applicationid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def applicationpassword(self) -> typing.Optional[builtins.str]:
        '''Application Password of Azure login Application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationpassword HypervisorAzure#applicationpassword}
        '''
        result = self._values.get("applicationpassword")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureCredentials"]]]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#credentials HypervisorAzure#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureCredentials"]]], result)

    @builtins.property
    def displayname(self) -> typing.Optional[builtins.str]:
        '''The name of the hypervisor that has to be changed.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#displayname HypervisorAzure#displayname}
        '''
        result = self._values.get("displayname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def etcdprotection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotection"]]]:
        '''etcdprotection block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#etcdprotection HypervisorAzure#etcdprotection}
        '''
        result = self._values.get("etcdprotection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotection"]]], result)

    @builtins.property
    def fbrunixmediaagent(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureFbrunixmediaagent"]]]:
        '''fbrunixmediaagent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#fbrunixmediaagent HypervisorAzure#fbrunixmediaagent}
        '''
        result = self._values.get("fbrunixmediaagent")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureFbrunixmediaagent"]]], result)

    @builtins.property
    def hypervisortype(self) -> typing.Optional[builtins.str]:
        '''[Azure_V2].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#hypervisortype HypervisorAzure#hypervisortype}
        '''
        result = self._values.get("hypervisortype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Application Password of Azure login Application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSecurity"]]]:
        '''security block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#security HypervisorAzure#security}
        '''
        result = self._values.get("security")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSecurity"]]], result)

    @builtins.property
    def servername(self) -> typing.Optional[builtins.str]:
        '''Client Name to Update.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#servername HypervisorAzure#servername}
        '''
        result = self._values.get("servername")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettings"]]]:
        '''settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#settings HypervisorAzure#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettings"]]], result)

    @builtins.property
    def skipcredentialvalidation(self) -> typing.Optional[builtins.str]:
        '''if credential validation has to be skipped.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#skipcredentialvalidation HypervisorAzure#skipcredentialvalidation}
        '''
        result = self._values.get("skipcredentialvalidation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usemanagedidentity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#usemanagedidentity HypervisorAzure#usemanagedidentity}.'''
        result = self._values.get("usemanagedidentity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Application id of Azure login Application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#username HypervisorAzure#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workloadregion(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureWorkloadregion"]]]:
        '''workloadregion block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#workloadregion HypervisorAzure#workloadregion}
        '''
        result = self._values.get("workloadregion")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureWorkloadregion"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureCredentials",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureCredentials:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97682cbbb7f412a9f9d45cd0a356d6b5a464e301b94c3f4242578023a7c3fb68)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureCredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureCredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureCredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__76dc8dc98318af3b110865b22c0529fffa5be160a8c4bb47e97930896cf27fa1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAzureCredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947a17a678eb26c243f259517f59e43ba4a687bea74c4a128dacdcc25d7e01dd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureCredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0466f2105e9d11ef8296ad9d14fdb3c5b797e931cf3b7181bd9c4085e7cee7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7730999ef1e3082587875f6dadba62f7d169b1d90ad65a7422cb960a0a3cf119)
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
            type_hints = typing.get_type_hints(_typecheckingstub__018a91e9c93a7104e36a921e08dd6e920638469a53470c96b000d279b3369f5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureCredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureCredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureCredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fb0e41e949a60fe6eee4371f675e6372ef28996277aa32e7b0cd9037b72aa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureCredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureCredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4e6781aaaa6a33deb48cec89bafac27400b946f72d2ff70e9f06aa653eb88cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e26cdbf3a95b5bb98e0846d8ebe34d6973949d1121295c56cd4fb2914cb8dca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cea21c6f8751d68e0c4fdf54c964d9573c11aed657b314948476bbfdfa0b5fcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureCredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureCredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureCredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2faf1b60023b3fb7d8be4df91ca1f01b9644ef244c93e72712a53115b026c38f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureEtcdprotection",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "plan": "plan"},
)
class HypervisorAzureEtcdprotection:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureEtcdprotectionPlan", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Denote if etcd protection is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enabled HypervisorAzure#enabled}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#plan HypervisorAzure#plan}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6230f4d19040ee2d925c8bd34273aab87b559a6fe3f1047afac770fce00ab700)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#enabled HypervisorAzure#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotectionPlan"]]]:
        '''plan block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#plan HypervisorAzure#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotectionPlan"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureEtcdprotection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureEtcdprotectionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureEtcdprotectionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__60a235574307518446c937ee59f45652b2481b5de17304a9b98006d10d5ebb8f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAzureEtcdprotectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9484f47811b87b1316b919aa18d148edadbdd1fb722f0e2a5a4401a4bded79cc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureEtcdprotectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca201b1dc59b0c422a135fc320f24aec5ccd7767194c9bdfd882c956bdbbf778)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b503be46c89a7edd4193d934d70e8439b5357218deacaed431831729d62275c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd9738a108c941d50f992614f5cf47cfa42886226d36418e0b3682e3f82c2d04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotection]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6d1b6b03a73680283ec1c282d6d96ddc938aaceab1b393a828a44acbf32b449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureEtcdprotectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureEtcdprotectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__50b41e1192700384b142e814588b5b7466aff051b2de759acd4626eaaad49f7b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureEtcdprotectionPlan", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e1ea25a98504c8703884151c5fdd31d4d717598acd594aded76c597b8a05021)
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
    def plan(self) -> "HypervisorAzureEtcdprotectionPlanList":
        return typing.cast("HypervisorAzureEtcdprotectionPlanList", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotectionPlan"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureEtcdprotectionPlan"]]], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d7095f7daaf7019d469efcf44c89567a5bc5a2a50d257cfa490ec64ddf3d6ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotection]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotection]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotection]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27337dabed68b71583db461495c92ee6f5ca1bd68927da9903687e1861fc66b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureEtcdprotectionPlan",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureEtcdprotectionPlan:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e98d3555388f26bcdf86cbf878b9bfc31e3cbe99be3f425a70bcea465028e31)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureEtcdprotectionPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureEtcdprotectionPlanList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureEtcdprotectionPlanList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__edaed5175e2ae3f5efa88327463e8c64a0938d9ef29a1f693793f6490c17b0f1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureEtcdprotectionPlanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f40cecc1ddc557f7e0bb147924f7513a5364603ced9f84d15ebd39c86f543e1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureEtcdprotectionPlanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7451797525a4bdc9290c93c701c0a4b2a7066f8799c38eb5cdae7868eef3197a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__18717bc631fba72d613e0974eb08fedc7dbc13c9b2a870bdcf476cdfd91e17a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f3280460efaa75a9223f9ca6ae4c54ec90fc805f5e4ba296b51acf7798f900a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotectionPlan]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotectionPlan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotectionPlan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86578fb8b10519eadc39a1925a0cc68cb162835f07e62460aa38ed388926e34a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureEtcdprotectionPlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureEtcdprotectionPlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90a1671efd5f17d08703b35d92b923e672f5db4e02136260015f9b4dccdc8899)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea2d889617d24cfacfc739e23a2363224c24cae7adc1c923401422acf609bd48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a01e3d381f1a8056b105285da42894750d0972c8bb846e82f402eaefbc5965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotectionPlan]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotectionPlan]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotectionPlan]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e5327618a06f026741c002a8ecc9f280e4d158c152a7cb70e4b81a0a81a0b85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureFbrunixmediaagent",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureFbrunixmediaagent:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1c94379b0c68c401293908d304704679aa6abba31b24105a06b38a1eb5980be)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureFbrunixmediaagent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureFbrunixmediaagentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureFbrunixmediaagentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc113b6a8f48e40d4f0bca7eaeb6c2c52e4c2eba5efa09417b3264a779888498)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureFbrunixmediaagentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4feab051444d9caa8801d1974ea808288079c6c2fd7da46e78dbf864584e049)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureFbrunixmediaagentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__135c7559a98cf85d23279584f21aa188daa312573c3629936e37bcf951b61858)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfc328fe7c5eeca13e5f840b1b0b366a2b689c58301435d6aafa8bbb4f90f5fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cee77cbaaa2659b8d9fb0bf2ad5bcc45bb22ae4b82aa3750cf03513565ab2e6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureFbrunixmediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureFbrunixmediaagent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureFbrunixmediaagent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8412178e40ae64f48f9bb0ca08c650a7ce27638b24d4da1d331b9e6dcaec5ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureFbrunixmediaagentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureFbrunixmediaagentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1a1c3ef478f076174525b3eff6987307df8d83324622e72c6cd5816b42a88a4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eeb890fe91055090624e9e58d5fac11850fc7c97e650f58c75e0526db0ee2c12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577ac4012f2f7f3fcab48814dd49e984ccc82968ae564542baf79c7e107ce152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureFbrunixmediaagent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureFbrunixmediaagent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureFbrunixmediaagent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eef18def4270dfe2656766a3f61b34fa4e8941ee3e4ca26be2723ec54858cb05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSecurity",
    jsii_struct_bases=[],
    name_mapping={
        "associatedusergroups": "associatedusergroups",
        "clientowners": "clientowners",
    },
)
class HypervisorAzureSecurity:
    def __init__(
        self,
        *,
        associatedusergroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSecurityAssociatedusergroups", typing.Dict[builtins.str, typing.Any]]]]] = None,
        clientowners: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param associatedusergroups: associatedusergroups block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#associatedusergroups HypervisorAzure#associatedusergroups}
        :param clientowners: Client owners for the Hypervisor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#clientowners HypervisorAzure#clientowners}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d750ac73d345fb400855197e2721e154a18814849d0182b6576f2b290123d05b)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSecurityAssociatedusergroups"]]]:
        '''associatedusergroups block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#associatedusergroups HypervisorAzure#associatedusergroups}
        '''
        result = self._values.get("associatedusergroups")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSecurityAssociatedusergroups"]]], result)

    @builtins.property
    def clientowners(self) -> typing.Optional[builtins.str]:
        '''Client owners for the Hypervisor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#clientowners HypervisorAzure#clientowners}
        '''
        result = self._values.get("clientowners")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSecurity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSecurityAssociatedusergroups",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class HypervisorAzureSecurityAssociatedusergroups:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4eed237b3b971378dc8003f14a00a787e484fd5d214e48e24ae9528dc4c82d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

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
        return "HypervisorAzureSecurityAssociatedusergroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSecurityAssociatedusergroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSecurityAssociatedusergroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__304d583bd41fed490a5bd7b536514273dd0044677ea9d7ead1f09627f6a9c069)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSecurityAssociatedusergroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6af154f08d33b041691876e2b55feebcb4c99973a69e7ab31ee47773e136cf1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSecurityAssociatedusergroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c876b02df52e03b0d5122da662c221b0dd782cd27dc354fdda9d8927c8741f0e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b872629e3520e60005bc2441d9ab0494772e9d041265e153bc9154c94ab4ee5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af9ff405dd30416b6aa7810b4f8a62a210eefef00f9e52f7b959f7a924bae16e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurityAssociatedusergroups]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurityAssociatedusergroups]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurityAssociatedusergroups]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc56d6a68142abbaeb1f74381d7824a62a5215761a25599389be28a307f50ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSecurityAssociatedusergroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSecurityAssociatedusergroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ecf1af7f8ee0d79a79fdd5b421dfa3a6045beaf203ef48345a3e27d8ed6da27a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e0c2f03efa639b52f1ce1c106d3b8721d2e627565eafc0b2239f9e5a6267ccd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurityAssociatedusergroups]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurityAssociatedusergroups]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurityAssociatedusergroups]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c54fa97d790f6a76edd317a2f8ed39d2cb877a933f704159a0fd6af08c953fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSecurityList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSecurityList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__44d75682d124df0fa794c4b6b503ae20483584e00c69434ad6cba43e60915b86)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAzureSecurityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf833b800e328494b134af5746226bfee7774c51711de6894eba35919397471)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSecurityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a31f8f2c7619c53e5d5209edea41e184ac81fbebb37e6db5632732c1dc079e7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29f389a91fc42dd4994b2c9a911caefe75f0c04d7cd659289e0e35d170abb94a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e963a1d4688c72b9c3af7b34c47017ccf7587386ee59283211bc92d9f669dbf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurity]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurity]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurity]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edf22345f9f9d46b525059464644cc826fd6256d765066ef5c33addaee081ff6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSecurityOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSecurityOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ac4a1de0401a11d41966d10073ccc7985dc3eb31f18666aa13e1100360292eb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAssociatedusergroups")
    def put_associatedusergroups(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSecurityAssociatedusergroups, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfb62e62924d59df243235e121b830d090e39957daeefa01ebddb3933547db94)
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
    def associatedusergroups(self) -> HypervisorAzureSecurityAssociatedusergroupsList:
        return typing.cast(HypervisorAzureSecurityAssociatedusergroupsList, jsii.get(self, "associatedusergroups"))

    @builtins.property
    @jsii.member(jsii_name="associatedusergroupsInput")
    def associatedusergroups_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurityAssociatedusergroups]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurityAssociatedusergroups]]], jsii.get(self, "associatedusergroupsInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__2b7d6e30dc62e438d27d273bb7e599e25a7bb0859598057bebee5691277c675b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientowners", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurity]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurity]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurity]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde10a269ff68152ab6a4e5d2e2803fdd67156db89823904cebbb9bce9fdda80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettings",
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
class HypervisorAzureSettings:
    def __init__(
        self,
        *,
        applicationcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsApplicationcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        customattributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsCustomattributes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        guestcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsGuestcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        metricsmonitoringpolicy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsMetricsmonitoringpolicy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mountaccessnode: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsMountaccessnode", typing.Dict[builtins.str, typing.Any]]]]] = None,
        regioninfo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsRegioninfo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param applicationcredentials: applicationcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationcredentials HypervisorAzure#applicationcredentials}
        :param customattributes: customattributes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#customattributes HypervisorAzure#customattributes}
        :param guestcredentials: guestcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#guestcredentials HypervisorAzure#guestcredentials}
        :param metricsmonitoringpolicy: metricsmonitoringpolicy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#metricsmonitoringpolicy HypervisorAzure#metricsmonitoringpolicy}
        :param mountaccessnode: mountaccessnode block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#mountaccessnode HypervisorAzure#mountaccessnode}
        :param regioninfo: regioninfo block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#regioninfo HypervisorAzure#regioninfo}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#timezone HypervisorAzure#timezone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e600358bf8e940710196eac3204a116aa097f855545c0c1c328b9e0e5592d4d)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsApplicationcredentials"]]]:
        '''applicationcredentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#applicationcredentials HypervisorAzure#applicationcredentials}
        '''
        result = self._values.get("applicationcredentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsApplicationcredentials"]]], result)

    @builtins.property
    def customattributes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsCustomattributes"]]]:
        '''customattributes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#customattributes HypervisorAzure#customattributes}
        '''
        result = self._values.get("customattributes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsCustomattributes"]]], result)

    @builtins.property
    def guestcredentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsGuestcredentials"]]]:
        '''guestcredentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#guestcredentials HypervisorAzure#guestcredentials}
        '''
        result = self._values.get("guestcredentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsGuestcredentials"]]], result)

    @builtins.property
    def metricsmonitoringpolicy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsMetricsmonitoringpolicy"]]]:
        '''metricsmonitoringpolicy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#metricsmonitoringpolicy HypervisorAzure#metricsmonitoringpolicy}
        '''
        result = self._values.get("metricsmonitoringpolicy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsMetricsmonitoringpolicy"]]], result)

    @builtins.property
    def mountaccessnode(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsMountaccessnode"]]]:
        '''mountaccessnode block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#mountaccessnode HypervisorAzure#mountaccessnode}
        '''
        result = self._values.get("mountaccessnode")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsMountaccessnode"]]], result)

    @builtins.property
    def regioninfo(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsRegioninfo"]]]:
        '''regioninfo block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#regioninfo HypervisorAzure#regioninfo}
        '''
        result = self._values.get("regioninfo")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsRegioninfo"]]], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#timezone HypervisorAzure#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsTimezone"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsApplicationcredentials",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "password": "password"},
)
class HypervisorAzureSettingsApplicationcredentials:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: username to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        :param password: password to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fd6d43793a62a3d729eb7905b98ddf484bff056e3404308221bb138b6e9eb9b)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''password to access the network path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsApplicationcredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsApplicationcredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsApplicationcredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__24ffcf362687ca251d2327cbace774f95d1e6e95cbdb9462960258064d66e515)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsApplicationcredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa5c5bc6f6dbbd9b75b491d252ad92a529bb9a2d70f742a1bc07ed2c1bc8e01)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsApplicationcredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b22819480603f5269fc113d759f6d0283015e33be9ef0d2b5efb7e01113e1f73)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1b291088c42ab07ea08028ee9ba33e85f57ae7d775f43ab8d4536b1ce6f78704)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4292a553c13098fc4cc55232a50cdffb7e58faa5de2a294f7fe3dc092c9b68af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsApplicationcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsApplicationcredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsApplicationcredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f9edea2baaf51d8d1f5fcec0b9e1713e06113b1c7f09ab32dfbf3a65f47ef96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsApplicationcredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsApplicationcredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e360a5bb16aa15e7ecfda0c5d5bac237fadc2496270ef35de4330108771d7669)
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
            type_hints = typing.get_type_hints(_typecheckingstub__168fb0cc4bc74af1edac274664c2aefad51c5d9749b7d0af7bc375a899e01672)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ff557dc14441b19b5ff1d3533ab1058f61d13936bc8adbd035fdd71c5214a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsApplicationcredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsApplicationcredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsApplicationcredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2b3ea5addf5398035499ee13ad736cb6f1621a1e6667a706ad15ed0ea11b7cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsCustomattributes",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "value": "value"},
)
class HypervisorAzureSettingsCustomattributes:
    def __init__(
        self,
        *,
        type: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: client custom attribute type . Ex- 3 - For client 8- For clientGroup. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#type HypervisorAzure#type}
        :param value: client/Client Group custom attribute value. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#value HypervisorAzure#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85cc24db2e88bdba19f73b0208d0ba69ab23728520b95c1962fbbcc382360a6)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#type HypervisorAzure#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''client/Client Group custom attribute value.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#value HypervisorAzure#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsCustomattributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsCustomattributesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsCustomattributesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__979f9ff8f8b5c98c6bd9c90b3fd261c7dae1974e6c0c62c60cbbe507516d3b45)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsCustomattributesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c232172ceae7644f7a2573f01405d5455996947b92c492a9751324ea015e7530)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsCustomattributesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a56f1a78ad5e644b58827078dd495498432b88ed76de6472e8c950cb9406c12a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__73bf04f9cce8399428d965e30bca8877d4ea28282c564f94c7e559d37ea229e1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd5ae1a8fe5f4673291025980b01803472d8bf3b3f2fc904ec5b188c268a2b28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsCustomattributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsCustomattributes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsCustomattributes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea24b03b21c52df74834c5ea2a44545aec7e6c55ef418dc96bd1783bc6322f4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsCustomattributesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsCustomattributesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90ee788715aa8f25c7e2a7213e2442fc9777b10319721ba9ad69a1a8c1a61726)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3e83c627294841505cd1b2135e75009f530b1410fa35fa9645b5e179eeece10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e0cd614f58472e88973b35096648bbe642cadaed409fcef3a9ec53fd842858d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsCustomattributes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsCustomattributes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsCustomattributes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3cdd2412e3c054a4decc6c317c10e4f7d60a806331212a5c1b4ce2e3aa6688)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsGuestcredentials",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "password": "password"},
)
class HypervisorAzureSettingsGuestcredentials:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: username to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        :param password: password to access the network path. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3490cc613d76a1ff88c9a99f04c801f633decdb857f125d8fa506d7c21c6c022)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''password to access the network path.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#password HypervisorAzure#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsGuestcredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsGuestcredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsGuestcredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__441a23e116e4f8040aee46af4c422bc6e49e5e12f7b4575549b8c223a5d0bb14)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsGuestcredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e20ac3471a64f2807fafe65903669f69cf72c771df0387fd60dbc6bae8cd6892)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsGuestcredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acd9e0ae6ebaf0101f4da98b657e4995e4ee3271ba71e74b1411780f970114c2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2228c45277224816f439c36e5939d39ea1396d60db96ad0b492be09daf0beb4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bd0d4a46bce93e80d8c6db360376645e6a7714df7f7b7cbf6d79b7bfefd92ead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsGuestcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsGuestcredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsGuestcredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81c63aa75e3bbd7989088a1749c3cb88c4de639ba49191ab681f25285e2455c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsGuestcredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsGuestcredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1cde5a5341b4d0c936291965953307f60f6c46c374a95a21e631d7412c3691d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3e0579595fd77c5d22b6b70ccfd02265da3ae683c495709d58a52c729e3e66aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b4c98a882e8d35e5ca4c63457d08766fea80951865ec203da7aa435819dd50c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsGuestcredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsGuestcredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsGuestcredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__570133f8960ba7c4b4b4a4d206228df9a07f47272568fa31e037bb4671a1fd9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b36b26b2d69cde148d3deb7cc07ff9706fbe0ced68459407f39c78f291501d85)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAzureSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51a7bc6954e1276a38d5b1593e0e31ea602636b24a72c3378e82d64f799ca10b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f530c586f4e6c16f96a81ce393e04769badb98ef7e88ec8e385ed99c147e71a5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__18051641ba0d5dfbec2783cd04ae4dfc2784c4827ce67361c63fe3cc4fc32252)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c93b6719098434292ce0bbd26de6d1461cd62dabcd44928e1799a27f03789e01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f77cd4caa1717caa5dd3b4c0ce5fe38c4031b224d63f02c8393fa07637ef9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsMetricsmonitoringpolicy",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "isenabled": "isenabled", "name": "name"},
)
class HypervisorAzureSettingsMetricsmonitoringpolicy:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        isenabled: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Metrics Moitoring PolicyId. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param isenabled: True if Metrics Monioring policy is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#isenabled HypervisorAzure#isenabled}
        :param name: Metrics Moitoring Policy Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a4db9e810ffa8ec99616fe61eab2f34159efaf5419abf8c5017ccb13147929)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def isenabled(self) -> typing.Optional[builtins.str]:
        '''True if Metrics Monioring policy is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#isenabled HypervisorAzure#isenabled}
        '''
        result = self._values.get("isenabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Metrics Moitoring Policy Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsMetricsmonitoringpolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsMetricsmonitoringpolicyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsMetricsmonitoringpolicyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2424b348428ff1138bbf6415ba4f54b88401c5669dda329a470feadb93ee6713)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsMetricsmonitoringpolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d966d5b70e78802f1360bc4582aa485f3054ba0a7b52be48269af84f5c9eda7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsMetricsmonitoringpolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d806a8e9d8fbff7a4bb2deca75209e97ade95490d4f78aa36b4d1817fa9207)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ec81d6370efd425d7e0f33ebf2429a02007f958a622dce3f5c1ad9f4d1b26da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a775f91b3a958604784e17c93b6f4413edbbca2f52582ac44d5443f41e7269ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMetricsmonitoringpolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMetricsmonitoringpolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMetricsmonitoringpolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8dbe6fdf5a2e4df5546b29309c1d94596951a6f0d7261439ddcc303deeb77fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsMetricsmonitoringpolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsMetricsmonitoringpolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6cddd8c5056386102c6e9752661e6127a725b94420e995a93f6399a7c0d5cf7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34ce0df3698ff5912ebd370a89d6f601d73c7364f7823dbd643fa50af17a2a77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isenabled")
    def isenabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isenabled"))

    @isenabled.setter
    def isenabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b5b66b1b75eaf7ee7cfee0563ee99afa3aacdccd9f20f42bba4bdf2cabf942b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isenabled", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62680c5d891742f4f5a5c93f1c7624c2d6b046d902f6186c751b5e53236c2c51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMetricsmonitoringpolicy]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMetricsmonitoringpolicy]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMetricsmonitoringpolicy]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cb285acdbea80cabff9512d19ba52d2fef93b3b564334d5cbaf7ecb87fe7d06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsMountaccessnode",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureSettingsMountaccessnode:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca24e89b8102007eef8d1caaf09186830eec8a2ecc2b92cb47dc11d6c99d9af4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsMountaccessnode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsMountaccessnodeList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsMountaccessnodeList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a4b940c35a55ba61a7f5853c50eaeafc30fe8f929d920c982665bf5353f68de6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsMountaccessnodeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bb11155b79ddc0d4c0c6a545251c792f28e01dd0f381a2d33c6320185aa7c64)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsMountaccessnodeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76147cda877eaaef1d2343b2dc09788cc884b384a1b771396607b30a4ed5527c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7435adb65f3ed930740677ded789be1a4f526bf282d81f6049f505e526563ab9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57a7342debe04d3c81c8a53f1469bd7e74b1745f23636d5f4f0abb570778e9ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMountaccessnode]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMountaccessnode]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMountaccessnode]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd1cf497009e2f38fa4f4ee5a308fb1ecbb3473b6643a73b49e9236c6ae2f50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsMountaccessnodeOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsMountaccessnodeOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bf1bb32df1585ddd5ee9987a4a1c97d0e519103b9b1c0087fb4ca81f8a616af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a12d806ff92ba6c0db3ee27b581d69b0aa7e52ff1c0fad0a069e4f189bf6c64b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9858e99c52e7171c05279a1367d3fdb0388610f7ded0ac62f5307394633a34d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMountaccessnode]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMountaccessnode]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMountaccessnode]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2203c8146c700a4337f3c82cd26fe9c31116ef9cac64cdbd2c463b403e5c340)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2f66a60f9009ffbad116c8f33644bf82c08dada7e03bc61aa155454966a37e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putApplicationcredentials")
    def put_applicationcredentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsApplicationcredentials, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b88ce14929fd33bd8769371dc055200da734b8515ac89570f7dda54a5a85aab9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplicationcredentials", [value]))

    @jsii.member(jsii_name="putCustomattributes")
    def put_customattributes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsCustomattributes, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a60c4a997a267ce72b5108113a1aff2f4024ed7d2775e318f5ffe613040dee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomattributes", [value]))

    @jsii.member(jsii_name="putGuestcredentials")
    def put_guestcredentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsGuestcredentials, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f23c42d0f58ecc85f9bddd8a18b9601fb5adf13a422c9c6ad396817ab61965)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putGuestcredentials", [value]))

    @jsii.member(jsii_name="putMetricsmonitoringpolicy")
    def put_metricsmonitoringpolicy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsMetricsmonitoringpolicy, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18fb7575df9b1b598f650d634718072478f86c894dee718dec850873a97d8ad4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetricsmonitoringpolicy", [value]))

    @jsii.member(jsii_name="putMountaccessnode")
    def put_mountaccessnode(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsMountaccessnode, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee957ae6b6fecdcaa55d8029b232485ffed243b127fef2709c7bd710419f8b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMountaccessnode", [value]))

    @jsii.member(jsii_name="putRegioninfo")
    def put_regioninfo(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsRegioninfo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8371ddf19189534af0f051c23d28c77980e21f6bfcc329e9bcda15d90654eadb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegioninfo", [value]))

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["HypervisorAzureSettingsTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71776542eb7db62dafbfc891cefe8b6dff9f0d9f0972b9745bb9e359f72c8b10)
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
    def applicationcredentials(
        self,
    ) -> HypervisorAzureSettingsApplicationcredentialsList:
        return typing.cast(HypervisorAzureSettingsApplicationcredentialsList, jsii.get(self, "applicationcredentials"))

    @builtins.property
    @jsii.member(jsii_name="customattributes")
    def customattributes(self) -> HypervisorAzureSettingsCustomattributesList:
        return typing.cast(HypervisorAzureSettingsCustomattributesList, jsii.get(self, "customattributes"))

    @builtins.property
    @jsii.member(jsii_name="guestcredentials")
    def guestcredentials(self) -> HypervisorAzureSettingsGuestcredentialsList:
        return typing.cast(HypervisorAzureSettingsGuestcredentialsList, jsii.get(self, "guestcredentials"))

    @builtins.property
    @jsii.member(jsii_name="metricsmonitoringpolicy")
    def metricsmonitoringpolicy(
        self,
    ) -> HypervisorAzureSettingsMetricsmonitoringpolicyList:
        return typing.cast(HypervisorAzureSettingsMetricsmonitoringpolicyList, jsii.get(self, "metricsmonitoringpolicy"))

    @builtins.property
    @jsii.member(jsii_name="mountaccessnode")
    def mountaccessnode(self) -> HypervisorAzureSettingsMountaccessnodeList:
        return typing.cast(HypervisorAzureSettingsMountaccessnodeList, jsii.get(self, "mountaccessnode"))

    @builtins.property
    @jsii.member(jsii_name="regioninfo")
    def regioninfo(self) -> "HypervisorAzureSettingsRegioninfoList":
        return typing.cast("HypervisorAzureSettingsRegioninfoList", jsii.get(self, "regioninfo"))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> "HypervisorAzureSettingsTimezoneList":
        return typing.cast("HypervisorAzureSettingsTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="applicationcredentialsInput")
    def applicationcredentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsApplicationcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsApplicationcredentials]]], jsii.get(self, "applicationcredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="customattributesInput")
    def customattributes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsCustomattributes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsCustomattributes]]], jsii.get(self, "customattributesInput"))

    @builtins.property
    @jsii.member(jsii_name="guestcredentialsInput")
    def guestcredentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsGuestcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsGuestcredentials]]], jsii.get(self, "guestcredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsmonitoringpolicyInput")
    def metricsmonitoringpolicy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMetricsmonitoringpolicy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMetricsmonitoringpolicy]]], jsii.get(self, "metricsmonitoringpolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="mountaccessnodeInput")
    def mountaccessnode_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMountaccessnode]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMountaccessnode]]], jsii.get(self, "mountaccessnodeInput"))

    @builtins.property
    @jsii.member(jsii_name="regioninfoInput")
    def regioninfo_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsRegioninfo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsRegioninfo"]]], jsii.get(self, "regioninfoInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["HypervisorAzureSettingsTimezone"]]], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deda1fcd680f044182e64bdff13fac93cf1a98c830f9b7ded4c898379e5c4b73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsRegioninfo",
    jsii_struct_bases=[],
    name_mapping={
        "displayname": "displayname",
        "id": "id",
        "latitude": "latitude",
        "longitude": "longitude",
        "name": "name",
    },
)
class HypervisorAzureSettingsRegioninfo:
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
        :param displayname: Display Name of Region. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#displayname HypervisorAzure#displayname}
        :param id: Region Id. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latitude: Geolocation Latitude. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#latitude HypervisorAzure#latitude}
        :param longitude: Geolocation Longitude. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#longitude HypervisorAzure#longitude}
        :param name: Region Name. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1faf9def2d5a1ca878b17053056444bf6c446b70711ed2cb9fd54fef335d9995)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#displayname HypervisorAzure#displayname}
        '''
        result = self._values.get("displayname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Region Id.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def latitude(self) -> typing.Optional[builtins.str]:
        '''Geolocation Latitude.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#latitude HypervisorAzure#latitude}
        '''
        result = self._values.get("latitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def longitude(self) -> typing.Optional[builtins.str]:
        '''Geolocation Longitude.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#longitude HypervisorAzure#longitude}
        '''
        result = self._values.get("longitude")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Region Name.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsRegioninfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsRegioninfoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsRegioninfoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cedd322933ab2618d285fc6c4289cf8be499e6fc7d99f502f0561eae50135be6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsRegioninfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f0cb09bcbfe3c727eb018ef475dc431d9a49cca35ac18403cdd7e76cee5047f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsRegioninfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e273aacabc2332f832761381eaec24310677a59f781ccb3a3d12f3cc0c1cf076)
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
            type_hints = typing.get_type_hints(_typecheckingstub__decb19787f8b44518836f5740ad6712298099776ec181c9c7664e48056393665)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1c9286e72bdea5aed5ee1c79fb8e63116a80a2443e4e040a2a0b497dcf095d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsRegioninfo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsRegioninfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsRegioninfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52c24f604da04bc6df59aed0c133378caa9990b9fa9a329d825767c3e4e75afa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsRegioninfoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsRegioninfoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fd76b3c9bf598913b184481f7556dab0f6628467e5751d1a383b9836761e1901)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1afbfcec7b7ab2ebdfe0e7c95952fe02b1eacea5ec20dde2737b141b9cd8a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fb2f3a9d6afdc03524e449ad5b4e0d9a504d35d9505be5c819ed77cf1354f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="latitude")
    def latitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latitude"))

    @latitude.setter
    def latitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c45fef772190c042bd6538b4a5f04c48a1e09706231ef61547b0a6b8cbfb749f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latitude", value)

    @builtins.property
    @jsii.member(jsii_name="longitude")
    def longitude(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "longitude"))

    @longitude.setter
    def longitude(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f1945134af58c9edd31a465bcc28cb48e004fbf6107181b883e8ab8e87a424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longitude", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802e579d6dbaf45aedd23ea32cdd71948fd7476b5777f2b51ee0f1b23b878683)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsRegioninfo]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsRegioninfo]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsRegioninfo]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21da88b3cf927e28f97e1b231ba755f27990624a54407da85df4b36657f30d8c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureSettingsTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc56d26c8d921f34e524645184ed048325276e84862887f809905576cca7a536)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureSettingsTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureSettingsTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__40d6eaa7bb9b5d33e1e61e8eacb34a14281833e3e28f90ad3d0c54ccc6d687f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HypervisorAzureSettingsTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d4d2f84658651ac20b240bb3723759148bbc165c33a78523d02bb3ce1fe8ef8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureSettingsTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e46c1254950302e164bf527e28035f912677eaade170c784e5276c2f215148c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__111bb5213a66db4df7a9a56d730b9877a109a1847a0cd735b5386ed1bc05e891)
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
            type_hints = typing.get_type_hints(_typecheckingstub__826d3cb8d611077beabca136e018d80dc8c73a678d97fd74ff8bfae46641ebca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c19e37f7b5823d34651e97191e0eca6893ca64cf3576a15d1d64ce63c1b23ed3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureSettingsTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureSettingsTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5fa1cb4317a4821abc61057f642b7030cd0c4596b661803522b7900ad2bdc71f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__550896be95fd390b7b9ccebdba5224c2fc65c30cac30723b8494bfc1457b50f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d65ecac06008d5ef3bfe3a5361bc1bfda97f962ab0bf5278b86bd72ffe2b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b240312589132a99a23228cde918c2da52e66f2706d7a72c63ad4c49618651e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.hypervisorAzure.HypervisorAzureWorkloadregion",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class HypervisorAzureWorkloadregion:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7212adb1c2287fafafc079b01a0b4635c0af21bd7ca3d209687517fc170a65bc)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#id HypervisorAzure#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/hypervisor_azure#name HypervisorAzure#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HypervisorAzureWorkloadregion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HypervisorAzureWorkloadregionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureWorkloadregionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__800c270baaf03b3c90a43eadaff0d198a9cf06fab47ad1dfc383a9089c0deaf5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "HypervisorAzureWorkloadregionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50d84a84f67c42d34daabd00878d28b965289f51abb617da2e076fa5f8931f2b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HypervisorAzureWorkloadregionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9272e8197ec19eae04fdc1581f375c3e5a02bed16d9d551c28aa279aa6990c5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1da6adc5e5b0e65f7db3c0cff6ee9102dde2205c1cbbbefbb802c883186645bd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a508a93fe1022ee758b5b93462fecda38cb9ffdbf6571b92cdc7d043edb946c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureWorkloadregion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureWorkloadregion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureWorkloadregion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee1d9ff4b4004e993d4114457a1263aff74ded14240224cb448f1b9fa9f3ed5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HypervisorAzureWorkloadregionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.hypervisorAzure.HypervisorAzureWorkloadregionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a6ab743f0633d1c25129cd29288f4e9e293bd83dc3a371cf84f8b5ee03642f2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f19339bb5a97f15aba0107446bd0ad468b5cc09510cda321ae3f95bb1d8fab0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28f2f228ec71a36b9862b87a418d0f6bbd0ef23bb33252c58db27c1b1e4737c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureWorkloadregion]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureWorkloadregion]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureWorkloadregion]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f9fe79489a3fe27106bb6b0ab9a83baf019328b1400390076b9f83b3429c54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HypervisorAzure",
    "HypervisorAzureAccessnodes",
    "HypervisorAzureAccessnodesList",
    "HypervisorAzureAccessnodesOutputReference",
    "HypervisorAzureActivitycontrol",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptions",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeList",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeOutputReference",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneList",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezoneOutputReference",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsList",
    "HypervisorAzureActivitycontrolBackupactivitycontroloptionsOutputReference",
    "HypervisorAzureActivitycontrolList",
    "HypervisorAzureActivitycontrolOutputReference",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptions",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeList",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeOutputReference",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneList",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezoneOutputReference",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsList",
    "HypervisorAzureActivitycontrolRestoreactivitycontroloptionsOutputReference",
    "HypervisorAzureConfig",
    "HypervisorAzureCredentials",
    "HypervisorAzureCredentialsList",
    "HypervisorAzureCredentialsOutputReference",
    "HypervisorAzureEtcdprotection",
    "HypervisorAzureEtcdprotectionList",
    "HypervisorAzureEtcdprotectionOutputReference",
    "HypervisorAzureEtcdprotectionPlan",
    "HypervisorAzureEtcdprotectionPlanList",
    "HypervisorAzureEtcdprotectionPlanOutputReference",
    "HypervisorAzureFbrunixmediaagent",
    "HypervisorAzureFbrunixmediaagentList",
    "HypervisorAzureFbrunixmediaagentOutputReference",
    "HypervisorAzureSecurity",
    "HypervisorAzureSecurityAssociatedusergroups",
    "HypervisorAzureSecurityAssociatedusergroupsList",
    "HypervisorAzureSecurityAssociatedusergroupsOutputReference",
    "HypervisorAzureSecurityList",
    "HypervisorAzureSecurityOutputReference",
    "HypervisorAzureSettings",
    "HypervisorAzureSettingsApplicationcredentials",
    "HypervisorAzureSettingsApplicationcredentialsList",
    "HypervisorAzureSettingsApplicationcredentialsOutputReference",
    "HypervisorAzureSettingsCustomattributes",
    "HypervisorAzureSettingsCustomattributesList",
    "HypervisorAzureSettingsCustomattributesOutputReference",
    "HypervisorAzureSettingsGuestcredentials",
    "HypervisorAzureSettingsGuestcredentialsList",
    "HypervisorAzureSettingsGuestcredentialsOutputReference",
    "HypervisorAzureSettingsList",
    "HypervisorAzureSettingsMetricsmonitoringpolicy",
    "HypervisorAzureSettingsMetricsmonitoringpolicyList",
    "HypervisorAzureSettingsMetricsmonitoringpolicyOutputReference",
    "HypervisorAzureSettingsMountaccessnode",
    "HypervisorAzureSettingsMountaccessnodeList",
    "HypervisorAzureSettingsMountaccessnodeOutputReference",
    "HypervisorAzureSettingsOutputReference",
    "HypervisorAzureSettingsRegioninfo",
    "HypervisorAzureSettingsRegioninfoList",
    "HypervisorAzureSettingsRegioninfoOutputReference",
    "HypervisorAzureSettingsTimezone",
    "HypervisorAzureSettingsTimezoneList",
    "HypervisorAzureSettingsTimezoneOutputReference",
    "HypervisorAzureWorkloadregion",
    "HypervisorAzureWorkloadregionList",
    "HypervisorAzureWorkloadregionOutputReference",
]

publication.publish()

def _typecheckingstub__b3481eb1ecf65bdf7575d1535f13c9031e61896855bfd9f3719c08a8f221558d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    subscriptionid: builtins.str,
    tenantid: builtins.str,
    accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    applicationid: typing.Optional[builtins.str] = None,
    applicationpassword: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    displayname: typing.Optional[builtins.str] = None,
    etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureEtcdprotection, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureFbrunixmediaagent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hypervisortype: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    servername: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skipcredentialvalidation: typing.Optional[builtins.str] = None,
    usemanagedidentity: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
    workloadregion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureWorkloadregion, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__f41d5e0da942d91dac227208f19a60ee2d2de3e3a89b1f9acbc67506178f467d(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1e98bc81e62b5a1fac87cc55916e07acfa3fef77501cf639dd6241304bed7a1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureAccessnodes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a5340c586de1a94d5c91e4d1f146c6de0db28b7f10791b60bb97d99e6d8e986(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrol, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d5bea7d341a7b9aa85572a89fb07e0d3a889611122f3e72f425b13fe9084a53(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureCredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4543300df08a3fb044744e19abc2ceec28b9dcf6e66c6fbbf6ab46355e069ee1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureEtcdprotection, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62e41f38538cb9c6ccd9c9363be043b6edce5a1dcf069cf41e082d8df8e5db7f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureFbrunixmediaagent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__664696d879eaa01dddacbe3fe5b84ee277c80f8ce8ac9f15d79d2f19cfd628d0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSecurity, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3eb5ffacec544e98429c47f1d71a9a09bdeab4ebefd7092dd7a2b95893798b1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__787cce75c9628d69871125ffd7b4d9a1bed6989420e6a7e96885f476227fb7e3(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureWorkloadregion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4526ab33118e90ebcaa543f6b1031b009c0d7bcbd7a0165b0f47eeeaa7848183(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabb2931428159c38873bb6dcc39e5dd9964e83e71fbac882ad491fff301c51c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905c013392d92239a807550f6ffa44d40f45395f374776489d70ad9e46dd2cd6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a589449532880f21cc10ea66e62b67d6f89d45a02781d225dd78e1687e4022c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e401586edb7e26fae6afc2e1358f4674546e70760cdda635e3e48e9905693962(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1c0d56e2501bb15323090d4867b1e34b03acbb178c1a02d22d0352b7d0e588(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c85e41daf00b10901d03d382bc0d4014257bcc4d8a6df5294e932ccf8136f751(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd24e129dfe88e7be6281edb4acaec3efb7da1c291a3d2fd077a01551caeaba0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123fd17e219cc0b4656dd9f500bedea6c4ce12eef3b8191619ab14583a1ae456(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d161b4369ccf695cee5225087370a2b74cc175f3353be0d6273b9b1ac0e32ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225a6253d7ed90d702e70e2b01663c09d7072084a674dc799752a156f9367fe3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2265727007d857a211810f44092505ead749d5314465aad911a9e905eb859618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d561310f9ce1d4f0e9458b194a931d66cdb56c2e04ea7c405b8cf31ecb009d28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7419c61850434fc1fcfd530009b3b362465ec595bc0bce6c916ed4df2b3301ea(
    *,
    id: typing.Optional[jsii.Number] = None,
    type: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57affcaac0606e0041684388295fc34c5ed0a6516589dee1e8362681bd138dc1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0e7eaa0008655531d76c7cf0df3fceaa2f4eadacf4dc8e49b7c0a84dff99731(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bea2e11d7361a965c6a640b6283e6feddeb71ea042e37c0323be9b24d649595(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a99a709a541e96859b46276db9c8d01e4266fbf02ee2db34b60c889253963fc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__110e193cc16bf72c3077b56b4cacca20e5eada215542ebfd9e1aa940d7b407d0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0958a0b9a5a8d9a3a72abe170f935dd1046ed22a89df41f54c3ce29811080460(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureAccessnodes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ec1abb7d117ba17ddbd545b3dbe5ab83217f58251eec5b186e2ce01a58d999(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4798f07cf92fe4cbad4f063d5f2d1ede327647f65cf23f6cc314edd5d53506cf(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b6ecfe1fea5c96d4dc09cdf7f29ecba153dee63bcce0353ec515bb3ce56bbb0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4365db920387aada43e4e3dfed4928829f987b9dc534a9652a4feea674201107(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureAccessnodes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2590c4685eadab13bc258028cfc98499ecfe8cb1c5917def1919753691f50f2(
    *,
    backupactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enablebackup: typing.Optional[builtins.str] = None,
    enablerestore: typing.Optional[builtins.str] = None,
    restoreactivitycontroloptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f29695ddbe2e13079416eed7b8e55b8a84390ec9976a21eef89e61d79951da(
    *,
    activitytype: typing.Optional[builtins.str] = None,
    delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enableactivitytype: typing.Optional[builtins.str] = None,
    enableafteradelay: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91b0d522625f7b2746e8824a45a5a364bff30ec92dff16596a1c1651e0c3fc3f(
    *,
    time: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c9e28487f9680cb2aaef81130c8d729183fe24588fa7c1d9017ccd98523e6b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50003a68046323971b3f8f84e447f3fb0ff09982f8a1655bde0cf5e227cd7f9(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655324293e1266153c10e00a506f3279916e35e73afec1aee604bdc63b809684(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07fe71a8f8f4d5e29b702b6b38d11d163a4015635b8500051f5b2058eaf035d7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6654b8412e1123006f4d883edcbcedc981489f28225e7769811ec564663f366(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb3582b75ee86b6d206d3b47316a97f5afe300c5e5caa656d4e6d0f6cbeaeb9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fecc3d590284a399e18b548488cef52c2ecef5b6417ea086a1531b86ba483ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c4b827c6366d59aba64ddf438752c07fc66f5b35831a7608ab1f038ee15280(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb8c9f94593ceae8f95984ff72fdad0695a883e214028e8e3f9feda6535b418c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc403fe334e4aff9e85c0ca2e5cd5396689ca69b867de33d29e165a53c68ae5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__233ecf73547ebb901a1c66eae9cf99f92a624439e521d5f5117d263bd6de22a3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__187e096926c0988a6570936dd5127fffd4870bb18aecba43cae737ccad627389(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467a6099b015e569f647fd0efb418c55a478a0dbf01877367233b1bd5677c5ed(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ead1f0c2d656da511145de6b931edb2dd030d6751e95c7b7738f60a67202f46(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5342b3b65c74dcdd1055c3fe9171da29a26a1be29dd516240a59582e49d255f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c9157f5fda45cf30311a392c571b3d99094ce3541c34fa502df36f1f53ab28(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff693bb4c7e3b8e393aee68edb86ef99e261149b7275653cf5b805433f1d1ce(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__021c1f081ce8e526559865f9923f65f80926bb62ddc7d76ee49ebbe6053e62d5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0257ab90acdf976eb743aef89514f0917104911bf42737e66ba344ddc678e32(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a94cf74053fa4700a63e7f519d6e29cc3f90e3cc55ff051e80c2519e3077e0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d6941850ac5c219aaf2aa818b761723eafd6df6226d9c4e56d9f1bb884ee11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcd76b13684bb7d74fc7fa7a7486dc6257ea28c9034a6f0a54d34e015d9eb306(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytimeTimezone]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64f78747605cff5eb4f091a41903f0da75ec94a03f53f068e827024deb0e83bf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f794b5015c78409acdc9f54adbf681d2316495f8db6a37933b639e42e14c169(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb9153939048baba37e27828b1a494a6c27c2e4df733c0c5b7fa0d922ef9b5de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf5cb8779d5390c9203dcbb6561cf5d044db5557f4ccd6eb69c4821fd74507b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc619d458f5f027f96e03cb378bced3054e3d0a74e53fff4cc0d0b2221b68ac(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__483e2a8e68e6a0ca9afd5a1616904688bfef99c650df783b01d73837e2b7fd24(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolBackupactivitycontroloptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__295fd9a40c196dde391cbc18a7362b2e14b2bc87f6174a037e40ae0ad69cb9ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f6372e55a60641446146911646d61f5423914e78108df9369abf38a3b65258(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38378b8ed46b58573c7c8b3d070bf4d07074b9ecf185a1eeb06dce37a9c5feb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ca4c6ee34091721eacc57f587cbbfe94b02dfb30b9011dd5c0d0cd0a8dc9dba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__334fb4ec0f7bea817ecc0f551215fc923a1b12fdca6daed20af6c46abf79c8cc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9de5bc260d1b719193b373404652a056339321704b203823ebbb995ecd918d5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolBackupactivitycontroloptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20cc355fef8a5cab05f132c24b97a4e449f2fc758f4063294b7362f97d3bb171(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846006b896dfa48d1e8c44d2b4653bc44b44939ba79266c19f49333465853a74(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79a718ee7c493f26402b5fb441c05c3894ee01fa22843c28940772196459bf13(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb7232ddc63064bea2e906f190a8b82d403d4b169c7e9c56041e19491c3a907(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20fc971336091521d4f39e0caa08ca009264eda56f7fafa81a21604b47054e80(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ecebd237bb25a11a9cc113f68bbd2eecc5f7ccf96e4c378c00a1506281c0b8f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrol]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86cd21d206930e2254314ef440e45598e884f7228a66e02147b0b55eca7595b4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3d12978f1e5ef1381ad6a441c57491b6113b650c3e90997ce700f820d52500(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolBackupactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c43c62bec18b53784899d1405dd1155234ef135ad815331fd44eb33607dd54e2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e85f6addbfbb0d4c0e784ee19454c5951a7aac442b85eb6f974084a3404b56b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f3ecb5bde9ed26a020112f7415a408902c334bf60f7f7bc2c2a8dbf538bbf8f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a88821b1cc841ab4cd1c20d0b6c0a50765bdeeefa8a898ebe2e54c37c45ff1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrol]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac1ef34f65e0463d94483d30b489fd88677ca58055be062c2c1eeb5a225f0e2(
    *,
    activitytype: typing.Optional[builtins.str] = None,
    delaytime: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enableactivitytype: typing.Optional[builtins.str] = None,
    enableafteradelay: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c7e04cd96f91dd9ab48fd1855e10e288d7ab483ecd5b5dad6a1719171834dfb(
    *,
    time: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb0f7965b7ef01d2a6e18f9468555e3fa0f7e4315e5dbda5ec9f19a000835d68(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be629157b35613f44d3b50a7ebb73a806ea3fb4205ee7e76f23e3b018df37b54(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ab84980c82bf1d4eb9a5532ce4f02c44ee9ef26c23e9adc276f8d97bbc1ffe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0617c0ba066b101209fd83b740f1860da8a11ead627b5602526cc50fa251455b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7de86527be857d0f0edebef75b5b850396dfed3cd2ea334d014493a461584f5d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06870c7965b6bc8c0fa77d1029ccdd0e2764e4505da90661fd25fdf521f43a5d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__655e99cb37e692428bcee0f74efcbd33ad4c5e85eaa4478bcac7ec4ed30de506(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__711375de0edb7566c4d0498731a7dd267b11815ba27ffa0bdf97f21213f05f1e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__645104a8dad5ffbac4ef1273f1ba12c6c76f72c816d4337dd7f7b0481f9b7430(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01f831f4736c147806c9d935119f036a791352e34d71d005581086c81cdc6a99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c1881561308b5a45a1712698c5cb761dcb7cd5d49fa9ce6e249caa1b3091c9e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94399e25e378bcfe11e2d1b078e665de3cc1e3ffbc1846e376b6a7adb55db64e(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b257a763d6ecb8f64b0cb99b583a8893f57a20295759adc83cb731bd15e908(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdb8faf40fa42dc893d8f1d866f370004483b1fda4e831f934eb738870877b80(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23b38f226485722910705681154202dfe37c6e27bbc3f1f414272e91a6e3ae8e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24ffd615427b5bc3fca6dbbcae928f69b2735a42466028adda2d2981f38767c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86c1d3c6210a3ceb3bad3c6f9071e104ebca16c03c9239426c78e87e0e07d66(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6b8b2d1fef5757a03a51f0eae37ac5c13228cce48486f0ff4609ab0ca6f2f84(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b15d4a10edd3b495093d7f548d2a65f52a7ee283602fcb87752c7646b5e0c219(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b8a2e377f7605edb0f7cda64a880e79c3112fa01151b5fe49aed2ae970210e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06baf72c0d80b7b2b56ecb4e1a6c4ddc617afa620983c9a6b641d0a7794c6cbd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d1d1f0560acb23ef0c4b512893b19f6111ae117b74cbb3c78ff03c3f8ce853d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytimeTimezone]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e3fd19bc58c2675a244c8671c3301b758e89b1f8e05505d7d3d44a26c55d9c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__714eefffe289378dc8db459c6abc7b9dcc86dff1b417d2622fb86455c02113d1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a49080121c182263b3eaa9f38f10e2276cf3fa76cf4530079a66659ab7358a4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff59a350bf6913cf3e6805bbe28c8f6e3a811ad272d028d77bcbff90d8a4255(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82dd47ae9f9f395291bc958766d8e226665612d30924abcd3cc1d305c78bfae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61e25bde1d4c9d371e8d1db6f1017fc4671b62ef25523bb5807035b09be232e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureActivitycontrolRestoreactivitycontroloptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__780537017ebde6c4ac8579310bd21fd26c2ac3647778378ea802f6ca9f652596(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c692719205d14c2510b49a84c4b152d4ea288bca88990158a4a5d47676b60f0b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrolRestoreactivitycontroloptionsDelaytime, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a3005d101cac693c9d465d65e7bd0cd3d979f6147d9bed32beb4ce0cdb8a75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26648c0b36592bfe4d52afaa4742a284a6202e95741820c5feca9e0b71d7fe21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f51bb169f57aa7a6ddf624484d9f258ec10d3ceffccffcfdf3b178d7184b55d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8fa79bc613cab9c48484be252f18fbc7e49e4bbfcd244691c2dc786e41236df(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureActivitycontrolRestoreactivitycontroloptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d96bab74861774e2a9a9d3c7a8fc7fdc4cc7a0d3ea55bcfd9e5c6e31eb3c4c16(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    subscriptionid: builtins.str,
    tenantid: builtins.str,
    accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    applicationid: typing.Optional[builtins.str] = None,
    applicationpassword: typing.Optional[builtins.str] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureCredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    displayname: typing.Optional[builtins.str] = None,
    etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureEtcdprotection, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fbrunixmediaagent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureFbrunixmediaagent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    hypervisortype: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    security: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSecurity, typing.Dict[builtins.str, typing.Any]]]]] = None,
    servername: typing.Optional[builtins.str] = None,
    settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skipcredentialvalidation: typing.Optional[builtins.str] = None,
    usemanagedidentity: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
    workloadregion: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureWorkloadregion, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97682cbbb7f412a9f9d45cd0a356d6b5a464e301b94c3f4242578023a7c3fb68(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76dc8dc98318af3b110865b22c0529fffa5be160a8c4bb47e97930896cf27fa1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__947a17a678eb26c243f259517f59e43ba4a687bea74c4a128dacdcc25d7e01dd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0466f2105e9d11ef8296ad9d14fdb3c5b797e931cf3b7181bd9c4085e7cee7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7730999ef1e3082587875f6dadba62f7d169b1d90ad65a7422cb960a0a3cf119(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018a91e9c93a7104e36a921e08dd6e920638469a53470c96b000d279b3369f5e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fb0e41e949a60fe6eee4371f675e6372ef28996277aa32e7b0cd9037b72aa8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureCredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e6781aaaa6a33deb48cec89bafac27400b946f72d2ff70e9f06aa653eb88cc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e26cdbf3a95b5bb98e0846d8ebe34d6973949d1121295c56cd4fb2914cb8dca(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cea21c6f8751d68e0c4fdf54c964d9573c11aed657b314948476bbfdfa0b5fcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2faf1b60023b3fb7d8be4df91ca1f01b9644ef244c93e72712a53115b026c38f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureCredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6230f4d19040ee2d925c8bd34273aab87b559a6fe3f1047afac770fce00ab700(
    *,
    enabled: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureEtcdprotectionPlan, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60a235574307518446c937ee59f45652b2481b5de17304a9b98006d10d5ebb8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9484f47811b87b1316b919aa18d148edadbdd1fb722f0e2a5a4401a4bded79cc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca201b1dc59b0c422a135fc320f24aec5ccd7767194c9bdfd882c956bdbbf778(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b503be46c89a7edd4193d934d70e8439b5357218deacaed431831729d62275c4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd9738a108c941d50f992614f5cf47cfa42886226d36418e0b3682e3f82c2d04(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6d1b6b03a73680283ec1c282d6d96ddc938aaceab1b393a828a44acbf32b449(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotection]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b41e1192700384b142e814588b5b7466aff051b2de759acd4626eaaad49f7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e1ea25a98504c8703884151c5fdd31d4d717598acd594aded76c597b8a05021(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureEtcdprotectionPlan, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7095f7daaf7019d469efcf44c89567a5bc5a2a50d257cfa490ec64ddf3d6ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27337dabed68b71583db461495c92ee6f5ca1bd68927da9903687e1861fc66b9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotection]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e98d3555388f26bcdf86cbf878b9bfc31e3cbe99be3f425a70bcea465028e31(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edaed5175e2ae3f5efa88327463e8c64a0938d9ef29a1f693793f6490c17b0f1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f40cecc1ddc557f7e0bb147924f7513a5364603ced9f84d15ebd39c86f543e1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7451797525a4bdc9290c93c701c0a4b2a7066f8799c38eb5cdae7868eef3197a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18717bc631fba72d613e0974eb08fedc7dbc13c9b2a870bdcf476cdfd91e17a5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3280460efaa75a9223f9ca6ae4c54ec90fc805f5e4ba296b51acf7798f900a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86578fb8b10519eadc39a1925a0cc68cb162835f07e62460aa38ed388926e34a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureEtcdprotectionPlan]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90a1671efd5f17d08703b35d92b923e672f5db4e02136260015f9b4dccdc8899(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2d889617d24cfacfc739e23a2363224c24cae7adc1c923401422acf609bd48(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a01e3d381f1a8056b105285da42894750d0972c8bb846e82f402eaefbc5965(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e5327618a06f026741c002a8ecc9f280e4d158c152a7cb70e4b81a0a81a0b85(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureEtcdprotectionPlan]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1c94379b0c68c401293908d304704679aa6abba31b24105a06b38a1eb5980be(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc113b6a8f48e40d4f0bca7eaeb6c2c52e4c2eba5efa09417b3264a779888498(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4feab051444d9caa8801d1974ea808288079c6c2fd7da46e78dbf864584e049(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__135c7559a98cf85d23279584f21aa188daa312573c3629936e37bcf951b61858(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc328fe7c5eeca13e5f840b1b0b366a2b689c58301435d6aafa8bbb4f90f5fe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee77cbaaa2659b8d9fb0bf2ad5bcc45bb22ae4b82aa3750cf03513565ab2e6a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8412178e40ae64f48f9bb0ca08c650a7ce27638b24d4da1d331b9e6dcaec5ff(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureFbrunixmediaagent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a1c3ef478f076174525b3eff6987307df8d83324622e72c6cd5816b42a88a4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeb890fe91055090624e9e58d5fac11850fc7c97e650f58c75e0526db0ee2c12(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577ac4012f2f7f3fcab48814dd49e984ccc82968ae564542baf79c7e107ce152(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eef18def4270dfe2656766a3f61b34fa4e8941ee3e4ca26be2723ec54858cb05(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureFbrunixmediaagent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d750ac73d345fb400855197e2721e154a18814849d0182b6576f2b290123d05b(
    *,
    associatedusergroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSecurityAssociatedusergroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
    clientowners: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4eed237b3b971378dc8003f14a00a787e484fd5d214e48e24ae9528dc4c82d(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__304d583bd41fed490a5bd7b536514273dd0044677ea9d7ead1f09627f6a9c069(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6af154f08d33b041691876e2b55feebcb4c99973a69e7ab31ee47773e136cf1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c876b02df52e03b0d5122da662c221b0dd782cd27dc354fdda9d8927c8741f0e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b872629e3520e60005bc2441d9ab0494772e9d041265e153bc9154c94ab4ee5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af9ff405dd30416b6aa7810b4f8a62a210eefef00f9e52f7b959f7a924bae16e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc56d6a68142abbaeb1f74381d7824a62a5215761a25599389be28a307f50ec2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurityAssociatedusergroups]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecf1af7f8ee0d79a79fdd5b421dfa3a6045beaf203ef48345a3e27d8ed6da27a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c2f03efa639b52f1ce1c106d3b8721d2e627565eafc0b2239f9e5a6267ccd9(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c54fa97d790f6a76edd317a2f8ed39d2cb877a933f704159a0fd6af08c953fb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurityAssociatedusergroups]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44d75682d124df0fa794c4b6b503ae20483584e00c69434ad6cba43e60915b86(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf833b800e328494b134af5746226bfee7774c51711de6894eba35919397471(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a31f8f2c7619c53e5d5209edea41e184ac81fbebb37e6db5632732c1dc079e7b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29f389a91fc42dd4994b2c9a911caefe75f0c04d7cd659289e0e35d170abb94a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e963a1d4688c72b9c3af7b34c47017ccf7587386ee59283211bc92d9f669dbf0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf22345f9f9d46b525059464644cc826fd6256d765066ef5c33addaee081ff6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSecurity]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac4a1de0401a11d41966d10073ccc7985dc3eb31f18666aa13e1100360292eb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfb62e62924d59df243235e121b830d090e39957daeefa01ebddb3933547db94(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSecurityAssociatedusergroups, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b7d6e30dc62e438d27d273bb7e599e25a7bb0859598057bebee5691277c675b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde10a269ff68152ab6a4e5d2e2803fdd67156db89823904cebbb9bce9fdda80(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSecurity]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e600358bf8e940710196eac3204a116aa097f855545c0c1c328b9e0e5592d4d(
    *,
    applicationcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsApplicationcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    customattributes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsCustomattributes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    guestcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsGuestcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    metricsmonitoringpolicy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsMetricsmonitoringpolicy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mountaccessnode: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsMountaccessnode, typing.Dict[builtins.str, typing.Any]]]]] = None,
    regioninfo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsRegioninfo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fd6d43793a62a3d729eb7905b98ddf484bff056e3404308221bb138b6e9eb9b(
    *,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24ffcf362687ca251d2327cbace774f95d1e6e95cbdb9462960258064d66e515(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa5c5bc6f6dbbd9b75b491d252ad92a529bb9a2d70f742a1bc07ed2c1bc8e01(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b22819480603f5269fc113d759f6d0283015e33be9ef0d2b5efb7e01113e1f73(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b291088c42ab07ea08028ee9ba33e85f57ae7d775f43ab8d4536b1ce6f78704(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4292a553c13098fc4cc55232a50cdffb7e58faa5de2a294f7fe3dc092c9b68af(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9edea2baaf51d8d1f5fcec0b9e1713e06113b1c7f09ab32dfbf3a65f47ef96(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsApplicationcredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e360a5bb16aa15e7ecfda0c5d5bac237fadc2496270ef35de4330108771d7669(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__168fb0cc4bc74af1edac274664c2aefad51c5d9749b7d0af7bc375a899e01672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ff557dc14441b19b5ff1d3533ab1058f61d13936bc8adbd035fdd71c5214a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2b3ea5addf5398035499ee13ad736cb6f1621a1e6667a706ad15ed0ea11b7cc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsApplicationcredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85cc24db2e88bdba19f73b0208d0ba69ab23728520b95c1962fbbcc382360a6(
    *,
    type: typing.Optional[jsii.Number] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979f9ff8f8b5c98c6bd9c90b3fd261c7dae1974e6c0c62c60cbbe507516d3b45(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c232172ceae7644f7a2573f01405d5455996947b92c492a9751324ea015e7530(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a56f1a78ad5e644b58827078dd495498432b88ed76de6472e8c950cb9406c12a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73bf04f9cce8399428d965e30bca8877d4ea28282c564f94c7e559d37ea229e1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd5ae1a8fe5f4673291025980b01803472d8bf3b3f2fc904ec5b188c268a2b28(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea24b03b21c52df74834c5ea2a44545aec7e6c55ef418dc96bd1783bc6322f4a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsCustomattributes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90ee788715aa8f25c7e2a7213e2442fc9777b10319721ba9ad69a1a8c1a61726(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3e83c627294841505cd1b2135e75009f530b1410fa35fa9645b5e179eeece10(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e0cd614f58472e88973b35096648bbe642cadaed409fcef3a9ec53fd842858d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3cdd2412e3c054a4decc6c317c10e4f7d60a806331212a5c1b4ce2e3aa6688(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsCustomattributes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3490cc613d76a1ff88c9a99f04c801f633decdb857f125d8fa506d7c21c6c022(
    *,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441a23e116e4f8040aee46af4c422bc6e49e5e12f7b4575549b8c223a5d0bb14(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e20ac3471a64f2807fafe65903669f69cf72c771df0387fd60dbc6bae8cd6892(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acd9e0ae6ebaf0101f4da98b657e4995e4ee3271ba71e74b1411780f970114c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2228c45277224816f439c36e5939d39ea1396d60db96ad0b492be09daf0beb4(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0d4a46bce93e80d8c6db360376645e6a7714df7f7b7cbf6d79b7bfefd92ead(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81c63aa75e3bbd7989088a1749c3cb88c4de639ba49191ab681f25285e2455c3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsGuestcredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1cde5a5341b4d0c936291965953307f60f6c46c374a95a21e631d7412c3691d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0579595fd77c5d22b6b70ccfd02265da3ae683c495709d58a52c729e3e66aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b4c98a882e8d35e5ca4c63457d08766fea80951865ec203da7aa435819dd50c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__570133f8960ba7c4b4b4a4d206228df9a07f47272568fa31e037bb4671a1fd9b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsGuestcredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b36b26b2d69cde148d3deb7cc07ff9706fbe0ced68459407f39c78f291501d85(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51a7bc6954e1276a38d5b1593e0e31ea602636b24a72c3378e82d64f799ca10b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f530c586f4e6c16f96a81ce393e04769badb98ef7e88ec8e385ed99c147e71a5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18051641ba0d5dfbec2783cd04ae4dfc2784c4827ce67361c63fe3cc4fc32252(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93b6719098434292ce0bbd26de6d1461cd62dabcd44928e1799a27f03789e01(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f77cd4caa1717caa5dd3b4c0ce5fe38c4031b224d63f02c8393fa07637ef9a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a4db9e810ffa8ec99616fe61eab2f34159efaf5419abf8c5017ccb13147929(
    *,
    id: typing.Optional[jsii.Number] = None,
    isenabled: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2424b348428ff1138bbf6415ba4f54b88401c5669dda329a470feadb93ee6713(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d966d5b70e78802f1360bc4582aa485f3054ba0a7b52be48269af84f5c9eda7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d806a8e9d8fbff7a4bb2deca75209e97ade95490d4f78aa36b4d1817fa9207(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec81d6370efd425d7e0f33ebf2429a02007f958a622dce3f5c1ad9f4d1b26da(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a775f91b3a958604784e17c93b6f4413edbbca2f52582ac44d5443f41e7269ed(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8dbe6fdf5a2e4df5546b29309c1d94596951a6f0d7261439ddcc303deeb77fd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMetricsmonitoringpolicy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cddd8c5056386102c6e9752661e6127a725b94420e995a93f6399a7c0d5cf7b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34ce0df3698ff5912ebd370a89d6f601d73c7364f7823dbd643fa50af17a2a77(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b5b66b1b75eaf7ee7cfee0563ee99afa3aacdccd9f20f42bba4bdf2cabf942b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62680c5d891742f4f5a5c93f1c7624c2d6b046d902f6186c751b5e53236c2c51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb285acdbea80cabff9512d19ba52d2fef93b3b564334d5cbaf7ecb87fe7d06(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMetricsmonitoringpolicy]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca24e89b8102007eef8d1caaf09186830eec8a2ecc2b92cb47dc11d6c99d9af4(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4b940c35a55ba61a7f5853c50eaeafc30fe8f929d920c982665bf5353f68de6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb11155b79ddc0d4c0c6a545251c792f28e01dd0f381a2d33c6320185aa7c64(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76147cda877eaaef1d2343b2dc09788cc884b384a1b771396607b30a4ed5527c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7435adb65f3ed930740677ded789be1a4f526bf282d81f6049f505e526563ab9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57a7342debe04d3c81c8a53f1469bd7e74b1745f23636d5f4f0abb570778e9ae(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd1cf497009e2f38fa4f4ee5a308fb1ecbb3473b6643a73b49e9236c6ae2f50(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsMountaccessnode]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf1bb32df1585ddd5ee9987a4a1c97d0e519103b9b1c0087fb4ca81f8a616af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a12d806ff92ba6c0db3ee27b581d69b0aa7e52ff1c0fad0a069e4f189bf6c64b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9858e99c52e7171c05279a1367d3fdb0388610f7ded0ac62f5307394633a34d3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2203c8146c700a4337f3c82cd26fe9c31116ef9cac64cdbd2c463b403e5c340(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsMountaccessnode]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f66a60f9009ffbad116c8f33644bf82c08dada7e03bc61aa155454966a37e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88ce14929fd33bd8769371dc055200da734b8515ac89570f7dda54a5a85aab9(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsApplicationcredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a60c4a997a267ce72b5108113a1aff2f4024ed7d2775e318f5ffe613040dee(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsCustomattributes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f23c42d0f58ecc85f9bddd8a18b9601fb5adf13a422c9c6ad396817ab61965(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsGuestcredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18fb7575df9b1b598f650d634718072478f86c894dee718dec850873a97d8ad4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsMetricsmonitoringpolicy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee957ae6b6fecdcaa55d8029b232485ffed243b127fef2709c7bd710419f8b7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsMountaccessnode, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8371ddf19189534af0f051c23d28c77980e21f6bfcc329e9bcda15d90654eadb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsRegioninfo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71776542eb7db62dafbfc891cefe8b6dff9f0d9f0972b9745bb9e359f72c8b10(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[HypervisorAzureSettingsTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deda1fcd680f044182e64bdff13fac93cf1a98c830f9b7ded4c898379e5c4b73(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1faf9def2d5a1ca878b17053056444bf6c446b70711ed2cb9fd54fef335d9995(
    *,
    displayname: typing.Optional[builtins.str] = None,
    id: typing.Optional[jsii.Number] = None,
    latitude: typing.Optional[builtins.str] = None,
    longitude: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cedd322933ab2618d285fc6c4289cf8be499e6fc7d99f502f0561eae50135be6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f0cb09bcbfe3c727eb018ef475dc431d9a49cca35ac18403cdd7e76cee5047f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e273aacabc2332f832761381eaec24310677a59f781ccb3a3d12f3cc0c1cf076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__decb19787f8b44518836f5740ad6712298099776ec181c9c7664e48056393665(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c9286e72bdea5aed5ee1c79fb8e63116a80a2443e4e040a2a0b497dcf095d8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52c24f604da04bc6df59aed0c133378caa9990b9fa9a329d825767c3e4e75afa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsRegioninfo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd76b3c9bf598913b184481f7556dab0f6628467e5751d1a383b9836761e1901(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1afbfcec7b7ab2ebdfe0e7c95952fe02b1eacea5ec20dde2737b141b9cd8a3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb2f3a9d6afdc03524e449ad5b4e0d9a504d35d9505be5c819ed77cf1354f1a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45fef772190c042bd6538b4a5f04c48a1e09706231ef61547b0a6b8cbfb749f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f1945134af58c9edd31a465bcc28cb48e004fbf6107181b883e8ab8e87a424(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802e579d6dbaf45aedd23ea32cdd71948fd7476b5777f2b51ee0f1b23b878683(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21da88b3cf927e28f97e1b231ba755f27990624a54407da85df4b36657f30d8c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsRegioninfo]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc56d26c8d921f34e524645184ed048325276e84862887f809905576cca7a536(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d6eaa7bb9b5d33e1e61e8eacb34a14281833e3e28f90ad3d0c54ccc6d687f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d4d2f84658651ac20b240bb3723759148bbc165c33a78523d02bb3ce1fe8ef8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e46c1254950302e164bf527e28035f912677eaade170c784e5276c2f215148c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__111bb5213a66db4df7a9a56d730b9877a109a1847a0cd735b5386ed1bc05e891(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__826d3cb8d611077beabca136e018d80dc8c73a678d97fd74ff8bfae46641ebca(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c19e37f7b5823d34651e97191e0eca6893ca64cf3576a15d1d64ce63c1b23ed3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureSettingsTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fa1cb4317a4821abc61057f642b7030cd0c4596b661803522b7900ad2bdc71f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550896be95fd390b7b9ccebdba5224c2fc65c30cac30723b8494bfc1457b50f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d65ecac06008d5ef3bfe3a5361bc1bfda97f962ab0bf5278b86bd72ffe2b5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b240312589132a99a23228cde918c2da52e66f2706d7a72c63ad4c49618651e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureSettingsTimezone]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7212adb1c2287fafafc079b01a0b4635c0af21bd7ca3d209687517fc170a65bc(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__800c270baaf03b3c90a43eadaff0d198a9cf06fab47ad1dfc383a9089c0deaf5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50d84a84f67c42d34daabd00878d28b965289f51abb617da2e076fa5f8931f2b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9272e8197ec19eae04fdc1581f375c3e5a02bed16d9d551c28aa279aa6990c5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da6adc5e5b0e65f7db3c0cff6ee9102dde2205c1cbbbefbb802c883186645bd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a508a93fe1022ee758b5b93462fecda38cb9ffdbf6571b92cdc7d043edb946c2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee1d9ff4b4004e993d4114457a1263aff74ded14240224cb448f1b9fa9f3ed5b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[HypervisorAzureWorkloadregion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a6ab743f0633d1c25129cd29288f4e9e293bd83dc3a371cf84f8b5ee03642f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f19339bb5a97f15aba0107446bd0ad468b5cc09510cda321ae3f95bb1d8fab0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28f2f228ec71a36b9862b87a418d0f6bbd0ef23bb33252c58db27c1b1e4737c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f9fe79489a3fe27106bb6b0ab9a83baf019328b1400390076b9f83b3429c54(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, HypervisorAzureWorkloadregion]],
) -> None:
    """Type checking stubs"""
    pass
