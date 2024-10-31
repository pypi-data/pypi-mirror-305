'''
# `commvault_usergroup`

Refer to the Terraform Registry for docs: [`commvault_usergroup`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup).
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


class Usergroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.Usergroup",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup commvault_usergroup}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        allowmultiplecompanymembers: typing.Optional[builtins.str] = None,
        associatedexternalgroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupAssociatedexternalgroups", typing.Dict[builtins.str, typing.Any]]]]] = None,
        azureguid: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        donotinheritrestrictconsoletypes: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.str] = None,
        enablelocalauthentication: typing.Optional[builtins.str] = None,
        enabletwofactorauthentication: typing.Optional[builtins.str] = None,
        enforcefsquota: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        laptopadmins: typing.Optional[builtins.str] = None,
        planoperationtype: typing.Optional[builtins.str] = None,
        quotalimitingb: typing.Optional[jsii.Number] = None,
        restrictconsoletypes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupRestrictconsoletypes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        users: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupUsers", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup commvault_usergroup} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: To create an active directory usergroup, the domain name should be mentioned along with the usergroup name (domainName\\usergroupName) and localUserGroup value must be given. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#name Usergroup#name}
        :param allowmultiplecompanymembers: This property can be used to allow addition of users/groups from child companies. Only applicable for commcell and reseller company group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#allowmultiplecompanymembers Usergroup#allowmultiplecompanymembers}
        :param associatedexternalgroups: associatedexternalgroups block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#associatedexternalgroups Usergroup#associatedexternalgroups}
        :param azureguid: Azure Object ID used to link this user group to Azure AD group and manage group membership of the user during SAML login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#azureguid Usergroup#azureguid}
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#description Usergroup#description}.
        :param donotinheritrestrictconsoletypes: Option to not inherit the RestrictConsoleTypes from the parent. By default the value is false, parent RestrictConsoleTypes will be inherited. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#donotinheritrestrictconsoletypes Usergroup#donotinheritrestrictconsoletypes}
        :param enabled: allows the enabling/disabling of the user group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enabled Usergroup#enabled}
        :param enablelocalauthentication: Allows two-factor authentication to be enabled for the specific types of usergroups. it can be turned on or off based on user preferences. There will be usergroups that will not have this option. [ON, OFF, DISABLED_AT_COMPANY] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enablelocalauthentication Usergroup#enablelocalauthentication}
        :param enabletwofactorauthentication: Allows two-factor authentication to be enabled for the specific types of usergroups. it can be turned on or off based on user preferences. There will be usergroups that will not have this option. [ON, OFF, DISABLED_AT_COMPANY] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enabletwofactorauthentication Usergroup#enabletwofactorauthentication}
        :param enforcefsquota: Used to determine if a backup data limit will be set for the user group being created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enforcefsquota Usergroup#enforcefsquota}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param laptopadmins: When set to true, users in this group cannot activate or be set as server owner. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#laptopadmins Usergroup#laptopadmins}
        :param planoperationtype: determines if an existing user has to be added to the user group or removed from the user group [ADD, DELETE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#planoperationtype Usergroup#planoperationtype}
        :param quotalimitingb: if enforceFSQuota is set to true, the quota limit can be set in GBs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#quotalimitingb Usergroup#quotalimitingb}
        :param restrictconsoletypes: restrictconsoletypes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#restrictconsoletypes Usergroup#restrictconsoletypes}
        :param users: users block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#users Usergroup#users}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda4ee5883acf0fd89c07ed3883aef0038703bd0e29a5b995cf59016660f6eb5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = UsergroupConfig(
            name=name,
            allowmultiplecompanymembers=allowmultiplecompanymembers,
            associatedexternalgroups=associatedexternalgroups,
            azureguid=azureguid,
            description=description,
            donotinheritrestrictconsoletypes=donotinheritrestrictconsoletypes,
            enabled=enabled,
            enablelocalauthentication=enablelocalauthentication,
            enabletwofactorauthentication=enabletwofactorauthentication,
            enforcefsquota=enforcefsquota,
            id=id,
            laptopadmins=laptopadmins,
            planoperationtype=planoperationtype,
            quotalimitingb=quotalimitingb,
            restrictconsoletypes=restrictconsoletypes,
            users=users,
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
        '''Generates CDKTF code for importing a Usergroup resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Usergroup to import.
        :param import_from_id: The id of the existing Usergroup that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Usergroup to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f290e2d37f6249cd60d57c16e7ed9782d7e680daeece1ed6eace32cddf15e7fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAssociatedexternalgroups")
    def put_associatedexternalgroups(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupAssociatedexternalgroups", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6e573b68d7c26b71d25ea6f4ab2b0808236d4f3f1d959c9a6f3dee1c9024ea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAssociatedexternalgroups", [value]))

    @jsii.member(jsii_name="putRestrictconsoletypes")
    def put_restrictconsoletypes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupRestrictconsoletypes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cddaec875117247097058e00f20f4384ac0994719e54131e5b738d7169efc802)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRestrictconsoletypes", [value]))

    @jsii.member(jsii_name="putUsers")
    def put_users(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupUsers", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da405363ef313777450fbb05ff5efb2ea0abb4c65d23a0f085eb2a0a8479223f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUsers", [value]))

    @jsii.member(jsii_name="resetAllowmultiplecompanymembers")
    def reset_allowmultiplecompanymembers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowmultiplecompanymembers", []))

    @jsii.member(jsii_name="resetAssociatedexternalgroups")
    def reset_associatedexternalgroups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatedexternalgroups", []))

    @jsii.member(jsii_name="resetAzureguid")
    def reset_azureguid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureguid", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDonotinheritrestrictconsoletypes")
    def reset_donotinheritrestrictconsoletypes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDonotinheritrestrictconsoletypes", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEnablelocalauthentication")
    def reset_enablelocalauthentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablelocalauthentication", []))

    @jsii.member(jsii_name="resetEnabletwofactorauthentication")
    def reset_enabletwofactorauthentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabletwofactorauthentication", []))

    @jsii.member(jsii_name="resetEnforcefsquota")
    def reset_enforcefsquota(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnforcefsquota", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLaptopadmins")
    def reset_laptopadmins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLaptopadmins", []))

    @jsii.member(jsii_name="resetPlanoperationtype")
    def reset_planoperationtype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlanoperationtype", []))

    @jsii.member(jsii_name="resetQuotalimitingb")
    def reset_quotalimitingb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuotalimitingb", []))

    @jsii.member(jsii_name="resetRestrictconsoletypes")
    def reset_restrictconsoletypes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictconsoletypes", []))

    @jsii.member(jsii_name="resetUsers")
    def reset_users(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsers", []))

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
    @jsii.member(jsii_name="associatedexternalgroups")
    def associatedexternalgroups(self) -> "UsergroupAssociatedexternalgroupsList":
        return typing.cast("UsergroupAssociatedexternalgroupsList", jsii.get(self, "associatedexternalgroups"))

    @builtins.property
    @jsii.member(jsii_name="restrictconsoletypes")
    def restrictconsoletypes(self) -> "UsergroupRestrictconsoletypesList":
        return typing.cast("UsergroupRestrictconsoletypesList", jsii.get(self, "restrictconsoletypes"))

    @builtins.property
    @jsii.member(jsii_name="users")
    def users(self) -> "UsergroupUsersList":
        return typing.cast("UsergroupUsersList", jsii.get(self, "users"))

    @builtins.property
    @jsii.member(jsii_name="allowmultiplecompanymembersInput")
    def allowmultiplecompanymembers_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowmultiplecompanymembersInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedexternalgroupsInput")
    def associatedexternalgroups_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupAssociatedexternalgroups"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupAssociatedexternalgroups"]]], jsii.get(self, "associatedexternalgroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="azureguidInput")
    def azureguid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureguidInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="donotinheritrestrictconsoletypesInput")
    def donotinheritrestrictconsoletypes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "donotinheritrestrictconsoletypesInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enablelocalauthenticationInput")
    def enablelocalauthentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablelocalauthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="enabletwofactorauthenticationInput")
    def enabletwofactorauthentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabletwofactorauthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="enforcefsquotaInput")
    def enforcefsquota_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enforcefsquotaInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="laptopadminsInput")
    def laptopadmins_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "laptopadminsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="planoperationtypeInput")
    def planoperationtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "planoperationtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="quotalimitingbInput")
    def quotalimitingb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "quotalimitingbInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictconsoletypesInput")
    def restrictconsoletypes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupRestrictconsoletypes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupRestrictconsoletypes"]]], jsii.get(self, "restrictconsoletypesInput"))

    @builtins.property
    @jsii.member(jsii_name="usersInput")
    def users_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupUsers"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupUsers"]]], jsii.get(self, "usersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowmultiplecompanymembers")
    def allowmultiplecompanymembers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowmultiplecompanymembers"))

    @allowmultiplecompanymembers.setter
    def allowmultiplecompanymembers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92ce486d8c4693105ba7f66cfe206a5ea64133b79c02e77601f6fcab6017752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowmultiplecompanymembers", value)

    @builtins.property
    @jsii.member(jsii_name="azureguid")
    def azureguid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureguid"))

    @azureguid.setter
    def azureguid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7d4c8e2af11770ace6ce66c036f5ad4187f41c706fa3d7060eed0a7952624d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureguid", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ad17db0a7332b13032a0508c1ee755a94dbe724ccfbd9bc0a3a7b4a8e00ff82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="donotinheritrestrictconsoletypes")
    def donotinheritrestrictconsoletypes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "donotinheritrestrictconsoletypes"))

    @donotinheritrestrictconsoletypes.setter
    def donotinheritrestrictconsoletypes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f029d5147e8bb2f373b99e538ad306f178970d106ceed71e308ff28169e59d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "donotinheritrestrictconsoletypes", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bea2707c4b4978e2a42d17321556d036cf5fad83bf18a878c7167b39d18bcf11)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="enablelocalauthentication")
    def enablelocalauthentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablelocalauthentication"))

    @enablelocalauthentication.setter
    def enablelocalauthentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__748681ca6b06f71c7ac9154966dc55bcb7080ecc608e693030ac4678b1e5f208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablelocalauthentication", value)

    @builtins.property
    @jsii.member(jsii_name="enabletwofactorauthentication")
    def enabletwofactorauthentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabletwofactorauthentication"))

    @enabletwofactorauthentication.setter
    def enabletwofactorauthentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11a65254a814dd9470e596da19683aa225aa124e2a729980738fa7aa1899c8ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabletwofactorauthentication", value)

    @builtins.property
    @jsii.member(jsii_name="enforcefsquota")
    def enforcefsquota(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enforcefsquota"))

    @enforcefsquota.setter
    def enforcefsquota(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4834fa281f40adef728b928ea49f3b40e24a573908c5969d5818c6875d558e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enforcefsquota", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99e91ae41acbfb4cbc122c99030f7999f18705818f4ab7d6a2826d1fe0e4a6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="laptopadmins")
    def laptopadmins(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "laptopadmins"))

    @laptopadmins.setter
    def laptopadmins(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94907034a097f62d10b5902d0c62acdf22de361f59afae5fe714d0080b25044e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "laptopadmins", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c42ad913bac6ee7895c5c87be0a2ebf2161941e207e575e08b860de0cce9921e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="planoperationtype")
    def planoperationtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "planoperationtype"))

    @planoperationtype.setter
    def planoperationtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e0b55f0580738f90f9ccc3f728d392f9bf3ae8f53873974d986961a8cfc2b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "planoperationtype", value)

    @builtins.property
    @jsii.member(jsii_name="quotalimitingb")
    def quotalimitingb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "quotalimitingb"))

    @quotalimitingb.setter
    def quotalimitingb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18cd3c794c490df8001017c48877d59eefc0700d8ca74a07c8023a9ba79ac992)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quotalimitingb", value)


