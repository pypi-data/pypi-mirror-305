'''
# `commvault_plan_server`

Refer to the Terraform Registry for docs: [`commvault_plan_server`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server).
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


class PlanServer(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServer",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server commvault_plan_server}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        planname: builtins.str,
        allowplanoverride: typing.Optional[builtins.str] = None,
        backupcontent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        backupdestinationids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        backupdestinations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinations", typing.Dict[builtins.str, typing.Any]]]]] = None,
        databaseoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerDatabaseoptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filesystemaddon: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overrideinheritsettings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerOverrideinheritsettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        overriderestrictions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerOverriderestrictions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        parentplan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerParentplan", typing.Dict[builtins.str, typing.Any]]]]] = None,
        regiontoconfigure: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRegiontoconfigure", typing.Dict[builtins.str, typing.Any]]]]] = None,
        rpo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        snapshotoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSnapshotoptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        workload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkload", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server commvault_plan_server} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param planname: Name of the new plan. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#planname PlanServer#planname}
        :param allowplanoverride: Flag to enable overriding of plan. Plan cannot be overriden by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#allowplanoverride PlanServer#allowplanoverride}
        :param backupcontent: backupcontent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        :param backupdestinationids: Primary Backup Destination Ids (which were created before plan creation). This is only considered when backupDestinations array object is not defined. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinationids PlanServer#backupdestinationids}
        :param backupdestinations: backupdestinations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinations PlanServer#backupdestinations}
        :param databaseoptions: databaseoptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#databaseoptions PlanServer#databaseoptions}
        :param filesystemaddon: flag to enable backup content association for applicable file system workload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#filesystemaddon PlanServer#filesystemaddon}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overrideinheritsettings: overrideinheritsettings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overrideinheritsettings PlanServer#overrideinheritsettings}
        :param overriderestrictions: overriderestrictions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overriderestrictions PlanServer#overriderestrictions}
        :param parentplan: parentplan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#parentplan PlanServer#parentplan}
        :param regiontoconfigure: regiontoconfigure block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#regiontoconfigure PlanServer#regiontoconfigure}
        :param rpo: rpo block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        :param settings: settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#settings PlanServer#settings}
        :param snapshotoptions: snapshotoptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#snapshotoptions PlanServer#snapshotoptions}
        :param workload: workload block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workload PlanServer#workload}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e432b8d2ea0e9669ad61aac9f4c1525a6f5bcc1645c90940ff2f8cd3e949cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PlanServerConfig(
            planname=planname,
            allowplanoverride=allowplanoverride,
            backupcontent=backupcontent,
            backupdestinationids=backupdestinationids,
            backupdestinations=backupdestinations,
            databaseoptions=databaseoptions,
            filesystemaddon=filesystemaddon,
            id=id,
            overrideinheritsettings=overrideinheritsettings,
            overriderestrictions=overriderestrictions,
            parentplan=parentplan,
            regiontoconfigure=regiontoconfigure,
            rpo=rpo,
            settings=settings,
            snapshotoptions=snapshotoptions,
            workload=workload,
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
        '''Generates CDKTF code for importing a PlanServer resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the PlanServer to import.
        :param import_from_id: The id of the existing PlanServer that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the PlanServer to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2516b8498e4cca96bdbeddd5f995bccad75d8f82dc8a2ca8a411ae64369ff290)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putBackupcontent")
    def put_backupcontent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__665d8c418c0ea7665d6f561d778c0e34022f37098ff395be34ecfcdd82db9977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackupcontent", [value]))

    @jsii.member(jsii_name="putBackupdestinations")
    def put_backupdestinations(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinations", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f12ae17a87ccb160188a41e5e332d3d7089581d467169bbc1c7395dc8dc2088d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackupdestinations", [value]))

    @jsii.member(jsii_name="putDatabaseoptions")
    def put_databaseoptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerDatabaseoptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1350f10f3732b99c9b7814de7783ad511dba69baf97c830d7708f4564611693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDatabaseoptions", [value]))

    @jsii.member(jsii_name="putOverrideinheritsettings")
    def put_overrideinheritsettings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerOverrideinheritsettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be74ab2bd508000bbcd8e7fe1ee9a9bcbe01957763d82422d7c48814a1f611ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverrideinheritsettings", [value]))

    @jsii.member(jsii_name="putOverriderestrictions")
    def put_overriderestrictions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerOverriderestrictions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3b1003edb6bbdd357ee371c00fbf042a72517b2fa3b814ad0add6f8adf84c74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOverriderestrictions", [value]))

    @jsii.member(jsii_name="putParentplan")
    def put_parentplan(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerParentplan", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__067f43ab282ea5f2a85cd257094fc123b3c691dd289aac39250ac8a4dce3e2db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putParentplan", [value]))

    @jsii.member(jsii_name="putRegiontoconfigure")
    def put_regiontoconfigure(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRegiontoconfigure", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c260fd1233d271e4e1b288ed0f3953d9574674011ff62e754dcb02ecc5796d4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegiontoconfigure", [value]))

    @jsii.member(jsii_name="putRpo")
    def put_rpo(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpo", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f189b69c9af965a26975aaedc0c53bdf3cf0b55e9f11e0452e605c5280905b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRpo", [value]))

    @jsii.member(jsii_name="putSettings")
    def put_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__691f009a27ef2bed1ad4b6d78976cf7461543f6bd146fe56b600ae6b243df6d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSettings", [value]))

    @jsii.member(jsii_name="putSnapshotoptions")
    def put_snapshotoptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSnapshotoptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91166b7ec47ee27894b607564260d97649d287678350e11d1b79bf55a27844fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSnapshotoptions", [value]))

    @jsii.member(jsii_name="putWorkload")
    def put_workload(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkload", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bb6989fa02a27f451803c56008af8adf30a3766cb10da584e03d40a1537518f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWorkload", [value]))

    @jsii.member(jsii_name="resetAllowplanoverride")
    def reset_allowplanoverride(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowplanoverride", []))

    @jsii.member(jsii_name="resetBackupcontent")
    def reset_backupcontent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupcontent", []))

    @jsii.member(jsii_name="resetBackupdestinationids")
    def reset_backupdestinationids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupdestinationids", []))

    @jsii.member(jsii_name="resetBackupdestinations")
    def reset_backupdestinations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupdestinations", []))

    @jsii.member(jsii_name="resetDatabaseoptions")
    def reset_databaseoptions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseoptions", []))

    @jsii.member(jsii_name="resetFilesystemaddon")
    def reset_filesystemaddon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesystemaddon", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOverrideinheritsettings")
    def reset_overrideinheritsettings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideinheritsettings", []))

    @jsii.member(jsii_name="resetOverriderestrictions")
    def reset_overriderestrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverriderestrictions", []))

    @jsii.member(jsii_name="resetParentplan")
    def reset_parentplan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentplan", []))

    @jsii.member(jsii_name="resetRegiontoconfigure")
    def reset_regiontoconfigure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegiontoconfigure", []))

    @jsii.member(jsii_name="resetRpo")
    def reset_rpo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRpo", []))

    @jsii.member(jsii_name="resetSettings")
    def reset_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettings", []))

    @jsii.member(jsii_name="resetSnapshotoptions")
    def reset_snapshotoptions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotoptions", []))

    @jsii.member(jsii_name="resetWorkload")
    def reset_workload(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkload", []))

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
    @jsii.member(jsii_name="backupcontent")
    def backupcontent(self) -> "PlanServerBackupcontentList":
        return typing.cast("PlanServerBackupcontentList", jsii.get(self, "backupcontent"))

    @builtins.property
    @jsii.member(jsii_name="backupdestinations")
    def backupdestinations(self) -> "PlanServerBackupdestinationsList":
        return typing.cast("PlanServerBackupdestinationsList", jsii.get(self, "backupdestinations"))

    @builtins.property
    @jsii.member(jsii_name="databaseoptions")
    def databaseoptions(self) -> "PlanServerDatabaseoptionsList":
        return typing.cast("PlanServerDatabaseoptionsList", jsii.get(self, "databaseoptions"))

    @builtins.property
    @jsii.member(jsii_name="overrideinheritsettings")
    def overrideinheritsettings(self) -> "PlanServerOverrideinheritsettingsList":
        return typing.cast("PlanServerOverrideinheritsettingsList", jsii.get(self, "overrideinheritsettings"))

    @builtins.property
    @jsii.member(jsii_name="overriderestrictions")
    def overriderestrictions(self) -> "PlanServerOverriderestrictionsList":
        return typing.cast("PlanServerOverriderestrictionsList", jsii.get(self, "overriderestrictions"))

    @builtins.property
    @jsii.member(jsii_name="parentplan")
    def parentplan(self) -> "PlanServerParentplanList":
        return typing.cast("PlanServerParentplanList", jsii.get(self, "parentplan"))

    @builtins.property
    @jsii.member(jsii_name="regiontoconfigure")
    def regiontoconfigure(self) -> "PlanServerRegiontoconfigureList":
        return typing.cast("PlanServerRegiontoconfigureList", jsii.get(self, "regiontoconfigure"))

    @builtins.property
    @jsii.member(jsii_name="rpo")
    def rpo(self) -> "PlanServerRpoList":
        return typing.cast("PlanServerRpoList", jsii.get(self, "rpo"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "PlanServerSettingsList":
        return typing.cast("PlanServerSettingsList", jsii.get(self, "settings"))

    @builtins.property
    @jsii.member(jsii_name="snapshotoptions")
    def snapshotoptions(self) -> "PlanServerSnapshotoptionsList":
        return typing.cast("PlanServerSnapshotoptionsList", jsii.get(self, "snapshotoptions"))

    @builtins.property
    @jsii.member(jsii_name="workload")
    def workload(self) -> "PlanServerWorkloadList":
        return typing.cast("PlanServerWorkloadList", jsii.get(self, "workload"))

    @builtins.property
    @jsii.member(jsii_name="allowplanoverrideInput")
    def allowplanoverride_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allowplanoverrideInput"))

    @builtins.property
    @jsii.member(jsii_name="backupcontentInput")
    def backupcontent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontent"]]], jsii.get(self, "backupcontentInput"))

    @builtins.property
    @jsii.member(jsii_name="backupdestinationidsInput")
    def backupdestinationids_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "backupdestinationidsInput"))

    @builtins.property
    @jsii.member(jsii_name="backupdestinationsInput")
    def backupdestinations_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinations"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinations"]]], jsii.get(self, "backupdestinationsInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseoptionsInput")
    def databaseoptions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerDatabaseoptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerDatabaseoptions"]]], jsii.get(self, "databaseoptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemaddonInput")
    def filesystemaddon_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filesystemaddonInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideinheritsettingsInput")
    def overrideinheritsettings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverrideinheritsettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverrideinheritsettings"]]], jsii.get(self, "overrideinheritsettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="overriderestrictionsInput")
    def overriderestrictions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverriderestrictions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverriderestrictions"]]], jsii.get(self, "overriderestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="parentplanInput")
    def parentplan_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerParentplan"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerParentplan"]]], jsii.get(self, "parentplanInput"))

    @builtins.property
    @jsii.member(jsii_name="plannameInput")
    def planname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "plannameInput"))

    @builtins.property
    @jsii.member(jsii_name="regiontoconfigureInput")
    def regiontoconfigure_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRegiontoconfigure"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRegiontoconfigure"]]], jsii.get(self, "regiontoconfigureInput"))

    @builtins.property
    @jsii.member(jsii_name="rpoInput")
    def rpo_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpo"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpo"]]], jsii.get(self, "rpoInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsInput")
    def settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSettings"]]], jsii.get(self, "settingsInput"))

    @builtins.property
    @jsii.member(jsii_name="snapshotoptionsInput")
    def snapshotoptions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSnapshotoptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSnapshotoptions"]]], jsii.get(self, "snapshotoptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadInput")
    def workload_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkload"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkload"]]], jsii.get(self, "workloadInput"))

    @builtins.property
    @jsii.member(jsii_name="allowplanoverride")
    def allowplanoverride(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "allowplanoverride"))

    @allowplanoverride.setter
    def allowplanoverride(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__745b643b5e21096f1aa054f08664f87cd2099185017aeeedca05117729b2c4fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowplanoverride", value)

    @builtins.property
    @jsii.member(jsii_name="backupdestinationids")
    def backupdestinationids(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "backupdestinationids"))

    @backupdestinationids.setter
    def backupdestinationids(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcb6a592e28478f2ac10da8848011a6f48cd91035939b38ded61fcf5c869ed97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupdestinationids", value)

    @builtins.property
    @jsii.member(jsii_name="filesystemaddon")
    def filesystemaddon(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filesystemaddon"))

    @filesystemaddon.setter
    def filesystemaddon(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dd3c9200e1ef822589db90be8d4dad7f440c1ed46d840cb575069eae09a0eaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesystemaddon", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee75d4a0122f8688ac55d90aa9331872ab407e15f61de32782e8e3ddd24b0e14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="planname")
    def planname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "planname"))

    @planname.setter
    def planname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ba117c04095e48b239a2100de552bd625a49e41e95c8124b4c4a3d561cbc51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "planname", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupcontent",
    jsii_struct_bases=[],
    name_mapping={
        "backupsystemstate": "backupsystemstate",
        "backupsystemstateonlywithfullbackup": "backupsystemstateonlywithfullbackup",
        "forceupdateproperties": "forceupdateproperties",
        "macexcludedpaths": "macexcludedpaths",
        "macfiltertoexcludepaths": "macfiltertoexcludepaths",
        "macincludedpaths": "macincludedpaths",
        "macnumberofdatareaders": "macnumberofdatareaders",
        "unixexcludedpaths": "unixexcludedpaths",
        "unixfiltertoexcludepaths": "unixfiltertoexcludepaths",
        "unixincludedpaths": "unixincludedpaths",
        "unixnumberofdatareaders": "unixnumberofdatareaders",
        "usevssforsystemstate": "usevssforsystemstate",
        "windowsexcludedpaths": "windowsexcludedpaths",
        "windowsfiltertoexcludepaths": "windowsfiltertoexcludepaths",
        "windowsincludedpaths": "windowsincludedpaths",
        "windowsnumberofdatareaders": "windowsnumberofdatareaders",
    },
)
class PlanServerBackupcontent:
    def __init__(
        self,
        *,
        backupsystemstate: typing.Optional[builtins.str] = None,
        backupsystemstateonlywithfullbackup: typing.Optional[builtins.str] = None,
        forceupdateproperties: typing.Optional[builtins.str] = None,
        macexcludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        macfiltertoexcludepaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        macincludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        macnumberofdatareaders: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontentMacnumberofdatareaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        unixexcludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        unixfiltertoexcludepaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        unixincludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        unixnumberofdatareaders: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontentUnixnumberofdatareaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
        usevssforsystemstate: typing.Optional[builtins.str] = None,
        windowsexcludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        windowsfiltertoexcludepaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        windowsincludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
        windowsnumberofdatareaders: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontentWindowsnumberofdatareaders", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backupsystemstate: Do you want to back up the system state? Applicable only for Windows. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupsystemstate PlanServer#backupsystemstate}
        :param backupsystemstateonlywithfullbackup: Do you want to back up system state only with full backup? Applicable only if the value of backupSystemState is true Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupsystemstateonlywithfullbackup PlanServer#backupsystemstateonlywithfullbackup}
        :param forceupdateproperties: Do you want to sync properties on associated subclients even if properties are overriden at subclient level? Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#forceupdateproperties PlanServer#forceupdateproperties}
        :param macexcludedpaths: Paths to exclude for Mac. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macexcludedpaths PlanServer#macexcludedpaths}
        :param macfiltertoexcludepaths: Paths that are exception to excluded paths for Mac. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macfiltertoexcludepaths PlanServer#macfiltertoexcludepaths}
        :param macincludedpaths: Paths to include for Mac. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macincludedpaths PlanServer#macincludedpaths}
        :param macnumberofdatareaders: macnumberofdatareaders block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macnumberofdatareaders PlanServer#macnumberofdatareaders}
        :param unixexcludedpaths: Paths to exclude for UNIX. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixexcludedpaths PlanServer#unixexcludedpaths}
        :param unixfiltertoexcludepaths: Paths that are exception to excluded paths for Unix. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixfiltertoexcludepaths PlanServer#unixfiltertoexcludepaths}
        :param unixincludedpaths: Paths to include for UNIX. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixincludedpaths PlanServer#unixincludedpaths}
        :param unixnumberofdatareaders: unixnumberofdatareaders block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixnumberofdatareaders PlanServer#unixnumberofdatareaders}
        :param usevssforsystemstate: Do you want to back up system state with VSS? Applicable only if the value of backupSystemState is true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usevssforsystemstate PlanServer#usevssforsystemstate}
        :param windowsexcludedpaths: Paths to exclude for Windows. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsexcludedpaths PlanServer#windowsexcludedpaths}
        :param windowsfiltertoexcludepaths: Paths that are exception to excluded paths for Windows. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsfiltertoexcludepaths PlanServer#windowsfiltertoexcludepaths}
        :param windowsincludedpaths: Paths to include for Windows. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsincludedpaths PlanServer#windowsincludedpaths}
        :param windowsnumberofdatareaders: windowsnumberofdatareaders block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsnumberofdatareaders PlanServer#windowsnumberofdatareaders}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8685d071c8be667872291d4c6d67d212f5e350bcd0a914334744148c99f18c37)
            check_type(argname="argument backupsystemstate", value=backupsystemstate, expected_type=type_hints["backupsystemstate"])
            check_type(argname="argument backupsystemstateonlywithfullbackup", value=backupsystemstateonlywithfullbackup, expected_type=type_hints["backupsystemstateonlywithfullbackup"])
            check_type(argname="argument forceupdateproperties", value=forceupdateproperties, expected_type=type_hints["forceupdateproperties"])
            check_type(argname="argument macexcludedpaths", value=macexcludedpaths, expected_type=type_hints["macexcludedpaths"])
            check_type(argname="argument macfiltertoexcludepaths", value=macfiltertoexcludepaths, expected_type=type_hints["macfiltertoexcludepaths"])
            check_type(argname="argument macincludedpaths", value=macincludedpaths, expected_type=type_hints["macincludedpaths"])
            check_type(argname="argument macnumberofdatareaders", value=macnumberofdatareaders, expected_type=type_hints["macnumberofdatareaders"])
            check_type(argname="argument unixexcludedpaths", value=unixexcludedpaths, expected_type=type_hints["unixexcludedpaths"])
            check_type(argname="argument unixfiltertoexcludepaths", value=unixfiltertoexcludepaths, expected_type=type_hints["unixfiltertoexcludepaths"])
            check_type(argname="argument unixincludedpaths", value=unixincludedpaths, expected_type=type_hints["unixincludedpaths"])
            check_type(argname="argument unixnumberofdatareaders", value=unixnumberofdatareaders, expected_type=type_hints["unixnumberofdatareaders"])
            check_type(argname="argument usevssforsystemstate", value=usevssforsystemstate, expected_type=type_hints["usevssforsystemstate"])
            check_type(argname="argument windowsexcludedpaths", value=windowsexcludedpaths, expected_type=type_hints["windowsexcludedpaths"])
            check_type(argname="argument windowsfiltertoexcludepaths", value=windowsfiltertoexcludepaths, expected_type=type_hints["windowsfiltertoexcludepaths"])
            check_type(argname="argument windowsincludedpaths", value=windowsincludedpaths, expected_type=type_hints["windowsincludedpaths"])
            check_type(argname="argument windowsnumberofdatareaders", value=windowsnumberofdatareaders, expected_type=type_hints["windowsnumberofdatareaders"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupsystemstate is not None:
            self._values["backupsystemstate"] = backupsystemstate
        if backupsystemstateonlywithfullbackup is not None:
            self._values["backupsystemstateonlywithfullbackup"] = backupsystemstateonlywithfullbackup
        if forceupdateproperties is not None:
            self._values["forceupdateproperties"] = forceupdateproperties
        if macexcludedpaths is not None:
            self._values["macexcludedpaths"] = macexcludedpaths
        if macfiltertoexcludepaths is not None:
            self._values["macfiltertoexcludepaths"] = macfiltertoexcludepaths
        if macincludedpaths is not None:
            self._values["macincludedpaths"] = macincludedpaths
        if macnumberofdatareaders is not None:
            self._values["macnumberofdatareaders"] = macnumberofdatareaders
        if unixexcludedpaths is not None:
            self._values["unixexcludedpaths"] = unixexcludedpaths
        if unixfiltertoexcludepaths is not None:
            self._values["unixfiltertoexcludepaths"] = unixfiltertoexcludepaths
        if unixincludedpaths is not None:
            self._values["unixincludedpaths"] = unixincludedpaths
        if unixnumberofdatareaders is not None:
            self._values["unixnumberofdatareaders"] = unixnumberofdatareaders
        if usevssforsystemstate is not None:
            self._values["usevssforsystemstate"] = usevssforsystemstate
        if windowsexcludedpaths is not None:
            self._values["windowsexcludedpaths"] = windowsexcludedpaths
        if windowsfiltertoexcludepaths is not None:
            self._values["windowsfiltertoexcludepaths"] = windowsfiltertoexcludepaths
        if windowsincludedpaths is not None:
            self._values["windowsincludedpaths"] = windowsincludedpaths
        if windowsnumberofdatareaders is not None:
            self._values["windowsnumberofdatareaders"] = windowsnumberofdatareaders

    @builtins.property
    def backupsystemstate(self) -> typing.Optional[builtins.str]:
        '''Do you want to back up the system state? Applicable only for Windows.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupsystemstate PlanServer#backupsystemstate}
        '''
        result = self._values.get("backupsystemstate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backupsystemstateonlywithfullbackup(self) -> typing.Optional[builtins.str]:
        '''Do you want to back up system state only with full backup?

        Applicable only if the value of backupSystemState is true

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupsystemstateonlywithfullbackup PlanServer#backupsystemstateonlywithfullbackup}
        '''
        result = self._values.get("backupsystemstateonlywithfullbackup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def forceupdateproperties(self) -> typing.Optional[builtins.str]:
        '''Do you want to sync properties on associated subclients even if properties are overriden at subclient level?

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#forceupdateproperties PlanServer#forceupdateproperties}
        '''
        result = self._values.get("forceupdateproperties")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def macexcludedpaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths to exclude for Mac.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macexcludedpaths PlanServer#macexcludedpaths}
        '''
        result = self._values.get("macexcludedpaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def macfiltertoexcludepaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths that are exception to excluded paths for Mac.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macfiltertoexcludepaths PlanServer#macfiltertoexcludepaths}
        '''
        result = self._values.get("macfiltertoexcludepaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def macincludedpaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths to include for Mac.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macincludedpaths PlanServer#macincludedpaths}
        '''
        result = self._values.get("macincludedpaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def macnumberofdatareaders(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentMacnumberofdatareaders"]]]:
        '''macnumberofdatareaders block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#macnumberofdatareaders PlanServer#macnumberofdatareaders}
        '''
        result = self._values.get("macnumberofdatareaders")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentMacnumberofdatareaders"]]], result)

    @builtins.property
    def unixexcludedpaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths to exclude for UNIX.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixexcludedpaths PlanServer#unixexcludedpaths}
        '''
        result = self._values.get("unixexcludedpaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def unixfiltertoexcludepaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths that are exception to excluded paths for Unix.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixfiltertoexcludepaths PlanServer#unixfiltertoexcludepaths}
        '''
        result = self._values.get("unixfiltertoexcludepaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def unixincludedpaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths to include for UNIX.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixincludedpaths PlanServer#unixincludedpaths}
        '''
        result = self._values.get("unixincludedpaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def unixnumberofdatareaders(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentUnixnumberofdatareaders"]]]:
        '''unixnumberofdatareaders block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#unixnumberofdatareaders PlanServer#unixnumberofdatareaders}
        '''
        result = self._values.get("unixnumberofdatareaders")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentUnixnumberofdatareaders"]]], result)

    @builtins.property
    def usevssforsystemstate(self) -> typing.Optional[builtins.str]:
        '''Do you want to back up system state with VSS? Applicable only if the value of backupSystemState is true.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usevssforsystemstate PlanServer#usevssforsystemstate}
        '''
        result = self._values.get("usevssforsystemstate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def windowsexcludedpaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths to exclude for Windows.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsexcludedpaths PlanServer#windowsexcludedpaths}
        '''
        result = self._values.get("windowsexcludedpaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def windowsfiltertoexcludepaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths that are exception to excluded paths for Windows.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsfiltertoexcludepaths PlanServer#windowsfiltertoexcludepaths}
        '''
        result = self._values.get("windowsfiltertoexcludepaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def windowsincludedpaths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Paths to include for Windows.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsincludedpaths PlanServer#windowsincludedpaths}
        '''
        result = self._values.get("windowsincludedpaths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def windowsnumberofdatareaders(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentWindowsnumberofdatareaders"]]]:
        '''windowsnumberofdatareaders block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#windowsnumberofdatareaders PlanServer#windowsnumberofdatareaders}
        '''
        result = self._values.get("windowsnumberofdatareaders")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentWindowsnumberofdatareaders"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupcontent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupcontentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c8371d2e155039760a040c04d50e1bfe80ad68f08720f3665adb1d90bc4f4d4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerBackupcontentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d445458422565ee223bedeaae994a5855a1a5458dbe1fac315ee2703434b092f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupcontentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__effa3da7f3195c6935a5572cbf72b9a1217a7a76e8b575adfbeb874936292bf1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf102ff45615eca46d7f30d0b21e6ff6caa6163faa0bcac2f620dc1b422cab45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1f5408d05f40c396c542e256ce034f66da9ffd5d260e03ae2254cbb413e1582a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__321f9423713da4810d738b4f41f79d99bab82bf4fa99a4aff0c1ddd124c41f25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupcontentMacnumberofdatareaders",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "useoptimal": "useoptimal"},
)
class PlanServerBackupcontentMacnumberofdatareaders:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        useoptimal: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Number of data readers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#count PlanServer#count}
        :param useoptimal: Set optimal number of data readers. if it is set to true, count will be ignored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useoptimal PlanServer#useoptimal}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1dbfc474a45a3b8508efcf51061681a829cfca8c03c110401089910ddd3fb9a)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument useoptimal", value=useoptimal, expected_type=type_hints["useoptimal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if useoptimal is not None:
            self._values["useoptimal"] = useoptimal

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Number of data readers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#count PlanServer#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def useoptimal(self) -> typing.Optional[builtins.str]:
        '''Set optimal number of data readers. if it is set to true, count will be ignored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useoptimal PlanServer#useoptimal}
        '''
        result = self._values.get("useoptimal")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupcontentMacnumberofdatareaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupcontentMacnumberofdatareadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentMacnumberofdatareadersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ce991efd5fc5a504f41aa7d0b6f4e6166acf05b9204cfa7044bdecc0fad145f2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupcontentMacnumberofdatareadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29058b86b96542d082aaaa78f30f9ee2c0d61d89c186461fc5b095847e57d3d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupcontentMacnumberofdatareadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e564dc88cea143224d46a42365b5e797bd1062e8797590d7617e5223ba559f96)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fbad3eabb14cfe9c383206b2d82913152206e42c6d30946bab4fab8628b82b7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1d47a205cd01b3e9bad64072c02692b48b95e470a30acf686b04d5779a3eb09f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentMacnumberofdatareaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentMacnumberofdatareaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentMacnumberofdatareaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e128b39518d41a940aca1c28701ff2b97f992eeb716f92e847e345419babf1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupcontentMacnumberofdatareadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentMacnumberofdatareadersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0f1024a52d8ccadd74d76f38ebf20ea882e38b4df7a6c3cd42eda4e268d3a10)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetUseoptimal")
    def reset_useoptimal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseoptimal", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="useoptimalInput")
    def useoptimal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useoptimalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__152b842128b4c03269ba5cf0cbd43b4832fe16e9f25b97a92d6281d5c7c50ad1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="useoptimal")
    def useoptimal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useoptimal"))

    @useoptimal.setter
    def useoptimal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8569c94f3ff1d7c2009349adbe755c354a9d3f7ec83abc30f319d01e6474f91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useoptimal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentMacnumberofdatareaders]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentMacnumberofdatareaders]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentMacnumberofdatareaders]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4255ea165dd9200869fd9bf67a5c17f1612ecc31ae00c81db33f4cdf438bfda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupcontentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c939aa24ce66838d3d4a11e0389e9594ee245a2ed768c46e5d636c59f2aa648d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMacnumberofdatareaders")
    def put_macnumberofdatareaders(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentMacnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__139c49ed34b5246b68bfe27803bd0962a70ab2fa7700f6f16c7b9c477c8797b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMacnumberofdatareaders", [value]))

    @jsii.member(jsii_name="putUnixnumberofdatareaders")
    def put_unixnumberofdatareaders(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontentUnixnumberofdatareaders", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6ea078188853b4a790ab46e18390c2038eb67fa82addd21697c68fe06e9c620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUnixnumberofdatareaders", [value]))

    @jsii.member(jsii_name="putWindowsnumberofdatareaders")
    def put_windowsnumberofdatareaders(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupcontentWindowsnumberofdatareaders", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9102858ab1f6f1dcede2f587905b11e4128a76664ffa9e41be379f2f8f156d0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWindowsnumberofdatareaders", [value]))

    @jsii.member(jsii_name="resetBackupsystemstate")
    def reset_backupsystemstate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupsystemstate", []))

    @jsii.member(jsii_name="resetBackupsystemstateonlywithfullbackup")
    def reset_backupsystemstateonlywithfullbackup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupsystemstateonlywithfullbackup", []))

    @jsii.member(jsii_name="resetForceupdateproperties")
    def reset_forceupdateproperties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceupdateproperties", []))

    @jsii.member(jsii_name="resetMacexcludedpaths")
    def reset_macexcludedpaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacexcludedpaths", []))

    @jsii.member(jsii_name="resetMacfiltertoexcludepaths")
    def reset_macfiltertoexcludepaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacfiltertoexcludepaths", []))

    @jsii.member(jsii_name="resetMacincludedpaths")
    def reset_macincludedpaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacincludedpaths", []))

    @jsii.member(jsii_name="resetMacnumberofdatareaders")
    def reset_macnumberofdatareaders(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacnumberofdatareaders", []))

    @jsii.member(jsii_name="resetUnixexcludedpaths")
    def reset_unixexcludedpaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnixexcludedpaths", []))

    @jsii.member(jsii_name="resetUnixfiltertoexcludepaths")
    def reset_unixfiltertoexcludepaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnixfiltertoexcludepaths", []))

    @jsii.member(jsii_name="resetUnixincludedpaths")
    def reset_unixincludedpaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnixincludedpaths", []))

    @jsii.member(jsii_name="resetUnixnumberofdatareaders")
    def reset_unixnumberofdatareaders(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUnixnumberofdatareaders", []))

    @jsii.member(jsii_name="resetUsevssforsystemstate")
    def reset_usevssforsystemstate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsevssforsystemstate", []))

    @jsii.member(jsii_name="resetWindowsexcludedpaths")
    def reset_windowsexcludedpaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsexcludedpaths", []))

    @jsii.member(jsii_name="resetWindowsfiltertoexcludepaths")
    def reset_windowsfiltertoexcludepaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsfiltertoexcludepaths", []))

    @jsii.member(jsii_name="resetWindowsincludedpaths")
    def reset_windowsincludedpaths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsincludedpaths", []))

    @jsii.member(jsii_name="resetWindowsnumberofdatareaders")
    def reset_windowsnumberofdatareaders(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsnumberofdatareaders", []))

    @builtins.property
    @jsii.member(jsii_name="macnumberofdatareaders")
    def macnumberofdatareaders(
        self,
    ) -> PlanServerBackupcontentMacnumberofdatareadersList:
        return typing.cast(PlanServerBackupcontentMacnumberofdatareadersList, jsii.get(self, "macnumberofdatareaders"))

    @builtins.property
    @jsii.member(jsii_name="unixnumberofdatareaders")
    def unixnumberofdatareaders(
        self,
    ) -> "PlanServerBackupcontentUnixnumberofdatareadersList":
        return typing.cast("PlanServerBackupcontentUnixnumberofdatareadersList", jsii.get(self, "unixnumberofdatareaders"))

    @builtins.property
    @jsii.member(jsii_name="windowsnumberofdatareaders")
    def windowsnumberofdatareaders(
        self,
    ) -> "PlanServerBackupcontentWindowsnumberofdatareadersList":
        return typing.cast("PlanServerBackupcontentWindowsnumberofdatareadersList", jsii.get(self, "windowsnumberofdatareaders"))

    @builtins.property
    @jsii.member(jsii_name="backupsystemstateInput")
    def backupsystemstate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupsystemstateInput"))

    @builtins.property
    @jsii.member(jsii_name="backupsystemstateonlywithfullbackupInput")
    def backupsystemstateonlywithfullbackup_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupsystemstateonlywithfullbackupInput"))

    @builtins.property
    @jsii.member(jsii_name="forceupdatepropertiesInput")
    def forceupdateproperties_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forceupdatepropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="macexcludedpathsInput")
    def macexcludedpaths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "macexcludedpathsInput"))

    @builtins.property
    @jsii.member(jsii_name="macfiltertoexcludepathsInput")
    def macfiltertoexcludepaths_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "macfiltertoexcludepathsInput"))

    @builtins.property
    @jsii.member(jsii_name="macincludedpathsInput")
    def macincludedpaths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "macincludedpathsInput"))

    @builtins.property
    @jsii.member(jsii_name="macnumberofdatareadersInput")
    def macnumberofdatareaders_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentMacnumberofdatareaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentMacnumberofdatareaders]]], jsii.get(self, "macnumberofdatareadersInput"))

    @builtins.property
    @jsii.member(jsii_name="unixexcludedpathsInput")
    def unixexcludedpaths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "unixexcludedpathsInput"))

    @builtins.property
    @jsii.member(jsii_name="unixfiltertoexcludepathsInput")
    def unixfiltertoexcludepaths_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "unixfiltertoexcludepathsInput"))

    @builtins.property
    @jsii.member(jsii_name="unixincludedpathsInput")
    def unixincludedpaths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "unixincludedpathsInput"))

    @builtins.property
    @jsii.member(jsii_name="unixnumberofdatareadersInput")
    def unixnumberofdatareaders_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentUnixnumberofdatareaders"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentUnixnumberofdatareaders"]]], jsii.get(self, "unixnumberofdatareadersInput"))

    @builtins.property
    @jsii.member(jsii_name="usevssforsystemstateInput")
    def usevssforsystemstate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usevssforsystemstateInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsexcludedpathsInput")
    def windowsexcludedpaths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "windowsexcludedpathsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsfiltertoexcludepathsInput")
    def windowsfiltertoexcludepaths_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "windowsfiltertoexcludepathsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsincludedpathsInput")
    def windowsincludedpaths_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "windowsincludedpathsInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsnumberofdatareadersInput")
    def windowsnumberofdatareaders_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentWindowsnumberofdatareaders"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupcontentWindowsnumberofdatareaders"]]], jsii.get(self, "windowsnumberofdatareadersInput"))

    @builtins.property
    @jsii.member(jsii_name="backupsystemstate")
    def backupsystemstate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupsystemstate"))

    @backupsystemstate.setter
    def backupsystemstate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d74a8b49fd532bf7269c89656ad41a9aead8f2d1e4ba34ad7525f9c3fefbff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupsystemstate", value)

    @builtins.property
    @jsii.member(jsii_name="backupsystemstateonlywithfullbackup")
    def backupsystemstateonlywithfullbackup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupsystemstateonlywithfullbackup"))

    @backupsystemstateonlywithfullbackup.setter
    def backupsystemstateonlywithfullbackup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36420f43307b9bff9abbd882e6219f6795a3074490ed4bbd843d29bbe6649b1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupsystemstateonlywithfullbackup", value)

    @builtins.property
    @jsii.member(jsii_name="forceupdateproperties")
    def forceupdateproperties(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceupdateproperties"))

    @forceupdateproperties.setter
    def forceupdateproperties(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b2ee47956e885656856504664e7e9788b9b728184a55d73976af1605347410)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceupdateproperties", value)

    @builtins.property
    @jsii.member(jsii_name="macexcludedpaths")
    def macexcludedpaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "macexcludedpaths"))

    @macexcludedpaths.setter
    def macexcludedpaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38a50469b480c47ab1e7b29351cc0f8468aa180af042e29b9b275e5acd8fef23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macexcludedpaths", value)

    @builtins.property
    @jsii.member(jsii_name="macfiltertoexcludepaths")
    def macfiltertoexcludepaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "macfiltertoexcludepaths"))

    @macfiltertoexcludepaths.setter
    def macfiltertoexcludepaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__808b1fef804fdd04ab87f8be54b4ef63e7b8b3586b9b2e70a6f33629a0c7c167)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macfiltertoexcludepaths", value)

    @builtins.property
    @jsii.member(jsii_name="macincludedpaths")
    def macincludedpaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "macincludedpaths"))

    @macincludedpaths.setter
    def macincludedpaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61ac56330664549c02a4deda4db9168dcdbd58b48e2f9a77c6ae8673f2f2cc5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macincludedpaths", value)

    @builtins.property
    @jsii.member(jsii_name="unixexcludedpaths")
    def unixexcludedpaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "unixexcludedpaths"))

    @unixexcludedpaths.setter
    def unixexcludedpaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf2baea9cfb991be037dcfb05cd83a28ea143c52bac8392f12d0bf2f0e690d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unixexcludedpaths", value)

    @builtins.property
    @jsii.member(jsii_name="unixfiltertoexcludepaths")
    def unixfiltertoexcludepaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "unixfiltertoexcludepaths"))

    @unixfiltertoexcludepaths.setter
    def unixfiltertoexcludepaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26190fe01eaa1ab83fb4e1ad91f64e2f04a74d52345cffa23a5b19e970ffa4da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unixfiltertoexcludepaths", value)

    @builtins.property
    @jsii.member(jsii_name="unixincludedpaths")
    def unixincludedpaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "unixincludedpaths"))

    @unixincludedpaths.setter
    def unixincludedpaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a52c0eb2bb186dbb8fdab989d3841cfa9c7f602d64c6dd823f5d19bae071361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "unixincludedpaths", value)

    @builtins.property
    @jsii.member(jsii_name="usevssforsystemstate")
    def usevssforsystemstate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usevssforsystemstate"))

    @usevssforsystemstate.setter
    def usevssforsystemstate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4973cdd2c81904a8ca989ebc92dff88c280ef18bd0eb4743ab4aa65730a7a3bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usevssforsystemstate", value)

    @builtins.property
    @jsii.member(jsii_name="windowsexcludedpaths")
    def windowsexcludedpaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "windowsexcludedpaths"))

    @windowsexcludedpaths.setter
    def windowsexcludedpaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf5c1c6819aa52e949aad92282248db40842ff02f79782cc9a7d27382759b8f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowsexcludedpaths", value)

    @builtins.property
    @jsii.member(jsii_name="windowsfiltertoexcludepaths")
    def windowsfiltertoexcludepaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "windowsfiltertoexcludepaths"))

    @windowsfiltertoexcludepaths.setter
    def windowsfiltertoexcludepaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccfc14ebdd8eeaa64bd6a3ea5c711b902a0c6d8f8f0df589d6dce0c2c540f45f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowsfiltertoexcludepaths", value)

    @builtins.property
    @jsii.member(jsii_name="windowsincludedpaths")
    def windowsincludedpaths(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "windowsincludedpaths"))

    @windowsincludedpaths.setter
    def windowsincludedpaths(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e28600fdfc558a24c76d1efded989520523807df7cca4e149551a2e89d8fb444)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "windowsincludedpaths", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4238512131820d1d0a1c6f821a67eb63903c14c9eb4341c91f05e230d7c6e48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupcontentUnixnumberofdatareaders",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "useoptimal": "useoptimal"},
)
class PlanServerBackupcontentUnixnumberofdatareaders:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        useoptimal: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Number of data readers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#count PlanServer#count}
        :param useoptimal: Set optimal number of data readers. if it is set to true, count will be ignored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useoptimal PlanServer#useoptimal}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b41ea06ef046a0db9b26b8a76822c591ad8ce55e686fd31e8e4e53cd02750f81)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument useoptimal", value=useoptimal, expected_type=type_hints["useoptimal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if useoptimal is not None:
            self._values["useoptimal"] = useoptimal

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Number of data readers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#count PlanServer#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def useoptimal(self) -> typing.Optional[builtins.str]:
        '''Set optimal number of data readers. if it is set to true, count will be ignored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useoptimal PlanServer#useoptimal}
        '''
        result = self._values.get("useoptimal")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupcontentUnixnumberofdatareaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupcontentUnixnumberofdatareadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentUnixnumberofdatareadersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f130f3b6ef0da73dd66c965eb4841167ccc0fcc855830f3c63958695cf6f917e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupcontentUnixnumberofdatareadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd8bf01fa64bd3f0f0c5c1c8438f5425382d4eb04ce66acbdd254d9dc9003e5a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupcontentUnixnumberofdatareadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c96dda09f259b559e95761b348d2caa831bfc6f242e10602be06c7a7a2c5c6f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1a969ecb96e5b8102b89e4241e327d5b06b2165c7402439a2f81559fd80bed0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3d7fa0d79aed4427734ed8d68367cdc87d49016e335c1e9aa208e150767aa2eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentUnixnumberofdatareaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentUnixnumberofdatareaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentUnixnumberofdatareaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a58b6f09df12f962d6106116ade85881c4d5671269668e2493d334f276a4e75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupcontentUnixnumberofdatareadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentUnixnumberofdatareadersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb73849d9447e2914b61a8e487347ccd4e2bf6f6d30710a9d5bd8a6ca83de0ab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetUseoptimal")
    def reset_useoptimal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseoptimal", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="useoptimalInput")
    def useoptimal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useoptimalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2ed10615abc7c72745f571ee10389393f29a02c62894e6de0f1fc985f7fcf27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="useoptimal")
    def useoptimal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useoptimal"))

    @useoptimal.setter
    def useoptimal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd98d5138836dc4316a40a1419deae32394bef1229372eac5f8739d936e35212)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useoptimal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentUnixnumberofdatareaders]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentUnixnumberofdatareaders]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentUnixnumberofdatareaders]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__308a5483236896d57e4dce6418801036505a58175b52cbdf6ab43d4efe41e11e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupcontentWindowsnumberofdatareaders",
    jsii_struct_bases=[],
    name_mapping={"count": "count", "useoptimal": "useoptimal"},
)
class PlanServerBackupcontentWindowsnumberofdatareaders:
    def __init__(
        self,
        *,
        count: typing.Optional[jsii.Number] = None,
        useoptimal: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param count: Number of data readers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#count PlanServer#count}
        :param useoptimal: Set optimal number of data readers. if it is set to true, count will be ignored. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useoptimal PlanServer#useoptimal}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__571a894648d40a4b3b3e7234d2e95e865c1652a082d112f8b4e61695e66f665a)
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument useoptimal", value=useoptimal, expected_type=type_hints["useoptimal"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if count is not None:
            self._values["count"] = count
        if useoptimal is not None:
            self._values["useoptimal"] = useoptimal

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''Number of data readers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#count PlanServer#count}
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def useoptimal(self) -> typing.Optional[builtins.str]:
        '''Set optimal number of data readers. if it is set to true, count will be ignored.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useoptimal PlanServer#useoptimal}
        '''
        result = self._values.get("useoptimal")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupcontentWindowsnumberofdatareaders(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupcontentWindowsnumberofdatareadersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentWindowsnumberofdatareadersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfce3ad63495d1cdae392858156a1f6a5210835994ac6b92b2d4f882666668ac)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupcontentWindowsnumberofdatareadersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45ae4f059e65c533e89592ef8ddd08f346f8de978db2a7f30bb1f28485c8051f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupcontentWindowsnumberofdatareadersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dba4de29b04d8cb7ce3d3e2121802c0ba6862551b55fd61749866759a62f1f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb4545d368a25d28be8a18a198023798fc0821c57dc7b300419e398edfd45093)
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
            type_hints = typing.get_type_hints(_typecheckingstub__38a7204f0017b6d8c9d91899f1af8481ce77321841dea206d9fcb24195cc12fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentWindowsnumberofdatareaders]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentWindowsnumberofdatareaders]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentWindowsnumberofdatareaders]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8196ebb2e6849e5e40e4f6febee38d5c8afa4d3975c06666698ed2ea974522e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupcontentWindowsnumberofdatareadersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupcontentWindowsnumberofdatareadersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__03b352db9a564de3251efacd4af8fb838328dc956103db6edd7c5fb4e94bb82e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCount")
    def reset_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCount", []))

    @jsii.member(jsii_name="resetUseoptimal")
    def reset_useoptimal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseoptimal", []))

    @builtins.property
    @jsii.member(jsii_name="countInput")
    def count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "countInput"))

    @builtins.property
    @jsii.member(jsii_name="useoptimalInput")
    def useoptimal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useoptimalInput"))

    @builtins.property
    @jsii.member(jsii_name="count")
    def count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "count"))

    @count.setter
    def count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7edb1c99a6ed792b493b3901b9fae4bc05070f2175ebe89926b7910f704246e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "count", value)

    @builtins.property
    @jsii.member(jsii_name="useoptimal")
    def useoptimal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useoptimal"))

    @useoptimal.setter
    def useoptimal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__156403f74b4499af1dd2e2fda4590296c65c3e3fdfad4c1ac28b1fadf5e6b156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useoptimal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentWindowsnumberofdatareaders]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentWindowsnumberofdatareaders]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentWindowsnumberofdatareaders]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e454008eeeef436618964330e52f411f9b22b8e9ad8f6b12ad706d0f7fc85bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinations",
    jsii_struct_bases=[],
    name_mapping={
        "storagepool": "storagepool",
        "backupdestinationname": "backupdestinationname",
        "backupstarttime": "backupstarttime",
        "backupstocopy": "backupstocopy",
        "extendedretentionrules": "extendedretentionrules",
        "fullbackuptypestocopy": "fullbackuptypestocopy",
        "ismirrorcopy": "ismirrorcopy",
        "issnapcopy": "issnapcopy",
        "mappings": "mappings",
        "netappcloudtarget": "netappcloudtarget",
        "optimizeforinstantclone": "optimizeforinstantclone",
        "overrideretentionsettings": "overrideretentionsettings",
        "region": "region",
        "retentionperioddays": "retentionperioddays",
        "retentionruletype": "retentionruletype",
        "snaprecoverypoints": "snaprecoverypoints",
        "sourcecopy": "sourcecopy",
        "storagetype": "storagetype",
        "useextendedretentionrules": "useextendedretentionrules",
    },
)
class PlanServerBackupdestinations:
    def __init__(
        self,
        *,
        storagepool: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsStoragepool", typing.Dict[builtins.str, typing.Any]]]],
        backupdestinationname: typing.Optional[builtins.str] = None,
        backupstarttime: typing.Optional[jsii.Number] = None,
        backupstocopy: typing.Optional[builtins.str] = None,
        extendedretentionrules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsExtendedretentionrules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fullbackuptypestocopy: typing.Optional[builtins.str] = None,
        ismirrorcopy: typing.Optional[builtins.str] = None,
        issnapcopy: typing.Optional[builtins.str] = None,
        mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        netappcloudtarget: typing.Optional[builtins.str] = None,
        optimizeforinstantclone: typing.Optional[builtins.str] = None,
        overrideretentionsettings: typing.Optional[builtins.str] = None,
        region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsRegion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        retentionruletype: typing.Optional[builtins.str] = None,
        snaprecoverypoints: typing.Optional[jsii.Number] = None,
        sourcecopy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsSourcecopy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        storagetype: typing.Optional[builtins.str] = None,
        useextendedretentionrules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param storagepool: storagepool block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#storagepool PlanServer#storagepool}
        :param backupdestinationname: Backup destination details. Enter the name during creation. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinationname PlanServer#backupdestinationname}
        :param backupstarttime: Backup start time in seconds. The time is provided in unix time format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupstarttime PlanServer#backupstarttime}
        :param backupstocopy: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupstocopy PlanServer#backupstocopy}
        :param extendedretentionrules: extendedretentionrules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#extendedretentionrules PlanServer#extendedretentionrules}
        :param fullbackuptypestocopy: Which type of backup type should be copied for the given backup destination when backup type is not all jobs. Default is LAST while adding new backup destination. [FIRST, LAST] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#fullbackuptypestocopy PlanServer#fullbackuptypestocopy}
        :param ismirrorcopy: Is this a mirror copy? Only considered when isSnapCopy is true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#ismirrorcopy PlanServer#ismirrorcopy}
        :param issnapcopy: Is this a snap copy? If isMirrorCopy is not set, then default is Vault/Replica. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#issnapcopy PlanServer#issnapcopy}
        :param mappings: mappings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#mappings PlanServer#mappings}
        :param netappcloudtarget: Only for snap copy. Enabling this changes SVM Mapping to NetApp cloud targets only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#netappcloudtarget PlanServer#netappcloudtarget}
        :param optimizeforinstantclone: Flag to specify if primary storage is copy data management enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#optimizeforinstantclone PlanServer#optimizeforinstantclone}
        :param overrideretentionsettings: Tells if this copy should use storage pool retention period days or the retention defined for this copy. Set as true to use retention defined on this copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overrideretentionsettings PlanServer#overrideretentionsettings}
        :param region: region block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#region PlanServer#region}
        :param retentionperioddays: Retention period in days. -1 can be specified for infinite retention. If this and snapRecoveryPoints both are not specified, this takes precedence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        :param retentionruletype: Which type of retention rule should be used for the given backup destination [RETENTION_PERIOD, SNAP_RECOVERY_POINTS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionruletype PlanServer#retentionruletype}
        :param snaprecoverypoints: Number of snap recovery points for snap copy for retention. Can be specified instead of retention period in Days for snap copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#snaprecoverypoints PlanServer#snaprecoverypoints}
        :param sourcecopy: sourcecopy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#sourcecopy PlanServer#sourcecopy}
        :param storagetype: [ALL, DISK, CLOUD, HYPERSCALE, TAPE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#storagetype PlanServer#storagetype}
        :param useextendedretentionrules: Use extended retention rules. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useextendedretentionrules PlanServer#useextendedretentionrules}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__258ffba03b2d99c22fe184dd52342ab038a1fe903587577398628798b103f06a)
            check_type(argname="argument storagepool", value=storagepool, expected_type=type_hints["storagepool"])
            check_type(argname="argument backupdestinationname", value=backupdestinationname, expected_type=type_hints["backupdestinationname"])
            check_type(argname="argument backupstarttime", value=backupstarttime, expected_type=type_hints["backupstarttime"])
            check_type(argname="argument backupstocopy", value=backupstocopy, expected_type=type_hints["backupstocopy"])
            check_type(argname="argument extendedretentionrules", value=extendedretentionrules, expected_type=type_hints["extendedretentionrules"])
            check_type(argname="argument fullbackuptypestocopy", value=fullbackuptypestocopy, expected_type=type_hints["fullbackuptypestocopy"])
            check_type(argname="argument ismirrorcopy", value=ismirrorcopy, expected_type=type_hints["ismirrorcopy"])
            check_type(argname="argument issnapcopy", value=issnapcopy, expected_type=type_hints["issnapcopy"])
            check_type(argname="argument mappings", value=mappings, expected_type=type_hints["mappings"])
            check_type(argname="argument netappcloudtarget", value=netappcloudtarget, expected_type=type_hints["netappcloudtarget"])
            check_type(argname="argument optimizeforinstantclone", value=optimizeforinstantclone, expected_type=type_hints["optimizeforinstantclone"])
            check_type(argname="argument overrideretentionsettings", value=overrideretentionsettings, expected_type=type_hints["overrideretentionsettings"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument retentionperioddays", value=retentionperioddays, expected_type=type_hints["retentionperioddays"])
            check_type(argname="argument retentionruletype", value=retentionruletype, expected_type=type_hints["retentionruletype"])
            check_type(argname="argument snaprecoverypoints", value=snaprecoverypoints, expected_type=type_hints["snaprecoverypoints"])
            check_type(argname="argument sourcecopy", value=sourcecopy, expected_type=type_hints["sourcecopy"])
            check_type(argname="argument storagetype", value=storagetype, expected_type=type_hints["storagetype"])
            check_type(argname="argument useextendedretentionrules", value=useextendedretentionrules, expected_type=type_hints["useextendedretentionrules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storagepool": storagepool,
        }
        if backupdestinationname is not None:
            self._values["backupdestinationname"] = backupdestinationname
        if backupstarttime is not None:
            self._values["backupstarttime"] = backupstarttime
        if backupstocopy is not None:
            self._values["backupstocopy"] = backupstocopy
        if extendedretentionrules is not None:
            self._values["extendedretentionrules"] = extendedretentionrules
        if fullbackuptypestocopy is not None:
            self._values["fullbackuptypestocopy"] = fullbackuptypestocopy
        if ismirrorcopy is not None:
            self._values["ismirrorcopy"] = ismirrorcopy
        if issnapcopy is not None:
            self._values["issnapcopy"] = issnapcopy
        if mappings is not None:
            self._values["mappings"] = mappings
        if netappcloudtarget is not None:
            self._values["netappcloudtarget"] = netappcloudtarget
        if optimizeforinstantclone is not None:
            self._values["optimizeforinstantclone"] = optimizeforinstantclone
        if overrideretentionsettings is not None:
            self._values["overrideretentionsettings"] = overrideretentionsettings
        if region is not None:
            self._values["region"] = region
        if retentionperioddays is not None:
            self._values["retentionperioddays"] = retentionperioddays
        if retentionruletype is not None:
            self._values["retentionruletype"] = retentionruletype
        if snaprecoverypoints is not None:
            self._values["snaprecoverypoints"] = snaprecoverypoints
        if sourcecopy is not None:
            self._values["sourcecopy"] = sourcecopy
        if storagetype is not None:
            self._values["storagetype"] = storagetype
        if useextendedretentionrules is not None:
            self._values["useextendedretentionrules"] = useextendedretentionrules

    @builtins.property
    def storagepool(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsStoragepool"]]:
        '''storagepool block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#storagepool PlanServer#storagepool}
        '''
        result = self._values.get("storagepool")
        assert result is not None, "Required property 'storagepool' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsStoragepool"]], result)

    @builtins.property
    def backupdestinationname(self) -> typing.Optional[builtins.str]:
        '''Backup destination details. Enter the name during creation.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinationname PlanServer#backupdestinationname}
        '''
        result = self._values.get("backupdestinationname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backupstarttime(self) -> typing.Optional[jsii.Number]:
        '''Backup start time in seconds. The time is provided in unix time format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupstarttime PlanServer#backupstarttime}
        '''
        result = self._values.get("backupstarttime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backupstocopy(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupstocopy PlanServer#backupstocopy}
        '''
        result = self._values.get("backupstocopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extendedretentionrules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrules"]]]:
        '''extendedretentionrules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#extendedretentionrules PlanServer#extendedretentionrules}
        '''
        result = self._values.get("extendedretentionrules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrules"]]], result)

    @builtins.property
    def fullbackuptypestocopy(self) -> typing.Optional[builtins.str]:
        '''Which type of backup type should be copied for the given backup destination when backup type is not all jobs.

        Default is LAST while adding new backup destination. [FIRST, LAST]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#fullbackuptypestocopy PlanServer#fullbackuptypestocopy}
        '''
        result = self._values.get("fullbackuptypestocopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ismirrorcopy(self) -> typing.Optional[builtins.str]:
        '''Is this a mirror copy? Only considered when isSnapCopy is true.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#ismirrorcopy PlanServer#ismirrorcopy}
        '''
        result = self._values.get("ismirrorcopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issnapcopy(self) -> typing.Optional[builtins.str]:
        '''Is this a snap copy? If isMirrorCopy is not set, then default is Vault/Replica.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#issnapcopy PlanServer#issnapcopy}
        '''
        result = self._values.get("issnapcopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mappings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappings"]]]:
        '''mappings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#mappings PlanServer#mappings}
        '''
        result = self._values.get("mappings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappings"]]], result)

    @builtins.property
    def netappcloudtarget(self) -> typing.Optional[builtins.str]:
        '''Only for snap copy. Enabling this changes SVM Mapping  to NetApp cloud targets only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#netappcloudtarget PlanServer#netappcloudtarget}
        '''
        result = self._values.get("netappcloudtarget")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optimizeforinstantclone(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if primary storage is copy data management enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#optimizeforinstantclone PlanServer#optimizeforinstantclone}
        '''
        result = self._values.get("optimizeforinstantclone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overrideretentionsettings(self) -> typing.Optional[builtins.str]:
        '''Tells if this copy should use storage pool retention period days or the retention defined for this copy.

        Set as true to use retention defined on this copy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overrideretentionsettings PlanServer#overrideretentionsettings}
        '''
        result = self._values.get("overrideretentionsettings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsRegion"]]]:
        '''region block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#region PlanServer#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsRegion"]]], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''Retention period in days.

        -1 can be specified for infinite retention. If this and snapRecoveryPoints both are not specified, this takes  precedence.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retentionruletype(self) -> typing.Optional[builtins.str]:
        '''Which type of retention rule should be used for the given backup destination [RETENTION_PERIOD, SNAP_RECOVERY_POINTS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionruletype PlanServer#retentionruletype}
        '''
        result = self._values.get("retentionruletype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snaprecoverypoints(self) -> typing.Optional[jsii.Number]:
        '''Number of snap recovery points for snap copy for retention.

        Can be specified instead of retention period in Days for snap copy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#snaprecoverypoints PlanServer#snaprecoverypoints}
        '''
        result = self._values.get("snaprecoverypoints")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sourcecopy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsSourcecopy"]]]:
        '''sourcecopy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#sourcecopy PlanServer#sourcecopy}
        '''
        result = self._values.get("sourcecopy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsSourcecopy"]]], result)

    @builtins.property
    def storagetype(self) -> typing.Optional[builtins.str]:
        '''[ALL, DISK, CLOUD, HYPERSCALE, TAPE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#storagetype PlanServer#storagetype}
        '''
        result = self._values.get("storagetype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def useextendedretentionrules(self) -> typing.Optional[builtins.str]:
        '''Use extended retention rules.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#useextendedretentionrules PlanServer#useextendedretentionrules}
        '''
        result = self._values.get("useextendedretentionrules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinations(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrules",
    jsii_struct_bases=[],
    name_mapping={
        "firstextendedretentionrule": "firstextendedretentionrule",
        "secondextendedretentionrule": "secondextendedretentionrule",
        "thirdextendedretentionrule": "thirdextendedretentionrule",
    },
)
class PlanServerBackupdestinationsExtendedretentionrules:
    def __init__(
        self,
        *,
        firstextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        thirdextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param firstextendedretentionrule: firstextendedretentionrule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#firstextendedretentionrule PlanServer#firstextendedretentionrule}
        :param secondextendedretentionrule: secondextendedretentionrule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#secondextendedretentionrule PlanServer#secondextendedretentionrule}
        :param thirdextendedretentionrule: thirdextendedretentionrule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#thirdextendedretentionrule PlanServer#thirdextendedretentionrule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39efe4c0d83bbd004534bcc9a89915e887828e6c2965639722cf236975141f87)
            check_type(argname="argument firstextendedretentionrule", value=firstextendedretentionrule, expected_type=type_hints["firstextendedretentionrule"])
            check_type(argname="argument secondextendedretentionrule", value=secondextendedretentionrule, expected_type=type_hints["secondextendedretentionrule"])
            check_type(argname="argument thirdextendedretentionrule", value=thirdextendedretentionrule, expected_type=type_hints["thirdextendedretentionrule"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if firstextendedretentionrule is not None:
            self._values["firstextendedretentionrule"] = firstextendedretentionrule
        if secondextendedretentionrule is not None:
            self._values["secondextendedretentionrule"] = secondextendedretentionrule
        if thirdextendedretentionrule is not None:
            self._values["thirdextendedretentionrule"] = thirdextendedretentionrule

    @builtins.property
    def firstextendedretentionrule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule"]]]:
        '''firstextendedretentionrule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#firstextendedretentionrule PlanServer#firstextendedretentionrule}
        '''
        result = self._values.get("firstextendedretentionrule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule"]]], result)

    @builtins.property
    def secondextendedretentionrule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule"]]]:
        '''secondextendedretentionrule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#secondextendedretentionrule PlanServer#secondextendedretentionrule}
        '''
        result = self._values.get("secondextendedretentionrule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule"]]], result)

    @builtins.property
    def thirdextendedretentionrule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule"]]]:
        '''thirdextendedretentionrule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#thirdextendedretentionrule PlanServer#thirdextendedretentionrule}
        '''
        result = self._values.get("thirdextendedretentionrule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsExtendedretentionrules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule",
    jsii_struct_bases=[],
    name_mapping={
        "isinfiniteretention": "isinfiniteretention",
        "retentionperioddays": "retentionperioddays",
        "type": "type",
    },
)
class PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule:
    def __init__(
        self,
        *,
        isinfiniteretention: typing.Optional[builtins.str] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param isinfiniteretention: If this is set as true, no need to specify retentionPeriodDays. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#isinfiniteretention PlanServer#isinfiniteretention}
        :param retentionperioddays: If this is set, no need to specify isInfiniteRetention as false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        :param type: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#type PlanServer#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8244daf054991252209e4fb6a15bc4b0a14bac18bb00f4ac248fbb17de54b7)
            check_type(argname="argument isinfiniteretention", value=isinfiniteretention, expected_type=type_hints["isinfiniteretention"])
            check_type(argname="argument retentionperioddays", value=retentionperioddays, expected_type=type_hints["retentionperioddays"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if isinfiniteretention is not None:
            self._values["isinfiniteretention"] = isinfiniteretention
        if retentionperioddays is not None:
            self._values["retentionperioddays"] = retentionperioddays
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def isinfiniteretention(self) -> typing.Optional[builtins.str]:
        '''If this is set as true, no need to specify retentionPeriodDays.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#isinfiniteretention PlanServer#isinfiniteretention}
        '''
        result = self._values.get("isinfiniteretention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''If this is set, no need to specify isInfiniteRetention as false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#type PlanServer#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__77b0e706f44b0630de46ebb749e8b23889176a454095f3e6b1648dc76de26120)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358ffae471839e145d25d9a9f11e9ce9032a903f061089facce99fdb988fa141)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ace07633191daa955bec670cd9274a906704324df666150c05d78bfd542e579)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4bcae20428571adc8ad5ed4bd07f8e999f677cf66b10d3e29c56fddd08ab4e9c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e55412b10d71ed57ffc51a5c7ec890fd9feaad105f6fa3860e24c99078a67424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8573f1c61befb25b91011ec1b4ce0faaaa1e901aba3892e5350207875f5183b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__71f990763a347c2c3d694b6f66ba0f2e0fdec029f17a79968c92b987c68ebc9a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsinfiniteretention")
    def reset_isinfiniteretention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsinfiniteretention", []))

    @jsii.member(jsii_name="resetRetentionperioddays")
    def reset_retentionperioddays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionperioddays", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="isinfiniteretentionInput")
    def isinfiniteretention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "isinfiniteretentionInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionperioddaysInput")
    def retentionperioddays_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionperioddaysInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="isinfiniteretention")
    def isinfiniteretention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isinfiniteretention"))

    @isinfiniteretention.setter
    def isinfiniteretention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eaf4e0317f03fa24fe7e010bfbcca2b24019af444e07753eaafced77111c713)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isinfiniteretention", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2870690fb74d046da24d2248757196661bde020c4c467097cf615b0847e007ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4121f9348ca851f15b1a80a755f5f7c3d85f5e47716716d39f683c0aefe9be3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef808f67c17ddb091295e68c38a9b7bbb58417f22e8ee305c5306e8087b5514)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsExtendedretentionrulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0c9ce861c649813a739ce61799e9fa18f5f47bff1a142d6ecc879cd43eb4834)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsExtendedretentionrulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8052b5c9ed63c090c914ddbb07ee43b1ba0fb1c3dc9ddb35f5349ce5e5555fa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsExtendedretentionrulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f010511270d2957497639d15c316d3dbb8535beb2a0d0ee6f32cc9d49e5ae7ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cbd3533811559d058cd4bc283ccfd764fb71a4cd287d3d42f62cdea4d3f6a84)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c6af1052c5b2d98125d73c9ef2c30429836bbe45cafe07d9d18f868e63cc080)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f328238829ef02d2ff4b6c137ff61491ee398d7e62fb99de67d11d138f2a85d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsExtendedretentionrulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__887cbc28e6edeb31476e62595f25af4e54e5ff8313fc952c2ef1a7e700cbb399)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFirstextendedretentionrule")
    def put_firstextendedretentionrule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7faf80aae7782d56142709ea6f4da57ab1bdca9de77a8814fda9b2aaa381eda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFirstextendedretentionrule", [value]))

    @jsii.member(jsii_name="putSecondextendedretentionrule")
    def put_secondextendedretentionrule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63be7903da70d123a0ffe0f7624154382d98bc1cab2cb439b4f8fe748a673bcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondextendedretentionrule", [value]))

    @jsii.member(jsii_name="putThirdextendedretentionrule")
    def put_thirdextendedretentionrule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__064bf76a9c2dbcf9f3f1886211f9bacafd06d04622882e8ba7b339f5d9094306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putThirdextendedretentionrule", [value]))

    @jsii.member(jsii_name="resetFirstextendedretentionrule")
    def reset_firstextendedretentionrule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFirstextendedretentionrule", []))

    @jsii.member(jsii_name="resetSecondextendedretentionrule")
    def reset_secondextendedretentionrule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondextendedretentionrule", []))

    @jsii.member(jsii_name="resetThirdextendedretentionrule")
    def reset_thirdextendedretentionrule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThirdextendedretentionrule", []))

    @builtins.property
    @jsii.member(jsii_name="firstextendedretentionrule")
    def firstextendedretentionrule(
        self,
    ) -> PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleList:
        return typing.cast(PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleList, jsii.get(self, "firstextendedretentionrule"))

    @builtins.property
    @jsii.member(jsii_name="secondextendedretentionrule")
    def secondextendedretentionrule(
        self,
    ) -> "PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleList":
        return typing.cast("PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleList", jsii.get(self, "secondextendedretentionrule"))

    @builtins.property
    @jsii.member(jsii_name="thirdextendedretentionrule")
    def thirdextendedretentionrule(
        self,
    ) -> "PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleList":
        return typing.cast("PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleList", jsii.get(self, "thirdextendedretentionrule"))

    @builtins.property
    @jsii.member(jsii_name="firstextendedretentionruleInput")
    def firstextendedretentionrule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]], jsii.get(self, "firstextendedretentionruleInput"))

    @builtins.property
    @jsii.member(jsii_name="secondextendedretentionruleInput")
    def secondextendedretentionrule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule"]]], jsii.get(self, "secondextendedretentionruleInput"))

    @builtins.property
    @jsii.member(jsii_name="thirdextendedretentionruleInput")
    def thirdextendedretentionrule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule"]]], jsii.get(self, "thirdextendedretentionruleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__621089bb8dd8356987bea6d9590b3cd7619e8e45cae5509c4b6589c173a20030)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule",
    jsii_struct_bases=[],
    name_mapping={
        "isinfiniteretention": "isinfiniteretention",
        "retentionperioddays": "retentionperioddays",
        "type": "type",
    },
)
class PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule:
    def __init__(
        self,
        *,
        isinfiniteretention: typing.Optional[builtins.str] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param isinfiniteretention: If this is set as true, no need to specify retentionPeriodDays. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#isinfiniteretention PlanServer#isinfiniteretention}
        :param retentionperioddays: If this is set, no need to specify isInfiniteRetention as false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        :param type: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#type PlanServer#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41a37839f39207d30239c20d81b9978641a8e65c76c31deb1a9e5808efdf32ea)
            check_type(argname="argument isinfiniteretention", value=isinfiniteretention, expected_type=type_hints["isinfiniteretention"])
            check_type(argname="argument retentionperioddays", value=retentionperioddays, expected_type=type_hints["retentionperioddays"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if isinfiniteretention is not None:
            self._values["isinfiniteretention"] = isinfiniteretention
        if retentionperioddays is not None:
            self._values["retentionperioddays"] = retentionperioddays
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def isinfiniteretention(self) -> typing.Optional[builtins.str]:
        '''If this is set as true, no need to specify retentionPeriodDays.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#isinfiniteretention PlanServer#isinfiniteretention}
        '''
        result = self._values.get("isinfiniteretention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''If this is set, no need to specify isInfiniteRetention as false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#type PlanServer#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8591dccbe51b9ce4001589290b5f8e03cb670ff18d47104d117f547f418d94e3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03add0d57f5c981e58389933e393c9724a53880917a2d27fd88cfe8bda2d09b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03bc8bbd98adde6b6e30fce2558d8af7a8703da427739cf0966bc30f5efc58f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e688a6221c70b01831397993797964944ca2501662e85bbe6ff1069ccaadc97)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4041faee4c7ed6fc96d98f9813445fa0f4bf3d52b2986155f7bcd25c25548fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da1b682e3967f7a253457121cfe4d7769d231628712d90458bb905e859f60ee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__871b25ee5985ec40b87113caaec9f373a36892b87760e34128f3a5fce7757185)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsinfiniteretention")
    def reset_isinfiniteretention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsinfiniteretention", []))

    @jsii.member(jsii_name="resetRetentionperioddays")
    def reset_retentionperioddays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionperioddays", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="isinfiniteretentionInput")
    def isinfiniteretention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "isinfiniteretentionInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionperioddaysInput")
    def retentionperioddays_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionperioddaysInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="isinfiniteretention")
    def isinfiniteretention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isinfiniteretention"))

    @isinfiniteretention.setter
    def isinfiniteretention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4ea83007b494ec76c7031d3b4af7a951702b91d1f0e6b096851b6b5d6efd4d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isinfiniteretention", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__952fe0345002b212e6097eb63eafb13500d5d279f4e76542dd4cf4573d1a2b14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5d88b81b2ca9a5d6bb6707757d5bcedf9f58df0335ec1494771a9afdbd1de91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eaf0391d4b929498663442d85ef9b2d8b1bbeb4827e11f07df2b000e6a5e6924)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule",
    jsii_struct_bases=[],
    name_mapping={
        "isinfiniteretention": "isinfiniteretention",
        "retentionperioddays": "retentionperioddays",
        "type": "type",
    },
)
class PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule:
    def __init__(
        self,
        *,
        isinfiniteretention: typing.Optional[builtins.str] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param isinfiniteretention: If this is set as true, no need to specify retentionPeriodDays. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#isinfiniteretention PlanServer#isinfiniteretention}
        :param retentionperioddays: If this is set, no need to specify isInfiniteRetention as false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        :param type: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#type PlanServer#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da9ebefe1129956b60847990347a76ffd4f5a7848330a166b132ececda04ac3d)
            check_type(argname="argument isinfiniteretention", value=isinfiniteretention, expected_type=type_hints["isinfiniteretention"])
            check_type(argname="argument retentionperioddays", value=retentionperioddays, expected_type=type_hints["retentionperioddays"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if isinfiniteretention is not None:
            self._values["isinfiniteretention"] = isinfiniteretention
        if retentionperioddays is not None:
            self._values["retentionperioddays"] = retentionperioddays
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def isinfiniteretention(self) -> typing.Optional[builtins.str]:
        '''If this is set as true, no need to specify retentionPeriodDays.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#isinfiniteretention PlanServer#isinfiniteretention}
        '''
        result = self._values.get("isinfiniteretention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''If this is set, no need to specify isInfiniteRetention as false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#retentionperioddays PlanServer#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#type PlanServer#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5a406447542819897f479fb1fa93cb0413a727a3c78ffa4c64c1a6b0a22dbd3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__603c08bb9fe1621172f96a62c770ad1c9df302b62d5661f235fc68905d78c6dc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d12ad4c69f03293750317a343cd004018e38678421b0430f89426ba746cab89)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5b3a4465b3c2b36b757504cc9af7c6c6b6d64b7c3477075506a0ed1ed0544f5c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6ae1856698e353b8cceb99e2fa7fa4c1b8044aa6b887c84d4cff6e99a0be8ff9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c63b7bd90c8b556a721852d611942be4f6ccceef4ddab14839758209799482ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__324df69e9d87d594041e84de6e9256be1107fa14dd945f13bdc47930d612ae17)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetIsinfiniteretention")
    def reset_isinfiniteretention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsinfiniteretention", []))

    @jsii.member(jsii_name="resetRetentionperioddays")
    def reset_retentionperioddays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionperioddays", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="isinfiniteretentionInput")
    def isinfiniteretention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "isinfiniteretentionInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionperioddaysInput")
    def retentionperioddays_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionperioddaysInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="isinfiniteretention")
    def isinfiniteretention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "isinfiniteretention"))

    @isinfiniteretention.setter
    def isinfiniteretention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b73f419b138c455e5151fbba84d8b053ae89f349254a59da0277789bb941a233)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isinfiniteretention", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcb735b835f28a0013d200e392266c1e613117c9973c25f882e8f235ca48ed6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bde59bd4d7537590f142edf770f2780a28c67bc84ccc91938ef3e007e0a93514)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0252eb994b154b99dfa3dc6c538da529ecbb260216c8c56a3bdb7279f519977)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5268cb4afe83be9024c2f780dfab25bae272f522c7dd1ae45edf216d9dd0b4f4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerBackupdestinationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d21dbd055a116b6dcbf91c26585e34fd87d3539230d2bb97de29ea89e64f9466)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e205ebf84f44f1182468f99e093fb8f6e453bc231e6ba0401a296565866ed4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a07d84ff964b50b2efe300d727aaa328176c2ebf144cf75842e765f3438084d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e2eb867772f741f5f11a57acc1bad1b3b12fe56dcf4896d625869094bac7645)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinations]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinations]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinations]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__018fc22196b1e2e18d532daddfdebd66d838bfb81a731c7eaa612a22cf1cb71d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappings",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "sourcevendor": "sourcevendor",
        "target": "target",
        "targetvendor": "targetvendor",
        "vendor": "vendor",
    },
)
class PlanServerBackupdestinationsMappings:
    def __init__(
        self,
        *,
        source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsSource", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sourcevendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsSourcevendor", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        targetvendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsTargetvendor", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#source PlanServer#source}
        :param sourcevendor: sourcevendor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#sourcevendor PlanServer#sourcevendor}
        :param target: target block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#target PlanServer#target}
        :param targetvendor: targetvendor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#targetvendor PlanServer#targetvendor}
        :param vendor: Snapshot vendors available for Snap Copy mappings [NETAPP, AMAZON, PURE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#vendor PlanServer#vendor}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40c5c2c255dd061370468c4b500b2843300c6dfd65097fcff8c66dee5b2f4df)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument sourcevendor", value=sourcevendor, expected_type=type_hints["sourcevendor"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument targetvendor", value=targetvendor, expected_type=type_hints["targetvendor"])
            check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if source is not None:
            self._values["source"] = source
        if sourcevendor is not None:
            self._values["sourcevendor"] = sourcevendor
        if target is not None:
            self._values["target"] = target
        if targetvendor is not None:
            self._values["targetvendor"] = targetvendor
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def source(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSource"]]]:
        '''source block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#source PlanServer#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSource"]]], result)

    @builtins.property
    def sourcevendor(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSourcevendor"]]]:
        '''sourcevendor block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#sourcevendor PlanServer#sourcevendor}
        '''
        result = self._values.get("sourcevendor")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSourcevendor"]]], result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTarget"]]]:
        '''target block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#target PlanServer#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTarget"]]], result)

    @builtins.property
    def targetvendor(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTargetvendor"]]]:
        '''targetvendor block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#targetvendor PlanServer#targetvendor}
        '''
        result = self._values.get("targetvendor")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTargetvendor"]]], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''Snapshot vendors available for Snap Copy mappings [NETAPP, AMAZON, PURE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#vendor PlanServer#vendor}
        '''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsMappingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7130e04649484b02f1669df8e4b8569f649830b6b407a6597ba19b2dae3dbf29)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0339fe62522453140bc10692522048ad499d05835bfd7c7de65feadbec01d392)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07e2fa0d34908bdf96ea9dca700bb16b7ea2b189b06957e7dae10059952c2d1b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__16f65894206e77e6d8f37d7bf6c69fa7249e8bc17b30dcac0295d0e6106987a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e91f57470f102df08767506ea7c1c08a880d858b75456677049b24de71a9498e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e4b3658411e319486c96245be63cf45aa5cdf5c010e928f8b75c6161b095c56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsMappingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a3e38c0a3bd1e07f6853849dcbc4ae5e92dc04545dfe7642a745d3c56b22b3c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsSource", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4299d86e45e57952474f0d466d4b02c70e7b9e5fb44d2a2802a1e7340f1c3981)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putSourcevendor")
    def put_sourcevendor(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsSourcevendor", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1d4941ef5fd0459f58487c7675fbf17489c3b34637c637f895729ceff9571f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourcevendor", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee31ef7986024842d685a303402b55bc0fad89877b993b3a7457b5b798818c83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="putTargetvendor")
    def put_targetvendor(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsMappingsTargetvendor", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42eb368e31bb5d53f5a121496aac3fe4dc3a03a34f3516eca1aca620dfeeabd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetvendor", [value]))

    @jsii.member(jsii_name="resetSource")
    def reset_source(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSource", []))

    @jsii.member(jsii_name="resetSourcevendor")
    def reset_sourcevendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcevendor", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetTargetvendor")
    def reset_targetvendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetvendor", []))

    @jsii.member(jsii_name="resetVendor")
    def reset_vendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendor", []))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> "PlanServerBackupdestinationsMappingsSourceList":
        return typing.cast("PlanServerBackupdestinationsMappingsSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="sourcevendor")
    def sourcevendor(self) -> "PlanServerBackupdestinationsMappingsSourcevendorList":
        return typing.cast("PlanServerBackupdestinationsMappingsSourcevendorList", jsii.get(self, "sourcevendor"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "PlanServerBackupdestinationsMappingsTargetList":
        return typing.cast("PlanServerBackupdestinationsMappingsTargetList", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="targetvendor")
    def targetvendor(self) -> "PlanServerBackupdestinationsMappingsTargetvendorList":
        return typing.cast("PlanServerBackupdestinationsMappingsTargetvendorList", jsii.get(self, "targetvendor"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSource"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSource"]]], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcevendorInput")
    def sourcevendor_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSourcevendor"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsSourcevendor"]]], jsii.get(self, "sourcevendorInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTarget"]]], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetvendorInput")
    def targetvendor_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTargetvendor"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsMappingsTargetvendor"]]], jsii.get(self, "targetvendorInput"))

    @builtins.property
    @jsii.member(jsii_name="vendorInput")
    def vendor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendorInput"))

    @builtins.property
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13cbe81886115608b0d93bb116afffd84c8edd5c1913710b3359b85bce4572e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10c896f3908d1967fa37fb64b4b4cab77327d18db2709d771473d823a2e86422)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsSource",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsMappingsSource:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9122b84cb1da4079e6a20836b8680afde23e1b48acf298f087308880f4aafd13)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsMappingsSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsMappingsSourceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsSourceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a3e04fec3d10711cc90905cea5b69bf399304f039cae5b06a009a8af7ec8424)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsMappingsSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4aa65124097e5614c63f21573e905cc18381207810995e4e8f34c60701d48ed6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsMappingsSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__115319e76b85c710c611ad493d7ea3a4f21afa038485f8b07fe94c1290b5c73b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__01660c5ad3c7eb46ab83165a8f067e88798c8db90fee403847cae5583523f9dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__95dd6de5848c19815a17fc039c7bb5d2b6ec8a203a1074256ce6ede422610388)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSource]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b9f109830fd841e85cc1a8a4f90cc279d61868312183ca19028f8f8dfacaa2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsMappingsSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95accfff3aca35f3518034ff4e26011af6880db558f88e8536633cd06610dbcd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb097ccc406db51eee6a9d5f3e7adff8ac0c0055b7afc9af4faf7bc113a1010d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__103afe445ce40509a8c9f7322508d11728d135937709f7b2ff595b407ec0fc22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSource]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSource]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSource]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3ab0bc0e72b07a93cf76ddd21315078e5a8f409b6c00ba2222a86e08afcad3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsSourcevendor",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsMappingsSourcevendor:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a9faeb22bbae4041cf588552a863184537434eb4f79de656af9b7d1b9f8301)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsMappingsSourcevendor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsMappingsSourcevendorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsSourcevendorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2755ad92705e59984ec15c768b22fc61591df0dfef135b0f4e687138ee746629)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsMappingsSourcevendorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a63f35cd8dc2084a46c81d7578ca773b6827fe5a501a2687c1bf13db56080f05)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsMappingsSourcevendorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a836f844abe0b655673f0b4520b119de6a004802f7a085cc9a7e381d146030f7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc9503a8650ef929145ef81a1a1fd559c4bf6e6fe2310ce7b574fa7b334f6373)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7adcf98a7861085d8ed899cca16fc76384441231d43c90bad1de343700ee14c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSourcevendor]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSourcevendor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSourcevendor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afe61124364b1a17352b0b1ee482645df2f1f531200b2d663df75324a073dba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsMappingsSourcevendorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsSourcevendorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f53d3c01e04862eb59d01f97cdd36fa2fd0dc197de0d50a0abcae4d0dd73695)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2627f1ddc8baa98b568863bf4c58c99d51944674a8cf6c9e6c517ba73259dbc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31524071b449429898a84bcb3267841e54148b3ece164cdcfc9c916f871d5d21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSourcevendor]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSourcevendor]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSourcevendor]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33a91969fb9dcb4d6f802ed89fdc471110680a5860f7979cb8f0f42de3bd0235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsTarget",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsMappingsTarget:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df13523a3eb7828abbf38ee31eea861b6a9aec972581f53c15a67bf865ccb40)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsMappingsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsMappingsTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7d64827f740772c63dcbf88b8173564d8a61917882aaf5bafc13ad808a25078)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsMappingsTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b25391f0390ce5d7a009b91a491eb1e85fb2aacef8aea19ee8814e8f878ac14b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsMappingsTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ceb5210e015e86844bb25ccd94dde3bf6579e4329bf451281b8e062edf38024)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a09adcc7e87743d6f31b283e4ee594065dde54cb21ebe0acbf2b9e431d81f3de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b87c9544e572ca04dec1a1d916552019553a5d6de5b13a1e52e573aab62a6273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__403c4bdac9ff0af8ce0f3a5c4c742510e90899702b1681b0b4f0a6356a070a53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsMappingsTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9adc7bac9b21d11dc0588828b1d55b9312b41b5640d0fccac681fa72c4da638b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48784e82676aad499b2916d460251afe83f99222db873b637250ef0918790c3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89088530afbbe4d9ecb49a5725ca0bfb0d2695f478975133682ae28ce056147a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTarget]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTarget]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTarget]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc70fe51d9be22c41800ee08ce56d1c0b802f46f92be5c2ae245e14872a429fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsTargetvendor",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsMappingsTargetvendor:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81b603b5b8260761ffad48b9c4013f03ee7c9d906f05851d45d3716f254b8f84)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsMappingsTargetvendor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsMappingsTargetvendorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsTargetvendorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ea1b7ee3be30dafec674959367b18a804412b2203e855ba89b93446229e502ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsMappingsTargetvendorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929154350963ddcc43e2c22226b338932ff2a09a72477978000ee0e84dc67d6b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsMappingsTargetvendorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dafbfb658b951ba1e49e796a0e1501983e4d0c129b6ef461d6c7e862b9b35be8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c01d66cafd328d6286e2ae896f61180be954fad29e044ca5f4eb269526c6006)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fbac3bf13950499b515c52b42fdecca4260f766bf08f5a6fe6e1b1837aab8aec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTargetvendor]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTargetvendor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTargetvendor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fc1e439a4f12dc34a72132c0d6897d4f6e4dba8bc27f27197d47dc7a757a62e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsMappingsTargetvendorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsMappingsTargetvendorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1700ce19a43ae31c72a8fdca86e38bb935ce8b96da5b12d5bccab9b96667f31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__777dbd0e4af2bef90300dbfda5b54242ce87e92a94babfe59c3b1a744fc064c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fecdf48c7f09fba155ef68b0e01d37d886729638cb6ae5a0bb2f527ed296f22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTargetvendor]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTargetvendor]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTargetvendor]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47a50c71bb3dd719676ee218b36e82465ad8121351c52890582e1fbd6330e48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6df82dbc5d5ca0aaa4bacb88a307dc1a397547ea0a428042b934c206a5340928)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExtendedretentionrules")
    def put_extendedretentionrules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrules, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71274f2a541cc4416ee3ec9c8de7f92d1dd8542a75905b8b6a5ae6bf16368034)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtendedretentionrules", [value]))

    @jsii.member(jsii_name="putMappings")
    def put_mappings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappings, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d771811529bf09876e471394291d69294acb4f7efdd6d01464ad58b9c20070c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMappings", [value]))

    @jsii.member(jsii_name="putRegion")
    def put_region(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsRegion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__942a6a027782807ae98607b35e8c4f714d8a93e49f5406dc9e2d07ca4d1510d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegion", [value]))

    @jsii.member(jsii_name="putSourcecopy")
    def put_sourcecopy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsSourcecopy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a2c7cfd78fce525b646fdd5b69e871f3a3cc3e7773c0b0bcde4fe48cfaa5937)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourcecopy", [value]))

    @jsii.member(jsii_name="putStoragepool")
    def put_storagepool(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerBackupdestinationsStoragepool", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a86c11f11be4c327e380e00183dc04b00565d2a22f49267d4c992acc4b5e43eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStoragepool", [value]))

    @jsii.member(jsii_name="resetBackupdestinationname")
    def reset_backupdestinationname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupdestinationname", []))

    @jsii.member(jsii_name="resetBackupstarttime")
    def reset_backupstarttime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupstarttime", []))

    @jsii.member(jsii_name="resetBackupstocopy")
    def reset_backupstocopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupstocopy", []))

    @jsii.member(jsii_name="resetExtendedretentionrules")
    def reset_extendedretentionrules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedretentionrules", []))

    @jsii.member(jsii_name="resetFullbackuptypestocopy")
    def reset_fullbackuptypestocopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullbackuptypestocopy", []))

    @jsii.member(jsii_name="resetIsmirrorcopy")
    def reset_ismirrorcopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsmirrorcopy", []))

    @jsii.member(jsii_name="resetIssnapcopy")
    def reset_issnapcopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssnapcopy", []))

    @jsii.member(jsii_name="resetMappings")
    def reset_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappings", []))

    @jsii.member(jsii_name="resetNetappcloudtarget")
    def reset_netappcloudtarget(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetappcloudtarget", []))

    @jsii.member(jsii_name="resetOptimizeforinstantclone")
    def reset_optimizeforinstantclone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptimizeforinstantclone", []))

    @jsii.member(jsii_name="resetOverrideretentionsettings")
    def reset_overrideretentionsettings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideretentionsettings", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetRetentionperioddays")
    def reset_retentionperioddays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionperioddays", []))

    @jsii.member(jsii_name="resetRetentionruletype")
    def reset_retentionruletype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionruletype", []))

    @jsii.member(jsii_name="resetSnaprecoverypoints")
    def reset_snaprecoverypoints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnaprecoverypoints", []))

    @jsii.member(jsii_name="resetSourcecopy")
    def reset_sourcecopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcecopy", []))

    @jsii.member(jsii_name="resetStoragetype")
    def reset_storagetype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoragetype", []))

    @jsii.member(jsii_name="resetUseextendedretentionrules")
    def reset_useextendedretentionrules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseextendedretentionrules", []))

    @builtins.property
    @jsii.member(jsii_name="extendedretentionrules")
    def extendedretentionrules(
        self,
    ) -> PlanServerBackupdestinationsExtendedretentionrulesList:
        return typing.cast(PlanServerBackupdestinationsExtendedretentionrulesList, jsii.get(self, "extendedretentionrules"))

    @builtins.property
    @jsii.member(jsii_name="mappings")
    def mappings(self) -> PlanServerBackupdestinationsMappingsList:
        return typing.cast(PlanServerBackupdestinationsMappingsList, jsii.get(self, "mappings"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> "PlanServerBackupdestinationsRegionList":
        return typing.cast("PlanServerBackupdestinationsRegionList", jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="sourcecopy")
    def sourcecopy(self) -> "PlanServerBackupdestinationsSourcecopyList":
        return typing.cast("PlanServerBackupdestinationsSourcecopyList", jsii.get(self, "sourcecopy"))

    @builtins.property
    @jsii.member(jsii_name="storagepool")
    def storagepool(self) -> "PlanServerBackupdestinationsStoragepoolList":
        return typing.cast("PlanServerBackupdestinationsStoragepoolList", jsii.get(self, "storagepool"))

    @builtins.property
    @jsii.member(jsii_name="backupdestinationnameInput")
    def backupdestinationname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupdestinationnameInput"))

    @builtins.property
    @jsii.member(jsii_name="backupstarttimeInput")
    def backupstarttime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupstarttimeInput"))

    @builtins.property
    @jsii.member(jsii_name="backupstocopyInput")
    def backupstocopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupstocopyInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedretentionrulesInput")
    def extendedretentionrules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrules]]], jsii.get(self, "extendedretentionrulesInput"))

    @builtins.property
    @jsii.member(jsii_name="fullbackuptypestocopyInput")
    def fullbackuptypestocopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullbackuptypestocopyInput"))

    @builtins.property
    @jsii.member(jsii_name="ismirrorcopyInput")
    def ismirrorcopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ismirrorcopyInput"))

    @builtins.property
    @jsii.member(jsii_name="issnapcopyInput")
    def issnapcopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issnapcopyInput"))

    @builtins.property
    @jsii.member(jsii_name="mappingsInput")
    def mappings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappings]]], jsii.get(self, "mappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="netappcloudtargetInput")
    def netappcloudtarget_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "netappcloudtargetInput"))

    @builtins.property
    @jsii.member(jsii_name="optimizeforinstantcloneInput")
    def optimizeforinstantclone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optimizeforinstantcloneInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideretentionsettingsInput")
    def overrideretentionsettings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overrideretentionsettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsRegion"]]], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionperioddaysInput")
    def retentionperioddays_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionperioddaysInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionruletypeInput")
    def retentionruletype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionruletypeInput"))

    @builtins.property
    @jsii.member(jsii_name="snaprecoverypointsInput")
    def snaprecoverypoints_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "snaprecoverypointsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcecopyInput")
    def sourcecopy_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsSourcecopy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsSourcecopy"]]], jsii.get(self, "sourcecopyInput"))

    @builtins.property
    @jsii.member(jsii_name="storagepoolInput")
    def storagepool_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsStoragepool"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerBackupdestinationsStoragepool"]]], jsii.get(self, "storagepoolInput"))

    @builtins.property
    @jsii.member(jsii_name="storagetypeInput")
    def storagetype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storagetypeInput"))

    @builtins.property
    @jsii.member(jsii_name="useextendedretentionrulesInput")
    def useextendedretentionrules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useextendedretentionrulesInput"))

    @builtins.property
    @jsii.member(jsii_name="backupdestinationname")
    def backupdestinationname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupdestinationname"))

    @backupdestinationname.setter
    def backupdestinationname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ffdcdb419c99f7074af63686ac7fc88ce2bc4f61afbc9faf95f63efa1e7c9cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupdestinationname", value)

    @builtins.property
    @jsii.member(jsii_name="backupstarttime")
    def backupstarttime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupstarttime"))

    @backupstarttime.setter
    def backupstarttime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5f6348601cb1100e391c40222deb8e4040639b2dd70e12aaad7a506f4301bf7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupstarttime", value)

    @builtins.property
    @jsii.member(jsii_name="backupstocopy")
    def backupstocopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupstocopy"))

    @backupstocopy.setter
    def backupstocopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a106c7f00a8ca94ecd34e8980de1bc4995b2ef9b29a170477b2d02e7fcc52008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupstocopy", value)

    @builtins.property
    @jsii.member(jsii_name="fullbackuptypestocopy")
    def fullbackuptypestocopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullbackuptypestocopy"))

    @fullbackuptypestocopy.setter
    def fullbackuptypestocopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffa9413194f14d7bd3a9833f56abf1e220a023d9911b8f50c7d9d7481bc87a06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullbackuptypestocopy", value)

    @builtins.property
    @jsii.member(jsii_name="ismirrorcopy")
    def ismirrorcopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ismirrorcopy"))

    @ismirrorcopy.setter
    def ismirrorcopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d67c56b5e05bd50c8b5cb886860826aa030261b0306080b6d5cd1bf2de45f78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ismirrorcopy", value)

    @builtins.property
    @jsii.member(jsii_name="issnapcopy")
    def issnapcopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issnapcopy"))

    @issnapcopy.setter
    def issnapcopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df577f64f32a159e93a7d75707ac1e2e03685ad818a7167cea9357215a17f681)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issnapcopy", value)

    @builtins.property
    @jsii.member(jsii_name="netappcloudtarget")
    def netappcloudtarget(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "netappcloudtarget"))

    @netappcloudtarget.setter
    def netappcloudtarget(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0da8c2bd6369831e45d56acd8948080a41caf1051a4d35a46f8201f8590bbb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netappcloudtarget", value)

    @builtins.property
    @jsii.member(jsii_name="optimizeforinstantclone")
    def optimizeforinstantclone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optimizeforinstantclone"))

    @optimizeforinstantclone.setter
    def optimizeforinstantclone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eaddbb682d3019e20a2ccdd5557915bb6c7f139c53e27f235fa9781e902c3b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optimizeforinstantclone", value)

    @builtins.property
    @jsii.member(jsii_name="overrideretentionsettings")
    def overrideretentionsettings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideretentionsettings"))

    @overrideretentionsettings.setter
    def overrideretentionsettings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c0329944b082a570c58ceb037da893c72a1e66d4d832abec69cb14960c9a7f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideretentionsettings", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__620ae7528f34d97f5e590d1ffc34b68a8aecb3745d3cc14a68ffd5a98cff1c88)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="retentionruletype")
    def retentionruletype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionruletype"))

    @retentionruletype.setter
    def retentionruletype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b95c9599463930c4118e32eea2e7f387c439a21624196a1f0c080559dcdf70a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionruletype", value)

    @builtins.property
    @jsii.member(jsii_name="snaprecoverypoints")
    def snaprecoverypoints(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snaprecoverypoints"))

    @snaprecoverypoints.setter
    def snaprecoverypoints(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4dfb6f174dcce3ed6b0268a3a4f24929e6ae65d39f9db8666abbd9e5393a6cfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snaprecoverypoints", value)

    @builtins.property
    @jsii.member(jsii_name="storagetype")
    def storagetype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storagetype"))

    @storagetype.setter
    def storagetype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51acb057c4a81e2f43268acdd676a3700c14f077f2316ad325c6fa1ec34d2301)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagetype", value)

    @builtins.property
    @jsii.member(jsii_name="useextendedretentionrules")
    def useextendedretentionrules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useextendedretentionrules"))

    @useextendedretentionrules.setter
    def useextendedretentionrules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88dc448e05ac7c77b694da1f224296e7cf85e89cf5cef390c0fbd6ab923f6d8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useextendedretentionrules", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinations]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinations]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinations]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c87aa613243dbdfd4b3e35c34dbe6486d79a6956eeeb79ef1db0a7cab3424b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsRegion",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsRegion:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c2931983314dfe1e5c9860a1738f8c2436f5bdcdd182f7390dfd87e0ad2f2d9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsRegionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsRegionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e6c95ceaa5972bbcfcdc74ffd47d1959daf4dd1a489074f7fcd86444410bb1f5)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15c97f071bf6076b8457e15fd37b06145fab42e4b52a1f7a99999f12d12e772e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsRegionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9164db40ab79eaef8a6e49afcb9db03ecd381244070300d020d355bc117a91c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fbbebce14fde6618244ba18f08147174e5510d5d64a19b42f73b625a903dfb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2219afa2084ea2231c0fe2149060967b47af05a96437bb487b32201a99a22081)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsRegion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsRegion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449bc156ebe740473a8d8a8f3fd5d180b54b3e135dd5aaf0b38ab9a914e085e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsRegionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsRegionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__46ad450a2918046151e193f6c7c45633d149cbe0934b6b1f876ff665ae3abc1a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f7b0596168628ec3d4feece5f6ccb590f00258870266d5f54ff770bcaa1d2709)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f0212225c8b4e3f2eb0f0bbc3a6778ccd30e7acea6506e9c2e7d4a7bd0edb28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsRegion]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsRegion]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsRegion]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae1144ad9247f0aa10640f47fb2a4f2222a82df81b0f8ac73d3009b911f807f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsSourcecopy",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsSourcecopy:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40a7e580581f07fdfc34bd2ae4eaf41e807d7e06a9cb120abd4aad28f9e37ebe)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsSourcecopy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsSourcecopyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsSourcecopyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d5609f6d330eb4fae18e9efcbce37f297905f471854ff4e34c17a1ca83c38704)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsSourcecopyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__546aba3d7bae937ae9c50b3b2ba098fc5fdf2ba68e2ede132a62d2b84c1b1b00)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsSourcecopyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9804b45b43fc2ae966694be11fd60e44f681115856a47b68ba7c47c772b744e4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__20cc41cab3fa6f7f6a9d04b09417e4d693baea1ed0b86ee3e003c0f47aa70602)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ec4d452f57f932ec6a3d641d03ed1850a753c4b3a8cffb65f5315d9c02e6e63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsSourcecopy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsSourcecopy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsSourcecopy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a689095a9c169ddbcf5c34540ed2617f4447f17435def94cdb3dd3d24359c042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsSourcecopyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsSourcecopyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__59f0e9ca32767822010f7684b1abd5c9f98eacfcb8d882e02df9e37400ce9390)
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
            type_hints = typing.get_type_hints(_typecheckingstub__30f1a2b2d2d041aeb3b7e0b5ca1f71c7114ffcd4f89a653c36c412bc84046d19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__affeb98c31350fdf586aac1678271766a557c07692b039f63935d70ddbd85a4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsSourcecopy]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsSourcecopy]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsSourcecopy]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ec90847c0589670af9caeae7285e1653fb066c006df96b5b3d5b8603f42589)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerBackupdestinationsStoragepool",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerBackupdestinationsStoragepool:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bf60ca4bb68b7ccb59e0fa1a139791f9891990c2ee5962062b5a4ceec608f6)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerBackupdestinationsStoragepool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerBackupdestinationsStoragepoolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsStoragepoolList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__be7defe2696d39994e3a70803188fb0e1e31c5bb136cd9de25a04e7569ceea53)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerBackupdestinationsStoragepoolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07ec6e9775d60ee123624337178403b841b98cc6465cc64171561cb6a7d1cd36)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerBackupdestinationsStoragepoolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47ddc4bd22cb6c780f30bcae87d2f7e3cda099795e1bb570757c827f0807f75)
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
            type_hints = typing.get_type_hints(_typecheckingstub__84ddd38cbadc5fd8363a68cf32b70dc4d4ff3c7fdd83ea00d361269272b0660f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cc5473d23278565dbd5f209e64e881d44a39e04d7355541fd3e422ad272ec2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsStoragepool]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsStoragepool]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsStoragepool]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed761eb0c705068e1e7a2c91317e1db0358437931968485bc88414a8ab3a394)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerBackupdestinationsStoragepoolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerBackupdestinationsStoragepoolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9be73cb8906a3718d8b85556783fb93c445f61b1a25c63e525038388ee47c4e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1b01f5735c2296142804c42b7a78dbba0d4c99d5ebb3fee76873be1f68e2632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6d2f838b32d3db9f474aa317fb026dfb0407b2ed472fbb2358a433d3461c5f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsStoragepool]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsStoragepool]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsStoragepool]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22708007f9b14360ca08fdaa03775bcf1e6918ccdb8f3ecd551b50b3862dba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "planname": "planname",
        "allowplanoverride": "allowplanoverride",
        "backupcontent": "backupcontent",
        "backupdestinationids": "backupdestinationids",
        "backupdestinations": "backupdestinations",
        "databaseoptions": "databaseoptions",
        "filesystemaddon": "filesystemaddon",
        "id": "id",
        "overrideinheritsettings": "overrideinheritsettings",
        "overriderestrictions": "overriderestrictions",
        "parentplan": "parentplan",
        "regiontoconfigure": "regiontoconfigure",
        "rpo": "rpo",
        "settings": "settings",
        "snapshotoptions": "snapshotoptions",
        "workload": "workload",
    },
)
class PlanServerConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        planname: builtins.str,
        allowplanoverride: typing.Optional[builtins.str] = None,
        backupcontent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontent, typing.Dict[builtins.str, typing.Any]]]]] = None,
        backupdestinationids: typing.Optional[typing.Sequence[jsii.Number]] = None,
        backupdestinations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinations, typing.Dict[builtins.str, typing.Any]]]]] = None,
        databaseoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerDatabaseoptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filesystemaddon: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        overrideinheritsettings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerOverrideinheritsettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        overriderestrictions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerOverriderestrictions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        parentplan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerParentplan", typing.Dict[builtins.str, typing.Any]]]]] = None,
        regiontoconfigure: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRegiontoconfigure", typing.Dict[builtins.str, typing.Any]]]]] = None,
        rpo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpo", typing.Dict[builtins.str, typing.Any]]]]] = None,
        settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        snapshotoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSnapshotoptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        workload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkload", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param planname: Name of the new plan. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#planname PlanServer#planname}
        :param allowplanoverride: Flag to enable overriding of plan. Plan cannot be overriden by default. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#allowplanoverride PlanServer#allowplanoverride}
        :param backupcontent: backupcontent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        :param backupdestinationids: Primary Backup Destination Ids (which were created before plan creation). This is only considered when backupDestinations array object is not defined. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinationids PlanServer#backupdestinationids}
        :param backupdestinations: backupdestinations block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinations PlanServer#backupdestinations}
        :param databaseoptions: databaseoptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#databaseoptions PlanServer#databaseoptions}
        :param filesystemaddon: flag to enable backup content association for applicable file system workload. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#filesystemaddon PlanServer#filesystemaddon}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param overrideinheritsettings: overrideinheritsettings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overrideinheritsettings PlanServer#overrideinheritsettings}
        :param overriderestrictions: overriderestrictions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overriderestrictions PlanServer#overriderestrictions}
        :param parentplan: parentplan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#parentplan PlanServer#parentplan}
        :param regiontoconfigure: regiontoconfigure block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#regiontoconfigure PlanServer#regiontoconfigure}
        :param rpo: rpo block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        :param settings: settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#settings PlanServer#settings}
        :param snapshotoptions: snapshotoptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#snapshotoptions PlanServer#snapshotoptions}
        :param workload: workload block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workload PlanServer#workload}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76feded72711271d1b1cfa41af8aefa1bc233619c1f777c230575bffe6502d71)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument planname", value=planname, expected_type=type_hints["planname"])
            check_type(argname="argument allowplanoverride", value=allowplanoverride, expected_type=type_hints["allowplanoverride"])
            check_type(argname="argument backupcontent", value=backupcontent, expected_type=type_hints["backupcontent"])
            check_type(argname="argument backupdestinationids", value=backupdestinationids, expected_type=type_hints["backupdestinationids"])
            check_type(argname="argument backupdestinations", value=backupdestinations, expected_type=type_hints["backupdestinations"])
            check_type(argname="argument databaseoptions", value=databaseoptions, expected_type=type_hints["databaseoptions"])
            check_type(argname="argument filesystemaddon", value=filesystemaddon, expected_type=type_hints["filesystemaddon"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument overrideinheritsettings", value=overrideinheritsettings, expected_type=type_hints["overrideinheritsettings"])
            check_type(argname="argument overriderestrictions", value=overriderestrictions, expected_type=type_hints["overriderestrictions"])
            check_type(argname="argument parentplan", value=parentplan, expected_type=type_hints["parentplan"])
            check_type(argname="argument regiontoconfigure", value=regiontoconfigure, expected_type=type_hints["regiontoconfigure"])
            check_type(argname="argument rpo", value=rpo, expected_type=type_hints["rpo"])
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument snapshotoptions", value=snapshotoptions, expected_type=type_hints["snapshotoptions"])
            check_type(argname="argument workload", value=workload, expected_type=type_hints["workload"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "planname": planname,
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
        if allowplanoverride is not None:
            self._values["allowplanoverride"] = allowplanoverride
        if backupcontent is not None:
            self._values["backupcontent"] = backupcontent
        if backupdestinationids is not None:
            self._values["backupdestinationids"] = backupdestinationids
        if backupdestinations is not None:
            self._values["backupdestinations"] = backupdestinations
        if databaseoptions is not None:
            self._values["databaseoptions"] = databaseoptions
        if filesystemaddon is not None:
            self._values["filesystemaddon"] = filesystemaddon
        if id is not None:
            self._values["id"] = id
        if overrideinheritsettings is not None:
            self._values["overrideinheritsettings"] = overrideinheritsettings
        if overriderestrictions is not None:
            self._values["overriderestrictions"] = overriderestrictions
        if parentplan is not None:
            self._values["parentplan"] = parentplan
        if regiontoconfigure is not None:
            self._values["regiontoconfigure"] = regiontoconfigure
        if rpo is not None:
            self._values["rpo"] = rpo
        if settings is not None:
            self._values["settings"] = settings
        if snapshotoptions is not None:
            self._values["snapshotoptions"] = snapshotoptions
        if workload is not None:
            self._values["workload"] = workload

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
    def planname(self) -> builtins.str:
        '''Name of the new plan.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#planname PlanServer#planname}
        '''
        result = self._values.get("planname")
        assert result is not None, "Required property 'planname' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowplanoverride(self) -> typing.Optional[builtins.str]:
        '''Flag to enable overriding of plan. Plan cannot be overriden by default.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#allowplanoverride PlanServer#allowplanoverride}
        '''
        result = self._values.get("allowplanoverride")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backupcontent(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontent]]]:
        '''backupcontent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        '''
        result = self._values.get("backupcontent")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontent]]], result)

    @builtins.property
    def backupdestinationids(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Primary Backup Destination Ids (which were created before plan creation).

        This is only considered when backupDestinations array object is not defined.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinationids PlanServer#backupdestinationids}
        '''
        result = self._values.get("backupdestinationids")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def backupdestinations(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinations]]]:
        '''backupdestinations block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestinations PlanServer#backupdestinations}
        '''
        result = self._values.get("backupdestinations")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinations]]], result)

    @builtins.property
    def databaseoptions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerDatabaseoptions"]]]:
        '''databaseoptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#databaseoptions PlanServer#databaseoptions}
        '''
        result = self._values.get("databaseoptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerDatabaseoptions"]]], result)

    @builtins.property
    def filesystemaddon(self) -> typing.Optional[builtins.str]:
        '''flag to enable backup content association for applicable file system workload.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#filesystemaddon PlanServer#filesystemaddon}
        '''
        result = self._values.get("filesystemaddon")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overrideinheritsettings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverrideinheritsettings"]]]:
        '''overrideinheritsettings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overrideinheritsettings PlanServer#overrideinheritsettings}
        '''
        result = self._values.get("overrideinheritsettings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverrideinheritsettings"]]], result)

    @builtins.property
    def overriderestrictions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverriderestrictions"]]]:
        '''overriderestrictions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#overriderestrictions PlanServer#overriderestrictions}
        '''
        result = self._values.get("overriderestrictions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerOverriderestrictions"]]], result)

    @builtins.property
    def parentplan(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerParentplan"]]]:
        '''parentplan block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#parentplan PlanServer#parentplan}
        '''
        result = self._values.get("parentplan")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerParentplan"]]], result)

    @builtins.property
    def regiontoconfigure(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRegiontoconfigure"]]]:
        '''regiontoconfigure block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#regiontoconfigure PlanServer#regiontoconfigure}
        '''
        result = self._values.get("regiontoconfigure")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRegiontoconfigure"]]], result)

    @builtins.property
    def rpo(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpo"]]]:
        '''rpo block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        '''
        result = self._values.get("rpo")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpo"]]], result)

    @builtins.property
    def settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSettings"]]]:
        '''settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#settings PlanServer#settings}
        '''
        result = self._values.get("settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSettings"]]], result)

    @builtins.property
    def snapshotoptions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSnapshotoptions"]]]:
        '''snapshotoptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#snapshotoptions PlanServer#snapshotoptions}
        '''
        result = self._values.get("snapshotoptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSnapshotoptions"]]], result)

    @builtins.property
    def workload(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkload"]]]:
        '''workload block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workload PlanServer#workload}
        '''
        result = self._values.get("workload")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkload"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerDatabaseoptions",
    jsii_struct_bases=[],
    name_mapping={
        "commitfrequencyinhours": "commitfrequencyinhours",
        "logbackuprpomins": "logbackuprpomins",
        "runfullbackupevery": "runfullbackupevery",
        "usediskcacheforlogbackups": "usediskcacheforlogbackups",
    },
)
class PlanServerDatabaseoptions:
    def __init__(
        self,
        *,
        commitfrequencyinhours: typing.Optional[jsii.Number] = None,
        logbackuprpomins: typing.Optional[jsii.Number] = None,
        runfullbackupevery: typing.Optional[jsii.Number] = None,
        usediskcacheforlogbackups: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param commitfrequencyinhours: Commit frequency in hours. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#commitfrequencyinhours PlanServer#commitfrequencyinhours}
        :param logbackuprpomins: Log backup RPO in minutes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#logbackuprpomins PlanServer#logbackuprpomins}
        :param runfullbackupevery: Full backup frequency in days. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#runfullbackupevery PlanServer#runfullbackupevery}
        :param usediskcacheforlogbackups: Use disk cache for log backups. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usediskcacheforlogbackups PlanServer#usediskcacheforlogbackups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46ac10c2c4acae61e266263c28e001ce39a2f728e253d7bf4c5f328644afc141)
            check_type(argname="argument commitfrequencyinhours", value=commitfrequencyinhours, expected_type=type_hints["commitfrequencyinhours"])
            check_type(argname="argument logbackuprpomins", value=logbackuprpomins, expected_type=type_hints["logbackuprpomins"])
            check_type(argname="argument runfullbackupevery", value=runfullbackupevery, expected_type=type_hints["runfullbackupevery"])
            check_type(argname="argument usediskcacheforlogbackups", value=usediskcacheforlogbackups, expected_type=type_hints["usediskcacheforlogbackups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if commitfrequencyinhours is not None:
            self._values["commitfrequencyinhours"] = commitfrequencyinhours
        if logbackuprpomins is not None:
            self._values["logbackuprpomins"] = logbackuprpomins
        if runfullbackupevery is not None:
            self._values["runfullbackupevery"] = runfullbackupevery
        if usediskcacheforlogbackups is not None:
            self._values["usediskcacheforlogbackups"] = usediskcacheforlogbackups

    @builtins.property
    def commitfrequencyinhours(self) -> typing.Optional[jsii.Number]:
        '''Commit frequency in hours.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#commitfrequencyinhours PlanServer#commitfrequencyinhours}
        '''
        result = self._values.get("commitfrequencyinhours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def logbackuprpomins(self) -> typing.Optional[jsii.Number]:
        '''Log backup RPO in minutes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#logbackuprpomins PlanServer#logbackuprpomins}
        '''
        result = self._values.get("logbackuprpomins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def runfullbackupevery(self) -> typing.Optional[jsii.Number]:
        '''Full backup frequency in days.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#runfullbackupevery PlanServer#runfullbackupevery}
        '''
        result = self._values.get("runfullbackupevery")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def usediskcacheforlogbackups(self) -> typing.Optional[builtins.str]:
        '''Use disk cache for log backups.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usediskcacheforlogbackups PlanServer#usediskcacheforlogbackups}
        '''
        result = self._values.get("usediskcacheforlogbackups")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerDatabaseoptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerDatabaseoptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerDatabaseoptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9ef80805d6aea0575ac696fb025a5ef499f1f9050d87e6aa169e868d57e87f28)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerDatabaseoptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23719ca37a40adf456b288784daa8858c2e0ba7bae3cfafb57150858d0006d22)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerDatabaseoptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__859544551ea4362ec769b6671db1d9edb5be91b8061246c1ae1a8786144ae0c4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f603f636553eb78479d8b2757b4253f66d8910e14ab11e21a96959277980bda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bbb7d4c9329b56bf5aa392be3e1f48bb4460dc3e6a432610846b96758857ff3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerDatabaseoptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerDatabaseoptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerDatabaseoptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de1e5e99462b4bd4dbd4c1b969ecf2d0c2b3eecde5d3e84f2037ef28b3bd7260)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerDatabaseoptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerDatabaseoptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d6d41e24f63d40b082c817cc5859639f8b70193d7dfefab85fafcf01ae61935)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCommitfrequencyinhours")
    def reset_commitfrequencyinhours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitfrequencyinhours", []))

    @jsii.member(jsii_name="resetLogbackuprpomins")
    def reset_logbackuprpomins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogbackuprpomins", []))

    @jsii.member(jsii_name="resetRunfullbackupevery")
    def reset_runfullbackupevery(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunfullbackupevery", []))

    @jsii.member(jsii_name="resetUsediskcacheforlogbackups")
    def reset_usediskcacheforlogbackups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsediskcacheforlogbackups", []))

    @builtins.property
    @jsii.member(jsii_name="commitfrequencyinhoursInput")
    def commitfrequencyinhours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "commitfrequencyinhoursInput"))

    @builtins.property
    @jsii.member(jsii_name="logbackuprpominsInput")
    def logbackuprpomins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "logbackuprpominsInput"))

    @builtins.property
    @jsii.member(jsii_name="runfullbackupeveryInput")
    def runfullbackupevery_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "runfullbackupeveryInput"))

    @builtins.property
    @jsii.member(jsii_name="usediskcacheforlogbackupsInput")
    def usediskcacheforlogbackups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usediskcacheforlogbackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="commitfrequencyinhours")
    def commitfrequencyinhours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "commitfrequencyinhours"))

    @commitfrequencyinhours.setter
    def commitfrequencyinhours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__677e3014b29d1739ed63474f51049530fe59d7d05530299c0295c7e06132daef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitfrequencyinhours", value)

    @builtins.property
    @jsii.member(jsii_name="logbackuprpomins")
    def logbackuprpomins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "logbackuprpomins"))

    @logbackuprpomins.setter
    def logbackuprpomins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cfaa3576c7dc710b8319b2546af2d4d30b59f983748e5da557181aad9ed8d5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logbackuprpomins", value)

    @builtins.property
    @jsii.member(jsii_name="runfullbackupevery")
    def runfullbackupevery(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "runfullbackupevery"))

    @runfullbackupevery.setter
    def runfullbackupevery(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60897e38c923a1ccb696ea62ad86ab10f9a76532dfc2d00b5093e30869fd8b71)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runfullbackupevery", value)

    @builtins.property
    @jsii.member(jsii_name="usediskcacheforlogbackups")
    def usediskcacheforlogbackups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usediskcacheforlogbackups"))

    @usediskcacheforlogbackups.setter
    def usediskcacheforlogbackups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a034358651df09af2f406649116e37f45eedc9065efc69560b7f7c901752121d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usediskcacheforlogbackups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerDatabaseoptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerDatabaseoptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerDatabaseoptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09c580bec69b45c450f9449619150b24ed7b18f30f01eb6c60fa142b9bf9eaff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerOverrideinheritsettings",
    jsii_struct_bases=[],
    name_mapping={
        "backupcontent": "backupcontent",
        "backupdestination": "backupdestination",
        "rpo": "rpo",
    },
)
class PlanServerOverrideinheritsettings:
    def __init__(
        self,
        *,
        backupcontent: typing.Optional[builtins.str] = None,
        backupdestination: typing.Optional[builtins.str] = None,
        rpo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backupcontent: Flag to specify if parent or derived plan backupContent should be used when inherit mode is optional. True - derived, False - Base. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        :param backupdestination: Flag to specify if parent or derived plan backupDestination should be used when inherit mode is optional. True - derived, False - Base. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestination PlanServer#backupdestination}
        :param rpo: Flag to specify if parent or derived plan rpo should be used when inherit mode is optional. True - derived, False - Base. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61085a2b61be3a2ea6865ae98eab9c8daa2cf8b35db548053a3f3a58b5258082)
            check_type(argname="argument backupcontent", value=backupcontent, expected_type=type_hints["backupcontent"])
            check_type(argname="argument backupdestination", value=backupdestination, expected_type=type_hints["backupdestination"])
            check_type(argname="argument rpo", value=rpo, expected_type=type_hints["rpo"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupcontent is not None:
            self._values["backupcontent"] = backupcontent
        if backupdestination is not None:
            self._values["backupdestination"] = backupdestination
        if rpo is not None:
            self._values["rpo"] = rpo

    @builtins.property
    def backupcontent(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if parent or derived plan backupContent should be used when inherit mode is optional.

        True - derived, False - Base.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        '''
        result = self._values.get("backupcontent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backupdestination(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if parent or derived plan backupDestination should be used when inherit mode is optional.

        True - derived, False - Base.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupdestination PlanServer#backupdestination}
        '''
        result = self._values.get("backupdestination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rpo(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if parent or derived plan rpo should be used when inherit mode is optional.

        True - derived, False - Base.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        '''
        result = self._values.get("rpo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerOverrideinheritsettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerOverrideinheritsettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerOverrideinheritsettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3c783987823e186bf26f067b9946778906fd927fc25389cd3e8b4a0637aed88)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerOverrideinheritsettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43bb1efd5abbea2debfb54cabba71c0e642387f5056d59e9f917b7548792a117)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerOverrideinheritsettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__092be14e27429621558eae49b47c170c7756259356500711b21ccce604f94cd7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ace07cea9d6c4f925cbe3fe04604ede0546b0c8cf3cd9120f6d03f1a149d289f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__abaac4437986154d8bcf700316e739f8facc9cbec3cd1dce8f0637213e9ad077)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverrideinheritsettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverrideinheritsettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverrideinheritsettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6c5ff5d832fba023f90747ee876ca17eb883c782ff1378246792fb2314eaab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerOverrideinheritsettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerOverrideinheritsettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a3125abd9eb46fe7b9e39ebb7d290a0def8a863f2c80bb734c21fa791d6402a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackupcontent")
    def reset_backupcontent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupcontent", []))

    @jsii.member(jsii_name="resetBackupdestination")
    def reset_backupdestination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupdestination", []))

    @jsii.member(jsii_name="resetRpo")
    def reset_rpo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRpo", []))

    @builtins.property
    @jsii.member(jsii_name="backupcontentInput")
    def backupcontent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupcontentInput"))

    @builtins.property
    @jsii.member(jsii_name="backupdestinationInput")
    def backupdestination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupdestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="rpoInput")
    def rpo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rpoInput"))

    @builtins.property
    @jsii.member(jsii_name="backupcontent")
    def backupcontent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupcontent"))

    @backupcontent.setter
    def backupcontent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c5304022ab6abd3b2de21449e2ecb40e0a193cbd937638ee1a032b021489932)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupcontent", value)

    @builtins.property
    @jsii.member(jsii_name="backupdestination")
    def backupdestination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupdestination"))

    @backupdestination.setter
    def backupdestination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a01759c401c5f2bfe07bfcc809537462d190fc0c0a215437648fd9269535014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupdestination", value)

    @builtins.property
    @jsii.member(jsii_name="rpo")
    def rpo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rpo"))

    @rpo.setter
    def rpo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ea66a31d47c81e89f609d7ce665a6e835cbbb531a34dbe1fca11d0440a632c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rpo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverrideinheritsettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverrideinheritsettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverrideinheritsettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f77e348a676d5f11434d7f0454caa61d91f2ed4277be824f9b1c72b075e30307)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerOverriderestrictions",
    jsii_struct_bases=[],
    name_mapping={
        "backupcontent": "backupcontent",
        "rpo": "rpo",
        "storagepool": "storagepool",
    },
)
class PlanServerOverriderestrictions:
    def __init__(
        self,
        *,
        backupcontent: typing.Optional[builtins.str] = None,
        rpo: typing.Optional[builtins.str] = None,
        storagepool: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backupcontent: [OPTIONAL, MUST, NOT_ALLOWED]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        :param rpo: [OPTIONAL, MUST, NOT_ALLOWED]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        :param storagepool: [OPTIONAL, MUST, NOT_ALLOWED]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#storagepool PlanServer#storagepool}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f652a9d1789c1b52042b9015955773a25b8025d1d27671e84f26698b3a297fba)
            check_type(argname="argument backupcontent", value=backupcontent, expected_type=type_hints["backupcontent"])
            check_type(argname="argument rpo", value=rpo, expected_type=type_hints["rpo"])
            check_type(argname="argument storagepool", value=storagepool, expected_type=type_hints["storagepool"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupcontent is not None:
            self._values["backupcontent"] = backupcontent
        if rpo is not None:
            self._values["rpo"] = rpo
        if storagepool is not None:
            self._values["storagepool"] = storagepool

    @builtins.property
    def backupcontent(self) -> typing.Optional[builtins.str]:
        '''[OPTIONAL, MUST, NOT_ALLOWED].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcontent PlanServer#backupcontent}
        '''
        result = self._values.get("backupcontent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rpo(self) -> typing.Optional[builtins.str]:
        '''[OPTIONAL, MUST, NOT_ALLOWED].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#rpo PlanServer#rpo}
        '''
        result = self._values.get("rpo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storagepool(self) -> typing.Optional[builtins.str]:
        '''[OPTIONAL, MUST, NOT_ALLOWED].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#storagepool PlanServer#storagepool}
        '''
        result = self._values.get("storagepool")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerOverriderestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerOverriderestrictionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerOverriderestrictionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__94e0a2acca73eca6d960494904a26f8312dbd280361cdfca32f8afcdbb4b4897)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerOverriderestrictionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3b81bc31fc3bbd4e1d43e530ec46c03151581bfe4233ef58b62cd10166f3e0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerOverriderestrictionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1bfe40ebfe2dee7dff892d34d1ae1062d4d04fc98e28a733c7c5b6fd4517676)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b5da47e67413a17d4cad9d273530ef0377a7f1f9914bb57a1f40c76f7896c630)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6e3b673d500d7290e6c5584325deb9ac39d26f203cde24d70b914d451faca1e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverriderestrictions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverriderestrictions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverriderestrictions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d5a465f80c1b55aa732b8f3c3fcdfd05ce47c4833bff2035ce6bc56f19fa901)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerOverriderestrictionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerOverriderestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a0a0429dd8d4bbb5fef2ee071cec4fbad4c647f91aff06d09f91018431ab815f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackupcontent")
    def reset_backupcontent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupcontent", []))

    @jsii.member(jsii_name="resetRpo")
    def reset_rpo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRpo", []))

    @jsii.member(jsii_name="resetStoragepool")
    def reset_storagepool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoragepool", []))

    @builtins.property
    @jsii.member(jsii_name="backupcontentInput")
    def backupcontent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupcontentInput"))

    @builtins.property
    @jsii.member(jsii_name="rpoInput")
    def rpo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rpoInput"))

    @builtins.property
    @jsii.member(jsii_name="storagepoolInput")
    def storagepool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storagepoolInput"))

    @builtins.property
    @jsii.member(jsii_name="backupcontent")
    def backupcontent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupcontent"))

    @backupcontent.setter
    def backupcontent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3eb1eb884aeebf216c3a7b288f136c676bb2d64440d453a933276cfcf987ffd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupcontent", value)

    @builtins.property
    @jsii.member(jsii_name="rpo")
    def rpo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rpo"))

    @rpo.setter
    def rpo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d0c1487dc3a628ce1950192378c90d39ca8adc24e48d4cd9c361f377dc295cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rpo", value)

    @builtins.property
    @jsii.member(jsii_name="storagepool")
    def storagepool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storagepool"))

    @storagepool.setter
    def storagepool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d143a43230dd5ee8ed269cf3f9c8d283ba3f55ab66ea4d66a88138d54455990)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagepool", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverriderestrictions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverriderestrictions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverriderestrictions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__518555a3322d910d88d139d4c23df3289e26ccd15f6d9d808855efb8d9ddab73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerParentplan",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerParentplan:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae3e3288e82107f7d2c00b982611bc1979db134a6a97da862640e92a49a5383d)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerParentplan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerParentplanList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerParentplanList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6a7b56c08685a5155df8d76f556fa2c0e345cd33e785b790a806d2261775486)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerParentplanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4fd7a25b33c2afc2a74eef930113e4bfaa55ac4200b30e5d1dc7ad700a74a42)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerParentplanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4be5ee074fefcb763f8117c586ada3981582ba6007b3da566f564f1446cf1ed5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a11d1e7154f666982529a486758c516347acb5eceeb61ee0e99430c0d2ae1cb1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__677500c0b7b6044e572bacec2ada747a88a6dd4ff52bd58b3ab2b0c0eb0a0d90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerParentplan]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerParentplan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerParentplan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__938a7717e9d1d95a0b5e0dbe96e856df1712c2b80bd6795a4d09e2b6dd9c0d05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerParentplanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerParentplanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c84590aee3b9497be998e9d063cfdd0d2aba7ff570f823d0a7e0d38c66b5d1e7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4be75b3c06e01af3c444ff73c78905cbb90eacce760dc0b0d426584400ede0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4a5602dc9357888a6e545739127b0177b9dac48789b7c8e4e7c17d67555006c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerParentplan]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerParentplan]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerParentplan]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6e970c0caa2be585cd7d9c250ef226d06d663ad44a42470494127d1e892e2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRegiontoconfigure",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerRegiontoconfigure:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22652de400f37797844af1262aa3d2662c5ecadc4a96a76f85f55d76c29ece90)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRegiontoconfigure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRegiontoconfigureList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRegiontoconfigureList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa546b00d34920a0bd68c6557d350143dd1855f1297de3f91fb173feef7cc8dd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerRegiontoconfigureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac270dc0f7867ffbf77ea05db2c23ff27423c13526bb57a494ca27de852ae5b8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRegiontoconfigureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfe6fa96a59c50646cd2d3a62f060d9f6257facf328f3c398e628bbdc804f473)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c564c1c341e64ce3b6670bbeb242bbd3e9b923054aa9a9d1768ae32e0ab4d3ed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7b81d6b54d26815653000290ba678c366c9b1ea4cd079c01db8bb4bc9f156a9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRegiontoconfigure]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRegiontoconfigure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRegiontoconfigure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6614e725084ec52a8a7858ef9b65b0f6a2205d6e65b729bf118514ccbedd96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRegiontoconfigureOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRegiontoconfigureOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__99f01a1783a0fbea57f7dfca1995ccde78b19a1a95f2d6d6f843ea875ecae2de)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f09b6a2ae06ac92642047a754ce662e8d13c6188b94acfb9c447603f84455cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a437ea5934478aa532b6ef1e60a4f94e1cf046ca701a205ec6e32317aa05b7b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRegiontoconfigure]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRegiontoconfigure]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRegiontoconfigure]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a3b1f33e8d2685fc423d44c1553093d476ae442ce7cc5bbcacfa86706704cad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpo",
    jsii_struct_bases=[],
    name_mapping={
        "backupfrequency": "backupfrequency",
        "backupwindow": "backupwindow",
        "fullbackupwindow": "fullbackupwindow",
        "sla": "sla",
    },
)
class PlanServerRpo:
    def __init__(
        self,
        *,
        backupfrequency: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequency", typing.Dict[builtins.str, typing.Any]]]]] = None,
        backupwindow: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupwindow", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fullbackupwindow: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoFullbackupwindow", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sla: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoSla", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backupfrequency: backupfrequency block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupfrequency PlanServer#backupfrequency}
        :param backupwindow: backupwindow block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupwindow PlanServer#backupwindow}
        :param fullbackupwindow: fullbackupwindow block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#fullbackupwindow PlanServer#fullbackupwindow}
        :param sla: sla block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#sla PlanServer#sla}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d6d4c609bdc343d6ec4e650f8d31db95cafb260dfd69713d1890f49c02957d2)
            check_type(argname="argument backupfrequency", value=backupfrequency, expected_type=type_hints["backupfrequency"])
            check_type(argname="argument backupwindow", value=backupwindow, expected_type=type_hints["backupwindow"])
            check_type(argname="argument fullbackupwindow", value=fullbackupwindow, expected_type=type_hints["fullbackupwindow"])
            check_type(argname="argument sla", value=sla, expected_type=type_hints["sla"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupfrequency is not None:
            self._values["backupfrequency"] = backupfrequency
        if backupwindow is not None:
            self._values["backupwindow"] = backupwindow
        if fullbackupwindow is not None:
            self._values["fullbackupwindow"] = fullbackupwindow
        if sla is not None:
            self._values["sla"] = sla

    @builtins.property
    def backupfrequency(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequency"]]]:
        '''backupfrequency block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupfrequency PlanServer#backupfrequency}
        '''
        result = self._values.get("backupfrequency")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequency"]]], result)

    @builtins.property
    def backupwindow(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupwindow"]]]:
        '''backupwindow block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupwindow PlanServer#backupwindow}
        '''
        result = self._values.get("backupwindow")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupwindow"]]], result)

    @builtins.property
    def fullbackupwindow(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoFullbackupwindow"]]]:
        '''fullbackupwindow block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#fullbackupwindow PlanServer#fullbackupwindow}
        '''
        result = self._values.get("fullbackupwindow")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoFullbackupwindow"]]], result)

    @builtins.property
    def sla(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoSla"]]]:
        '''sla block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#sla PlanServer#sla}
        '''
        result = self._values.get("sla")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoSla"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequency",
    jsii_struct_bases=[],
    name_mapping={"schedules": "schedules"},
)
class PlanServerRpoBackupfrequency:
    def __init__(
        self,
        *,
        schedules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedules", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param schedules: schedules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedules PlanServer#schedules}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6772b97f61f9047b1d6b514027bba1a7502b7673cb9cdb2edde3c1e91b3dede)
            check_type(argname="argument schedules", value=schedules, expected_type=type_hints["schedules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if schedules is not None:
            self._values["schedules"] = schedules

    @builtins.property
    def schedules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedules"]]]:
        '''schedules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedules PlanServer#schedules}
        '''
        result = self._values.get("schedules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupfrequency(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoBackupfrequencyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__363eeb52ad3fdb939cb89f32af0cd2369c4a861ebe0e64c03ad2b158e21ef388)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerRpoBackupfrequencyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13b322065e99d3dda0697617614ed6fdbc7b4e1cd3b1c967473c9733c064c965)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupfrequencyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057ddb67514e54270e7b61bc44200c985336be7a570a12961f555d69c1cf9c81)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b1a3a79b06b8fa344ffefd2796265dca443511ef46cb2baed499cbc6108a32e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eea7979b805c22f9c642de50838dee7ffcd9c7d61218e23f462b739d5c2e17df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequency]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequency]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequency]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a352bbcea08e5e25e0cc5eb3efe5fa3179621f448ebbae97d765656edfc671f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__da32781722328c96f5ae1463625ca6c0bd0b0b841aa87ec057b938cc06c795df)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSchedules")
    def put_schedules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__010e78892812e809b68fd1e8af66447dc903dcee25300eacaa179d24017c1a5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchedules", [value]))

    @jsii.member(jsii_name="resetSchedules")
    def reset_schedules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedules", []))

    @builtins.property
    @jsii.member(jsii_name="schedules")
    def schedules(self) -> "PlanServerRpoBackupfrequencySchedulesList":
        return typing.cast("PlanServerRpoBackupfrequencySchedulesList", jsii.get(self, "schedules"))

    @builtins.property
    @jsii.member(jsii_name="schedulesInput")
    def schedules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedules"]]], jsii.get(self, "schedulesInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequency]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequency]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequency]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ea9ed7f96291b02ef10f99b2ebfa17c06bc72d4a19f0ff250c90ef1712a57a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedules",
    jsii_struct_bases=[],
    name_mapping={
        "backuptype": "backuptype",
        "schedulename": "schedulename",
        "schedulepattern": "schedulepattern",
        "fordatabasesonly": "fordatabasesonly",
        "scheduleoption": "scheduleoption",
        "vmoperationtype": "vmoperationtype",
    },
)
class PlanServerRpoBackupfrequencySchedules:
    def __init__(
        self,
        *,
        backuptype: builtins.str,
        schedulename: builtins.str,
        schedulepattern: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesSchedulepattern", typing.Dict[builtins.str, typing.Any]]]],
        fordatabasesonly: typing.Optional[builtins.str] = None,
        scheduleoption: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesScheduleoption", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vmoperationtype: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backuptype: Schedule Backup level [FULL, INCREMENTAL, DIFFERENTIAL, SYNTHETICFULL, TRANSACTIONLOG]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backuptype PlanServer#backuptype}
        :param schedulename: Name of the schedule, for modify. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedulename PlanServer#schedulename}
        :param schedulepattern: schedulepattern block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedulepattern PlanServer#schedulepattern}
        :param fordatabasesonly: Boolean to indicate if schedule is for database agents. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#fordatabasesonly PlanServer#fordatabasesonly}
        :param scheduleoption: scheduleoption block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#scheduleoption PlanServer#scheduleoption}
        :param vmoperationtype: Type of DR operation (only applicable for Failover groups) [PLANNED_FAILOVER, TEST_BOOT]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#vmoperationtype PlanServer#vmoperationtype}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be745b4802565b3ebbdcfb33311c92a076a5d9b0d25ed34456008f1c3a038b9e)
            check_type(argname="argument backuptype", value=backuptype, expected_type=type_hints["backuptype"])
            check_type(argname="argument schedulename", value=schedulename, expected_type=type_hints["schedulename"])
            check_type(argname="argument schedulepattern", value=schedulepattern, expected_type=type_hints["schedulepattern"])
            check_type(argname="argument fordatabasesonly", value=fordatabasesonly, expected_type=type_hints["fordatabasesonly"])
            check_type(argname="argument scheduleoption", value=scheduleoption, expected_type=type_hints["scheduleoption"])
            check_type(argname="argument vmoperationtype", value=vmoperationtype, expected_type=type_hints["vmoperationtype"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "backuptype": backuptype,
            "schedulename": schedulename,
            "schedulepattern": schedulepattern,
        }
        if fordatabasesonly is not None:
            self._values["fordatabasesonly"] = fordatabasesonly
        if scheduleoption is not None:
            self._values["scheduleoption"] = scheduleoption
        if vmoperationtype is not None:
            self._values["vmoperationtype"] = vmoperationtype

    @builtins.property
    def backuptype(self) -> builtins.str:
        '''Schedule Backup level [FULL, INCREMENTAL, DIFFERENTIAL, SYNTHETICFULL, TRANSACTIONLOG].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backuptype PlanServer#backuptype}
        '''
        result = self._values.get("backuptype")
        assert result is not None, "Required property 'backuptype' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedulename(self) -> builtins.str:
        '''Name of the schedule, for modify.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedulename PlanServer#schedulename}
        '''
        result = self._values.get("schedulename")
        assert result is not None, "Required property 'schedulename' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedulepattern(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepattern"]]:
        '''schedulepattern block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedulepattern PlanServer#schedulepattern}
        '''
        result = self._values.get("schedulepattern")
        assert result is not None, "Required property 'schedulepattern' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepattern"]], result)

    @builtins.property
    def fordatabasesonly(self) -> typing.Optional[builtins.str]:
        '''Boolean to indicate if schedule is for database agents.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#fordatabasesonly PlanServer#fordatabasesonly}
        '''
        result = self._values.get("fordatabasesonly")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduleoption(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesScheduleoption"]]]:
        '''scheduleoption block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#scheduleoption PlanServer#scheduleoption}
        '''
        result = self._values.get("scheduleoption")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesScheduleoption"]]], result)

    @builtins.property
    def vmoperationtype(self) -> typing.Optional[builtins.str]:
        '''Type of DR operation (only applicable for Failover groups) [PLANNED_FAILOVER, TEST_BOOT].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#vmoperationtype PlanServer#vmoperationtype}
        '''
        result = self._values.get("vmoperationtype")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupfrequencySchedules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoBackupfrequencySchedulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b46eaaf180684db5a4e21217ba214a723856717245249b9658edef71d4031995)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerRpoBackupfrequencySchedulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec8efd28dceda0ada18d33925f200ebd7d6828381cbaaa96f49685412302d427)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupfrequencySchedulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fbb2f83d21d99c4d0dde240b5ee9b986d4077c6cd204bae2731d7ecfa3b3dff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c91586b36a89ea07a4ad38fed838fd7e4aed216bedc4551104d1687cbdf6283a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4478de508ee3cac794d6828fc23ee654c77683779056ef66a5428636142c200c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2ff61fb5e3a32bd8c5eafa20382d5767a650f06a86e2651e1be4fccaae89716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencySchedulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__323644867b95356031a41fb48a91642613d6233884dafccc8251adea8b71c0ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putScheduleoption")
    def put_scheduleoption(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesScheduleoption", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85ebe4be18112c51cf0e8cc6a6b4ff9f50838f16206902240eb969f3d4bfb3a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScheduleoption", [value]))

    @jsii.member(jsii_name="putSchedulepattern")
    def put_schedulepattern(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesSchedulepattern", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a3e55067b9c930e8e3e046d044c730b2fc2ef0136573c4d109245f75de3833)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSchedulepattern", [value]))

    @jsii.member(jsii_name="resetFordatabasesonly")
    def reset_fordatabasesonly(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFordatabasesonly", []))

    @jsii.member(jsii_name="resetScheduleoption")
    def reset_scheduleoption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduleoption", []))

    @jsii.member(jsii_name="resetVmoperationtype")
    def reset_vmoperationtype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVmoperationtype", []))

    @builtins.property
    @jsii.member(jsii_name="scheduleoption")
    def scheduleoption(
        self,
    ) -> "PlanServerRpoBackupfrequencySchedulesScheduleoptionList":
        return typing.cast("PlanServerRpoBackupfrequencySchedulesScheduleoptionList", jsii.get(self, "scheduleoption"))

    @builtins.property
    @jsii.member(jsii_name="schedulepattern")
    def schedulepattern(
        self,
    ) -> "PlanServerRpoBackupfrequencySchedulesSchedulepatternList":
        return typing.cast("PlanServerRpoBackupfrequencySchedulesSchedulepatternList", jsii.get(self, "schedulepattern"))

    @builtins.property
    @jsii.member(jsii_name="backuptypeInput")
    def backuptype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backuptypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fordatabasesonlyInput")
    def fordatabasesonly_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fordatabasesonlyInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulenameInput")
    def schedulename_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulenameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleoptionInput")
    def scheduleoption_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesScheduleoption"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesScheduleoption"]]], jsii.get(self, "scheduleoptionInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulepatternInput")
    def schedulepattern_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepattern"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepattern"]]], jsii.get(self, "schedulepatternInput"))

    @builtins.property
    @jsii.member(jsii_name="vmoperationtypeInput")
    def vmoperationtype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmoperationtypeInput"))

    @builtins.property
    @jsii.member(jsii_name="backuptype")
    def backuptype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backuptype"))

    @backuptype.setter
    def backuptype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7463a1b18016321d22e2c36e52ef833e56b2f63c322f37c7ec0876d6f48496fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backuptype", value)

    @builtins.property
    @jsii.member(jsii_name="fordatabasesonly")
    def fordatabasesonly(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fordatabasesonly"))

    @fordatabasesonly.setter
    def fordatabasesonly(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56ef6b91bb23d659197961cfcd352dc4b88da8a859a8a1c0384b368085642294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fordatabasesonly", value)

    @builtins.property
    @jsii.member(jsii_name="schedulename")
    def schedulename(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulename"))

    @schedulename.setter
    def schedulename(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa3395fdaa5951311fc9a8dba265a6dbb5d510aafbdadee894ba57fa2cdaad3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulename", value)

    @builtins.property
    @jsii.member(jsii_name="vmoperationtype")
    def vmoperationtype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmoperationtype"))

    @vmoperationtype.setter
    def vmoperationtype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a04005604fad5431d5756f1a06d15e555530f57c453853d9b57c4ecb40153bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmoperationtype", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82b84dc2856d9e79a8a07b06fe323684ad1ff275d89c3d17738b2dc4ec34f1eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesScheduleoption",
    jsii_struct_bases=[],
    name_mapping={
        "commitfrequencyinhours": "commitfrequencyinhours",
        "daysbetweenautoconvert": "daysbetweenautoconvert",
        "jobrunningtimeinmins": "jobrunningtimeinmins",
        "o365_itemselectionoption": "o365Itemselectionoption",
        "usediskcacheforlogbackups": "usediskcacheforlogbackups",
    },
)
class PlanServerRpoBackupfrequencySchedulesScheduleoption:
    def __init__(
        self,
        *,
        commitfrequencyinhours: typing.Optional[jsii.Number] = None,
        daysbetweenautoconvert: typing.Optional[jsii.Number] = None,
        jobrunningtimeinmins: typing.Optional[jsii.Number] = None,
        o365_itemselectionoption: typing.Optional[builtins.str] = None,
        usediskcacheforlogbackups: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param commitfrequencyinhours: Commit frequency in hours for disk cache backups from automatic schedules. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#commitfrequencyinhours PlanServer#commitfrequencyinhours}
        :param daysbetweenautoconvert: Number of days between auto conversion of backup level applicable for databases on incremental and differential schedules of server plan. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#daysbetweenautoconvert PlanServer#daysbetweenautoconvert}
        :param jobrunningtimeinmins: total job running time in minutes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#jobrunningtimeinmins PlanServer#jobrunningtimeinmins}
        :param o365_itemselectionoption: item backup option for O365 V2 backup jobs [SELECT_ALL, SELECT_NEVER_PROCESSED, SELECT_MEETING_SLA, SELECT_NOT_MEETING_SLA_PROCESSED_ATLEAST_ONCE, SELECT_FAILED_LAST_ATTEMPT, SELECT_PROCESSED_ATLEAST_ONCE, SELECT_NOT_MEETING_SLA, SELECT_MEETING_SLA_NOT_RECENTLY_BACKED_UP]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#o365itemselectionoption PlanServer#o365itemselectionoption}
        :param usediskcacheforlogbackups: Used to enable disk caching feature on databases for automatic schedules on server plan. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usediskcacheforlogbackups PlanServer#usediskcacheforlogbackups}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1849b507a629efc91d1b7f46bbaa9c5e14193781f94b0d12050e2a889a95276f)
            check_type(argname="argument commitfrequencyinhours", value=commitfrequencyinhours, expected_type=type_hints["commitfrequencyinhours"])
            check_type(argname="argument daysbetweenautoconvert", value=daysbetweenautoconvert, expected_type=type_hints["daysbetweenautoconvert"])
            check_type(argname="argument jobrunningtimeinmins", value=jobrunningtimeinmins, expected_type=type_hints["jobrunningtimeinmins"])
            check_type(argname="argument o365_itemselectionoption", value=o365_itemselectionoption, expected_type=type_hints["o365_itemselectionoption"])
            check_type(argname="argument usediskcacheforlogbackups", value=usediskcacheforlogbackups, expected_type=type_hints["usediskcacheforlogbackups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if commitfrequencyinhours is not None:
            self._values["commitfrequencyinhours"] = commitfrequencyinhours
        if daysbetweenautoconvert is not None:
            self._values["daysbetweenautoconvert"] = daysbetweenautoconvert
        if jobrunningtimeinmins is not None:
            self._values["jobrunningtimeinmins"] = jobrunningtimeinmins
        if o365_itemselectionoption is not None:
            self._values["o365_itemselectionoption"] = o365_itemselectionoption
        if usediskcacheforlogbackups is not None:
            self._values["usediskcacheforlogbackups"] = usediskcacheforlogbackups

    @builtins.property
    def commitfrequencyinhours(self) -> typing.Optional[jsii.Number]:
        '''Commit frequency in hours for disk cache backups from automatic schedules.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#commitfrequencyinhours PlanServer#commitfrequencyinhours}
        '''
        result = self._values.get("commitfrequencyinhours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def daysbetweenautoconvert(self) -> typing.Optional[jsii.Number]:
        '''Number of days between auto conversion of backup level applicable for databases on incremental and differential schedules of server plan.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#daysbetweenautoconvert PlanServer#daysbetweenautoconvert}
        '''
        result = self._values.get("daysbetweenautoconvert")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def jobrunningtimeinmins(self) -> typing.Optional[jsii.Number]:
        '''total job running time in minutes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#jobrunningtimeinmins PlanServer#jobrunningtimeinmins}
        '''
        result = self._values.get("jobrunningtimeinmins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def o365_itemselectionoption(self) -> typing.Optional[builtins.str]:
        '''item backup option for O365 V2 backup jobs [SELECT_ALL, SELECT_NEVER_PROCESSED, SELECT_MEETING_SLA, SELECT_NOT_MEETING_SLA_PROCESSED_ATLEAST_ONCE, SELECT_FAILED_LAST_ATTEMPT, SELECT_PROCESSED_ATLEAST_ONCE, SELECT_NOT_MEETING_SLA, SELECT_MEETING_SLA_NOT_RECENTLY_BACKED_UP].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#o365itemselectionoption PlanServer#o365itemselectionoption}
        '''
        result = self._values.get("o365_itemselectionoption")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usediskcacheforlogbackups(self) -> typing.Optional[builtins.str]:
        '''Used to enable disk caching feature on databases for automatic schedules on server plan.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usediskcacheforlogbackups PlanServer#usediskcacheforlogbackups}
        '''
        result = self._values.get("usediskcacheforlogbackups")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupfrequencySchedulesScheduleoption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoBackupfrequencySchedulesScheduleoptionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesScheduleoptionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2ece895fdf4666bedafafc6ba27c78d040e4c4191112e91db38c23c9dddd313f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerRpoBackupfrequencySchedulesScheduleoptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0438aee4c5954f8583bbfb5667e7741617d8b6fa909b4bf9f3bf43cf82bcc56c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupfrequencySchedulesScheduleoptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8af34fedfd98f26a8065eafe10492b9d79ce2944051f93b6415d2474921bbf9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8ac289ffa00ddb275b1c3b3d3395dd6fdef7b756c1f10060a3511d5950f1ed0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4215e5f2e2b9b3e79148a3a65828e78bdaeaee0601f239ac2c608cf4081d400b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesScheduleoption]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesScheduleoption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesScheduleoption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff8accecbbc22562bdf1f3d4ade2e5d273446da1ec989588c53cd800a6f67a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencySchedulesScheduleoptionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesScheduleoptionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9761dd6cabe0b5b7da5771eed5dc8c2d40542c5c3478c5604f0e24caf6361d20)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCommitfrequencyinhours")
    def reset_commitfrequencyinhours(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommitfrequencyinhours", []))

    @jsii.member(jsii_name="resetDaysbetweenautoconvert")
    def reset_daysbetweenautoconvert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysbetweenautoconvert", []))

    @jsii.member(jsii_name="resetJobrunningtimeinmins")
    def reset_jobrunningtimeinmins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobrunningtimeinmins", []))

    @jsii.member(jsii_name="resetO365Itemselectionoption")
    def reset_o365_itemselectionoption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetO365Itemselectionoption", []))

    @jsii.member(jsii_name="resetUsediskcacheforlogbackups")
    def reset_usediskcacheforlogbackups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsediskcacheforlogbackups", []))

    @builtins.property
    @jsii.member(jsii_name="commitfrequencyinhoursInput")
    def commitfrequencyinhours_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "commitfrequencyinhoursInput"))

    @builtins.property
    @jsii.member(jsii_name="daysbetweenautoconvertInput")
    def daysbetweenautoconvert_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysbetweenautoconvertInput"))

    @builtins.property
    @jsii.member(jsii_name="jobrunningtimeinminsInput")
    def jobrunningtimeinmins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jobrunningtimeinminsInput"))

    @builtins.property
    @jsii.member(jsii_name="o365ItemselectionoptionInput")
    def o365_itemselectionoption_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "o365ItemselectionoptionInput"))

    @builtins.property
    @jsii.member(jsii_name="usediskcacheforlogbackupsInput")
    def usediskcacheforlogbackups_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usediskcacheforlogbackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="commitfrequencyinhours")
    def commitfrequencyinhours(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "commitfrequencyinhours"))

    @commitfrequencyinhours.setter
    def commitfrequencyinhours(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a979c9cf1c0e78be5d17ba2b10c0d8debb2dd226514cdb70394bfab7b83bc26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commitfrequencyinhours", value)

    @builtins.property
    @jsii.member(jsii_name="daysbetweenautoconvert")
    def daysbetweenautoconvert(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysbetweenautoconvert"))

    @daysbetweenautoconvert.setter
    def daysbetweenautoconvert(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1661517d0d26aa06e7c59ef7d6895f164384d125b0deaf25900c58a87160ed50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysbetweenautoconvert", value)

    @builtins.property
    @jsii.member(jsii_name="jobrunningtimeinmins")
    def jobrunningtimeinmins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "jobrunningtimeinmins"))

    @jobrunningtimeinmins.setter
    def jobrunningtimeinmins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4978752b57b208168638c64da22c3b666845b3bdba3476999a1f2c4d3c2ed3fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobrunningtimeinmins", value)

    @builtins.property
    @jsii.member(jsii_name="o365Itemselectionoption")
    def o365_itemselectionoption(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "o365Itemselectionoption"))

    @o365_itemselectionoption.setter
    def o365_itemselectionoption(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6b04ea25e9b80a35893713ccec53eba325d1593fcfd721a890ba042bf6ec384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "o365Itemselectionoption", value)

    @builtins.property
    @jsii.member(jsii_name="usediskcacheforlogbackups")
    def usediskcacheforlogbackups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usediskcacheforlogbackups"))

    @usediskcacheforlogbackups.setter
    def usediskcacheforlogbackups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__527ae308f568899ae86675cb717ebc8576b5b04e323271e0cfa23e2bb24a516b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usediskcacheforlogbackups", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesScheduleoption]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesScheduleoption]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesScheduleoption]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd94bb64455e824debc4f40fc385c52010fae4365d503bfa9aaff56ee71e158)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepattern",
    jsii_struct_bases=[],
    name_mapping={
        "schedulefrequencytype": "schedulefrequencytype",
        "dayofmonth": "dayofmonth",
        "dayofweek": "dayofweek",
        "daysbetweensyntheticfulls": "daysbetweensyntheticfulls",
        "enddate": "enddate",
        "exceptions": "exceptions",
        "frequency": "frequency",
        "maxbackupintervalinmins": "maxbackupintervalinmins",
        "monthofyear": "monthofyear",
        "nooftimes": "nooftimes",
        "repeatintervalinminutes": "repeatintervalinminutes",
        "repeatuntiltime": "repeatuntiltime",
        "startdate": "startdate",
        "starttime": "starttime",
        "timezone": "timezone",
        "weeklydays": "weeklydays",
        "weekofmonth": "weekofmonth",
    },
)
class PlanServerRpoBackupfrequencySchedulesSchedulepattern:
    def __init__(
        self,
        *,
        schedulefrequencytype: builtins.str,
        dayofmonth: typing.Optional[jsii.Number] = None,
        dayofweek: typing.Optional[builtins.str] = None,
        daysbetweensyntheticfulls: typing.Optional[jsii.Number] = None,
        enddate: typing.Optional[jsii.Number] = None,
        exceptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        frequency: typing.Optional[jsii.Number] = None,
        maxbackupintervalinmins: typing.Optional[jsii.Number] = None,
        monthofyear: typing.Optional[builtins.str] = None,
        nooftimes: typing.Optional[jsii.Number] = None,
        repeatintervalinminutes: typing.Optional[jsii.Number] = None,
        repeatuntiltime: typing.Optional[jsii.Number] = None,
        startdate: typing.Optional[jsii.Number] = None,
        starttime: typing.Optional[jsii.Number] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
        weeklydays: typing.Optional[typing.Sequence[builtins.str]] = None,
        weekofmonth: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param schedulefrequencytype: schedule frequency type [MINUTES, DAILY, WEEKLY, MONTHLY, YEARLY, AUTOMATIC]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedulefrequencytype PlanServer#schedulefrequencytype}
        :param dayofmonth: Day on which to run the schedule, applicable for monthly, yearly. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofmonth PlanServer#dayofmonth}
        :param dayofweek: [SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, DAY, WEEKDAY, WEEKEND_DAYS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofweek PlanServer#dayofweek}
        :param daysbetweensyntheticfulls: No of days between two synthetic full jobs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#daysbetweensyntheticfulls PlanServer#daysbetweensyntheticfulls}
        :param enddate: Schedule end date in epoch format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enddate PlanServer#enddate}
        :param exceptions: exceptions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#exceptions PlanServer#exceptions}
        :param frequency: Frequency of the schedule based on schedule frequency type eg. for Hours, value 2 is 2 hours, for Minutes, 30 is 30 minutes, for Daily, 2 is 2 days. for Monthly 2 is it repeats every 2 months Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#frequency PlanServer#frequency}
        :param maxbackupintervalinmins: The number of mins to force a backup on automatic schedule. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#maxbackupintervalinmins PlanServer#maxbackupintervalinmins}
        :param monthofyear: [JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#monthofyear PlanServer#monthofyear}
        :param nooftimes: The number of times you want the schedule to run. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#nooftimes PlanServer#nooftimes}
        :param repeatintervalinminutes: How often in minutes in a day the schedule runs, applicable for daily, weekly, monthly and yearly frequency types. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#repeatintervalinminutes PlanServer#repeatintervalinminutes}
        :param repeatuntiltime: Until what time to repeat the schedule in a day, requires repeatIntervalInMinutes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#repeatuntiltime PlanServer#repeatuntiltime}
        :param startdate: start date of schedule in epoch format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#startdate PlanServer#startdate}
        :param starttime: start time of schedule in seconds. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#starttime PlanServer#starttime}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#timezone PlanServer#timezone}
        :param weeklydays: Days of the week for weekly frequency. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#weeklydays PlanServer#weeklydays}
        :param weekofmonth: Specific week of a month [FIRST, SECOND, THIRD, FOURTH, LAST]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#weekofmonth PlanServer#weekofmonth}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c00affcf6ccbe2b21ab290a4acc09b9c7f579f2f3139c340326e8d273b768f3e)
            check_type(argname="argument schedulefrequencytype", value=schedulefrequencytype, expected_type=type_hints["schedulefrequencytype"])
            check_type(argname="argument dayofmonth", value=dayofmonth, expected_type=type_hints["dayofmonth"])
            check_type(argname="argument dayofweek", value=dayofweek, expected_type=type_hints["dayofweek"])
            check_type(argname="argument daysbetweensyntheticfulls", value=daysbetweensyntheticfulls, expected_type=type_hints["daysbetweensyntheticfulls"])
            check_type(argname="argument enddate", value=enddate, expected_type=type_hints["enddate"])
            check_type(argname="argument exceptions", value=exceptions, expected_type=type_hints["exceptions"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument maxbackupintervalinmins", value=maxbackupintervalinmins, expected_type=type_hints["maxbackupintervalinmins"])
            check_type(argname="argument monthofyear", value=monthofyear, expected_type=type_hints["monthofyear"])
            check_type(argname="argument nooftimes", value=nooftimes, expected_type=type_hints["nooftimes"])
            check_type(argname="argument repeatintervalinminutes", value=repeatintervalinminutes, expected_type=type_hints["repeatintervalinminutes"])
            check_type(argname="argument repeatuntiltime", value=repeatuntiltime, expected_type=type_hints["repeatuntiltime"])
            check_type(argname="argument startdate", value=startdate, expected_type=type_hints["startdate"])
            check_type(argname="argument starttime", value=starttime, expected_type=type_hints["starttime"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
            check_type(argname="argument weeklydays", value=weeklydays, expected_type=type_hints["weeklydays"])
            check_type(argname="argument weekofmonth", value=weekofmonth, expected_type=type_hints["weekofmonth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedulefrequencytype": schedulefrequencytype,
        }
        if dayofmonth is not None:
            self._values["dayofmonth"] = dayofmonth
        if dayofweek is not None:
            self._values["dayofweek"] = dayofweek
        if daysbetweensyntheticfulls is not None:
            self._values["daysbetweensyntheticfulls"] = daysbetweensyntheticfulls
        if enddate is not None:
            self._values["enddate"] = enddate
        if exceptions is not None:
            self._values["exceptions"] = exceptions
        if frequency is not None:
            self._values["frequency"] = frequency
        if maxbackupintervalinmins is not None:
            self._values["maxbackupintervalinmins"] = maxbackupintervalinmins
        if monthofyear is not None:
            self._values["monthofyear"] = monthofyear
        if nooftimes is not None:
            self._values["nooftimes"] = nooftimes
        if repeatintervalinminutes is not None:
            self._values["repeatintervalinminutes"] = repeatintervalinminutes
        if repeatuntiltime is not None:
            self._values["repeatuntiltime"] = repeatuntiltime
        if startdate is not None:
            self._values["startdate"] = startdate
        if starttime is not None:
            self._values["starttime"] = starttime
        if timezone is not None:
            self._values["timezone"] = timezone
        if weeklydays is not None:
            self._values["weeklydays"] = weeklydays
        if weekofmonth is not None:
            self._values["weekofmonth"] = weekofmonth

    @builtins.property
    def schedulefrequencytype(self) -> builtins.str:
        '''schedule frequency type [MINUTES, DAILY, WEEKLY, MONTHLY, YEARLY, AUTOMATIC].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#schedulefrequencytype PlanServer#schedulefrequencytype}
        '''
        result = self._values.get("schedulefrequencytype")
        assert result is not None, "Required property 'schedulefrequencytype' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dayofmonth(self) -> typing.Optional[jsii.Number]:
        '''Day on which to run the schedule, applicable for monthly, yearly.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofmonth PlanServer#dayofmonth}
        '''
        result = self._values.get("dayofmonth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def dayofweek(self) -> typing.Optional[builtins.str]:
        '''[SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, DAY, WEEKDAY, WEEKEND_DAYS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofweek PlanServer#dayofweek}
        '''
        result = self._values.get("dayofweek")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def daysbetweensyntheticfulls(self) -> typing.Optional[jsii.Number]:
        '''No of days between two synthetic full jobs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#daysbetweensyntheticfulls PlanServer#daysbetweensyntheticfulls}
        '''
        result = self._values.get("daysbetweensyntheticfulls")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enddate(self) -> typing.Optional[jsii.Number]:
        '''Schedule end date in epoch format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enddate PlanServer#enddate}
        '''
        result = self._values.get("enddate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def exceptions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions"]]]:
        '''exceptions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#exceptions PlanServer#exceptions}
        '''
        result = self._values.get("exceptions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions"]]], result)

    @builtins.property
    def frequency(self) -> typing.Optional[jsii.Number]:
        '''Frequency of the schedule based on schedule frequency type eg.

        for Hours, value 2 is 2 hours, for Minutes, 30 is 30 minutes, for Daily, 2 is 2 days. for Monthly 2 is it repeats every 2 months

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#frequency PlanServer#frequency}
        '''
        result = self._values.get("frequency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maxbackupintervalinmins(self) -> typing.Optional[jsii.Number]:
        '''The number of mins to force a backup on automatic schedule.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#maxbackupintervalinmins PlanServer#maxbackupintervalinmins}
        '''
        result = self._values.get("maxbackupintervalinmins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def monthofyear(self) -> typing.Optional[builtins.str]:
        '''[JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#monthofyear PlanServer#monthofyear}
        '''
        result = self._values.get("monthofyear")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nooftimes(self) -> typing.Optional[jsii.Number]:
        '''The number of times you want the schedule to run.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#nooftimes PlanServer#nooftimes}
        '''
        result = self._values.get("nooftimes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def repeatintervalinminutes(self) -> typing.Optional[jsii.Number]:
        '''How often in minutes in a day the schedule runs, applicable for daily, weekly, monthly and yearly frequency types.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#repeatintervalinminutes PlanServer#repeatintervalinminutes}
        '''
        result = self._values.get("repeatintervalinminutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def repeatuntiltime(self) -> typing.Optional[jsii.Number]:
        '''Until what time to repeat the schedule in a day, requires repeatIntervalInMinutes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#repeatuntiltime PlanServer#repeatuntiltime}
        '''
        result = self._values.get("repeatuntiltime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def startdate(self) -> typing.Optional[jsii.Number]:
        '''start date of schedule in epoch format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#startdate PlanServer#startdate}
        '''
        result = self._values.get("startdate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def starttime(self) -> typing.Optional[jsii.Number]:
        '''start time of schedule in seconds.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#starttime PlanServer#starttime}
        '''
        result = self._values.get("starttime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#timezone PlanServer#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone"]]], result)

    @builtins.property
    def weeklydays(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Days of the week for weekly frequency.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#weeklydays PlanServer#weeklydays}
        '''
        result = self._values.get("weeklydays")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def weekofmonth(self) -> typing.Optional[builtins.str]:
        '''Specific week of a month [FIRST, SECOND, THIRD, FOURTH, LAST].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#weekofmonth PlanServer#weekofmonth}
        '''
        result = self._values.get("weekofmonth")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupfrequencySchedulesSchedulepattern(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions",
    jsii_struct_bases=[],
    name_mapping={
        "ondates": "ondates",
        "ondayoftheweek": "ondayoftheweek",
        "onweekofthemonth": "onweekofthemonth",
    },
)
class PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions:
    def __init__(
        self,
        *,
        ondates: typing.Optional[typing.Sequence[jsii.Number]] = None,
        ondayoftheweek: typing.Optional[typing.Sequence[builtins.str]] = None,
        onweekofthemonth: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param ondates: list of dates in a month. For ex: 1, 20. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#ondates PlanServer#ondates}
        :param ondayoftheweek: On which days, for ex: MONDAY, FRIDAY. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#ondayoftheweek PlanServer#ondayoftheweek}
        :param onweekofthemonth: On which week of month, for ex: FIRST, LAST. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#onweekofthemonth PlanServer#onweekofthemonth}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70b6ce06c6bbcdb2a8c38a96588ae22c4c879d1c6533062754b16b96252c79de)
            check_type(argname="argument ondates", value=ondates, expected_type=type_hints["ondates"])
            check_type(argname="argument ondayoftheweek", value=ondayoftheweek, expected_type=type_hints["ondayoftheweek"])
            check_type(argname="argument onweekofthemonth", value=onweekofthemonth, expected_type=type_hints["onweekofthemonth"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ondates is not None:
            self._values["ondates"] = ondates
        if ondayoftheweek is not None:
            self._values["ondayoftheweek"] = ondayoftheweek
        if onweekofthemonth is not None:
            self._values["onweekofthemonth"] = onweekofthemonth

    @builtins.property
    def ondates(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''list of dates in a month. For ex: 1, 20.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#ondates PlanServer#ondates}
        '''
        result = self._values.get("ondates")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def ondayoftheweek(self) -> typing.Optional[typing.List[builtins.str]]:
        '''On which days, for ex: MONDAY, FRIDAY.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#ondayoftheweek PlanServer#ondayoftheweek}
        '''
        result = self._values.get("ondayoftheweek")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def onweekofthemonth(self) -> typing.Optional[typing.List[builtins.str]]:
        '''On which week of month, for ex: FIRST, LAST.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#onweekofthemonth PlanServer#onweekofthemonth}
        '''
        result = self._values.get("onweekofthemonth")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fd6332fd3ff662753a3f45275e9d714a0ee70a2b3f9113b22834ab0faf22943)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d54ba8527f58966697d6cd1052cfaddffbe278eb067cc18cf7894966c56ffcf8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce3446fa077578ffed18325433362b9cab0ba1a1788738fc80c6f9eb0b7a2ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__40e615482023072b62752535070230529833ca6646d11b43e9a7668f2bff168d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__594911f99353bae4d3a250e6413b2c2f2569d6bd67074d083b8e76b0c40af7d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21c091bffddc1d12426dc5c53ea8229a746fee722875684149b477cbf2280bae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd7ee23843fb2b3170e34613950b99185b6eb52152a42ce4760c7d20a25471af)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetOndates")
    def reset_ondates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOndates", []))

    @jsii.member(jsii_name="resetOndayoftheweek")
    def reset_ondayoftheweek(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOndayoftheweek", []))

    @jsii.member(jsii_name="resetOnweekofthemonth")
    def reset_onweekofthemonth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnweekofthemonth", []))

    @builtins.property
    @jsii.member(jsii_name="ondatesInput")
    def ondates_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "ondatesInput"))

    @builtins.property
    @jsii.member(jsii_name="ondayoftheweekInput")
    def ondayoftheweek_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ondayoftheweekInput"))

    @builtins.property
    @jsii.member(jsii_name="onweekofthemonthInput")
    def onweekofthemonth_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "onweekofthemonthInput"))

    @builtins.property
    @jsii.member(jsii_name="ondates")
    def ondates(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "ondates"))

    @ondates.setter
    def ondates(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78f90b3f4fb32eaa79d7f16f57c38f0abcb29461280ae657a3196cab41544e6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ondates", value)

    @builtins.property
    @jsii.member(jsii_name="ondayoftheweek")
    def ondayoftheweek(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ondayoftheweek"))

    @ondayoftheweek.setter
    def ondayoftheweek(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52de1a755dda9a9b604cd8fe718ddf23bc2f6ceca13635a0e07ccc9a17ca64cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ondayoftheweek", value)

    @builtins.property
    @jsii.member(jsii_name="onweekofthemonth")
    def onweekofthemonth(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "onweekofthemonth"))

    @onweekofthemonth.setter
    def onweekofthemonth(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b45b170d780eac7f0057b7a7d410eb0929e45812263cc73e76e4af72444f0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onweekofthemonth", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a4bd2c55ecec212bfbce6abd0e247b859df1df774af603f67995672bced4edc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencySchedulesSchedulepatternList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0975894ababfd0d5e2987c897cfa07f7d936967cc1a324137ee3162c2aa4e306)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerRpoBackupfrequencySchedulesSchedulepatternOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2e3101f4f665b96e0202ea31ab492e0f86d3308dbfdd1c37d4a071792a7c1f1)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupfrequencySchedulesSchedulepatternOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db27d70615ab63821767cea6c761a68f848d288c7acfaaba2cc008062bb2c441)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f197c0f2b14572f8cfc4e2c67627973449bbbb2fff072bd9040c9d7a053bc5c3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__345192bc17cc1ac285b1ceb9a097c6e9204a1b758246cad3082f6a19d202e366)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepattern]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepattern]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepattern]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c37e1cfa6b2266c104c60205c22549afe3295d0cdc1686bcef6633d5de40e6ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencySchedulesSchedulepatternOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4ed42ae07f1f0ca168b432ebc076f13e7148467b5c17cc17adf18dce2bbb538f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putExceptions")
    def put_exceptions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c203769816d161cd856bc0fe1453c7a95c69958e5641dc32394b421dd3c226cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExceptions", [value]))

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f49ad612f4d0fa3280c69ce36795cda842da394190e40f46de8883182e26d8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimezone", [value]))

    @jsii.member(jsii_name="resetDayofmonth")
    def reset_dayofmonth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayofmonth", []))

    @jsii.member(jsii_name="resetDayofweek")
    def reset_dayofweek(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayofweek", []))

    @jsii.member(jsii_name="resetDaysbetweensyntheticfulls")
    def reset_daysbetweensyntheticfulls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysbetweensyntheticfulls", []))

    @jsii.member(jsii_name="resetEnddate")
    def reset_enddate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnddate", []))

    @jsii.member(jsii_name="resetExceptions")
    def reset_exceptions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExceptions", []))

    @jsii.member(jsii_name="resetFrequency")
    def reset_frequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrequency", []))

    @jsii.member(jsii_name="resetMaxbackupintervalinmins")
    def reset_maxbackupintervalinmins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxbackupintervalinmins", []))

    @jsii.member(jsii_name="resetMonthofyear")
    def reset_monthofyear(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonthofyear", []))

    @jsii.member(jsii_name="resetNooftimes")
    def reset_nooftimes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNooftimes", []))

    @jsii.member(jsii_name="resetRepeatintervalinminutes")
    def reset_repeatintervalinminutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepeatintervalinminutes", []))

    @jsii.member(jsii_name="resetRepeatuntiltime")
    def reset_repeatuntiltime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepeatuntiltime", []))

    @jsii.member(jsii_name="resetStartdate")
    def reset_startdate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartdate", []))

    @jsii.member(jsii_name="resetStarttime")
    def reset_starttime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStarttime", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

    @jsii.member(jsii_name="resetWeeklydays")
    def reset_weeklydays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeeklydays", []))

    @jsii.member(jsii_name="resetWeekofmonth")
    def reset_weekofmonth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeekofmonth", []))

    @builtins.property
    @jsii.member(jsii_name="exceptions")
    def exceptions(
        self,
    ) -> PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsList:
        return typing.cast(PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsList, jsii.get(self, "exceptions"))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(
        self,
    ) -> "PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneList":
        return typing.cast("PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="dayofmonthInput")
    def dayofmonth_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dayofmonthInput"))

    @builtins.property
    @jsii.member(jsii_name="dayofweekInput")
    def dayofweek_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayofweekInput"))

    @builtins.property
    @jsii.member(jsii_name="daysbetweensyntheticfullsInput")
    def daysbetweensyntheticfulls_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysbetweensyntheticfullsInput"))

    @builtins.property
    @jsii.member(jsii_name="enddateInput")
    def enddate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enddateInput"))

    @builtins.property
    @jsii.member(jsii_name="exceptionsInput")
    def exceptions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]], jsii.get(self, "exceptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="maxbackupintervalinminsInput")
    def maxbackupintervalinmins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxbackupintervalinminsInput"))

    @builtins.property
    @jsii.member(jsii_name="monthofyearInput")
    def monthofyear_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monthofyearInput"))

    @builtins.property
    @jsii.member(jsii_name="nooftimesInput")
    def nooftimes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nooftimesInput"))

    @builtins.property
    @jsii.member(jsii_name="repeatintervalinminutesInput")
    def repeatintervalinminutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "repeatintervalinminutesInput"))

    @builtins.property
    @jsii.member(jsii_name="repeatuntiltimeInput")
    def repeatuntiltime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "repeatuntiltimeInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulefrequencytypeInput")
    def schedulefrequencytype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulefrequencytypeInput"))

    @builtins.property
    @jsii.member(jsii_name="startdateInput")
    def startdate_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startdateInput"))

    @builtins.property
    @jsii.member(jsii_name="starttimeInput")
    def starttime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "starttimeInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone"]]], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="weeklydaysInput")
    def weeklydays_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "weeklydaysInput"))

    @builtins.property
    @jsii.member(jsii_name="weekofmonthInput")
    def weekofmonth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "weekofmonthInput"))

    @builtins.property
    @jsii.member(jsii_name="dayofmonth")
    def dayofmonth(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dayofmonth"))

    @dayofmonth.setter
    def dayofmonth(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51047dabaff2f19552a76cf95da11f2a9950b616544b88b5b152c5ca086febc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayofmonth", value)

    @builtins.property
    @jsii.member(jsii_name="dayofweek")
    def dayofweek(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayofweek"))

    @dayofweek.setter
    def dayofweek(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fac3a97187ec66855f54a3369f61b783e14288901fff7f63ab22f44ac11f999)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayofweek", value)

    @builtins.property
    @jsii.member(jsii_name="daysbetweensyntheticfulls")
    def daysbetweensyntheticfulls(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysbetweensyntheticfulls"))

    @daysbetweensyntheticfulls.setter
    def daysbetweensyntheticfulls(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea722c6bc0b09e6c700e2a4926c24fa7904dc39ae9767b5d720d363475048863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysbetweensyntheticfulls", value)

    @builtins.property
    @jsii.member(jsii_name="enddate")
    def enddate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enddate"))

    @enddate.setter
    def enddate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9368077fdbb24346f232048c521bf4b5d31d85d7d4d0f4db3f3cd8bcaabacaad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enddate", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__117e2421f9ca473b6dbf0c1f35e4a48e690c22aa6fbbc9b1e42fd5a591e2d721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="maxbackupintervalinmins")
    def maxbackupintervalinmins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxbackupintervalinmins"))

    @maxbackupintervalinmins.setter
    def maxbackupintervalinmins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9d89a90d9df5bcac53d2ffe4a124c59c78c9c29fc3f96970cfe3497041c6263)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxbackupintervalinmins", value)

    @builtins.property
    @jsii.member(jsii_name="monthofyear")
    def monthofyear(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monthofyear"))

    @monthofyear.setter
    def monthofyear(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a47feb3ddf6dd8605b4e1dc6700dbd3848675bcb2bd7a1832dcc48c71331614e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monthofyear", value)

    @builtins.property
    @jsii.member(jsii_name="nooftimes")
    def nooftimes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nooftimes"))

    @nooftimes.setter
    def nooftimes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4053c5df63474499d0879dfc839cea70585b7452987626f365d76e1dc9f67b5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nooftimes", value)

    @builtins.property
    @jsii.member(jsii_name="repeatintervalinminutes")
    def repeatintervalinminutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "repeatintervalinminutes"))

    @repeatintervalinminutes.setter
    def repeatintervalinminutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__867358c82fb9c1c380fd3939f005e32c5e88277ab747a4a00758efc76ad0df68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repeatintervalinminutes", value)

    @builtins.property
    @jsii.member(jsii_name="repeatuntiltime")
    def repeatuntiltime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "repeatuntiltime"))

    @repeatuntiltime.setter
    def repeatuntiltime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f61cc7e2eb1305d879253e5e9611aa4595f84c7ee5ecf8b259f5079b5e39e4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repeatuntiltime", value)

    @builtins.property
    @jsii.member(jsii_name="schedulefrequencytype")
    def schedulefrequencytype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedulefrequencytype"))

    @schedulefrequencytype.setter
    def schedulefrequencytype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdde73321b55fce4e1671acc1a919af0c060f8b86e54890ce6aeb78512c72f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulefrequencytype", value)

    @builtins.property
    @jsii.member(jsii_name="startdate")
    def startdate(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startdate"))

    @startdate.setter
    def startdate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ec21e9aea59f00e8813d87dfa279ac6bef82a8f82204f37796930d39259b7ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startdate", value)

    @builtins.property
    @jsii.member(jsii_name="starttime")
    def starttime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "starttime"))

    @starttime.setter
    def starttime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2767e32c30e756b88eb6aa863f161f9c616cf8383e96deffba6ceb499085b34d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "starttime", value)

    @builtins.property
    @jsii.member(jsii_name="weeklydays")
    def weeklydays(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "weeklydays"))

    @weeklydays.setter
    def weeklydays(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__405b6fcb2d72a15f7bb823c6d0a226df7c2cafba24192a62d3801914ba3b218b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weeklydays", value)

    @builtins.property
    @jsii.member(jsii_name="weekofmonth")
    def weekofmonth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "weekofmonth"))

    @weekofmonth.setter
    def weekofmonth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11c52ddc0563825b1b5d1e5d17d89f28f86b161422fe691f8af5ad61586739cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weekofmonth", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepattern]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepattern]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepattern]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70658e45bfc88be4ed72d7ae250833def2103324e5eb6053ff8a66ac56afff3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a82268f27827023b120116002be20db9e26590fa897e757927aa6bf784d73e36)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#name PlanServer#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__bfd45d63f808c1917ce76dc5ea303d82c9abbad3dd7ea23a210139d34719d3a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5df74d9025569950f681e241ae37819fc3a68e904846e024e1d16f588a8c0082)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c61d69b6e0f1c1ea7ce8d64d18c56a0519da12ec14d68a390ec0ec3b7c05387a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__13d453573abd2f41699d30603201fc60b2d4b7a78f30c2db62f557d3559ac08f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c63196622d7f3be0ad3ea7db1a0db0e528aa5f18637e2135a55793e017b5669f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41416b9f657ff1fccfff998f25cb70cd0d4ec6af95b2ea73615cc7d7b2944bfb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e3d20a09b38413180715ccb61a0c010fbc9ce10d89ccace5b9400a07f9633423)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fee06d211dbec0eb848fcdd9c810e06e192cd79e47cbe990247ab9af5885c04c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a3463c86e126255c971e097a7218f8fdaf790f38bb84a778ba73c769aabe9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4af8c9d3c64fa32018f7caf5833ad6b69d421f3dfddd378332f52a684edb24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoBackupwindow",
    jsii_struct_bases=[],
    name_mapping={
        "dayofweek": "dayofweek",
        "endtime": "endtime",
        "starttime": "starttime",
    },
)
class PlanServerRpoBackupwindow:
    def __init__(
        self,
        *,
        dayofweek: typing.Optional[typing.Sequence[builtins.str]] = None,
        endtime: typing.Optional[jsii.Number] = None,
        starttime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dayofweek: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofweek PlanServer#dayofweek}.
        :param endtime: Time in seconds since the beginning of the day. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#endtime PlanServer#endtime}
        :param starttime: Time in seconds since the beginning of the day. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#starttime PlanServer#starttime}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b10ba9a3a98989d2804c1437a90463192b95f56a059b97d31d3be6970ed9feaf)
            check_type(argname="argument dayofweek", value=dayofweek, expected_type=type_hints["dayofweek"])
            check_type(argname="argument endtime", value=endtime, expected_type=type_hints["endtime"])
            check_type(argname="argument starttime", value=starttime, expected_type=type_hints["starttime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dayofweek is not None:
            self._values["dayofweek"] = dayofweek
        if endtime is not None:
            self._values["endtime"] = endtime
        if starttime is not None:
            self._values["starttime"] = starttime

    @builtins.property
    def dayofweek(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofweek PlanServer#dayofweek}.'''
        result = self._values.get("dayofweek")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def endtime(self) -> typing.Optional[jsii.Number]:
        '''Time in seconds since the beginning of the day.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#endtime PlanServer#endtime}
        '''
        result = self._values.get("endtime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def starttime(self) -> typing.Optional[jsii.Number]:
        '''Time in seconds since the beginning of the day.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#starttime PlanServer#starttime}
        '''
        result = self._values.get("starttime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoBackupwindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoBackupwindowList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupwindowList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b068be2629ef9b89366d6928861168db9af080a0ba4194993f05becdee87e864)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerRpoBackupwindowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6315ce5ffdaaeb4836876d1ae329d754fc0775ab987886e429da1a7a5805bae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoBackupwindowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2255b6714e042e3f025872da6d0d2d9ee4e015195138a650a0f05afd772aa124)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e70f4bc665aff5713c675a07d448a0a16e8e3b69d4aa5d126f40180140f49d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aa93457eba7fe3e14664aab5a19e1e33864b3e3f79b40dd8c47da329cff33ebb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupwindow]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupwindow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupwindow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b12b91a9b2ca4ed230830e353cdec1813b4bc2c1f69f90bda450f565ffd1a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoBackupwindowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoBackupwindowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c7d2bacffe85428dd9f5da757b91708e039e164eb5f294b58b0280d88c55b8f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDayofweek")
    def reset_dayofweek(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayofweek", []))

    @jsii.member(jsii_name="resetEndtime")
    def reset_endtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndtime", []))

    @jsii.member(jsii_name="resetStarttime")
    def reset_starttime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStarttime", []))

    @builtins.property
    @jsii.member(jsii_name="dayofweekInput")
    def dayofweek_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dayofweekInput"))

    @builtins.property
    @jsii.member(jsii_name="endtimeInput")
    def endtime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="starttimeInput")
    def starttime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "starttimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dayofweek")
    def dayofweek(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dayofweek"))

    @dayofweek.setter
    def dayofweek(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88140868b14794fee5c2d82122637a360887727eb0fbfba83b7b848e9b1303d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayofweek", value)

    @builtins.property
    @jsii.member(jsii_name="endtime")
    def endtime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "endtime"))

    @endtime.setter
    def endtime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aa6a80fec2b3280e9c08fbd6000265ee2588d934cd34effbc7153a97f258f04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endtime", value)

    @builtins.property
    @jsii.member(jsii_name="starttime")
    def starttime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "starttime"))

    @starttime.setter
    def starttime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1617848d7080d2720063d3420d0dfd9d6e6ee5751b74530ad85268f3f8ff290a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "starttime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupwindow]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupwindow]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupwindow]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__195e7f5ace0cf821be2ea72f35cd60ee892d4ad3851a7b602f4dc92ecb9722a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoFullbackupwindow",
    jsii_struct_bases=[],
    name_mapping={
        "dayofweek": "dayofweek",
        "endtime": "endtime",
        "starttime": "starttime",
    },
)
class PlanServerRpoFullbackupwindow:
    def __init__(
        self,
        *,
        dayofweek: typing.Optional[typing.Sequence[builtins.str]] = None,
        endtime: typing.Optional[jsii.Number] = None,
        starttime: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param dayofweek: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofweek PlanServer#dayofweek}.
        :param endtime: Time in seconds since the beginning of the day. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#endtime PlanServer#endtime}
        :param starttime: Time in seconds since the beginning of the day. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#starttime PlanServer#starttime}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__947f16679dcce022072fa0057bc2d3b69c0a5fb520f204dec2ac4234264688ee)
            check_type(argname="argument dayofweek", value=dayofweek, expected_type=type_hints["dayofweek"])
            check_type(argname="argument endtime", value=endtime, expected_type=type_hints["endtime"])
            check_type(argname="argument starttime", value=starttime, expected_type=type_hints["starttime"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dayofweek is not None:
            self._values["dayofweek"] = dayofweek
        if endtime is not None:
            self._values["endtime"] = endtime
        if starttime is not None:
            self._values["starttime"] = starttime

    @builtins.property
    def dayofweek(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#dayofweek PlanServer#dayofweek}.'''
        result = self._values.get("dayofweek")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def endtime(self) -> typing.Optional[jsii.Number]:
        '''Time in seconds since the beginning of the day.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#endtime PlanServer#endtime}
        '''
        result = self._values.get("endtime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def starttime(self) -> typing.Optional[jsii.Number]:
        '''Time in seconds since the beginning of the day.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#starttime PlanServer#starttime}
        '''
        result = self._values.get("starttime")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoFullbackupwindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoFullbackupwindowList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoFullbackupwindowList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f9e2e209c7a895bb37c341b16326adfa8f0642ce76305f7da75c013304c7ccd9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerRpoFullbackupwindowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66393315dc880c52d0f21f79dc3d4c7d43db706441f346abc1fa81ec36c61b15)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoFullbackupwindowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__892dc85837ce85e0126fb829daf73bba92d01368c8725ea9728007a3ccd4e673)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19eca7dbc09bc1a0d2441b0566ed4a96c7b88e4bd9337166dad28b2fbb7059c0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cc299a75f7fbb02eb56ebd44b77dc7bdde7cd02bb62b1495ad8091bfa22e681b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoFullbackupwindow]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoFullbackupwindow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoFullbackupwindow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbdf36ea09a6efea0462d3766e8ebaa10f6bc4aabded7147ce9a8c9c43af9c61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoFullbackupwindowOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoFullbackupwindowOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b23f2d690606c0a56bb002f4f99b963b36ed366acc00212b6c7e3d1e52069e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDayofweek")
    def reset_dayofweek(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDayofweek", []))

    @jsii.member(jsii_name="resetEndtime")
    def reset_endtime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndtime", []))

    @jsii.member(jsii_name="resetStarttime")
    def reset_starttime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStarttime", []))

    @builtins.property
    @jsii.member(jsii_name="dayofweekInput")
    def dayofweek_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dayofweekInput"))

    @builtins.property
    @jsii.member(jsii_name="endtimeInput")
    def endtime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endtimeInput"))

    @builtins.property
    @jsii.member(jsii_name="starttimeInput")
    def starttime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "starttimeInput"))

    @builtins.property
    @jsii.member(jsii_name="dayofweek")
    def dayofweek(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dayofweek"))

    @dayofweek.setter
    def dayofweek(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1c5d4123cdaeacb4f2cd75a23915d4ae4f02d30c2afc728e425976a0fa3f5f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayofweek", value)

    @builtins.property
    @jsii.member(jsii_name="endtime")
    def endtime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "endtime"))

    @endtime.setter
    def endtime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a3b8c5e9dd623ca352f82b6e70dd7e413be745e85ee7868cc063ae5416895d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endtime", value)

    @builtins.property
    @jsii.member(jsii_name="starttime")
    def starttime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "starttime"))

    @starttime.setter
    def starttime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6b83d819add7abdc8b746e04d29806e81edcc246fc794b68ce1d52d6db4df1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "starttime", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoFullbackupwindow]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoFullbackupwindow]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoFullbackupwindow]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07efd830e7fb365b739c9c090d005850728da1200e84ed17c95b746439be0eea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0767ebff00b1a9fa80df815438054afc531c61cce967fd14cf3798537277ea5f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerRpoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d84e44be040e7bab1e50db8ee336f41f4bb68c7683296622e90e3bd48254d72)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ca90452f48c9d79db5e1ada3e1792468c98f63591198eaf20ab4a4d92cb70d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__12f41dfbc3f473c1b92eb8049554132316237321b1da04aa7698a686b0089273)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c135e4defae0473751fb7f6178fb6dfc68002020978e7710b1f209b85ddf6cfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpo]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8ae3b157c0c29aa2c70d1a725f1e9ccfcecd0471ad7cc3bb7dcad71a158496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d97278e8d317acd510a12ad936ab908995f5ae72267789e4bcd4e1149ce3dee4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBackupfrequency")
    def put_backupfrequency(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequency, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e5c8e5c5169f9a11a23e1b5bed07272e20ccb708cb43dad9883f69824d7aea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackupfrequency", [value]))

    @jsii.member(jsii_name="putBackupwindow")
    def put_backupwindow(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupwindow, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ed482bd9fbe34003fef681fafe16a4bd25bd7a75a1ea658b2440dbee120c1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putBackupwindow", [value]))

    @jsii.member(jsii_name="putFullbackupwindow")
    def put_fullbackupwindow(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoFullbackupwindow, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f214eab09349ea964e1b401d7cb8e88b3451770669f74f3924993e6a1daa5345)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFullbackupwindow", [value]))

    @jsii.member(jsii_name="putSla")
    def put_sla(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerRpoSla", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7745d911d18f757ccb4b2a6e8e0d4b02fe86098cf6c2d62e9fa50901ad8fffb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSla", [value]))

    @jsii.member(jsii_name="resetBackupfrequency")
    def reset_backupfrequency(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupfrequency", []))

    @jsii.member(jsii_name="resetBackupwindow")
    def reset_backupwindow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupwindow", []))

    @jsii.member(jsii_name="resetFullbackupwindow")
    def reset_fullbackupwindow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullbackupwindow", []))

    @jsii.member(jsii_name="resetSla")
    def reset_sla(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSla", []))

    @builtins.property
    @jsii.member(jsii_name="backupfrequency")
    def backupfrequency(self) -> PlanServerRpoBackupfrequencyList:
        return typing.cast(PlanServerRpoBackupfrequencyList, jsii.get(self, "backupfrequency"))

    @builtins.property
    @jsii.member(jsii_name="backupwindow")
    def backupwindow(self) -> PlanServerRpoBackupwindowList:
        return typing.cast(PlanServerRpoBackupwindowList, jsii.get(self, "backupwindow"))

    @builtins.property
    @jsii.member(jsii_name="fullbackupwindow")
    def fullbackupwindow(self) -> PlanServerRpoFullbackupwindowList:
        return typing.cast(PlanServerRpoFullbackupwindowList, jsii.get(self, "fullbackupwindow"))

    @builtins.property
    @jsii.member(jsii_name="sla")
    def sla(self) -> "PlanServerRpoSlaList":
        return typing.cast("PlanServerRpoSlaList", jsii.get(self, "sla"))

    @builtins.property
    @jsii.member(jsii_name="backupfrequencyInput")
    def backupfrequency_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequency]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequency]]], jsii.get(self, "backupfrequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="backupwindowInput")
    def backupwindow_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupwindow]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupwindow]]], jsii.get(self, "backupwindowInput"))

    @builtins.property
    @jsii.member(jsii_name="fullbackupwindowInput")
    def fullbackupwindow_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoFullbackupwindow]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoFullbackupwindow]]], jsii.get(self, "fullbackupwindowInput"))

    @builtins.property
    @jsii.member(jsii_name="slaInput")
    def sla_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoSla"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerRpoSla"]]], jsii.get(self, "slaInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpo]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpo]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpo]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7264569cceb8c9175034c63dcc0b70a33b6e1b916f88d7b93d777ed339255f83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerRpoSla",
    jsii_struct_bases=[],
    name_mapping={
        "enableafterdelay": "enableafterdelay",
        "excludefromsla": "excludefromsla",
        "exclusionreason": "exclusionreason",
        "slaperiod": "slaperiod",
        "usesystemdefaultsla": "usesystemdefaultsla",
    },
)
class PlanServerRpoSla:
    def __init__(
        self,
        *,
        enableafterdelay: typing.Optional[jsii.Number] = None,
        excludefromsla: typing.Optional[builtins.str] = None,
        exclusionreason: typing.Optional[builtins.str] = None,
        slaperiod: typing.Optional[jsii.Number] = None,
        usesystemdefaultsla: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enableafterdelay: Time provided in Unix format. Give 0 to reset any existing delay. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enableafterdelay PlanServer#enableafterdelay}
        :param excludefromsla: Flag to set to exclude plan from SLA. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#excludefromsla PlanServer#excludefromsla}
        :param exclusionreason: Reason for exclusion from SLA. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#exclusionreason PlanServer#exclusionreason}
        :param slaperiod: SLA Period in Days. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#slaperiod PlanServer#slaperiod}
        :param usesystemdefaultsla: Flag to set to use System Default Service Level Agreement. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usesystemdefaultsla PlanServer#usesystemdefaultsla}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccd4008cf3917732a2b3f96ef45d1b3c1b543cedaeef42c905c2343f4b1727e5)
            check_type(argname="argument enableafterdelay", value=enableafterdelay, expected_type=type_hints["enableafterdelay"])
            check_type(argname="argument excludefromsla", value=excludefromsla, expected_type=type_hints["excludefromsla"])
            check_type(argname="argument exclusionreason", value=exclusionreason, expected_type=type_hints["exclusionreason"])
            check_type(argname="argument slaperiod", value=slaperiod, expected_type=type_hints["slaperiod"])
            check_type(argname="argument usesystemdefaultsla", value=usesystemdefaultsla, expected_type=type_hints["usesystemdefaultsla"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enableafterdelay is not None:
            self._values["enableafterdelay"] = enableafterdelay
        if excludefromsla is not None:
            self._values["excludefromsla"] = excludefromsla
        if exclusionreason is not None:
            self._values["exclusionreason"] = exclusionreason
        if slaperiod is not None:
            self._values["slaperiod"] = slaperiod
        if usesystemdefaultsla is not None:
            self._values["usesystemdefaultsla"] = usesystemdefaultsla

    @builtins.property
    def enableafterdelay(self) -> typing.Optional[jsii.Number]:
        '''Time provided in Unix format. Give 0 to reset any existing delay.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enableafterdelay PlanServer#enableafterdelay}
        '''
        result = self._values.get("enableafterdelay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def excludefromsla(self) -> typing.Optional[builtins.str]:
        '''Flag to set to exclude plan from SLA.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#excludefromsla PlanServer#excludefromsla}
        '''
        result = self._values.get("excludefromsla")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exclusionreason(self) -> typing.Optional[builtins.str]:
        '''Reason for exclusion from SLA.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#exclusionreason PlanServer#exclusionreason}
        '''
        result = self._values.get("exclusionreason")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slaperiod(self) -> typing.Optional[jsii.Number]:
        '''SLA Period in Days.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#slaperiod PlanServer#slaperiod}
        '''
        result = self._values.get("slaperiod")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def usesystemdefaultsla(self) -> typing.Optional[builtins.str]:
        '''Flag to set to use System Default Service Level Agreement.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#usesystemdefaultsla PlanServer#usesystemdefaultsla}
        '''
        result = self._values.get("usesystemdefaultsla")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerRpoSla(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerRpoSlaList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoSlaList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__63eadcb283557b138870ea5f45129df1e9e65c1a2760f1e49337a48f59c49c19)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerRpoSlaOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef6946c3e6b31d45a1dce97a4e56b4970e45b3a1a19102365220cd2b61a5281)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerRpoSlaOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__708fc1585672f463cda06fe115bf1b6238ff206b3804f13c1cdb31cb1ca8e010)
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
            type_hints = typing.get_type_hints(_typecheckingstub__121478278a6e8c602ace41b80a4ee8f27cc25829785d33c5285570d87857000a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c6a3335b1fda1e2c10fc06d069100135b8e479969b8e0d9a554c4a22e7a0fa48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoSla]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoSla]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoSla]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6feb030d14b6d80e03f8e4be89f58f0985dc0a994091c5e8d75b8612a16f3076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerRpoSlaOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerRpoSlaOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d04be0f657473c9b27d687e98a20f71e3f5b6237df4985f3033a9beeeaba5dda)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnableafterdelay")
    def reset_enableafterdelay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableafterdelay", []))

    @jsii.member(jsii_name="resetExcludefromsla")
    def reset_excludefromsla(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExcludefromsla", []))

    @jsii.member(jsii_name="resetExclusionreason")
    def reset_exclusionreason(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExclusionreason", []))

    @jsii.member(jsii_name="resetSlaperiod")
    def reset_slaperiod(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlaperiod", []))

    @jsii.member(jsii_name="resetUsesystemdefaultsla")
    def reset_usesystemdefaultsla(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsesystemdefaultsla", []))

    @builtins.property
    @jsii.member(jsii_name="enableafterdelayInput")
    def enableafterdelay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enableafterdelayInput"))

    @builtins.property
    @jsii.member(jsii_name="excludefromslaInput")
    def excludefromsla_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "excludefromslaInput"))

    @builtins.property
    @jsii.member(jsii_name="exclusionreasonInput")
    def exclusionreason_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exclusionreasonInput"))

    @builtins.property
    @jsii.member(jsii_name="slaperiodInput")
    def slaperiod_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "slaperiodInput"))

    @builtins.property
    @jsii.member(jsii_name="usesystemdefaultslaInput")
    def usesystemdefaultsla_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usesystemdefaultslaInput"))

    @builtins.property
    @jsii.member(jsii_name="enableafterdelay")
    def enableafterdelay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enableafterdelay"))

    @enableafterdelay.setter
    def enableafterdelay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6049dcb45f3d46f45dca9f781cec870fb4caf5176aea9349b794c469021d52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableafterdelay", value)

    @builtins.property
    @jsii.member(jsii_name="excludefromsla")
    def excludefromsla(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "excludefromsla"))

    @excludefromsla.setter
    def excludefromsla(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7d0de008cf0a21a6389ffcce19696697990b3fe11758367401ed7d9c3c27ab0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "excludefromsla", value)

    @builtins.property
    @jsii.member(jsii_name="exclusionreason")
    def exclusionreason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exclusionreason"))

    @exclusionreason.setter
    def exclusionreason(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02cb2eefed630b7ad305fc446622144a1d065dd238c3f9c3806a5d0ac17aefb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exclusionreason", value)

    @builtins.property
    @jsii.member(jsii_name="slaperiod")
    def slaperiod(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "slaperiod"))

    @slaperiod.setter
    def slaperiod(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4188de852f9ab8d92a5cfc8f0b11bc921ffad35becf41461ddc9f7ddebebb81c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slaperiod", value)

    @builtins.property
    @jsii.member(jsii_name="usesystemdefaultsla")
    def usesystemdefaultsla(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usesystemdefaultsla"))

    @usesystemdefaultsla.setter
    def usesystemdefaultsla(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__496bf18af26cf00ae7fb5d0e1b719947967b69c89cc65cde908f4f8797e8d0de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usesystemdefaultsla", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoSla]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoSla]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoSla]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__364d3db73c58661206a5ad8251b691bb0fb829b1e77bd30d6f06bb789857235f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enableadvancedview": "enableadvancedview",
        "filesearch": "filesearch",
    },
)
class PlanServerSettings:
    def __init__(
        self,
        *,
        enableadvancedview: typing.Optional[builtins.str] = None,
        filesearch: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerSettingsFilesearch", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enableadvancedview: Setting to suggest plan has some advanced settings present. Setting is OEM specific and not applicable for all cases. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enableadvancedview PlanServer#enableadvancedview}
        :param filesearch: filesearch block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#filesearch PlanServer#filesearch}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90b76f54bda83a206a3b8460eef501e015ab531f279207867cd1ede849109865)
            check_type(argname="argument enableadvancedview", value=enableadvancedview, expected_type=type_hints["enableadvancedview"])
            check_type(argname="argument filesearch", value=filesearch, expected_type=type_hints["filesearch"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enableadvancedview is not None:
            self._values["enableadvancedview"] = enableadvancedview
        if filesearch is not None:
            self._values["filesearch"] = filesearch

    @builtins.property
    def enableadvancedview(self) -> typing.Optional[builtins.str]:
        '''Setting to suggest plan has some advanced settings present. Setting is OEM specific and not applicable for all cases.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enableadvancedview PlanServer#enableadvancedview}
        '''
        result = self._values.get("enableadvancedview")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def filesearch(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSettingsFilesearch"]]]:
        '''filesearch block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#filesearch PlanServer#filesearch}
        '''
        result = self._values.get("filesearch")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerSettingsFilesearch"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerSettingsFilesearch",
    jsii_struct_bases=[],
    name_mapping={
        "enabled": "enabled",
        "status": "status",
        "statusmessage": "statusmessage",
    },
)
class PlanServerSettingsFilesearch:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        statusmessage: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param enabled: Flag for enabling indexing. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enabled PlanServer#enabled}
        :param status: Type of indexing status. [NOT_APPLICABLE, ENABLED, SETUP_IN_PROGRESS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#status PlanServer#status}
        :param statusmessage: Tells what is happening behind the scene, so that user can knows why indexing is not enabled or if its in progress. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#statusmessage PlanServer#statusmessage}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1592e24c9b87be87bc53b440268afb43be47e3107ba7dbae057b5ea5e765854c)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument statusmessage", value=statusmessage, expected_type=type_hints["statusmessage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled
        if status is not None:
            self._values["status"] = status
        if statusmessage is not None:
            self._values["statusmessage"] = statusmessage

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.str]:
        '''Flag for enabling indexing.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enabled PlanServer#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Type of indexing status. [NOT_APPLICABLE, ENABLED, SETUP_IN_PROGRESS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#status PlanServer#status}
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statusmessage(self) -> typing.Optional[builtins.str]:
        '''Tells what is happening behind the scene, so that user can knows why indexing is not enabled or if its in progress.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#statusmessage PlanServer#statusmessage}
        '''
        result = self._values.get("statusmessage")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerSettingsFilesearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerSettingsFilesearchList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerSettingsFilesearchList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5425a8da0be7830e8665e70ba3bd31bd9927dd870e37b90b1b2f5f2ba16ba4a1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerSettingsFilesearchOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5208a099492dc1d0a06174ba1ae16ebf2f73faa82396a7d67cb7f3432cdc9f2e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerSettingsFilesearchOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b91d5fee917d869ec2d39004f8758555554846bf674e55d03156aefb9af0fe1d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__743a7e54001c0de0a9d9eb15de005cef6cdd9bf0094d53c95ed80109e7cd55d3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__83900bac25cd53c2dd35bf22fa02a4625937ac3862d428f6289268b271c30ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettingsFilesearch]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettingsFilesearch]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettingsFilesearch]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f841d7e2462b9372289a6d0898872b75c61841f251c8b8605fb9e6bf0c070cac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerSettingsFilesearchOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerSettingsFilesearchOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f49c9c26b06f43cfdc2ac6919676e160d4cf1ca5a72e657f1b0960f0d4e49036)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @jsii.member(jsii_name="resetStatusmessage")
    def reset_statusmessage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatusmessage", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="statusmessageInput")
    def statusmessage_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusmessageInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9128a7c362f5cd2011ed8c686c791d56212d746f7763fd8be82714a37ff64b34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c662a24940fcff34a1657fb5184589c0876c4a89925ae53050462d6bd4590d7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="statusmessage")
    def statusmessage(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statusmessage"))

    @statusmessage.setter
    def statusmessage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__336562e13b028403ff0cda0039f864aeab0ad01a3cc12ab54aed4235bc4cb452)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statusmessage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettingsFilesearch]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettingsFilesearch]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettingsFilesearch]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59656435635bfe3e5637b272479c1d8729c42c3ff9039b91c1d742695996877b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0307986b3ddc34daa181bc69c90e73f714bb4be57007c8e7f3402e272a206c02)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76771d6bb3504a03b0ef0a7aea21bff8c5f6b5371c91f41fd06c59e7591cb8a7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c08129135e5ab1babbf5d9a95b55ce33152a34271cf2887fd1b87b7631a827be)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbf3569f68ec1ec040ea7d524135a55a2545a91faafd8acb1871baa9e16f260e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ec4f11004c3d1d55208fbe169344b2fd6300684ce59b5cbaf6cee08646ef63d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1de63713e90de7e962ca50ba491da49d7f49f32ca318928f78182db0d022d7e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__189f00a3eccb7043828d910dd4cf8fa642364ae7ad0ca7dc0ab3e9e32e50530f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFilesearch")
    def put_filesearch(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSettingsFilesearch, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__180a8bb42547e15f7ef9b627befebbec235d5945acda82869c3f9e97951bafa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilesearch", [value]))

    @jsii.member(jsii_name="resetEnableadvancedview")
    def reset_enableadvancedview(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableadvancedview", []))

    @jsii.member(jsii_name="resetFilesearch")
    def reset_filesearch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesearch", []))

    @builtins.property
    @jsii.member(jsii_name="filesearch")
    def filesearch(self) -> PlanServerSettingsFilesearchList:
        return typing.cast(PlanServerSettingsFilesearchList, jsii.get(self, "filesearch"))

    @builtins.property
    @jsii.member(jsii_name="enableadvancedviewInput")
    def enableadvancedview_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableadvancedviewInput"))

    @builtins.property
    @jsii.member(jsii_name="filesearchInput")
    def filesearch_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettingsFilesearch]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettingsFilesearch]]], jsii.get(self, "filesearchInput"))

    @builtins.property
    @jsii.member(jsii_name="enableadvancedview")
    def enableadvancedview(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableadvancedview"))

    @enableadvancedview.setter
    def enableadvancedview(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__829be533b6266f01eeab355360afda22a4cd62fb303505de36ce7a4ba5018464)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableadvancedview", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d4045e1d77cce7ae39b5b21febf41aad36355e1f2b7d4791304c52ffd920622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerSnapshotoptions",
    jsii_struct_bases=[],
    name_mapping={
        "backupcopyrpomins": "backupcopyrpomins",
        "enablebackupcopy": "enablebackupcopy",
    },
)
class PlanServerSnapshotoptions:
    def __init__(
        self,
        *,
        backupcopyrpomins: typing.Optional[jsii.Number] = None,
        enablebackupcopy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param backupcopyrpomins: Backup copy RPO in minutes. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcopyrpomins PlanServer#backupcopyrpomins}
        :param enablebackupcopy: Flag to enable backup copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enablebackupcopy PlanServer#enablebackupcopy}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f42cd48963db11967fb727bf38ddc6931fe05e672012b68cadd79c3cd44b695)
            check_type(argname="argument backupcopyrpomins", value=backupcopyrpomins, expected_type=type_hints["backupcopyrpomins"])
            check_type(argname="argument enablebackupcopy", value=enablebackupcopy, expected_type=type_hints["enablebackupcopy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupcopyrpomins is not None:
            self._values["backupcopyrpomins"] = backupcopyrpomins
        if enablebackupcopy is not None:
            self._values["enablebackupcopy"] = enablebackupcopy

    @builtins.property
    def backupcopyrpomins(self) -> typing.Optional[jsii.Number]:
        '''Backup copy RPO in minutes.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#backupcopyrpomins PlanServer#backupcopyrpomins}
        '''
        result = self._values.get("backupcopyrpomins")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enablebackupcopy(self) -> typing.Optional[builtins.str]:
        '''Flag to enable backup copy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#enablebackupcopy PlanServer#enablebackupcopy}
        '''
        result = self._values.get("enablebackupcopy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerSnapshotoptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerSnapshotoptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerSnapshotoptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e75eee46c5c58387882c43fd9d62f5f234e0a49acfc755a337ce839b2b5d8e7a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerSnapshotoptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__014e03066ca25adff2f5582dfad4cf37a85352fc469b747657e0a48c322bb378)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerSnapshotoptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1ff795aba96f8744ce7ad6150a0320466b99dc3a38e5c7e4f6b9d134ad23c35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9b7b2c01c924354062524e16ccf7e7b7a06f3466bd3718b87c630c08be7830c8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b584ca9dbb1f70f5aaa50e8f26bf9c3af63216cdae9d738bd393c9cd247ae6c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSnapshotoptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSnapshotoptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSnapshotoptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__febb60f7468595075d62dc1e2aa3e83afdcf383f19717303d569c67883105ac1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerSnapshotoptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerSnapshotoptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0ab9101a2bf338523e9dd66d584d0e196ff0133025c5eea50547939f80a60ba)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBackupcopyrpomins")
    def reset_backupcopyrpomins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupcopyrpomins", []))

    @jsii.member(jsii_name="resetEnablebackupcopy")
    def reset_enablebackupcopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablebackupcopy", []))

    @builtins.property
    @jsii.member(jsii_name="backupcopyrpominsInput")
    def backupcopyrpomins_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupcopyrpominsInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackupcopyInput")
    def enablebackupcopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablebackupcopyInput"))

    @builtins.property
    @jsii.member(jsii_name="backupcopyrpomins")
    def backupcopyrpomins(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupcopyrpomins"))

    @backupcopyrpomins.setter
    def backupcopyrpomins(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c975cccfe64ea8c5f5babe260c543c5a1161064405aa090524c87af26facaf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupcopyrpomins", value)

    @builtins.property
    @jsii.member(jsii_name="enablebackupcopy")
    def enablebackupcopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablebackupcopy"))

    @enablebackupcopy.setter
    def enablebackupcopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9791377d9ec776a1aee4759708c56fb9b83a2d9364e38e99a6e53edff3d3902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackupcopy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSnapshotoptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSnapshotoptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSnapshotoptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0df0d9906f332b466ee1311985e5c84523dfe5012e54fc27b273f3b1ce75b01e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerWorkload",
    jsii_struct_bases=[],
    name_mapping={
        "solutions": "solutions",
        "workloadgrouptypes": "workloadgrouptypes",
        "workloadtypes": "workloadtypes",
    },
)
class PlanServerWorkload:
    def __init__(
        self,
        *,
        solutions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkloadSolutions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        workloadgrouptypes: typing.Optional[typing.Sequence[builtins.str]] = None,
        workloadtypes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkloadWorkloadtypes", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param solutions: solutions block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#solutions PlanServer#solutions}
        :param workloadgrouptypes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workloadgrouptypes PlanServer#workloadgrouptypes}.
        :param workloadtypes: workloadtypes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workloadtypes PlanServer#workloadtypes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae175010f8b0287fe2749f269a9611b8d4a5a72455c87a8e723ad7e021adfe3)
            check_type(argname="argument solutions", value=solutions, expected_type=type_hints["solutions"])
            check_type(argname="argument workloadgrouptypes", value=workloadgrouptypes, expected_type=type_hints["workloadgrouptypes"])
            check_type(argname="argument workloadtypes", value=workloadtypes, expected_type=type_hints["workloadtypes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if solutions is not None:
            self._values["solutions"] = solutions
        if workloadgrouptypes is not None:
            self._values["workloadgrouptypes"] = workloadgrouptypes
        if workloadtypes is not None:
            self._values["workloadtypes"] = workloadtypes

    @builtins.property
    def solutions(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadSolutions"]]]:
        '''solutions block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#solutions PlanServer#solutions}
        '''
        result = self._values.get("solutions")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadSolutions"]]], result)

    @builtins.property
    def workloadgrouptypes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workloadgrouptypes PlanServer#workloadgrouptypes}.'''
        result = self._values.get("workloadgrouptypes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def workloadtypes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadWorkloadtypes"]]]:
        '''workloadtypes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#workloadtypes PlanServer#workloadtypes}
        '''
        result = self._values.get("workloadtypes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadWorkloadtypes"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanServerWorkload(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerWorkloadList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerWorkloadList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e9b4220445d205475b16d79571eecc7ee069fc855b0f1fc88d4b0b0dc75a9be4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerWorkloadOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77e096e1dd30422b42243c691cb448a52c8962ede25705cc3a835a24cd6c6000)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerWorkloadOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02378665c7ca488eba0cd5b7bffb3be27707fea3513af8de7ec4155c44fb8f63)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a53d46d16cb7d6de92635a0f1f94044f25ccdf1012bd8f148cc7f8d5c966a396)
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
            type_hints = typing.get_type_hints(_typecheckingstub__72b1820e36d57c464af231d338e03bba8a05667770dbb50077d3ddcff28741a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkload]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkload]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkload]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2dc163bc89978c856003d7831f612b02bc864784bf619152c88cbdd3ab4404e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerWorkloadOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerWorkloadOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__27e61115779ae46ef9e4dd094e8c69f3ea55c219c00233174db3efbf349384f8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSolutions")
    def put_solutions(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkloadSolutions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2841b0e0c85d1fec704fe801674c16040525f76eba80c4b846bd969efb43718a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSolutions", [value]))

    @jsii.member(jsii_name="putWorkloadtypes")
    def put_workloadtypes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanServerWorkloadWorkloadtypes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d89fa7dae45f315582e178e4ce1e7b2304e1e035acbad9bc2f476d39e1703c61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWorkloadtypes", [value]))

    @jsii.member(jsii_name="resetSolutions")
    def reset_solutions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSolutions", []))

    @jsii.member(jsii_name="resetWorkloadgrouptypes")
    def reset_workloadgrouptypes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadgrouptypes", []))

    @jsii.member(jsii_name="resetWorkloadtypes")
    def reset_workloadtypes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkloadtypes", []))

    @builtins.property
    @jsii.member(jsii_name="solutions")
    def solutions(self) -> "PlanServerWorkloadSolutionsList":
        return typing.cast("PlanServerWorkloadSolutionsList", jsii.get(self, "solutions"))

    @builtins.property
    @jsii.member(jsii_name="workloadtypes")
    def workloadtypes(self) -> "PlanServerWorkloadWorkloadtypesList":
        return typing.cast("PlanServerWorkloadWorkloadtypesList", jsii.get(self, "workloadtypes"))

    @builtins.property
    @jsii.member(jsii_name="solutionsInput")
    def solutions_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadSolutions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadSolutions"]]], jsii.get(self, "solutionsInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadgrouptypesInput")
    def workloadgrouptypes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "workloadgrouptypesInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadtypesInput")
    def workloadtypes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadWorkloadtypes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanServerWorkloadWorkloadtypes"]]], jsii.get(self, "workloadtypesInput"))

    @builtins.property
    @jsii.member(jsii_name="workloadgrouptypes")
    def workloadgrouptypes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "workloadgrouptypes"))

    @workloadgrouptypes.setter
    def workloadgrouptypes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c24854de6fbfc6b3990fc9519c0da4268769bfcbf8bd8140dcd94f2616ba7b0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workloadgrouptypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkload]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkload]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkload]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69169f5eeda3f8d62a72eab06000942e09f0555ef6928657dcab9a503947baba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerWorkloadSolutions",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class PlanServerWorkloadSolutions:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2b2c172a29bf42c69f7f836a10dc05d9c094d4050de91acfda8d32898d8def4)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

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
        return "PlanServerWorkloadSolutions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerWorkloadSolutionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerWorkloadSolutionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__407770e36425e777b8ee566a306e1a7e5e6ad26befe9a70e8162963113a933ad)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanServerWorkloadSolutionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0693ee229c4840bb7f63abdab9939ff7969c2cc1efba2a9001f5551fc9bc083c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerWorkloadSolutionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7ef5651a61c67763e734c33def5bd3936d0569d1459083a9347b3cdc393db7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4fd09c99f3e67d8844449e54ca825e1d17960ad9200c101763246f8396534560)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7565ca82674573268d0f4b04428af7777adbc5f08037a351410e65211911cbd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadSolutions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadSolutions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadSolutions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eaa8f9f912e57b33814f73fc75ca83df8610b70cb0642374c0be959e420763e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerWorkloadSolutionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerWorkloadSolutionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ea4d7a4579223de624ca18dd8f4c7b6355797ac91d9c78ac7f6586fb7eba45f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0984955ef4ee0091b8de7a4c5edf994bdb73c483be211046e9ec921ce460f452)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadSolutions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadSolutions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadSolutions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f2e4a6b467bfd20dd19b309f01d409b053e2c81ce9e6574a6e59697a673c99e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planServer.PlanServerWorkloadWorkloadtypes",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class PlanServerWorkloadWorkloadtypes:
    def __init__(self, *, id: typing.Optional[jsii.Number] = None) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7796b2c3b9850932ff6975df45d8487cd2004b599f5430af5621cd9141e8efa)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_server#id PlanServer#id}.

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
        return "PlanServerWorkloadWorkloadtypes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanServerWorkloadWorkloadtypesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerWorkloadWorkloadtypesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__585bffd908153657fa64f45852b4b51a143f95f954b8e410e3556573a15fa758)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanServerWorkloadWorkloadtypesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a03473063f23426aa15efe19d128194706c5f9618137fa17c4fa60fe73ad925c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanServerWorkloadWorkloadtypesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1586d6b7f4ee2cced2f305a01de2e5cfb775573adfa44a7773ae5c4516ec6c22)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4febea0943cc82d72785a85bc0edc6c7c16d3bcd5dd4dc981b7aeb8d89ec8d54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3cf00af18cb85ad3f60cf65abbfa48c8643bb6639a200af2c613b7efad62702a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadWorkloadtypes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadWorkloadtypes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadWorkloadtypes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bb85492d50ba6383bd2bd8439bf55884df32823fde8ddc9b0c0fa5f2eb8c3db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanServerWorkloadWorkloadtypesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planServer.PlanServerWorkloadWorkloadtypesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d3193a767cb3cc70a1b9be0591d35e0babc1bcaaf2e602c3a6f8dea5761af3d2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1224d890e277a63989cec58c301a53082b05b3544d07dcbc2d383aef2787d25c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadWorkloadtypes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadWorkloadtypes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadWorkloadtypes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c03e74ed8e34874a56d6154ae30da8d446f451430864bd21a03c116b03754b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PlanServer",
    "PlanServerBackupcontent",
    "PlanServerBackupcontentList",
    "PlanServerBackupcontentMacnumberofdatareaders",
    "PlanServerBackupcontentMacnumberofdatareadersList",
    "PlanServerBackupcontentMacnumberofdatareadersOutputReference",
    "PlanServerBackupcontentOutputReference",
    "PlanServerBackupcontentUnixnumberofdatareaders",
    "PlanServerBackupcontentUnixnumberofdatareadersList",
    "PlanServerBackupcontentUnixnumberofdatareadersOutputReference",
    "PlanServerBackupcontentWindowsnumberofdatareaders",
    "PlanServerBackupcontentWindowsnumberofdatareadersList",
    "PlanServerBackupcontentWindowsnumberofdatareadersOutputReference",
    "PlanServerBackupdestinations",
    "PlanServerBackupdestinationsExtendedretentionrules",
    "PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule",
    "PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleList",
    "PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionruleOutputReference",
    "PlanServerBackupdestinationsExtendedretentionrulesList",
    "PlanServerBackupdestinationsExtendedretentionrulesOutputReference",
    "PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule",
    "PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleList",
    "PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionruleOutputReference",
    "PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule",
    "PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleList",
    "PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionruleOutputReference",
    "PlanServerBackupdestinationsList",
    "PlanServerBackupdestinationsMappings",
    "PlanServerBackupdestinationsMappingsList",
    "PlanServerBackupdestinationsMappingsOutputReference",
    "PlanServerBackupdestinationsMappingsSource",
    "PlanServerBackupdestinationsMappingsSourceList",
    "PlanServerBackupdestinationsMappingsSourceOutputReference",
    "PlanServerBackupdestinationsMappingsSourcevendor",
    "PlanServerBackupdestinationsMappingsSourcevendorList",
    "PlanServerBackupdestinationsMappingsSourcevendorOutputReference",
    "PlanServerBackupdestinationsMappingsTarget",
    "PlanServerBackupdestinationsMappingsTargetList",
    "PlanServerBackupdestinationsMappingsTargetOutputReference",
    "PlanServerBackupdestinationsMappingsTargetvendor",
    "PlanServerBackupdestinationsMappingsTargetvendorList",
    "PlanServerBackupdestinationsMappingsTargetvendorOutputReference",
    "PlanServerBackupdestinationsOutputReference",
    "PlanServerBackupdestinationsRegion",
    "PlanServerBackupdestinationsRegionList",
    "PlanServerBackupdestinationsRegionOutputReference",
    "PlanServerBackupdestinationsSourcecopy",
    "PlanServerBackupdestinationsSourcecopyList",
    "PlanServerBackupdestinationsSourcecopyOutputReference",
    "PlanServerBackupdestinationsStoragepool",
    "PlanServerBackupdestinationsStoragepoolList",
    "PlanServerBackupdestinationsStoragepoolOutputReference",
    "PlanServerConfig",
    "PlanServerDatabaseoptions",
    "PlanServerDatabaseoptionsList",
    "PlanServerDatabaseoptionsOutputReference",
    "PlanServerOverrideinheritsettings",
    "PlanServerOverrideinheritsettingsList",
    "PlanServerOverrideinheritsettingsOutputReference",
    "PlanServerOverriderestrictions",
    "PlanServerOverriderestrictionsList",
    "PlanServerOverriderestrictionsOutputReference",
    "PlanServerParentplan",
    "PlanServerParentplanList",
    "PlanServerParentplanOutputReference",
    "PlanServerRegiontoconfigure",
    "PlanServerRegiontoconfigureList",
    "PlanServerRegiontoconfigureOutputReference",
    "PlanServerRpo",
    "PlanServerRpoBackupfrequency",
    "PlanServerRpoBackupfrequencyList",
    "PlanServerRpoBackupfrequencyOutputReference",
    "PlanServerRpoBackupfrequencySchedules",
    "PlanServerRpoBackupfrequencySchedulesList",
    "PlanServerRpoBackupfrequencySchedulesOutputReference",
    "PlanServerRpoBackupfrequencySchedulesScheduleoption",
    "PlanServerRpoBackupfrequencySchedulesScheduleoptionList",
    "PlanServerRpoBackupfrequencySchedulesScheduleoptionOutputReference",
    "PlanServerRpoBackupfrequencySchedulesSchedulepattern",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsList",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptionsOutputReference",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternList",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternOutputReference",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneList",
    "PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezoneOutputReference",
    "PlanServerRpoBackupwindow",
    "PlanServerRpoBackupwindowList",
    "PlanServerRpoBackupwindowOutputReference",
    "PlanServerRpoFullbackupwindow",
    "PlanServerRpoFullbackupwindowList",
    "PlanServerRpoFullbackupwindowOutputReference",
    "PlanServerRpoList",
    "PlanServerRpoOutputReference",
    "PlanServerRpoSla",
    "PlanServerRpoSlaList",
    "PlanServerRpoSlaOutputReference",
    "PlanServerSettings",
    "PlanServerSettingsFilesearch",
    "PlanServerSettingsFilesearchList",
    "PlanServerSettingsFilesearchOutputReference",
    "PlanServerSettingsList",
    "PlanServerSettingsOutputReference",
    "PlanServerSnapshotoptions",
    "PlanServerSnapshotoptionsList",
    "PlanServerSnapshotoptionsOutputReference",
    "PlanServerWorkload",
    "PlanServerWorkloadList",
    "PlanServerWorkloadOutputReference",
    "PlanServerWorkloadSolutions",
    "PlanServerWorkloadSolutionsList",
    "PlanServerWorkloadSolutionsOutputReference",
    "PlanServerWorkloadWorkloadtypes",
    "PlanServerWorkloadWorkloadtypesList",
    "PlanServerWorkloadWorkloadtypesOutputReference",
]

publication.publish()

def _typecheckingstub__22e432b8d2ea0e9669ad61aac9f4c1525a6f5bcc1645c90940ff2f8cd3e949cc(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    planname: builtins.str,
    allowplanoverride: typing.Optional[builtins.str] = None,
    backupcontent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backupdestinationids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    backupdestinations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    databaseoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerDatabaseoptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filesystemaddon: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    overrideinheritsettings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerOverrideinheritsettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    overriderestrictions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerOverriderestrictions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parentplan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerParentplan, typing.Dict[builtins.str, typing.Any]]]]] = None,
    regiontoconfigure: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRegiontoconfigure, typing.Dict[builtins.str, typing.Any]]]]] = None,
    rpo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    snapshotoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSnapshotoptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    workload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkload, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__2516b8498e4cca96bdbeddd5f995bccad75d8f82dc8a2ca8a411ae64369ff290(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__665d8c418c0ea7665d6f561d778c0e34022f37098ff395be34ecfcdd82db9977(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f12ae17a87ccb160188a41e5e332d3d7089581d467169bbc1c7395dc8dc2088d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinations, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1350f10f3732b99c9b7814de7783ad511dba69baf97c830d7708f4564611693(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerDatabaseoptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be74ab2bd508000bbcd8e7fe1ee9a9bcbe01957763d82422d7c48814a1f611ad(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerOverrideinheritsettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3b1003edb6bbdd357ee371c00fbf042a72517b2fa3b814ad0add6f8adf84c74(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerOverriderestrictions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__067f43ab282ea5f2a85cd257094fc123b3c691dd289aac39250ac8a4dce3e2db(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerParentplan, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c260fd1233d271e4e1b288ed0f3953d9574674011ff62e754dcb02ecc5796d4e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRegiontoconfigure, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f189b69c9af965a26975aaedc0c53bdf3cf0b55e9f11e0452e605c5280905b6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpo, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__691f009a27ef2bed1ad4b6d78976cf7461543f6bd146fe56b600ae6b243df6d8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91166b7ec47ee27894b607564260d97649d287678350e11d1b79bf55a27844fd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSnapshotoptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb6989fa02a27f451803c56008af8adf30a3766cb10da584e03d40a1537518f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkload, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__745b643b5e21096f1aa054f08664f87cd2099185017aeeedca05117729b2c4fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcb6a592e28478f2ac10da8848011a6f48cd91035939b38ded61fcf5c869ed97(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dd3c9200e1ef822589db90be8d4dad7f440c1ed46d840cb575069eae09a0eaf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee75d4a0122f8688ac55d90aa9331872ab407e15f61de32782e8e3ddd24b0e14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ba117c04095e48b239a2100de552bd625a49e41e95c8124b4c4a3d561cbc51(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8685d071c8be667872291d4c6d67d212f5e350bcd0a914334744148c99f18c37(
    *,
    backupsystemstate: typing.Optional[builtins.str] = None,
    backupsystemstateonlywithfullbackup: typing.Optional[builtins.str] = None,
    forceupdateproperties: typing.Optional[builtins.str] = None,
    macexcludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    macfiltertoexcludepaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    macincludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    macnumberofdatareaders: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentMacnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    unixexcludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    unixfiltertoexcludepaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    unixincludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    unixnumberofdatareaders: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentUnixnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
    usevssforsystemstate: typing.Optional[builtins.str] = None,
    windowsexcludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    windowsfiltertoexcludepaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    windowsincludedpaths: typing.Optional[typing.Sequence[builtins.str]] = None,
    windowsnumberofdatareaders: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentWindowsnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8371d2e155039760a040c04d50e1bfe80ad68f08720f3665adb1d90bc4f4d4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d445458422565ee223bedeaae994a5855a1a5458dbe1fac315ee2703434b092f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__effa3da7f3195c6935a5572cbf72b9a1217a7a76e8b575adfbeb874936292bf1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf102ff45615eca46d7f30d0b21e6ff6caa6163faa0bcac2f620dc1b422cab45(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f5408d05f40c396c542e256ce034f66da9ffd5d260e03ae2254cbb413e1582a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__321f9423713da4810d738b4f41f79d99bab82bf4fa99a4aff0c1ddd124c41f25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1dbfc474a45a3b8508efcf51061681a829cfca8c03c110401089910ddd3fb9a(
    *,
    count: typing.Optional[jsii.Number] = None,
    useoptimal: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce991efd5fc5a504f41aa7d0b6f4e6166acf05b9204cfa7044bdecc0fad145f2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29058b86b96542d082aaaa78f30f9ee2c0d61d89c186461fc5b095847e57d3d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e564dc88cea143224d46a42365b5e797bd1062e8797590d7617e5223ba559f96(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbad3eabb14cfe9c383206b2d82913152206e42c6d30946bab4fab8628b82b7c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d47a205cd01b3e9bad64072c02692b48b95e470a30acf686b04d5779a3eb09f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e128b39518d41a940aca1c28701ff2b97f992eeb716f92e847e345419babf1a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentMacnumberofdatareaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f1024a52d8ccadd74d76f38ebf20ea882e38b4df7a6c3cd42eda4e268d3a10(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152b842128b4c03269ba5cf0cbd43b4832fe16e9f25b97a92d6281d5c7c50ad1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8569c94f3ff1d7c2009349adbe755c354a9d3f7ec83abc30f319d01e6474f91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4255ea165dd9200869fd9bf67a5c17f1612ecc31ae00c81db33f4cdf438bfda(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentMacnumberofdatareaders]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c939aa24ce66838d3d4a11e0389e9594ee245a2ed768c46e5d636c59f2aa648d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__139c49ed34b5246b68bfe27803bd0962a70ab2fa7700f6f16c7b9c477c8797b6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentMacnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6ea078188853b4a790ab46e18390c2038eb67fa82addd21697c68fe06e9c620(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentUnixnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9102858ab1f6f1dcede2f587905b11e4128a76664ffa9e41be379f2f8f156d0c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontentWindowsnumberofdatareaders, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d74a8b49fd532bf7269c89656ad41a9aead8f2d1e4ba34ad7525f9c3fefbff9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36420f43307b9bff9abbd882e6219f6795a3074490ed4bbd843d29bbe6649b1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b2ee47956e885656856504664e7e9788b9b728184a55d73976af1605347410(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a50469b480c47ab1e7b29351cc0f8468aa180af042e29b9b275e5acd8fef23(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__808b1fef804fdd04ab87f8be54b4ef63e7b8b3586b9b2e70a6f33629a0c7c167(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61ac56330664549c02a4deda4db9168dcdbd58b48e2f9a77c6ae8673f2f2cc5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf2baea9cfb991be037dcfb05cd83a28ea143c52bac8392f12d0bf2f0e690d1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26190fe01eaa1ab83fb4e1ad91f64e2f04a74d52345cffa23a5b19e970ffa4da(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a52c0eb2bb186dbb8fdab989d3841cfa9c7f602d64c6dd823f5d19bae071361(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4973cdd2c81904a8ca989ebc92dff88c280ef18bd0eb4743ab4aa65730a7a3bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5c1c6819aa52e949aad92282248db40842ff02f79782cc9a7d27382759b8f7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccfc14ebdd8eeaa64bd6a3ea5c711b902a0c6d8f8f0df589d6dce0c2c540f45f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e28600fdfc558a24c76d1efded989520523807df7cca4e149551a2e89d8fb444(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4238512131820d1d0a1c6f821a67eb63903c14c9eb4341c91f05e230d7c6e48(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b41ea06ef046a0db9b26b8a76822c591ad8ce55e686fd31e8e4e53cd02750f81(
    *,
    count: typing.Optional[jsii.Number] = None,
    useoptimal: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f130f3b6ef0da73dd66c965eb4841167ccc0fcc855830f3c63958695cf6f917e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8bf01fa64bd3f0f0c5c1c8438f5425382d4eb04ce66acbdd254d9dc9003e5a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c96dda09f259b559e95761b348d2caa831bfc6f242e10602be06c7a7a2c5c6f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a969ecb96e5b8102b89e4241e327d5b06b2165c7402439a2f81559fd80bed0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7fa0d79aed4427734ed8d68367cdc87d49016e335c1e9aa208e150767aa2eb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a58b6f09df12f962d6106116ade85881c4d5671269668e2493d334f276a4e75(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentUnixnumberofdatareaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb73849d9447e2914b61a8e487347ccd4e2bf6f6d30710a9d5bd8a6ca83de0ab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2ed10615abc7c72745f571ee10389393f29a02c62894e6de0f1fc985f7fcf27(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd98d5138836dc4316a40a1419deae32394bef1229372eac5f8739d936e35212(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__308a5483236896d57e4dce6418801036505a58175b52cbdf6ab43d4efe41e11e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentUnixnumberofdatareaders]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__571a894648d40a4b3b3e7234d2e95e865c1652a082d112f8b4e61695e66f665a(
    *,
    count: typing.Optional[jsii.Number] = None,
    useoptimal: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfce3ad63495d1cdae392858156a1f6a5210835994ac6b92b2d4f882666668ac(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ae4f059e65c533e89592ef8ddd08f346f8de978db2a7f30bb1f28485c8051f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dba4de29b04d8cb7ce3d3e2121802c0ba6862551b55fd61749866759a62f1f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb4545d368a25d28be8a18a198023798fc0821c57dc7b300419e398edfd45093(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a7204f0017b6d8c9d91899f1af8481ce77321841dea206d9fcb24195cc12fe(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8196ebb2e6849e5e40e4f6febee38d5c8afa4d3975c06666698ed2ea974522e1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupcontentWindowsnumberofdatareaders]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b352db9a564de3251efacd4af8fb838328dc956103db6edd7c5fb4e94bb82e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7edb1c99a6ed792b493b3901b9fae4bc05070f2175ebe89926b7910f704246e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156403f74b4499af1dd2e2fda4590296c65c3e3fdfad4c1ac28b1fadf5e6b156(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e454008eeeef436618964330e52f411f9b22b8e9ad8f6b12ad706d0f7fc85bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupcontentWindowsnumberofdatareaders]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__258ffba03b2d99c22fe184dd52342ab038a1fe903587577398628798b103f06a(
    *,
    storagepool: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsStoragepool, typing.Dict[builtins.str, typing.Any]]]],
    backupdestinationname: typing.Optional[builtins.str] = None,
    backupstarttime: typing.Optional[jsii.Number] = None,
    backupstocopy: typing.Optional[builtins.str] = None,
    extendedretentionrules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrules, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fullbackuptypestocopy: typing.Optional[builtins.str] = None,
    ismirrorcopy: typing.Optional[builtins.str] = None,
    issnapcopy: typing.Optional[builtins.str] = None,
    mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    netappcloudtarget: typing.Optional[builtins.str] = None,
    optimizeforinstantclone: typing.Optional[builtins.str] = None,
    overrideretentionsettings: typing.Optional[builtins.str] = None,
    region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsRegion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    retentionruletype: typing.Optional[builtins.str] = None,
    snaprecoverypoints: typing.Optional[jsii.Number] = None,
    sourcecopy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsSourcecopy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    storagetype: typing.Optional[builtins.str] = None,
    useextendedretentionrules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39efe4c0d83bbd004534bcc9a89915e887828e6c2965639722cf236975141f87(
    *,
    firstextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    thirdextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8244daf054991252209e4fb6a15bc4b0a14bac18bb00f4ac248fbb17de54b7(
    *,
    isinfiniteretention: typing.Optional[builtins.str] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77b0e706f44b0630de46ebb749e8b23889176a454095f3e6b1648dc76de26120(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358ffae471839e145d25d9a9f11e9ce9032a903f061089facce99fdb988fa141(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ace07633191daa955bec670cd9274a906704324df666150c05d78bfd542e579(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bcae20428571adc8ad5ed4bd07f8e999f677cf66b10d3e29c56fddd08ab4e9c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e55412b10d71ed57ffc51a5c7ec890fd9feaad105f6fa3860e24c99078a67424(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8573f1c61befb25b91011ec1b4ce0faaaa1e901aba3892e5350207875f5183b4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f990763a347c2c3d694b6f66ba0f2e0fdec029f17a79968c92b987c68ebc9a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eaf4e0317f03fa24fe7e010bfbcca2b24019af444e07753eaafced77111c713(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2870690fb74d046da24d2248757196661bde020c4c467097cf615b0847e007ac(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4121f9348ca851f15b1a80a755f5f7c3d85f5e47716716d39f683c0aefe9be3f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef808f67c17ddb091295e68c38a9b7bbb58417f22e8ee305c5306e8087b5514(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0c9ce861c649813a739ce61799e9fa18f5f47bff1a142d6ecc879cd43eb4834(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8052b5c9ed63c090c914ddbb07ee43b1ba0fb1c3dc9ddb35f5349ce5e5555fa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f010511270d2957497639d15c316d3dbb8535beb2a0d0ee6f32cc9d49e5ae7ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cbd3533811559d058cd4bc283ccfd764fb71a4cd287d3d42f62cdea4d3f6a84(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6af1052c5b2d98125d73c9ef2c30429836bbe45cafe07d9d18f868e63cc080(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f328238829ef02d2ff4b6c137ff61491ee398d7e62fb99de67d11d138f2a85d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__887cbc28e6edeb31476e62595f25af4e54e5ff8313fc952c2ef1a7e700cbb399(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7faf80aae7782d56142709ea6f4da57ab1bdca9de77a8814fda9b2aaa381eda(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesFirstextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63be7903da70d123a0ffe0f7624154382d98bc1cab2cb439b4f8fe748a673bcf(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__064bf76a9c2dbcf9f3f1886211f9bacafd06d04622882e8ba7b339f5d9094306(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621089bb8dd8356987bea6d9590b3cd7619e8e45cae5509c4b6589c173a20030(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrules]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41a37839f39207d30239c20d81b9978641a8e65c76c31deb1a9e5808efdf32ea(
    *,
    isinfiniteretention: typing.Optional[builtins.str] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8591dccbe51b9ce4001589290b5f8e03cb670ff18d47104d117f547f418d94e3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03add0d57f5c981e58389933e393c9724a53880917a2d27fd88cfe8bda2d09b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03bc8bbd98adde6b6e30fce2558d8af7a8703da427739cf0966bc30f5efc58f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e688a6221c70b01831397993797964944ca2501662e85bbe6ff1069ccaadc97(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4041faee4c7ed6fc96d98f9813445fa0f4bf3d52b2986155f7bcd25c25548fd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da1b682e3967f7a253457121cfe4d7769d231628712d90458bb905e859f60ee8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__871b25ee5985ec40b87113caaec9f373a36892b87760e34128f3a5fce7757185(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ea83007b494ec76c7031d3b4af7a951702b91d1f0e6b096851b6b5d6efd4d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952fe0345002b212e6097eb63eafb13500d5d279f4e76542dd4cf4573d1a2b14(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d88b81b2ca9a5d6bb6707757d5bcedf9f58df0335ec1494771a9afdbd1de91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eaf0391d4b929498663442d85ef9b2d8b1bbeb4827e11f07df2b000e6a5e6924(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesSecondextendedretentionrule]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da9ebefe1129956b60847990347a76ffd4f5a7848330a166b132ececda04ac3d(
    *,
    isinfiniteretention: typing.Optional[builtins.str] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5a406447542819897f479fb1fa93cb0413a727a3c78ffa4c64c1a6b0a22dbd3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__603c08bb9fe1621172f96a62c770ad1c9df302b62d5661f235fc68905d78c6dc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d12ad4c69f03293750317a343cd004018e38678421b0430f89426ba746cab89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b3a4465b3c2b36b757504cc9af7c6c6b6d64b7c3477075506a0ed1ed0544f5c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae1856698e353b8cceb99e2fa7fa4c1b8044aa6b887c84d4cff6e99a0be8ff9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c63b7bd90c8b556a721852d611942be4f6ccceef4ddab14839758209799482ce(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324df69e9d87d594041e84de6e9256be1107fa14dd945f13bdc47930d612ae17(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b73f419b138c455e5151fbba84d8b053ae89f349254a59da0277789bb941a233(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcb735b835f28a0013d200e392266c1e613117c9973c25f882e8f235ca48ed6f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bde59bd4d7537590f142edf770f2780a28c67bc84ccc91938ef3e007e0a93514(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0252eb994b154b99dfa3dc6c538da529ecbb260216c8c56a3bdb7279f519977(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsExtendedretentionrulesThirdextendedretentionrule]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5268cb4afe83be9024c2f780dfab25bae272f522c7dd1ae45edf216d9dd0b4f4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d21dbd055a116b6dcbf91c26585e34fd87d3539230d2bb97de29ea89e64f9466(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e205ebf84f44f1182468f99e093fb8f6e453bc231e6ba0401a296565866ed4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a07d84ff964b50b2efe300d727aaa328176c2ebf144cf75842e765f3438084d5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e2eb867772f741f5f11a57acc1bad1b3b12fe56dcf4896d625869094bac7645(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__018fc22196b1e2e18d532daddfdebd66d838bfb81a731c7eaa612a22cf1cb71d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinations]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40c5c2c255dd061370468c4b500b2843300c6dfd65097fcff8c66dee5b2f4df(
    *,
    source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsSource, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sourcevendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsSourcevendor, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    targetvendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsTargetvendor, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7130e04649484b02f1669df8e4b8569f649830b6b407a6597ba19b2dae3dbf29(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0339fe62522453140bc10692522048ad499d05835bfd7c7de65feadbec01d392(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07e2fa0d34908bdf96ea9dca700bb16b7ea2b189b06957e7dae10059952c2d1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16f65894206e77e6d8f37d7bf6c69fa7249e8bc17b30dcac0295d0e6106987a9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e91f57470f102df08767506ea7c1c08a880d858b75456677049b24de71a9498e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e4b3658411e319486c96245be63cf45aa5cdf5c010e928f8b75c6161b095c56(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a3e38c0a3bd1e07f6853849dcbc4ae5e92dc04545dfe7642a745d3c56b22b3c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4299d86e45e57952474f0d466d4b02c70e7b9e5fb44d2a2802a1e7340f1c3981(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsSource, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1d4941ef5fd0459f58487c7675fbf17489c3b34637c637f895729ceff9571f2(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsSourcevendor, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee31ef7986024842d685a303402b55bc0fad89877b993b3a7457b5b798818c83(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42eb368e31bb5d53f5a121496aac3fe4dc3a03a34f3516eca1aca620dfeeabd7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappingsTargetvendor, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13cbe81886115608b0d93bb116afffd84c8edd5c1913710b3359b85bce4572e5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10c896f3908d1967fa37fb64b4b4cab77327d18db2709d771473d823a2e86422(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9122b84cb1da4079e6a20836b8680afde23e1b48acf298f087308880f4aafd13(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a3e04fec3d10711cc90905cea5b69bf399304f039cae5b06a009a8af7ec8424(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4aa65124097e5614c63f21573e905cc18381207810995e4e8f34c60701d48ed6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__115319e76b85c710c611ad493d7ea3a4f21afa038485f8b07fe94c1290b5c73b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01660c5ad3c7eb46ab83165a8f067e88798c8db90fee403847cae5583523f9dc(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95dd6de5848c19815a17fc039c7bb5d2b6ec8a203a1074256ce6ede422610388(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b9f109830fd841e85cc1a8a4f90cc279d61868312183ca19028f8f8dfacaa2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSource]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95accfff3aca35f3518034ff4e26011af6880db558f88e8536633cd06610dbcd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb097ccc406db51eee6a9d5f3e7adff8ac0c0055b7afc9af4faf7bc113a1010d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__103afe445ce40509a8c9f7322508d11728d135937709f7b2ff595b407ec0fc22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3ab0bc0e72b07a93cf76ddd21315078e5a8f409b6c00ba2222a86e08afcad3e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSource]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a9faeb22bbae4041cf588552a863184537434eb4f79de656af9b7d1b9f8301(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2755ad92705e59984ec15c768b22fc61591df0dfef135b0f4e687138ee746629(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a63f35cd8dc2084a46c81d7578ca773b6827fe5a501a2687c1bf13db56080f05(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a836f844abe0b655673f0b4520b119de6a004802f7a085cc9a7e381d146030f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9503a8650ef929145ef81a1a1fd559c4bf6e6fe2310ce7b574fa7b334f6373(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7adcf98a7861085d8ed899cca16fc76384441231d43c90bad1de343700ee14c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afe61124364b1a17352b0b1ee482645df2f1f531200b2d663df75324a073dba8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsSourcevendor]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f53d3c01e04862eb59d01f97cdd36fa2fd0dc197de0d50a0abcae4d0dd73695(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2627f1ddc8baa98b568863bf4c58c99d51944674a8cf6c9e6c517ba73259dbc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31524071b449429898a84bcb3267841e54148b3ece164cdcfc9c916f871d5d21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33a91969fb9dcb4d6f802ed89fdc471110680a5860f7979cb8f0f42de3bd0235(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsSourcevendor]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df13523a3eb7828abbf38ee31eea861b6a9aec972581f53c15a67bf865ccb40(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d64827f740772c63dcbf88b8173564d8a61917882aaf5bafc13ad808a25078(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b25391f0390ce5d7a009b91a491eb1e85fb2aacef8aea19ee8814e8f878ac14b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ceb5210e015e86844bb25ccd94dde3bf6579e4329bf451281b8e062edf38024(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a09adcc7e87743d6f31b283e4ee594065dde54cb21ebe0acbf2b9e431d81f3de(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b87c9544e572ca04dec1a1d916552019553a5d6de5b13a1e52e573aab62a6273(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__403c4bdac9ff0af8ce0f3a5c4c742510e90899702b1681b0b4f0a6356a070a53(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9adc7bac9b21d11dc0588828b1d55b9312b41b5640d0fccac681fa72c4da638b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48784e82676aad499b2916d460251afe83f99222db873b637250ef0918790c3f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89088530afbbe4d9ecb49a5725ca0bfb0d2695f478975133682ae28ce056147a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc70fe51d9be22c41800ee08ce56d1c0b802f46f92be5c2ae245e14872a429fc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTarget]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81b603b5b8260761ffad48b9c4013f03ee7c9d906f05851d45d3716f254b8f84(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1b7ee3be30dafec674959367b18a804412b2203e855ba89b93446229e502ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929154350963ddcc43e2c22226b338932ff2a09a72477978000ee0e84dc67d6b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dafbfb658b951ba1e49e796a0e1501983e4d0c129b6ef461d6c7e862b9b35be8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c01d66cafd328d6286e2ae896f61180be954fad29e044ca5f4eb269526c6006(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbac3bf13950499b515c52b42fdecca4260f766bf08f5a6fe6e1b1837aab8aec(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fc1e439a4f12dc34a72132c0d6897d4f6e4dba8bc27f27197d47dc7a757a62e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsMappingsTargetvendor]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1700ce19a43ae31c72a8fdca86e38bb935ce8b96da5b12d5bccab9b96667f31(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777dbd0e4af2bef90300dbfda5b54242ce87e92a94babfe59c3b1a744fc064c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fecdf48c7f09fba155ef68b0e01d37d886729638cb6ae5a0bb2f527ed296f22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47a50c71bb3dd719676ee218b36e82465ad8121351c52890582e1fbd6330e48(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsMappingsTargetvendor]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df82dbc5d5ca0aaa4bacb88a307dc1a397547ea0a428042b934c206a5340928(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71274f2a541cc4416ee3ec9c8de7f92d1dd8542a75905b8b6a5ae6bf16368034(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsExtendedretentionrules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d771811529bf09876e471394291d69294acb4f7efdd6d01464ad58b9c20070c8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsMappings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__942a6a027782807ae98607b35e8c4f714d8a93e49f5406dc9e2d07ca4d1510d8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsRegion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2c7cfd78fce525b646fdd5b69e871f3a3cc3e7773c0b0bcde4fe48cfaa5937(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsSourcecopy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86c11f11be4c327e380e00183dc04b00565d2a22f49267d4c992acc4b5e43eb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinationsStoragepool, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ffdcdb419c99f7074af63686ac7fc88ce2bc4f61afbc9faf95f63efa1e7c9cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f6348601cb1100e391c40222deb8e4040639b2dd70e12aaad7a506f4301bf7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a106c7f00a8ca94ecd34e8980de1bc4995b2ef9b29a170477b2d02e7fcc52008(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa9413194f14d7bd3a9833f56abf1e220a023d9911b8f50c7d9d7481bc87a06(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d67c56b5e05bd50c8b5cb886860826aa030261b0306080b6d5cd1bf2de45f78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df577f64f32a159e93a7d75707ac1e2e03685ad818a7167cea9357215a17f681(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0da8c2bd6369831e45d56acd8948080a41caf1051a4d35a46f8201f8590bbb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eaddbb682d3019e20a2ccdd5557915bb6c7f139c53e27f235fa9781e902c3b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c0329944b082a570c58ceb037da893c72a1e66d4d832abec69cb14960c9a7f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620ae7528f34d97f5e590d1ffc34b68a8aecb3745d3cc14a68ffd5a98cff1c88(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b95c9599463930c4118e32eea2e7f387c439a21624196a1f0c080559dcdf70a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4dfb6f174dcce3ed6b0268a3a4f24929e6ae65d39f9db8666abbd9e5393a6cfe(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51acb057c4a81e2f43268acdd676a3700c14f077f2316ad325c6fa1ec34d2301(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88dc448e05ac7c77b694da1f224296e7cf85e89cf5cef390c0fbd6ab923f6d8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c87aa613243dbdfd4b3e35c34dbe6486d79a6956eeeb79ef1db0a7cab3424b1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinations]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c2931983314dfe1e5c9860a1738f8c2436f5bdcdd182f7390dfd87e0ad2f2d9(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c95ceaa5972bbcfcdc74ffd47d1959daf4dd1a489074f7fcd86444410bb1f5(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15c97f071bf6076b8457e15fd37b06145fab42e4b52a1f7a99999f12d12e772e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9164db40ab79eaef8a6e49afcb9db03ecd381244070300d020d355bc117a91c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fbbebce14fde6618244ba18f08147174e5510d5d64a19b42f73b625a903dfb7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2219afa2084ea2231c0fe2149060967b47af05a96437bb487b32201a99a22081(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449bc156ebe740473a8d8a8f3fd5d180b54b3e135dd5aaf0b38ab9a914e085e5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsRegion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ad450a2918046151e193f6c7c45633d149cbe0934b6b1f876ff665ae3abc1a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7b0596168628ec3d4feece5f6ccb590f00258870266d5f54ff770bcaa1d2709(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f0212225c8b4e3f2eb0f0bbc3a6778ccd30e7acea6506e9c2e7d4a7bd0edb28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae1144ad9247f0aa10640f47fb2a4f2222a82df81b0f8ac73d3009b911f807f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsRegion]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40a7e580581f07fdfc34bd2ae4eaf41e807d7e06a9cb120abd4aad28f9e37ebe(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5609f6d330eb4fae18e9efcbce37f297905f471854ff4e34c17a1ca83c38704(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__546aba3d7bae937ae9c50b3b2ba098fc5fdf2ba68e2ede132a62d2b84c1b1b00(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9804b45b43fc2ae966694be11fd60e44f681115856a47b68ba7c47c772b744e4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20cc41cab3fa6f7f6a9d04b09417e4d693baea1ed0b86ee3e003c0f47aa70602(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ec4d452f57f932ec6a3d641d03ed1850a753c4b3a8cffb65f5315d9c02e6e63(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a689095a9c169ddbcf5c34540ed2617f4447f17435def94cdb3dd3d24359c042(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsSourcecopy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59f0e9ca32767822010f7684b1abd5c9f98eacfcb8d882e02df9e37400ce9390(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30f1a2b2d2d041aeb3b7e0b5ca1f71c7114ffcd4f89a653c36c412bc84046d19(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__affeb98c31350fdf586aac1678271766a557c07692b039f63935d70ddbd85a4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ec90847c0589670af9caeae7285e1653fb066c006df96b5b3d5b8603f42589(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsSourcecopy]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bf60ca4bb68b7ccb59e0fa1a139791f9891990c2ee5962062b5a4ceec608f6(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7defe2696d39994e3a70803188fb0e1e31c5bb136cd9de25a04e7569ceea53(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ec6e9775d60ee123624337178403b841b98cc6465cc64171561cb6a7d1cd36(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47ddc4bd22cb6c780f30bcae87d2f7e3cda099795e1bb570757c827f0807f75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84ddd38cbadc5fd8363a68cf32b70dc4d4ff3c7fdd83ea00d361269272b0660f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc5473d23278565dbd5f209e64e881d44a39e04d7355541fd3e422ad272ec2f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed761eb0c705068e1e7a2c91317e1db0358437931968485bc88414a8ab3a394(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerBackupdestinationsStoragepool]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be73cb8906a3718d8b85556783fb93c445f61b1a25c63e525038388ee47c4e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b01f5735c2296142804c42b7a78dbba0d4c99d5ebb3fee76873be1f68e2632(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6d2f838b32d3db9f474aa317fb026dfb0407b2ed472fbb2358a433d3461c5f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22708007f9b14360ca08fdaa03775bcf1e6918ccdb8f3ecd551b50b3862dba8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerBackupdestinationsStoragepool]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76feded72711271d1b1cfa41af8aefa1bc233619c1f777c230575bffe6502d71(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    planname: builtins.str,
    allowplanoverride: typing.Optional[builtins.str] = None,
    backupcontent: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupcontent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backupdestinationids: typing.Optional[typing.Sequence[jsii.Number]] = None,
    backupdestinations: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerBackupdestinations, typing.Dict[builtins.str, typing.Any]]]]] = None,
    databaseoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerDatabaseoptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filesystemaddon: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    overrideinheritsettings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerOverrideinheritsettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    overriderestrictions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerOverriderestrictions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    parentplan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerParentplan, typing.Dict[builtins.str, typing.Any]]]]] = None,
    regiontoconfigure: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRegiontoconfigure, typing.Dict[builtins.str, typing.Any]]]]] = None,
    rpo: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpo, typing.Dict[builtins.str, typing.Any]]]]] = None,
    settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    snapshotoptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSnapshotoptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    workload: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkload, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46ac10c2c4acae61e266263c28e001ce39a2f728e253d7bf4c5f328644afc141(
    *,
    commitfrequencyinhours: typing.Optional[jsii.Number] = None,
    logbackuprpomins: typing.Optional[jsii.Number] = None,
    runfullbackupevery: typing.Optional[jsii.Number] = None,
    usediskcacheforlogbackups: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ef80805d6aea0575ac696fb025a5ef499f1f9050d87e6aa169e868d57e87f28(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23719ca37a40adf456b288784daa8858c2e0ba7bae3cfafb57150858d0006d22(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__859544551ea4362ec769b6671db1d9edb5be91b8061246c1ae1a8786144ae0c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f603f636553eb78479d8b2757b4253f66d8910e14ab11e21a96959277980bda(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bbb7d4c9329b56bf5aa392be3e1f48bb4460dc3e6a432610846b96758857ff3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de1e5e99462b4bd4dbd4c1b969ecf2d0c2b3eecde5d3e84f2037ef28b3bd7260(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerDatabaseoptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6d41e24f63d40b082c817cc5859639f8b70193d7dfefab85fafcf01ae61935(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677e3014b29d1739ed63474f51049530fe59d7d05530299c0295c7e06132daef(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cfaa3576c7dc710b8319b2546af2d4d30b59f983748e5da557181aad9ed8d5d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60897e38c923a1ccb696ea62ad86ab10f9a76532dfc2d00b5093e30869fd8b71(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a034358651df09af2f406649116e37f45eedc9065efc69560b7f7c901752121d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09c580bec69b45c450f9449619150b24ed7b18f30f01eb6c60fa142b9bf9eaff(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerDatabaseoptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61085a2b61be3a2ea6865ae98eab9c8daa2cf8b35db548053a3f3a58b5258082(
    *,
    backupcontent: typing.Optional[builtins.str] = None,
    backupdestination: typing.Optional[builtins.str] = None,
    rpo: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3c783987823e186bf26f067b9946778906fd927fc25389cd3e8b4a0637aed88(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43bb1efd5abbea2debfb54cabba71c0e642387f5056d59e9f917b7548792a117(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__092be14e27429621558eae49b47c170c7756259356500711b21ccce604f94cd7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace07cea9d6c4f925cbe3fe04604ede0546b0c8cf3cd9120f6d03f1a149d289f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abaac4437986154d8bcf700316e739f8facc9cbec3cd1dce8f0637213e9ad077(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6c5ff5d832fba023f90747ee876ca17eb883c782ff1378246792fb2314eaab(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverrideinheritsettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3125abd9eb46fe7b9e39ebb7d290a0def8a863f2c80bb734c21fa791d6402a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c5304022ab6abd3b2de21449e2ecb40e0a193cbd937638ee1a032b021489932(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a01759c401c5f2bfe07bfcc809537462d190fc0c0a215437648fd9269535014(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ea66a31d47c81e89f609d7ce665a6e835cbbb531a34dbe1fca11d0440a632c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f77e348a676d5f11434d7f0454caa61d91f2ed4277be824f9b1c72b075e30307(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverrideinheritsettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f652a9d1789c1b52042b9015955773a25b8025d1d27671e84f26698b3a297fba(
    *,
    backupcontent: typing.Optional[builtins.str] = None,
    rpo: typing.Optional[builtins.str] = None,
    storagepool: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e0a2acca73eca6d960494904a26f8312dbd280361cdfca32f8afcdbb4b4897(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3b81bc31fc3bbd4e1d43e530ec46c03151581bfe4233ef58b62cd10166f3e0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1bfe40ebfe2dee7dff892d34d1ae1062d4d04fc98e28a733c7c5b6fd4517676(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5da47e67413a17d4cad9d273530ef0377a7f1f9914bb57a1f40c76f7896c630(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3b673d500d7290e6c5584325deb9ac39d26f203cde24d70b914d451faca1e2(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5a465f80c1b55aa732b8f3c3fcdfd05ce47c4833bff2035ce6bc56f19fa901(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerOverriderestrictions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0a0429dd8d4bbb5fef2ee071cec4fbad4c647f91aff06d09f91018431ab815f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3eb1eb884aeebf216c3a7b288f136c676bb2d64440d453a933276cfcf987ffd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d0c1487dc3a628ce1950192378c90d39ca8adc24e48d4cd9c361f377dc295cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d143a43230dd5ee8ed269cf3f9c8d283ba3f55ab66ea4d66a88138d54455990(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__518555a3322d910d88d139d4c23df3289e26ccd15f6d9d808855efb8d9ddab73(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerOverriderestrictions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae3e3288e82107f7d2c00b982611bc1979db134a6a97da862640e92a49a5383d(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6a7b56c08685a5155df8d76f556fa2c0e345cd33e785b790a806d2261775486(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4fd7a25b33c2afc2a74eef930113e4bfaa55ac4200b30e5d1dc7ad700a74a42(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be5ee074fefcb763f8117c586ada3981582ba6007b3da566f564f1446cf1ed5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a11d1e7154f666982529a486758c516347acb5eceeb61ee0e99430c0d2ae1cb1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__677500c0b7b6044e572bacec2ada747a88a6dd4ff52bd58b3ab2b0c0eb0a0d90(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938a7717e9d1d95a0b5e0dbe96e856df1712c2b80bd6795a4d09e2b6dd9c0d05(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerParentplan]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c84590aee3b9497be998e9d063cfdd0d2aba7ff570f823d0a7e0d38c66b5d1e7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4be75b3c06e01af3c444ff73c78905cbb90eacce760dc0b0d426584400ede0a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4a5602dc9357888a6e545739127b0177b9dac48789b7c8e4e7c17d67555006c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6e970c0caa2be585cd7d9c250ef226d06d663ad44a42470494127d1e892e2a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerParentplan]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22652de400f37797844af1262aa3d2662c5ecadc4a96a76f85f55d76c29ece90(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa546b00d34920a0bd68c6557d350143dd1855f1297de3f91fb173feef7cc8dd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac270dc0f7867ffbf77ea05db2c23ff27423c13526bb57a494ca27de852ae5b8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfe6fa96a59c50646cd2d3a62f060d9f6257facf328f3c398e628bbdc804f473(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c564c1c341e64ce3b6670bbeb242bbd3e9b923054aa9a9d1768ae32e0ab4d3ed(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b81d6b54d26815653000290ba678c366c9b1ea4cd079c01db8bb4bc9f156a9a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6614e725084ec52a8a7858ef9b65b0f6a2205d6e65b729bf118514ccbedd96(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRegiontoconfigure]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f01a1783a0fbea57f7dfca1995ccde78b19a1a95f2d6d6f843ea875ecae2de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f09b6a2ae06ac92642047a754ce662e8d13c6188b94acfb9c447603f84455cda(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a437ea5934478aa532b6ef1e60a4f94e1cf046ca701a205ec6e32317aa05b7b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3b1f33e8d2685fc423d44c1553093d476ae442ce7cc5bbcacfa86706704cad(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRegiontoconfigure]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d6d4c609bdc343d6ec4e650f8d31db95cafb260dfd69713d1890f49c02957d2(
    *,
    backupfrequency: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequency, typing.Dict[builtins.str, typing.Any]]]]] = None,
    backupwindow: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupwindow, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fullbackupwindow: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoFullbackupwindow, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sla: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoSla, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6772b97f61f9047b1d6b514027bba1a7502b7673cb9cdb2edde3c1e91b3dede(
    *,
    schedules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedules, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363eeb52ad3fdb939cb89f32af0cd2369c4a861ebe0e64c03ad2b158e21ef388(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13b322065e99d3dda0697617614ed6fdbc7b4e1cd3b1c967473c9733c064c965(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057ddb67514e54270e7b61bc44200c985336be7a570a12961f555d69c1cf9c81(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b1a3a79b06b8fa344ffefd2796265dca443511ef46cb2baed499cbc6108a32e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea7979b805c22f9c642de50838dee7ffcd9c7d61218e23f462b739d5c2e17df(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a352bbcea08e5e25e0cc5eb3efe5fa3179621f448ebbae97d765656edfc671f4(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequency]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da32781722328c96f5ae1463625ca6c0bd0b0b841aa87ec057b938cc06c795df(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__010e78892812e809b68fd1e8af66447dc903dcee25300eacaa179d24017c1a5e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ea9ed7f96291b02ef10f99b2ebfa17c06bc72d4a19f0ff250c90ef1712a57a3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequency]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be745b4802565b3ebbdcfb33311c92a076a5d9b0d25ed34456008f1c3a038b9e(
    *,
    backuptype: builtins.str,
    schedulename: builtins.str,
    schedulepattern: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepattern, typing.Dict[builtins.str, typing.Any]]]],
    fordatabasesonly: typing.Optional[builtins.str] = None,
    scheduleoption: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesScheduleoption, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vmoperationtype: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b46eaaf180684db5a4e21217ba214a723856717245249b9658edef71d4031995(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec8efd28dceda0ada18d33925f200ebd7d6828381cbaaa96f49685412302d427(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fbb2f83d21d99c4d0dde240b5ee9b986d4077c6cd204bae2731d7ecfa3b3dff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91586b36a89ea07a4ad38fed838fd7e4aed216bedc4551104d1687cbdf6283a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4478de508ee3cac794d6828fc23ee654c77683779056ef66a5428636142c200c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2ff61fb5e3a32bd8c5eafa20382d5767a650f06a86e2651e1be4fccaae89716(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__323644867b95356031a41fb48a91642613d6233884dafccc8251adea8b71c0ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85ebe4be18112c51cf0e8cc6a6b4ff9f50838f16206902240eb969f3d4bfb3a7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesScheduleoption, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a3e55067b9c930e8e3e046d044c730b2fc2ef0136573c4d109245f75de3833(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepattern, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7463a1b18016321d22e2c36e52ef833e56b2f63c322f37c7ec0876d6f48496fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ef6b91bb23d659197961cfcd352dc4b88da8a859a8a1c0384b368085642294(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa3395fdaa5951311fc9a8dba265a6dbb5d510aafbdadee894ba57fa2cdaad3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a04005604fad5431d5756f1a06d15e555530f57c453853d9b57c4ecb40153bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b84dc2856d9e79a8a07b06fe323684ad1ff275d89c3d17738b2dc4ec34f1eb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedules]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1849b507a629efc91d1b7f46bbaa9c5e14193781f94b0d12050e2a889a95276f(
    *,
    commitfrequencyinhours: typing.Optional[jsii.Number] = None,
    daysbetweenautoconvert: typing.Optional[jsii.Number] = None,
    jobrunningtimeinmins: typing.Optional[jsii.Number] = None,
    o365_itemselectionoption: typing.Optional[builtins.str] = None,
    usediskcacheforlogbackups: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ece895fdf4666bedafafc6ba27c78d040e4c4191112e91db38c23c9dddd313f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0438aee4c5954f8583bbfb5667e7741617d8b6fa909b4bf9f3bf43cf82bcc56c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8af34fedfd98f26a8065eafe10492b9d79ce2944051f93b6415d2474921bbf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ac289ffa00ddb275b1c3b3d3395dd6fdef7b756c1f10060a3511d5950f1ed0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4215e5f2e2b9b3e79148a3a65828e78bdaeaee0601f239ac2c608cf4081d400b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff8accecbbc22562bdf1f3d4ade2e5d273446da1ec989588c53cd800a6f67a3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesScheduleoption]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9761dd6cabe0b5b7da5771eed5dc8c2d40542c5c3478c5604f0e24caf6361d20(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a979c9cf1c0e78be5d17ba2b10c0d8debb2dd226514cdb70394bfab7b83bc26(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1661517d0d26aa06e7c59ef7d6895f164384d125b0deaf25900c58a87160ed50(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4978752b57b208168638c64da22c3b666845b3bdba3476999a1f2c4d3c2ed3fd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b04ea25e9b80a35893713ccec53eba325d1593fcfd721a890ba042bf6ec384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__527ae308f568899ae86675cb717ebc8576b5b04e323271e0cfa23e2bb24a516b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd94bb64455e824debc4f40fc385c52010fae4365d503bfa9aaff56ee71e158(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesScheduleoption]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00affcf6ccbe2b21ab290a4acc09b9c7f579f2f3139c340326e8d273b768f3e(
    *,
    schedulefrequencytype: builtins.str,
    dayofmonth: typing.Optional[jsii.Number] = None,
    dayofweek: typing.Optional[builtins.str] = None,
    daysbetweensyntheticfulls: typing.Optional[jsii.Number] = None,
    enddate: typing.Optional[jsii.Number] = None,
    exceptions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    frequency: typing.Optional[jsii.Number] = None,
    maxbackupintervalinmins: typing.Optional[jsii.Number] = None,
    monthofyear: typing.Optional[builtins.str] = None,
    nooftimes: typing.Optional[jsii.Number] = None,
    repeatintervalinminutes: typing.Optional[jsii.Number] = None,
    repeatuntiltime: typing.Optional[jsii.Number] = None,
    startdate: typing.Optional[jsii.Number] = None,
    starttime: typing.Optional[jsii.Number] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
    weeklydays: typing.Optional[typing.Sequence[builtins.str]] = None,
    weekofmonth: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70b6ce06c6bbcdb2a8c38a96588ae22c4c879d1c6533062754b16b96252c79de(
    *,
    ondates: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ondayoftheweek: typing.Optional[typing.Sequence[builtins.str]] = None,
    onweekofthemonth: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd6332fd3ff662753a3f45275e9d714a0ee70a2b3f9113b22834ab0faf22943(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d54ba8527f58966697d6cd1052cfaddffbe278eb067cc18cf7894966c56ffcf8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce3446fa077578ffed18325433362b9cab0ba1a1788738fc80c6f9eb0b7a2ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e615482023072b62752535070230529833ca6646d11b43e9a7668f2bff168d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__594911f99353bae4d3a250e6413b2c2f2569d6bd67074d083b8e76b0c40af7d3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21c091bffddc1d12426dc5c53ea8229a746fee722875684149b477cbf2280bae(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd7ee23843fb2b3170e34613950b99185b6eb52152a42ce4760c7d20a25471af(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78f90b3f4fb32eaa79d7f16f57c38f0abcb29461280ae657a3196cab41544e6f(
    value: typing.List[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52de1a755dda9a9b604cd8fe718ddf23bc2f6ceca13635a0e07ccc9a17ca64cb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b45b170d780eac7f0057b7a7d410eb0929e45812263cc73e76e4af72444f0c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a4bd2c55ecec212bfbce6abd0e247b859df1df774af603f67995672bced4edc(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0975894ababfd0d5e2987c897cfa07f7d936967cc1a324137ee3162c2aa4e306(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2e3101f4f665b96e0202ea31ab492e0f86d3308dbfdd1c37d4a071792a7c1f1(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db27d70615ab63821767cea6c761a68f848d288c7acfaaba2cc008062bb2c441(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f197c0f2b14572f8cfc4e2c67627973449bbbb2fff072bd9040c9d7a053bc5c3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345192bc17cc1ac285b1ceb9a097c6e9204a1b758246cad3082f6a19d202e366(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c37e1cfa6b2266c104c60205c22549afe3295d0cdc1686bcef6633d5de40e6ce(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepattern]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ed42ae07f1f0ca168b432ebc076f13e7148467b5c17cc17adf18dce2bbb538f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c203769816d161cd856bc0fe1453c7a95c69958e5641dc32394b421dd3c226cd(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepatternExceptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f49ad612f4d0fa3280c69ce36795cda842da394190e40f46de8883182e26d8d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51047dabaff2f19552a76cf95da11f2a9950b616544b88b5b152c5ca086febc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fac3a97187ec66855f54a3369f61b783e14288901fff7f63ab22f44ac11f999(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea722c6bc0b09e6c700e2a4926c24fa7904dc39ae9767b5d720d363475048863(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9368077fdbb24346f232048c521bf4b5d31d85d7d4d0f4db3f3cd8bcaabacaad(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__117e2421f9ca473b6dbf0c1f35e4a48e690c22aa6fbbc9b1e42fd5a591e2d721(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9d89a90d9df5bcac53d2ffe4a124c59c78c9c29fc3f96970cfe3497041c6263(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a47feb3ddf6dd8605b4e1dc6700dbd3848675bcb2bd7a1832dcc48c71331614e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4053c5df63474499d0879dfc839cea70585b7452987626f365d76e1dc9f67b5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__867358c82fb9c1c380fd3939f005e32c5e88277ab747a4a00758efc76ad0df68(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f61cc7e2eb1305d879253e5e9611aa4595f84c7ee5ecf8b259f5079b5e39e4d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdde73321b55fce4e1671acc1a919af0c060f8b86e54890ce6aeb78512c72f75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec21e9aea59f00e8813d87dfa279ac6bef82a8f82204f37796930d39259b7ab(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2767e32c30e756b88eb6aa863f161f9c616cf8383e96deffba6ceb499085b34d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__405b6fcb2d72a15f7bb823c6d0a226df7c2cafba24192a62d3801914ba3b218b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11c52ddc0563825b1b5d1e5d17d89f28f86b161422fe691f8af5ad61586739cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70658e45bfc88be4ed72d7ae250833def2103324e5eb6053ff8a66ac56afff3c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepattern]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a82268f27827023b120116002be20db9e26590fa897e757927aa6bf784d73e36(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd45d63f808c1917ce76dc5ea303d82c9abbad3dd7ea23a210139d34719d3a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5df74d9025569950f681e241ae37819fc3a68e904846e024e1d16f588a8c0082(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c61d69b6e0f1c1ea7ce8d64d18c56a0519da12ec14d68a390ec0ec3b7c05387a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d453573abd2f41699d30603201fc60b2d4b7a78f30c2db62f557d3559ac08f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c63196622d7f3be0ad3ea7db1a0db0e528aa5f18637e2135a55793e017b5669f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41416b9f657ff1fccfff998f25cb70cd0d4ec6af95b2ea73615cc7d7b2944bfb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3d20a09b38413180715ccb61a0c010fbc9ce10d89ccace5b9400a07f9633423(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fee06d211dbec0eb848fcdd9c810e06e192cd79e47cbe990247ab9af5885c04c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a3463c86e126255c971e097a7218f8fdaf790f38bb84a778ba73c769aabe9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4af8c9d3c64fa32018f7caf5833ad6b69d421f3dfddd378332f52a684edb24(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupfrequencySchedulesSchedulepatternTimezone]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b10ba9a3a98989d2804c1437a90463192b95f56a059b97d31d3be6970ed9feaf(
    *,
    dayofweek: typing.Optional[typing.Sequence[builtins.str]] = None,
    endtime: typing.Optional[jsii.Number] = None,
    starttime: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b068be2629ef9b89366d6928861168db9af080a0ba4194993f05becdee87e864(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6315ce5ffdaaeb4836876d1ae329d754fc0775ab987886e429da1a7a5805bae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2255b6714e042e3f025872da6d0d2d9ee4e015195138a650a0f05afd772aa124(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e70f4bc665aff5713c675a07d448a0a16e8e3b69d4aa5d126f40180140f49d5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa93457eba7fe3e14664aab5a19e1e33864b3e3f79b40dd8c47da329cff33ebb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b12b91a9b2ca4ed230830e353cdec1813b4bc2c1f69f90bda450f565ffd1a7(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoBackupwindow]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c7d2bacffe85428dd9f5da757b91708e039e164eb5f294b58b0280d88c55b8f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88140868b14794fee5c2d82122637a360887727eb0fbfba83b7b848e9b1303d2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aa6a80fec2b3280e9c08fbd6000265ee2588d934cd34effbc7153a97f258f04(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1617848d7080d2720063d3420d0dfd9d6e6ee5751b74530ad85268f3f8ff290a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__195e7f5ace0cf821be2ea72f35cd60ee892d4ad3851a7b602f4dc92ecb9722a8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoBackupwindow]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__947f16679dcce022072fa0057bc2d3b69c0a5fb520f204dec2ac4234264688ee(
    *,
    dayofweek: typing.Optional[typing.Sequence[builtins.str]] = None,
    endtime: typing.Optional[jsii.Number] = None,
    starttime: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e2e209c7a895bb37c341b16326adfa8f0642ce76305f7da75c013304c7ccd9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66393315dc880c52d0f21f79dc3d4c7d43db706441f346abc1fa81ec36c61b15(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__892dc85837ce85e0126fb829daf73bba92d01368c8725ea9728007a3ccd4e673(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19eca7dbc09bc1a0d2441b0566ed4a96c7b88e4bd9337166dad28b2fbb7059c0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc299a75f7fbb02eb56ebd44b77dc7bdde7cd02bb62b1495ad8091bfa22e681b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbdf36ea09a6efea0462d3766e8ebaa10f6bc4aabded7147ce9a8c9c43af9c61(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoFullbackupwindow]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b23f2d690606c0a56bb002f4f99b963b36ed366acc00212b6c7e3d1e52069e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1c5d4123cdaeacb4f2cd75a23915d4ae4f02d30c2afc728e425976a0fa3f5f5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3b8c5e9dd623ca352f82b6e70dd7e413be745e85ee7868cc063ae5416895d1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6b83d819add7abdc8b746e04d29806e81edcc246fc794b68ce1d52d6db4df1e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07efd830e7fb365b739c9c090d005850728da1200e84ed17c95b746439be0eea(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoFullbackupwindow]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0767ebff00b1a9fa80df815438054afc531c61cce967fd14cf3798537277ea5f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d84e44be040e7bab1e50db8ee336f41f4bb68c7683296622e90e3bd48254d72(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca90452f48c9d79db5e1ada3e1792468c98f63591198eaf20ab4a4d92cb70d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12f41dfbc3f473c1b92eb8049554132316237321b1da04aa7698a686b0089273(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c135e4defae0473751fb7f6178fb6dfc68002020978e7710b1f209b85ddf6cfd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8ae3b157c0c29aa2c70d1a725f1e9ccfcecd0471ad7cc3bb7dcad71a158496(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpo]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d97278e8d317acd510a12ad936ab908995f5ae72267789e4bcd4e1149ce3dee4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e5c8e5c5169f9a11a23e1b5bed07272e20ccb708cb43dad9883f69824d7aea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupfrequency, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ed482bd9fbe34003fef681fafe16a4bd25bd7a75a1ea658b2440dbee120c1d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoBackupwindow, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f214eab09349ea964e1b401d7cb8e88b3451770669f74f3924993e6a1daa5345(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoFullbackupwindow, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7745d911d18f757ccb4b2a6e8e0d4b02fe86098cf6c2d62e9fa50901ad8fffb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerRpoSla, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7264569cceb8c9175034c63dcc0b70a33b6e1b916f88d7b93d777ed339255f83(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpo]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccd4008cf3917732a2b3f96ef45d1b3c1b543cedaeef42c905c2343f4b1727e5(
    *,
    enableafterdelay: typing.Optional[jsii.Number] = None,
    excludefromsla: typing.Optional[builtins.str] = None,
    exclusionreason: typing.Optional[builtins.str] = None,
    slaperiod: typing.Optional[jsii.Number] = None,
    usesystemdefaultsla: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63eadcb283557b138870ea5f45129df1e9e65c1a2760f1e49337a48f59c49c19(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef6946c3e6b31d45a1dce97a4e56b4970e45b3a1a19102365220cd2b61a5281(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__708fc1585672f463cda06fe115bf1b6238ff206b3804f13c1cdb31cb1ca8e010(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121478278a6e8c602ace41b80a4ee8f27cc25829785d33c5285570d87857000a(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a3335b1fda1e2c10fc06d069100135b8e479969b8e0d9a554c4a22e7a0fa48(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6feb030d14b6d80e03f8e4be89f58f0985dc0a994091c5e8d75b8612a16f3076(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerRpoSla]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d04be0f657473c9b27d687e98a20f71e3f5b6237df4985f3033a9beeeaba5dda(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6049dcb45f3d46f45dca9f781cec870fb4caf5176aea9349b794c469021d52(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7d0de008cf0a21a6389ffcce19696697990b3fe11758367401ed7d9c3c27ab0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02cb2eefed630b7ad305fc446622144a1d065dd238c3f9c3806a5d0ac17aefb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4188de852f9ab8d92a5cfc8f0b11bc921ffad35becf41461ddc9f7ddebebb81c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496bf18af26cf00ae7fb5d0e1b719947967b69c89cc65cde908f4f8797e8d0de(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__364d3db73c58661206a5ad8251b691bb0fb829b1e77bd30d6f06bb789857235f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerRpoSla]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90b76f54bda83a206a3b8460eef501e015ab531f279207867cd1ede849109865(
    *,
    enableadvancedview: typing.Optional[builtins.str] = None,
    filesearch: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSettingsFilesearch, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1592e24c9b87be87bc53b440268afb43be47e3107ba7dbae057b5ea5e765854c(
    *,
    enabled: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    statusmessage: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5425a8da0be7830e8665e70ba3bd31bd9927dd870e37b90b1b2f5f2ba16ba4a1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5208a099492dc1d0a06174ba1ae16ebf2f73faa82396a7d67cb7f3432cdc9f2e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b91d5fee917d869ec2d39004f8758555554846bf674e55d03156aefb9af0fe1d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743a7e54001c0de0a9d9eb15de005cef6cdd9bf0094d53c95ed80109e7cd55d3(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83900bac25cd53c2dd35bf22fa02a4625937ac3862d428f6289268b271c30ba4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f841d7e2462b9372289a6d0898872b75c61841f251c8b8605fb9e6bf0c070cac(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettingsFilesearch]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49c9c26b06f43cfdc2ac6919676e160d4cf1ca5a72e657f1b0960f0d4e49036(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9128a7c362f5cd2011ed8c686c791d56212d746f7763fd8be82714a37ff64b34(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c662a24940fcff34a1657fb5184589c0876c4a89925ae53050462d6bd4590d7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__336562e13b028403ff0cda0039f864aeab0ad01a3cc12ab54aed4235bc4cb452(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59656435635bfe3e5637b272479c1d8729c42c3ff9039b91c1d742695996877b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettingsFilesearch]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0307986b3ddc34daa181bc69c90e73f714bb4be57007c8e7f3402e272a206c02(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76771d6bb3504a03b0ef0a7aea21bff8c5f6b5371c91f41fd06c59e7591cb8a7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c08129135e5ab1babbf5d9a95b55ce33152a34271cf2887fd1b87b7631a827be(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbf3569f68ec1ec040ea7d524135a55a2545a91faafd8acb1871baa9e16f260e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ec4f11004c3d1d55208fbe169344b2fd6300684ce59b5cbaf6cee08646ef63d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1de63713e90de7e962ca50ba491da49d7f49f32ca318928f78182db0d022d7e6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__189f00a3eccb7043828d910dd4cf8fa642364ae7ad0ca7dc0ab3e9e32e50530f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__180a8bb42547e15f7ef9b627befebbec235d5945acda82869c3f9e97951bafa4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerSettingsFilesearch, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__829be533b6266f01eeab355360afda22a4cd62fb303505de36ce7a4ba5018464(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d4045e1d77cce7ae39b5b21febf41aad36355e1f2b7d4791304c52ffd920622(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f42cd48963db11967fb727bf38ddc6931fe05e672012b68cadd79c3cd44b695(
    *,
    backupcopyrpomins: typing.Optional[jsii.Number] = None,
    enablebackupcopy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e75eee46c5c58387882c43fd9d62f5f234e0a49acfc755a337ce839b2b5d8e7a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__014e03066ca25adff2f5582dfad4cf37a85352fc469b747657e0a48c322bb378(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1ff795aba96f8744ce7ad6150a0320466b99dc3a38e5c7e4f6b9d134ad23c35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7b2c01c924354062524e16ccf7e7b7a06f3466bd3718b87c630c08be7830c8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b584ca9dbb1f70f5aaa50e8f26bf9c3af63216cdae9d738bd393c9cd247ae6c3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__febb60f7468595075d62dc1e2aa3e83afdcf383f19717303d569c67883105ac1(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerSnapshotoptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ab9101a2bf338523e9dd66d584d0e196ff0133025c5eea50547939f80a60ba(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c975cccfe64ea8c5f5babe260c543c5a1161064405aa090524c87af26facaf4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9791377d9ec776a1aee4759708c56fb9b83a2d9364e38e99a6e53edff3d3902(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0df0d9906f332b466ee1311985e5c84523dfe5012e54fc27b273f3b1ce75b01e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerSnapshotoptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae175010f8b0287fe2749f269a9611b8d4a5a72455c87a8e723ad7e021adfe3(
    *,
    solutions: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkloadSolutions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    workloadgrouptypes: typing.Optional[typing.Sequence[builtins.str]] = None,
    workloadtypes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkloadWorkloadtypes, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b4220445d205475b16d79571eecc7ee069fc855b0f1fc88d4b0b0dc75a9be4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77e096e1dd30422b42243c691cb448a52c8962ede25705cc3a835a24cd6c6000(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02378665c7ca488eba0cd5b7bffb3be27707fea3513af8de7ec4155c44fb8f63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53d46d16cb7d6de92635a0f1f94044f25ccdf1012bd8f148cc7f8d5c966a396(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72b1820e36d57c464af231d338e03bba8a05667770dbb50077d3ddcff28741a6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2dc163bc89978c856003d7831f612b02bc864784bf619152c88cbdd3ab4404e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkload]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27e61115779ae46ef9e4dd094e8c69f3ea55c219c00233174db3efbf349384f8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2841b0e0c85d1fec704fe801674c16040525f76eba80c4b846bd969efb43718a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkloadSolutions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d89fa7dae45f315582e178e4ce1e7b2304e1e035acbad9bc2f476d39e1703c61(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanServerWorkloadWorkloadtypes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24854de6fbfc6b3990fc9519c0da4268769bfcbf8bd8140dcd94f2616ba7b0d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69169f5eeda3f8d62a72eab06000942e09f0555ef6928657dcab9a503947baba(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkload]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2b2c172a29bf42c69f7f836a10dc05d9c094d4050de91acfda8d32898d8def4(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407770e36425e777b8ee566a306e1a7e5e6ad26befe9a70e8162963113a933ad(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0693ee229c4840bb7f63abdab9939ff7969c2cc1efba2a9001f5551fc9bc083c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7ef5651a61c67763e734c33def5bd3936d0569d1459083a9347b3cdc393db7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fd09c99f3e67d8844449e54ca825e1d17960ad9200c101763246f8396534560(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7565ca82674573268d0f4b04428af7777adbc5f08037a351410e65211911cbd7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eaa8f9f912e57b33814f73fc75ca83df8610b70cb0642374c0be959e420763e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadSolutions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea4d7a4579223de624ca18dd8f4c7b6355797ac91d9c78ac7f6586fb7eba45f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0984955ef4ee0091b8de7a4c5edf994bdb73c483be211046e9ec921ce460f452(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f2e4a6b467bfd20dd19b309f01d409b053e2c81ce9e6574a6e59697a673c99e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadSolutions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7796b2c3b9850932ff6975df45d8487cd2004b599f5430af5621cd9141e8efa(
    *,
    id: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585bffd908153657fa64f45852b4b51a143f95f954b8e410e3556573a15fa758(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a03473063f23426aa15efe19d128194706c5f9618137fa17c4fa60fe73ad925c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1586d6b7f4ee2cced2f305a01de2e5cfb775573adfa44a7773ae5c4516ec6c22(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4febea0943cc82d72785a85bc0edc6c7c16d3bcd5dd4dc981b7aeb8d89ec8d54(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cf00af18cb85ad3f60cf65abbfa48c8643bb6639a200af2c613b7efad62702a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb85492d50ba6383bd2bd8439bf55884df32823fde8ddc9b0c0fa5f2eb8c3db(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanServerWorkloadWorkloadtypes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3193a767cb3cc70a1b9be0591d35e0babc1bcaaf2e602c3a6f8dea5761af3d2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1224d890e277a63989cec58c301a53082b05b3544d07dcbc2d383aef2787d25c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c03e74ed8e34874a56d6154ae30da8d446f451430864bd21a03c116b03754b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanServerWorkloadWorkloadtypes]],
) -> None:
    """Type checking stubs"""
    pass