@jsii.data_type(
    jsii_type="commvault.usergroup.UsergroupAssociatedexternalgroups",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class UsergroupAssociatedexternalgroups:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f38b9a4b8df53ea2b8089db6b787809c5d5d05d60b02cc78536495cf5f0755bb)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}.

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
        return "UsergroupAssociatedexternalgroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsergroupAssociatedexternalgroupsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.UsergroupAssociatedexternalgroupsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03416b3a85860a392c54efde048cfd1d70444f10cd374b6b0a3240f34f010936)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "UsergroupAssociatedexternalgroupsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e78f574c59ed118c10df35077565279d2e8f1610a59d15b625dd2d75025e9d96)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UsergroupAssociatedexternalgroupsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8582b400096f90dd0cc56c0e244e5fbe1f45f07dfa5ed1487fc0cd27acb5774b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ce65bbb210dce7c0a6f3b2f7563bc7124a726b154febbe9d9b67c3e65d7bf21)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77053e2e919569a7aaa1f3abb63453914e003a93780b5fa7ffda132c505afcc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupAssociatedexternalgroups]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupAssociatedexternalgroups]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupAssociatedexternalgroups]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35a18facdd969099db9b435ae1e16bde71979ff197506863db064a2a07a6d3aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UsergroupAssociatedexternalgroupsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.UsergroupAssociatedexternalgroupsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__67895b8fbde9d34e571f92946890f9672ea2bb052ce1ceb3680790293e5de4ec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f5f6bf50037bcd97f4d72d694b39f0ee4a0e3bd3788564b22532be8a1539f2a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupAssociatedexternalgroups]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupAssociatedexternalgroups]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupAssociatedexternalgroups]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8945ba1e36c397bd41f066c9843c6a1efafe80afa4c406d27b12f0d9af822b3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.usergroup.UsergroupConfig",
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
        "allowmultiplecompanymembers": "allowmultiplecompanymembers",
        "associatedexternalgroups": "associatedexternalgroups",
        "azureguid": "azureguid",
        "description": "description",
        "donotinheritrestrictconsoletypes": "donotinheritrestrictconsoletypes",
        "enabled": "enabled",
        "enablelocalauthentication": "enablelocalauthentication",
        "enabletwofactorauthentication": "enabletwofactorauthentication",
        "enforcefsquota": "enforcefsquota",
        "id": "id",
        "laptopadmins": "laptopadmins",
        "planoperationtype": "planoperationtype",
        "quotalimitingb": "quotalimitingb",
        "restrictconsoletypes": "restrictconsoletypes",
        "users": "users",
    },
)
class UsergroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        allowmultiplecompanymembers: typing.Optional[builtins.str] = None,
        associatedexternalgroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupAssociatedexternalgroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
        azureguid: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        donotinheritrestrictconsoletypes: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.str] = None,
        enablelocalauthentication: typing.Optional[builtins.str] = None,
        enabletwofactorauthentication: typing.Optional[builtins.str] = None,
        enforcefsquota: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        laptopadmins: typing.Optional[builtins.str] = None,
        planoperationtype: typing.Optional[builtins.str] = None,
        quotalimitingb: typing.Optional[jsii.Number] = None,
        restrictconsoletypes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupRestrictconsoletypes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        users: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UsergroupUsers", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: To create an active directory usergroup, the domain name should be mentioned along with the usergroup name (domainName\\usergroupName) and localUserGroup value must be given. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#name Usergroup#name}
        :param allowmultiplecompanymembers: This property can be used to allow addition of users/groups from child companies. Only applicable for commcell and reseller company group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#allowmultiplecompanymembers Usergroup#allowmultiplecompanymembers}
        :param associatedexternalgroups: associatedexternalgroups block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#associatedexternalgroups Usergroup#associatedexternalgroups}
        :param azureguid: Azure Object ID used to link this user group to Azure AD group and manage group membership of the user during SAML login. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#azureguid Usergroup#azureguid}
        :param description: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#description Usergroup#description}.
        :param donotinheritrestrictconsoletypes: Option to not inherit the RestrictConsoleTypes from the parent. By default the value is false, parent RestrictConsoleTypes will be inherited. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#donotinheritrestrictconsoletypes Usergroup#donotinheritrestrictconsoletypes}
        :param enabled: allows the enabling/disabling of the user group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enabled Usergroup#enabled}
        :param enablelocalauthentication: Allows two-factor authentication to be enabled for the specific types of usergroups. it can be turned on or off based on user preferences. There will be usergroups that will not have this option. [ON, OFF, DISABLED_AT_COMPANY] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enablelocalauthentication Usergroup#enablelocalauthentication}
        :param enabletwofactorauthentication: Allows two-factor authentication to be enabled for the specific types of usergroups. it can be turned on or off based on user preferences. There will be usergroups that will not have this option. [ON, OFF, DISABLED_AT_COMPANY] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enabletwofactorauthentication Usergroup#enabletwofactorauthentication}
        :param enforcefsquota: Used to determine if a backup data limit will be set for the user group being created. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enforcefsquota Usergroup#enforcefsquota}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param laptopadmins: When set to true, users in this group cannot activate or be set as server owner. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#laptopadmins Usergroup#laptopadmins}
        :param planoperationtype: determines if an existing user has to be added to the user group or removed from the user group [ADD, DELETE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#planoperationtype Usergroup#planoperationtype}
        :param quotalimitingb: if enforceFSQuota is set to true, the quota limit can be set in GBs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#quotalimitingb Usergroup#quotalimitingb}
        :param restrictconsoletypes: restrictconsoletypes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#restrictconsoletypes Usergroup#restrictconsoletypes}
        :param users: users block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#users Usergroup#users}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbec686bd5dff75a11f7f69b570b27ed814ad3170184a2ad6654de33f4868580)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowmultiplecompanymembers", value=allowmultiplecompanymembers, expected_type=type_hints["allowmultiplecompanymembers"])
            check_type(argname="argument associatedexternalgroups", value=associatedexternalgroups, expected_type=type_hints["associatedexternalgroups"])
            check_type(argname="argument azureguid", value=azureguid, expected_type=type_hints["azureguid"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument donotinheritrestrictconsoletypes", value=donotinheritrestrictconsoletypes, expected_type=type_hints["donotinheritrestrictconsoletypes"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument enablelocalauthentication", value=enablelocalauthentication, expected_type=type_hints["enablelocalauthentication"])
            check_type(argname="argument enabletwofactorauthentication", value=enabletwofactorauthentication, expected_type=type_hints["enabletwofactorauthentication"])
            check_type(argname="argument enforcefsquota", value=enforcefsquota, expected_type=type_hints["enforcefsquota"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument laptopadmins", value=laptopadmins, expected_type=type_hints["laptopadmins"])
            check_type(argname="argument planoperationtype", value=planoperationtype, expected_type=type_hints["planoperationtype"])
            check_type(argname="argument quotalimitingb", value=quotalimitingb, expected_type=type_hints["quotalimitingb"])
            check_type(argname="argument restrictconsoletypes", value=restrictconsoletypes, expected_type=type_hints["restrictconsoletypes"])
            check_type(argname="argument users", value=users, expected_type=type_hints["users"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
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
        if allowmultiplecompanymembers is not None:
            self._values["allowmultiplecompanymembers"] = allowmultiplecompanymembers
        if associatedexternalgroups is not None:
            self._values["associatedexternalgroups"] = associatedexternalgroups
        if azureguid is not None:
            self._values["azureguid"] = azureguid
        if description is not None:
            self._values["description"] = description
        if donotinheritrestrictconsoletypes is not None:
            self._values["donotinheritrestrictconsoletypes"] = donotinheritrestrictconsoletypes
        if enabled is not None:
            self._values["enabled"] = enabled
        if enablelocalauthentication is not None:
            self._values["enablelocalauthentication"] = enablelocalauthentication
        if enabletwofactorauthentication is not None:
            self._values["enabletwofactorauthentication"] = enabletwofactorauthentication
        if enforcefsquota is not None:
            self._values["enforcefsquota"] = enforcefsquota
        if id is not None:
            self._values["id"] = id
        if laptopadmins is not None:
            self._values["laptopadmins"] = laptopadmins
        if planoperationtype is not None:
            self._values["planoperationtype"] = planoperationtype
        if quotalimitingb is not None:
            self._values["quotalimitingb"] = quotalimitingb
        if restrictconsoletypes is not None:
            self._values["restrictconsoletypes"] = restrictconsoletypes
        if users is not None:
            self._values["users"] = users

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
        '''To create an active directory usergroup, the domain name should be mentioned along with the usergroup name (domainName\\usergroupName) and localUserGroup value must be given.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#name Usergroup#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowmultiplecompanymembers(self) -> typing.Optional[builtins.str]:
        '''This property can be used to allow addition of users/groups from child companies.

        Only applicable for commcell and reseller company group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#allowmultiplecompanymembers Usergroup#allowmultiplecompanymembers}
        '''
        result = self._values.get("allowmultiplecompanymembers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def associatedexternalgroups(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupAssociatedexternalgroups]]]:
        '''associatedexternalgroups block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#associatedexternalgroups Usergroup#associatedexternalgroups}
        '''
        result = self._values.get("associatedexternalgroups")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupAssociatedexternalgroups]]], result)

    @builtins.property
    def azureguid(self) -> typing.Optional[builtins.str]:
        '''Azure Object ID used to link this user group to Azure AD group and manage group membership of the user during SAML login.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#azureguid Usergroup#azureguid}
        '''
        result = self._values.get("azureguid")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#description Usergroup#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def donotinheritrestrictconsoletypes(self) -> typing.Optional[builtins.str]:
        '''Option to not inherit the RestrictConsoleTypes from the parent.

        By default the value is false, parent RestrictConsoleTypes will be inherited.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#donotinheritrestrictconsoletypes Usergroup#donotinheritrestrictconsoletypes}
        '''
        result = self._values.get("donotinheritrestrictconsoletypes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.str]:
        '''allows the enabling/disabling of the user group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enabled Usergroup#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enablelocalauthentication(self) -> typing.Optional[builtins.str]:
        '''Allows two-factor authentication to be enabled for the specific types of usergroups.

        it can be turned on or off based on user preferences. There will be usergroups that will not have this option. [ON, OFF, DISABLED_AT_COMPANY]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enablelocalauthentication Usergroup#enablelocalauthentication}
        '''
        result = self._values.get("enablelocalauthentication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabletwofactorauthentication(self) -> typing.Optional[builtins.str]:
        '''Allows two-factor authentication to be enabled for the specific types of usergroups.

        it can be turned on or off based on user preferences. There will be usergroups that will not have this option. [ON, OFF, DISABLED_AT_COMPANY]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enabletwofactorauthentication Usergroup#enabletwofactorauthentication}
        '''
        result = self._values.get("enabletwofactorauthentication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enforcefsquota(self) -> typing.Optional[builtins.str]:
        '''Used to determine if a backup data limit will be set for the user group being created.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#enforcefsquota Usergroup#enforcefsquota}
        '''
        result = self._values.get("enforcefsquota")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def laptopadmins(self) -> typing.Optional[builtins.str]:
        '''When set to true, users in this group cannot activate or be set as server owner.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#laptopadmins Usergroup#laptopadmins}
        '''
        result = self._values.get("laptopadmins")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def planoperationtype(self) -> typing.Optional[builtins.str]:
        '''determines if an existing user has to be added to the user group or removed from the user group [ADD, DELETE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#planoperationtype Usergroup#planoperationtype}
        '''
        result = self._values.get("planoperationtype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def quotalimitingb(self) -> typing.Optional[jsii.Number]:
        '''if enforceFSQuota is set to true, the quota limit can be set in GBs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#quotalimitingb Usergroup#quotalimitingb}
        '''
        result = self._values.get("quotalimitingb")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def restrictconsoletypes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupRestrictconsoletypes"]]]:
        '''restrictconsoletypes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#restrictconsoletypes Usergroup#restrictconsoletypes}
        '''
        result = self._values.get("restrictconsoletypes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupRestrictconsoletypes"]]], result)

    @builtins.property
    def users(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupUsers"]]]:
        '''users block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#users Usergroup#users}
        '''
        result = self._values.get("users")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UsergroupUsers"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsergroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.usergroup.UsergroupRestrictconsoletypes",
    jsii_struct_bases=[],
    name_mapping={"consoletype": "consoletype"},
)
class UsergroupRestrictconsoletypes:
    def __init__(
        self,
        *,
        consoletype: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param consoletype: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#consoletype Usergroup#consoletype}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00172d2e7d7a06a7f9cef204cb201945f403486f96e860d310017bac8ae7b76f)
            check_type(argname="argument consoletype", value=consoletype, expected_type=type_hints["consoletype"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if consoletype is not None:
            self._values["consoletype"] = consoletype

    @builtins.property
    def consoletype(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#consoletype Usergroup#consoletype}.'''
        result = self._values.get("consoletype")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsergroupRestrictconsoletypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsergroupRestrictconsoletypesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.UsergroupRestrictconsoletypesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1d0c3b75132bd65f750149dc097aa7d3b8898bd37f7d28c1cd2153d82e4ba7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UsergroupRestrictconsoletypesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97b59493969c80f9f42daa14bd96162f318943c6c003c9af7b879941758c9c66)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UsergroupRestrictconsoletypesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd1444739c35bb9fb44fe0018c0339f425eab5bb2668e8455f64e294370aea4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6421173be34efd7d2f2d23ca8668b24eb07acc5c65dedac05260b629d8c1aa25)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b9268ea2829a013a0d9225add0c642c48562dbf064ab85ee6ad02daa21ff149)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupRestrictconsoletypes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupRestrictconsoletypes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupRestrictconsoletypes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__664ffa35034179bee5df36cead33cf4a7915ee9c8800585978c628b1d497533e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UsergroupRestrictconsoletypesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.UsergroupRestrictconsoletypesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3f82878928e8a74a086c8795ac96154285196aebc1b3ddaa4e77478ffa31afe0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetConsoletype")
    def reset_consoletype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConsoletype", []))

    @builtins.property
    @jsii.member(jsii_name="consoletypeInput")
    def consoletype_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "consoletypeInput"))

    @builtins.property
    @jsii.member(jsii_name="consoletype")
    def consoletype(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "consoletype"))

    @consoletype.setter
    def consoletype(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b302a766cd65164ecccc5ce1a90feab3b9e6086f8c777609955e7ca5578dd7f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "consoletype", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupRestrictconsoletypes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupRestrictconsoletypes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupRestrictconsoletypes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__764d388c03251bdef0cd141fe3f0fcc64661fb2543d96d02b7d0d296a851b6a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.usergroup.UsergroupUsers",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class UsergroupUsers:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d869bbf0a27a21cbfc2c01aed194cecd684f6ea3537583d3e2a1378ac49eab6b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/usergroup#id Usergroup#id}.

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
        return "UsergroupUsers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UsergroupUsersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.UsergroupUsersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5430f8c2223ec96705c6ee1a7dad2f120c80474a7fd2d572ee5a1adf74bc92ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UsergroupUsersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ad8c954daae4af12ec1f328a6f55b3b82aa64223c0bed5a99ce4b5ae1c55828)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UsergroupUsersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__364ecdee4b122c56d628ab4fec3bcfff7d08d2a747e37f4fe07f537e1cfcbb54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b2df88cff6b9b7470d89d47ff2b653462f67128c0dadf46858716614e6dcb28)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4aac50f9c2479733cc6ff6e0aab3711315af4f7f6e51a6e5aeabc2d6ab217daa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupUsers]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupUsers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupUsers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0580f0a3c4df9ce7fea4f6df0c77e9c05a847e772be27df2c704c5dac2e7205c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UsergroupUsersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.usergroup.UsergroupUsersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__57db4f801c13d648b318d8f098556361dc7e2a586e1e8b3e6b9ea8b31652e26d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3179f3f7b4c960300d2da4cd7b1c456f721b167743efc0e3f21b2e234599eabb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupUsers]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupUsers]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupUsers]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac146f5ca004afd765ea86a25ffcc99fcd7eab5edbdd0dae52dd91a7dcdbe4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Usergroup",
    "UsergroupAssociatedexternalgroups",
    "UsergroupAssociatedexternalgroupsList",
    "UsergroupAssociatedexternalgroupsOutputReference",
    "UsergroupConfig",
    "UsergroupRestrictconsoletypes",
    "UsergroupRestrictconsoletypesList",
    "UsergroupRestrictconsoletypesOutputReference",
    "UsergroupUsers",
    "UsergroupUsersList",
    "UsergroupUsersOutputReference",
]

publication.publish()

def _typecheckingstub__cda4ee5883acf0fd89c07ed3883aef0038703bd0e29a5b995cf59016660f6eb5(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    allowmultiplecompanymembers: typing.Optional[builtins.str] = None,
    associatedexternalgroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupAssociatedexternalgroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
    azureguid: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    donotinheritrestrictconsoletypes: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.str] = None,
    enablelocalauthentication: typing.Optional[builtins.str] = None,
    enabletwofactorauthentication: typing.Optional[builtins.str] = None,
    enforcefsquota: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    laptopadmins: typing.Optional[builtins.str] = None,
    planoperationtype: typing.Optional[builtins.str] = None,
    quotalimitingb: typing.Optional[jsii.Number] = None,
    restrictconsoletypes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupRestrictconsoletypes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    users: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupUsers, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__f290e2d37f6249cd60d57c16e7ed9782d7e680daeece1ed6eace32cddf15e7fc(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6e573b68d7c26b71d25ea6f4ab2b0808236d4f3f1d959c9a6f3dee1c9024ea8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupAssociatedexternalgroups, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cddaec875117247097058e00f20f4384ac0994719e54131e5b738d7169efc802(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupRestrictconsoletypes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da405363ef313777450fbb05ff5efb2ea0abb4c65d23a0f085eb2a0a8479223f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupUsers, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92ce486d8c4693105ba7f66cfe206a5ea64133b79c02e77601f6fcab6017752(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7d4c8e2af11770ace6ce66c036f5ad4187f41c706fa3d7060eed0a7952624d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ad17db0a7332b13032a0508c1ee755a94dbe724ccfbd9bc0a3a7b4a8e00ff82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f029d5147e8bb2f373b99e538ad306f178970d106ceed71e308ff28169e59d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea2707c4b4978e2a42d17321556d036cf5fad83bf18a878c7167b39d18bcf11(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__748681ca6b06f71c7ac9154966dc55bcb7080ecc608e693030ac4678b1e5f208(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11a65254a814dd9470e596da19683aa225aa124e2a729980738fa7aa1899c8ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4834fa281f40adef728b928ea49f3b40e24a573908c5969d5818c6875d558e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99e91ae41acbfb4cbc122c99030f7999f18705818f4ab7d6a2826d1fe0e4a6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94907034a097f62d10b5902d0c62acdf22de361f59afae5fe714d0080b25044e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c42ad913bac6ee7895c5c87be0a2ebf2161941e207e575e08b860de0cce9921e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e0b55f0580738f90f9ccc3f728d392f9bf3ae8f53873974d986961a8cfc2b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18cd3c794c490df8001017c48877d59eefc0700d8ca74a07c8023a9ba79ac992(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f38b9a4b8df53ea2b8089db6b787809c5d5d05d60b02cc78536495cf5f0755bb(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03416b3a85860a392c54efde048cfd1d70444f10cd374b6b0a3240f34f010936(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e78f574c59ed118c10df35077565279d2e8f1610a59d15b625dd2d75025e9d96(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8582b400096f90dd0cc56c0e244e5fbe1f45f07dfa5ed1487fc0cd27acb5774b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ce65bbb210dce7c0a6f3b2f7563bc7124a726b154febbe9d9b67c3e65d7bf21(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77053e2e919569a7aaa1f3abb63453914e003a93780b5fa7ffda132c505afcc5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35a18facdd969099db9b435ae1e16bde71979ff197506863db064a2a07a6d3aa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupAssociatedexternalgroups]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67895b8fbde9d34e571f92946890f9672ea2bb052ce1ceb3680790293e5de4ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5f6bf50037bcd97f4d72d694b39f0ee4a0e3bd3788564b22532be8a1539f2a8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8945ba1e36c397bd41f066c9843c6a1efafe80afa4c406d27b12f0d9af822b3a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupAssociatedexternalgroups]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbec686bd5dff75a11f7f69b570b27ed814ad3170184a2ad6654de33f4868580(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    allowmultiplecompanymembers: typing.Optional[builtins.str] = None,
    associatedexternalgroups: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupAssociatedexternalgroups, typing.Dict[builtins.str, typing.Any]]]]] = None,
    azureguid: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    donotinheritrestrictconsoletypes: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.str] = None,
    enablelocalauthentication: typing.Optional[builtins.str] = None,
    enabletwofactorauthentication: typing.Optional[builtins.str] = None,
    enforcefsquota: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    laptopadmins: typing.Optional[builtins.str] = None,
    planoperationtype: typing.Optional[builtins.str] = None,
    quotalimitingb: typing.Optional[jsii.Number] = None,
    restrictconsoletypes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupRestrictconsoletypes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    users: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UsergroupUsers, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00172d2e7d7a06a7f9cef204cb201945f403486f96e860d310017bac8ae7b76f(
    *,
    consoletype: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1d0c3b75132bd65f750149dc097aa7d3b8898bd37f7d28c1cd2153d82e4ba7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97b59493969c80f9f42daa14bd96162f318943c6c003c9af7b879941758c9c66(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd1444739c35bb9fb44fe0018c0339f425eab5bb2668e8455f64e294370aea4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6421173be34efd7d2f2d23ca8668b24eb07acc5c65dedac05260b629d8c1aa25(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9268ea2829a013a0d9225add0c642c48562dbf064ab85ee6ad02daa21ff149(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__664ffa35034179bee5df36cead33cf4a7915ee9c8800585978c628b1d497533e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupRestrictconsoletypes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f82878928e8a74a086c8795ac96154285196aebc1b3ddaa4e77478ffa31afe0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b302a766cd65164ecccc5ce1a90feab3b9e6086f8c777609955e7ca5578dd7f5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__764d388c03251bdef0cd141fe3f0fcc64661fb2543d96d02b7d0d296a851b6a9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupRestrictconsoletypes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d869bbf0a27a21cbfc2c01aed194cecd684f6ea3537583d3e2a1378ac49eab6b(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5430f8c2223ec96705c6ee1a7dad2f120c80474a7fd2d572ee5a1adf74bc92ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ad8c954daae4af12ec1f328a6f55b3b82aa64223c0bed5a99ce4b5ae1c55828(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__364ecdee4b122c56d628ab4fec3bcfff7d08d2a747e37f4fe07f537e1cfcbb54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b2df88cff6b9b7470d89d47ff2b653462f67128c0dadf46858716614e6dcb28(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aac50f9c2479733cc6ff6e0aab3711315af4f7f6e51a6e5aeabc2d6ab217daa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0580f0a3c4df9ce7fea4f6df0c77e9c05a847e772be27df2c704c5dac2e7205c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UsergroupUsers]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57db4f801c13d648b318d8f098556361dc7e2a586e1e8b3e6b9ea8b31652e26d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3179f3f7b4c960300d2da4cd7b1c456f721b167743efc0e3f21b2e234599eabb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac146f5ca004afd765ea86a25ffcc99fcd7eab5edbdd0dae52dd91a7dcdbe4c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UsergroupUsers]],
) -> None:
    """Type checking stubs"""
    pass
