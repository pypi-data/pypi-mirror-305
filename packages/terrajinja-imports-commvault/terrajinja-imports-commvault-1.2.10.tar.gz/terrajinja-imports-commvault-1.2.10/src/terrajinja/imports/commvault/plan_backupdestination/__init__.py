'''
# `commvault_plan_backupdestination`

Refer to the Terraform Registry for docs: [`commvault_plan_backupdestination`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination).
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


class PlanBackupdestination(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestination",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination commvault_plan_backupdestination}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        storagepool: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationStoragepool", typing.Dict[builtins.str, typing.Any]]]],
        backupstarttime: typing.Optional[jsii.Number] = None,
        backupstocopy: typing.Optional[builtins.str] = None,
        enabledataaging: typing.Optional[builtins.str] = None,
        extendedretentionrules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fullbackuptypestocopy: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ismirrorcopy: typing.Optional[builtins.str] = None,
        issnapcopy: typing.Optional[builtins.str] = None,
        mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        netappcloudtarget: typing.Optional[builtins.str] = None,
        optimizeforinstantclone: typing.Optional[builtins.str] = None,
        overrideretentionsettings: typing.Optional[builtins.str] = None,
        region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationRegion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        retentionruletype: typing.Optional[builtins.str] = None,
        snaprecoverypoints: typing.Optional[jsii.Number] = None,
        sourcecopy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationSourcecopy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        storagetype: typing.Optional[builtins.str] = None,
        useextendedretentionrules: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination commvault_plan_backupdestination} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param storagepool: storagepool block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#storagepool PlanBackupdestination#storagepool}
        :param backupstarttime: Backup start time in seconds. The time is provided in unix time format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#backupstarttime PlanBackupdestination#backupstarttime}
        :param backupstocopy: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#backupstocopy PlanBackupdestination#backupstocopy}
        :param enabledataaging: Tells if this copy has data aging enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#enabledataaging PlanBackupdestination#enabledataaging}
        :param extendedretentionrules: extendedretentionrules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#extendedretentionrules PlanBackupdestination#extendedretentionrules}
        :param fullbackuptypestocopy: Which type of backup type should be copied for the given backup destination when backup type is not all jobs. Default is LAST while adding new backup destination. [FIRST, LAST] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#fullbackuptypestocopy PlanBackupdestination#fullbackuptypestocopy}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ismirrorcopy: Is this a mirror copy? Only considered when isSnapCopy is true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#ismirrorcopy PlanBackupdestination#ismirrorcopy}
        :param issnapcopy: Is this a snap copy? If isMirrorCopy is not set, then default is Vault/Replica. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#issnapcopy PlanBackupdestination#issnapcopy}
        :param mappings: mappings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#mappings PlanBackupdestination#mappings}
        :param name: Name of backup destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}
        :param netappcloudtarget: Only for snap copy. Enabling this changes SVM Mapping to NetApp cloud targets only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#netappcloudtarget PlanBackupdestination#netappcloudtarget}
        :param optimizeforinstantclone: Flag to specify if primary storage is copy data management enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#optimizeforinstantclone PlanBackupdestination#optimizeforinstantclone}
        :param overrideretentionsettings: Tells if this copy should use storage pool retention period days or the retention defined for this copy. Set as true to use retention defined on this copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#overrideretentionsettings PlanBackupdestination#overrideretentionsettings}
        :param region: region block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#region PlanBackupdestination#region}
        :param retentionperioddays: Retention period in days. -1 can be specified for infinite retention. If this and snapRecoveryPoints both are not specified, this takes precedence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        :param retentionruletype: Which type of retention rule should be used for the given backup destination [RETENTION_PERIOD, SNAP_RECOVERY_POINTS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionruletype PlanBackupdestination#retentionruletype}
        :param snaprecoverypoints: Number of snap recovery points for snap copy for retention. Can be specified instead of retention period in Days for snap copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#snaprecoverypoints PlanBackupdestination#snaprecoverypoints}
        :param sourcecopy: sourcecopy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#sourcecopy PlanBackupdestination#sourcecopy}
        :param storagetype: [ALL, DISK, CLOUD, HYPERSCALE, TAPE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#storagetype PlanBackupdestination#storagetype}
        :param useextendedretentionrules: Use extended retention rules. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#useextendedretentionrules PlanBackupdestination#useextendedretentionrules}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afe9afc89a50b677d21bd6eb16161b18e0c0d440740fd0ed9aca7c7f6cbdc5a8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PlanBackupdestinationConfig(
            storagepool=storagepool,
            backupstarttime=backupstarttime,
            backupstocopy=backupstocopy,
            enabledataaging=enabledataaging,
            extendedretentionrules=extendedretentionrules,
            fullbackuptypestocopy=fullbackuptypestocopy,
            id=id,
            ismirrorcopy=ismirrorcopy,
            issnapcopy=issnapcopy,
            mappings=mappings,
            name=name,
            netappcloudtarget=netappcloudtarget,
            optimizeforinstantclone=optimizeforinstantclone,
            overrideretentionsettings=overrideretentionsettings,
            region=region,
            retentionperioddays=retentionperioddays,
            retentionruletype=retentionruletype,
            snaprecoverypoints=snaprecoverypoints,
            sourcecopy=sourcecopy,
            storagetype=storagetype,
            useextendedretentionrules=useextendedretentionrules,
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
        '''Generates CDKTF code for importing a PlanBackupdestination resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the PlanBackupdestination to import.
        :param import_from_id: The id of the existing PlanBackupdestination that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the PlanBackupdestination to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5cac8905fd1485b17c65726e4401d43dc62dc3136cdb60df184e2f676fa4b15)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putExtendedretentionrules")
    def put_extendedretentionrules(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrules", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da6726e44ad816469f1829d87cedc859cb7dae95846b1ee5d9f749d223d7774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtendedretentionrules", [value]))

    @jsii.member(jsii_name="putMappings")
    def put_mappings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1edf1dd826e5f547b33c41c2eb03b71fdd1db9623fe8c088024cb20ea7dd8091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMappings", [value]))

    @jsii.member(jsii_name="putRegion")
    def put_region(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationRegion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d2917c9848c038127e495695e18358a1ea04d84b35afc878bccc59f0a294c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegion", [value]))

    @jsii.member(jsii_name="putSourcecopy")
    def put_sourcecopy(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationSourcecopy", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9e658391caa819cf5b91ff2afde5f876034b2dd77fa2459edcab22e03845c8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourcecopy", [value]))

    @jsii.member(jsii_name="putStoragepool")
    def put_storagepool(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationStoragepool", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bddafe8bbad1303c00bcd451c7ac55cfa5d2c7560fb40962dc83bd72846dc0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStoragepool", [value]))

    @jsii.member(jsii_name="resetBackupstarttime")
    def reset_backupstarttime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupstarttime", []))

    @jsii.member(jsii_name="resetBackupstocopy")
    def reset_backupstocopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupstocopy", []))

    @jsii.member(jsii_name="resetEnabledataaging")
    def reset_enabledataaging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabledataaging", []))

    @jsii.member(jsii_name="resetExtendedretentionrules")
    def reset_extendedretentionrules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtendedretentionrules", []))

    @jsii.member(jsii_name="resetFullbackuptypestocopy")
    def reset_fullbackuptypestocopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullbackuptypestocopy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsmirrorcopy")
    def reset_ismirrorcopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsmirrorcopy", []))

    @jsii.member(jsii_name="resetIssnapcopy")
    def reset_issnapcopy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssnapcopy", []))

    @jsii.member(jsii_name="resetMappings")
    def reset_mappings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMappings", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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
    @jsii.member(jsii_name="extendedretentionrules")
    def extendedretentionrules(
        self,
    ) -> "PlanBackupdestinationExtendedretentionrulesList":
        return typing.cast("PlanBackupdestinationExtendedretentionrulesList", jsii.get(self, "extendedretentionrules"))

    @builtins.property
    @jsii.member(jsii_name="mappings")
    def mappings(self) -> "PlanBackupdestinationMappingsList":
        return typing.cast("PlanBackupdestinationMappingsList", jsii.get(self, "mappings"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> "PlanBackupdestinationRegionList":
        return typing.cast("PlanBackupdestinationRegionList", jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="sourcecopy")
    def sourcecopy(self) -> "PlanBackupdestinationSourcecopyList":
        return typing.cast("PlanBackupdestinationSourcecopyList", jsii.get(self, "sourcecopy"))

    @builtins.property
    @jsii.member(jsii_name="storagepool")
    def storagepool(self) -> "PlanBackupdestinationStoragepoolList":
        return typing.cast("PlanBackupdestinationStoragepoolList", jsii.get(self, "storagepool"))

    @builtins.property
    @jsii.member(jsii_name="backupstarttimeInput")
    def backupstarttime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupstarttimeInput"))

    @builtins.property
    @jsii.member(jsii_name="backupstocopyInput")
    def backupstocopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backupstocopyInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledataagingInput")
    def enabledataaging_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledataagingInput"))

    @builtins.property
    @jsii.member(jsii_name="extendedretentionrulesInput")
    def extendedretentionrules_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrules"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrules"]]], jsii.get(self, "extendedretentionrulesInput"))

    @builtins.property
    @jsii.member(jsii_name="fullbackuptypestocopyInput")
    def fullbackuptypestocopy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullbackuptypestocopyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappings"]]], jsii.get(self, "mappingsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationRegion"]]], jsii.get(self, "regionInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationSourcecopy"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationSourcecopy"]]], jsii.get(self, "sourcecopyInput"))

    @builtins.property
    @jsii.member(jsii_name="storagepoolInput")
    def storagepool_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationStoragepool"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationStoragepool"]]], jsii.get(self, "storagepoolInput"))

    @builtins.property
    @jsii.member(jsii_name="storagetypeInput")
    def storagetype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storagetypeInput"))

    @builtins.property
    @jsii.member(jsii_name="useextendedretentionrulesInput")
    def useextendedretentionrules_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "useextendedretentionrulesInput"))

    @builtins.property
    @jsii.member(jsii_name="backupstarttime")
    def backupstarttime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupstarttime"))

    @backupstarttime.setter
    def backupstarttime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__273d2102d7b98dcd60a322978b963e33552a78d039f3771dbd47e01a7bb14d12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupstarttime", value)

    @builtins.property
    @jsii.member(jsii_name="backupstocopy")
    def backupstocopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backupstocopy"))

    @backupstocopy.setter
    def backupstocopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4e950e9c69bc3651acff0d7f19d0cdb7114d0b5a8a5c66ba5691879287424f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupstocopy", value)

    @builtins.property
    @jsii.member(jsii_name="enabledataaging")
    def enabledataaging(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabledataaging"))

    @enabledataaging.setter
    def enabledataaging(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd4a1ec6ad054a3270c2fad2131b92cd1f5374a7a33f29bf4b710a3da26899b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabledataaging", value)

    @builtins.property
    @jsii.member(jsii_name="fullbackuptypestocopy")
    def fullbackuptypestocopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullbackuptypestocopy"))

    @fullbackuptypestocopy.setter
    def fullbackuptypestocopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcab93742a123a19bd20ab4576c15ca0f6ffc105df47be9e1ec3a9655f93d9ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullbackuptypestocopy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3439701104bc3d2d91e95349b40a908c244cfc1828a389941931de3c5f78731a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ismirrorcopy")
    def ismirrorcopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ismirrorcopy"))

    @ismirrorcopy.setter
    def ismirrorcopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea2e711afae1d85754eef1f352ca5f10b6617766199c5da3a5d6410c15e7546b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ismirrorcopy", value)

    @builtins.property
    @jsii.member(jsii_name="issnapcopy")
    def issnapcopy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issnapcopy"))

    @issnapcopy.setter
    def issnapcopy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__429617ede57a62a0f655e5641a2a34dd5fc1e172efafcf15cc3cef2f7582e7ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issnapcopy", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62d1161c804b7ef227d217a3b5ea1762a6779846ada41f69ad15728c561ba7c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="netappcloudtarget")
    def netappcloudtarget(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "netappcloudtarget"))

    @netappcloudtarget.setter
    def netappcloudtarget(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8974b972dc431a1960fb0e5c71f0e26aae3cfca8efd246512acd38d716143e82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "netappcloudtarget", value)

    @builtins.property
    @jsii.member(jsii_name="optimizeforinstantclone")
    def optimizeforinstantclone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "optimizeforinstantclone"))

    @optimizeforinstantclone.setter
    def optimizeforinstantclone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5507715a3b00a1c9dccc92388cc6ece343e839a4fa698557254d20a06679ede7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optimizeforinstantclone", value)

    @builtins.property
    @jsii.member(jsii_name="overrideretentionsettings")
    def overrideretentionsettings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideretentionsettings"))

    @overrideretentionsettings.setter
    def overrideretentionsettings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75e5600d4f64c11a38526014cc447cf2063f486a5f1486ada6d3ba0a47265fae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideretentionsettings", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ffdfecec6194b75a5ef9271af21523e33255d1cffbf480116bff299c7c7be1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="retentionruletype")
    def retentionruletype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "retentionruletype"))

    @retentionruletype.setter
    def retentionruletype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551cbdc7dd4c8bd9cbde21fa21d050b37b0323839918d0417865da5c147ee3c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionruletype", value)

    @builtins.property
    @jsii.member(jsii_name="snaprecoverypoints")
    def snaprecoverypoints(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "snaprecoverypoints"))

    @snaprecoverypoints.setter
    def snaprecoverypoints(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9035efd0e0d7467c643ba8ff3d756b78a271a59be6f3428dcc462ae38ab959c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snaprecoverypoints", value)

    @builtins.property
    @jsii.member(jsii_name="storagetype")
    def storagetype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storagetype"))

    @storagetype.setter
    def storagetype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5ddc4b2a02617c1bc4839f5aed478070cf771f5edfd11ef8cbc3cc0b01d966b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storagetype", value)

    @builtins.property
    @jsii.member(jsii_name="useextendedretentionrules")
    def useextendedretentionrules(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "useextendedretentionrules"))

    @useextendedretentionrules.setter
    def useextendedretentionrules(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d160dea90b969ff92391a9569deac06a89d655697e0337e4f92787dc2fd3c384)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useextendedretentionrules", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "storagepool": "storagepool",
        "backupstarttime": "backupstarttime",
        "backupstocopy": "backupstocopy",
        "enabledataaging": "enabledataaging",
        "extendedretentionrules": "extendedretentionrules",
        "fullbackuptypestocopy": "fullbackuptypestocopy",
        "id": "id",
        "ismirrorcopy": "ismirrorcopy",
        "issnapcopy": "issnapcopy",
        "mappings": "mappings",
        "name": "name",
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
class PlanBackupdestinationConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        storagepool: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationStoragepool", typing.Dict[builtins.str, typing.Any]]]],
        backupstarttime: typing.Optional[jsii.Number] = None,
        backupstocopy: typing.Optional[builtins.str] = None,
        enabledataaging: typing.Optional[builtins.str] = None,
        extendedretentionrules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrules", typing.Dict[builtins.str, typing.Any]]]]] = None,
        fullbackuptypestocopy: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        ismirrorcopy: typing.Optional[builtins.str] = None,
        issnapcopy: typing.Optional[builtins.str] = None,
        mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        netappcloudtarget: typing.Optional[builtins.str] = None,
        optimizeforinstantclone: typing.Optional[builtins.str] = None,
        overrideretentionsettings: typing.Optional[builtins.str] = None,
        region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationRegion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        retentionruletype: typing.Optional[builtins.str] = None,
        snaprecoverypoints: typing.Optional[jsii.Number] = None,
        sourcecopy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationSourcecopy", typing.Dict[builtins.str, typing.Any]]]]] = None,
        storagetype: typing.Optional[builtins.str] = None,
        useextendedretentionrules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param storagepool: storagepool block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#storagepool PlanBackupdestination#storagepool}
        :param backupstarttime: Backup start time in seconds. The time is provided in unix time format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#backupstarttime PlanBackupdestination#backupstarttime}
        :param backupstocopy: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#backupstocopy PlanBackupdestination#backupstocopy}
        :param enabledataaging: Tells if this copy has data aging enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#enabledataaging PlanBackupdestination#enabledataaging}
        :param extendedretentionrules: extendedretentionrules block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#extendedretentionrules PlanBackupdestination#extendedretentionrules}
        :param fullbackuptypestocopy: Which type of backup type should be copied for the given backup destination when backup type is not all jobs. Default is LAST while adding new backup destination. [FIRST, LAST] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#fullbackuptypestocopy PlanBackupdestination#fullbackuptypestocopy}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ismirrorcopy: Is this a mirror copy? Only considered when isSnapCopy is true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#ismirrorcopy PlanBackupdestination#ismirrorcopy}
        :param issnapcopy: Is this a snap copy? If isMirrorCopy is not set, then default is Vault/Replica. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#issnapcopy PlanBackupdestination#issnapcopy}
        :param mappings: mappings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#mappings PlanBackupdestination#mappings}
        :param name: Name of backup destination. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}
        :param netappcloudtarget: Only for snap copy. Enabling this changes SVM Mapping to NetApp cloud targets only. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#netappcloudtarget PlanBackupdestination#netappcloudtarget}
        :param optimizeforinstantclone: Flag to specify if primary storage is copy data management enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#optimizeforinstantclone PlanBackupdestination#optimizeforinstantclone}
        :param overrideretentionsettings: Tells if this copy should use storage pool retention period days or the retention defined for this copy. Set as true to use retention defined on this copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#overrideretentionsettings PlanBackupdestination#overrideretentionsettings}
        :param region: region block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#region PlanBackupdestination#region}
        :param retentionperioddays: Retention period in days. -1 can be specified for infinite retention. If this and snapRecoveryPoints both are not specified, this takes precedence. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        :param retentionruletype: Which type of retention rule should be used for the given backup destination [RETENTION_PERIOD, SNAP_RECOVERY_POINTS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionruletype PlanBackupdestination#retentionruletype}
        :param snaprecoverypoints: Number of snap recovery points for snap copy for retention. Can be specified instead of retention period in Days for snap copy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#snaprecoverypoints PlanBackupdestination#snaprecoverypoints}
        :param sourcecopy: sourcecopy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#sourcecopy PlanBackupdestination#sourcecopy}
        :param storagetype: [ALL, DISK, CLOUD, HYPERSCALE, TAPE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#storagetype PlanBackupdestination#storagetype}
        :param useextendedretentionrules: Use extended retention rules. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#useextendedretentionrules PlanBackupdestination#useextendedretentionrules}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__759ca3f594fe25b1fa13767693b603067e17393c98d863c9f43c36cbf0008d63)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument storagepool", value=storagepool, expected_type=type_hints["storagepool"])
            check_type(argname="argument backupstarttime", value=backupstarttime, expected_type=type_hints["backupstarttime"])
            check_type(argname="argument backupstocopy", value=backupstocopy, expected_type=type_hints["backupstocopy"])
            check_type(argname="argument enabledataaging", value=enabledataaging, expected_type=type_hints["enabledataaging"])
            check_type(argname="argument extendedretentionrules", value=extendedretentionrules, expected_type=type_hints["extendedretentionrules"])
            check_type(argname="argument fullbackuptypestocopy", value=fullbackuptypestocopy, expected_type=type_hints["fullbackuptypestocopy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ismirrorcopy", value=ismirrorcopy, expected_type=type_hints["ismirrorcopy"])
            check_type(argname="argument issnapcopy", value=issnapcopy, expected_type=type_hints["issnapcopy"])
            check_type(argname="argument mappings", value=mappings, expected_type=type_hints["mappings"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
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
        if backupstarttime is not None:
            self._values["backupstarttime"] = backupstarttime
        if backupstocopy is not None:
            self._values["backupstocopy"] = backupstocopy
        if enabledataaging is not None:
            self._values["enabledataaging"] = enabledataaging
        if extendedretentionrules is not None:
            self._values["extendedretentionrules"] = extendedretentionrules
        if fullbackuptypestocopy is not None:
            self._values["fullbackuptypestocopy"] = fullbackuptypestocopy
        if id is not None:
            self._values["id"] = id
        if ismirrorcopy is not None:
            self._values["ismirrorcopy"] = ismirrorcopy
        if issnapcopy is not None:
            self._values["issnapcopy"] = issnapcopy
        if mappings is not None:
            self._values["mappings"] = mappings
        if name is not None:
            self._values["name"] = name
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
    def storagepool(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationStoragepool"]]:
        '''storagepool block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#storagepool PlanBackupdestination#storagepool}
        '''
        result = self._values.get("storagepool")
        assert result is not None, "Required property 'storagepool' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationStoragepool"]], result)

    @builtins.property
    def backupstarttime(self) -> typing.Optional[jsii.Number]:
        '''Backup start time in seconds. The time is provided in unix time format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#backupstarttime PlanBackupdestination#backupstarttime}
        '''
        result = self._values.get("backupstarttime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backupstocopy(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#backupstocopy PlanBackupdestination#backupstocopy}
        '''
        result = self._values.get("backupstocopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabledataaging(self) -> typing.Optional[builtins.str]:
        '''Tells if this copy has data aging enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#enabledataaging PlanBackupdestination#enabledataaging}
        '''
        result = self._values.get("enabledataaging")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extendedretentionrules(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrules"]]]:
        '''extendedretentionrules block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#extendedretentionrules PlanBackupdestination#extendedretentionrules}
        '''
        result = self._values.get("extendedretentionrules")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrules"]]], result)

    @builtins.property
    def fullbackuptypestocopy(self) -> typing.Optional[builtins.str]:
        '''Which type of backup type should be copied for the given backup destination when backup type is not all jobs.

        Default is LAST while adding new backup destination. [FIRST, LAST]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#fullbackuptypestocopy PlanBackupdestination#fullbackuptypestocopy}
        '''
        result = self._values.get("fullbackuptypestocopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ismirrorcopy(self) -> typing.Optional[builtins.str]:
        '''Is this a mirror copy? Only considered when isSnapCopy is true.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#ismirrorcopy PlanBackupdestination#ismirrorcopy}
        '''
        result = self._values.get("ismirrorcopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issnapcopy(self) -> typing.Optional[builtins.str]:
        '''Is this a snap copy? If isMirrorCopy is not set, then default is Vault/Replica.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#issnapcopy PlanBackupdestination#issnapcopy}
        '''
        result = self._values.get("issnapcopy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def mappings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappings"]]]:
        '''mappings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#mappings PlanBackupdestination#mappings}
        '''
        result = self._values.get("mappings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappings"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of backup destination.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def netappcloudtarget(self) -> typing.Optional[builtins.str]:
        '''Only for snap copy. Enabling this changes SVM Mapping  to NetApp cloud targets only.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#netappcloudtarget PlanBackupdestination#netappcloudtarget}
        '''
        result = self._values.get("netappcloudtarget")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def optimizeforinstantclone(self) -> typing.Optional[builtins.str]:
        '''Flag to specify if primary storage is copy data management enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#optimizeforinstantclone PlanBackupdestination#optimizeforinstantclone}
        '''
        result = self._values.get("optimizeforinstantclone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def overrideretentionsettings(self) -> typing.Optional[builtins.str]:
        '''Tells if this copy should use storage pool retention period days or the retention defined for this copy.

        Set as true to use retention defined on this copy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#overrideretentionsettings PlanBackupdestination#overrideretentionsettings}
        '''
        result = self._values.get("overrideretentionsettings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationRegion"]]]:
        '''region block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#region PlanBackupdestination#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationRegion"]]], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''Retention period in days.

        -1 can be specified for infinite retention. If this and snapRecoveryPoints both are not specified, this takes  precedence.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def retentionruletype(self) -> typing.Optional[builtins.str]:
        '''Which type of retention rule should be used for the given backup destination [RETENTION_PERIOD, SNAP_RECOVERY_POINTS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionruletype PlanBackupdestination#retentionruletype}
        '''
        result = self._values.get("retentionruletype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def snaprecoverypoints(self) -> typing.Optional[jsii.Number]:
        '''Number of snap recovery points for snap copy for retention.

        Can be specified instead of retention period in Days for snap copy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#snaprecoverypoints PlanBackupdestination#snaprecoverypoints}
        '''
        result = self._values.get("snaprecoverypoints")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sourcecopy(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationSourcecopy"]]]:
        '''sourcecopy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#sourcecopy PlanBackupdestination#sourcecopy}
        '''
        result = self._values.get("sourcecopy")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationSourcecopy"]]], result)

    @builtins.property
    def storagetype(self) -> typing.Optional[builtins.str]:
        '''[ALL, DISK, CLOUD, HYPERSCALE, TAPE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#storagetype PlanBackupdestination#storagetype}
        '''
        result = self._values.get("storagetype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def useextendedretentionrules(self) -> typing.Optional[builtins.str]:
        '''Use extended retention rules.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#useextendedretentionrules PlanBackupdestination#useextendedretentionrules}
        '''
        result = self._values.get("useextendedretentionrules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrules",
    jsii_struct_bases=[],
    name_mapping={
        "firstextendedretentionrule": "firstextendedretentionrule",
        "secondextendedretentionrule": "secondextendedretentionrule",
        "thirdextendedretentionrule": "thirdextendedretentionrule",
    },
)
class PlanBackupdestinationExtendedretentionrules:
    def __init__(
        self,
        *,
        firstextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        secondextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]]] = None,
        thirdextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param firstextendedretentionrule: firstextendedretentionrule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#firstextendedretentionrule PlanBackupdestination#firstextendedretentionrule}
        :param secondextendedretentionrule: secondextendedretentionrule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#secondextendedretentionrule PlanBackupdestination#secondextendedretentionrule}
        :param thirdextendedretentionrule: thirdextendedretentionrule block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#thirdextendedretentionrule PlanBackupdestination#thirdextendedretentionrule}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cf1d11dc9b915468793146efa58d8c847edac3dec7e87d1ee39334d02611b23)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule"]]]:
        '''firstextendedretentionrule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#firstextendedretentionrule PlanBackupdestination#firstextendedretentionrule}
        '''
        result = self._values.get("firstextendedretentionrule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule"]]], result)

    @builtins.property
    def secondextendedretentionrule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule"]]]:
        '''secondextendedretentionrule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#secondextendedretentionrule PlanBackupdestination#secondextendedretentionrule}
        '''
        result = self._values.get("secondextendedretentionrule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule"]]], result)

    @builtins.property
    def thirdextendedretentionrule(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule"]]]:
        '''thirdextendedretentionrule block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#thirdextendedretentionrule PlanBackupdestination#thirdextendedretentionrule}
        '''
        result = self._values.get("thirdextendedretentionrule")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationExtendedretentionrules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule",
    jsii_struct_bases=[],
    name_mapping={
        "isinfiniteretention": "isinfiniteretention",
        "retentionperioddays": "retentionperioddays",
        "type": "type",
    },
)
class PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule:
    def __init__(
        self,
        *,
        isinfiniteretention: typing.Optional[builtins.str] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param isinfiniteretention: If this is set as true, no need to specify retentionPeriodDays. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#isinfiniteretention PlanBackupdestination#isinfiniteretention}
        :param retentionperioddays: If this is set, no need to specify isInfiniteRetention as false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        :param type: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#type PlanBackupdestination#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7deeaef569f6ab6ed9f9af54d4591d1391e00ee2b3bfcf7caec63b7d053cfdb6)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#isinfiniteretention PlanBackupdestination#isinfiniteretention}
        '''
        result = self._values.get("isinfiniteretention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''If this is set, no need to specify isInfiniteRetention as false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#type PlanBackupdestination#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8d68ce0543409be10600bd6ce721b19271b182b34f25a66b419f9f388694d00)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__537e71e278825e8bb3fba830e22f700fe5ee92f7daad3c3c7d7ffb3c7ba8f0b0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435b60a04d69d51882478c8af316b7946f8ad8ac14ab146017f1e4d4aaa1287d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7e705ccb621bceb1ec40944b5ee0304f213a41a46964d9e0ee1599f74049e01e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97db0bc65e986f86cb95516a43cc02ebcfb73c1e8b93f47e897e0bd1a56b260c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba3c4fda4e17accad08393c10ed3f3e5f140f62265f7ec111888d217fb942777)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f41f131f8472f355a7171113fbae340a41fdf5d44ded20ebb8b28341d2e25c69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__624753575cebe0c1757ab35e0d7c76fb5958c4ac56257d06a9fcee6361f4250f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isinfiniteretention", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56728a38a5342dc0df99612495bc44d7b8d0364538b9d285b7ff616af7df7056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__247e62cec15dc3c23c9b6e66f79d1c2d6b7e706a11b305a6e3f473b1bbb9ff1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__318d849f17f4c6de68d9649c9d104fdabb6fb7c90490e6f98c7dd019870678c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationExtendedretentionrulesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__41cf2ebc87aab8fea051d1390d9d6c8cd4d360e5340c4a274f3061282493479e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationExtendedretentionrulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb4adf419d30240db461ff628588666cdde9eff75266f53d1f7cbfd2bc96b7d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationExtendedretentionrulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0005214713661ef33e86412bcdb3dd45861527ebaff97393d3ae2abcc7041618)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1885eaf163d2db8c8c48ebec806313c13063900be74a129d8a924e5b0e8a6eb5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77bcf8b0e83e8073394b146d3cb3f648666e4fbdc8c8a823f301a0c6670974cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrules]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec5cc5cf9c28989605931d8ce17bbbc6c3871ee163c3c808ebe3a38ed85ba2b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationExtendedretentionrulesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__93609181fcc46a045be938645746ee716c6ee450c093d1ffabe8067726a7bf69)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putFirstextendedretentionrule")
    def put_firstextendedretentionrule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5de32bd0c12bfeb8a684b6bab8a24e17d9105cf53cc5ee124573a499f3c08847)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFirstextendedretentionrule", [value]))

    @jsii.member(jsii_name="putSecondextendedretentionrule")
    def put_secondextendedretentionrule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33e5a9e2479f3bb88282fe2289c8d2d811470ad7c89b4cf6d0531289eea87ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecondextendedretentionrule", [value]))

    @jsii.member(jsii_name="putThirdextendedretentionrule")
    def put_thirdextendedretentionrule(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac9fc0503d99fa733784ebab70af4d98f9e3844115960a01ae6fc6341cb92925)
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
    ) -> PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleList:
        return typing.cast(PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleList, jsii.get(self, "firstextendedretentionrule"))

    @builtins.property
    @jsii.member(jsii_name="secondextendedretentionrule")
    def secondextendedretentionrule(
        self,
    ) -> "PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleList":
        return typing.cast("PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleList", jsii.get(self, "secondextendedretentionrule"))

    @builtins.property
    @jsii.member(jsii_name="thirdextendedretentionrule")
    def thirdextendedretentionrule(
        self,
    ) -> "PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleList":
        return typing.cast("PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleList", jsii.get(self, "thirdextendedretentionrule"))

    @builtins.property
    @jsii.member(jsii_name="firstextendedretentionruleInput")
    def firstextendedretentionrule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]], jsii.get(self, "firstextendedretentionruleInput"))

    @builtins.property
    @jsii.member(jsii_name="secondextendedretentionruleInput")
    def secondextendedretentionrule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule"]]], jsii.get(self, "secondextendedretentionruleInput"))

    @builtins.property
    @jsii.member(jsii_name="thirdextendedretentionruleInput")
    def thirdextendedretentionrule_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule"]]], jsii.get(self, "thirdextendedretentionruleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrules]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrules]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrules]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4caf87273b71ee08fcf4bb0396cebdbc46221fd3e34e65afee70aea582b8b2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule",
    jsii_struct_bases=[],
    name_mapping={
        "isinfiniteretention": "isinfiniteretention",
        "retentionperioddays": "retentionperioddays",
        "type": "type",
    },
)
class PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule:
    def __init__(
        self,
        *,
        isinfiniteretention: typing.Optional[builtins.str] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param isinfiniteretention: If this is set as true, no need to specify retentionPeriodDays. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#isinfiniteretention PlanBackupdestination#isinfiniteretention}
        :param retentionperioddays: If this is set, no need to specify isInfiniteRetention as false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        :param type: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#type PlanBackupdestination#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a2a7296928bdb4803bc66c704d9101ebfe57f3d49188989ae694fd89a1dd355)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#isinfiniteretention PlanBackupdestination#isinfiniteretention}
        '''
        result = self._values.get("isinfiniteretention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''If this is set, no need to specify isInfiniteRetention as false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#type PlanBackupdestination#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__437361456ae9118e0e805b01c8ebb95bc89972e548f3e019c05ce18cd08e1917)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae3a69ce40d9d22e7d8fa7cb0ff06acd44bd51f29db6ed846022a3bc4f2c0f6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0908f48f9614ec7d230bbcd762a032388839ad137ee2469cad8757eca5b50db)
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
            type_hints = typing.get_type_hints(_typecheckingstub__57245266060482e7c191ab14471d8442b29a1666f52a7d65abafde25b59ffdda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb47da0450d77ad5b5e6c2a11908081abb7192932edfcd5d3ea933a531258a30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ffbefb60fcdb8bfe26e301e8de061bfd5787f888c8a0d1be36ed6cff05dd528)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1a34af8df9b3dedf682e5d283c98b65919f3613303d2b0c4cd0dfbe60487891)
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
            type_hints = typing.get_type_hints(_typecheckingstub__167d01d713e52c5f1e34d2637de5201d4f5b0cf92b44a52088552f594d96c678)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isinfiniteretention", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e0e6fa1c38895eeb67bb5b4e3d42cd874940df2e5d036b16ea48065b6d7cccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61b76a8d5678d4041412af42975cf90c083234afe45118bf71314295017135bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931a30c3a715b81655524db87b2a7fe59ec7c70b8e7e46b12e2d4effdede919d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule",
    jsii_struct_bases=[],
    name_mapping={
        "isinfiniteretention": "isinfiniteretention",
        "retentionperioddays": "retentionperioddays",
        "type": "type",
    },
)
class PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule:
    def __init__(
        self,
        *,
        isinfiniteretention: typing.Optional[builtins.str] = None,
        retentionperioddays: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param isinfiniteretention: If this is set as true, no need to specify retentionPeriodDays. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#isinfiniteretention PlanBackupdestination#isinfiniteretention}
        :param retentionperioddays: If this is set, no need to specify isInfiniteRetention as false. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        :param type: All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only. [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#type PlanBackupdestination#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dc71c68690963151149b51e696e15ee3cfd296650e48a4b32a93cc5872d8d86)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#isinfiniteretention PlanBackupdestination#isinfiniteretention}
        '''
        result = self._values.get("isinfiniteretention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retentionperioddays(self) -> typing.Optional[jsii.Number]:
        '''If this is set, no need to specify isInfiniteRetention as false.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#retentionperioddays PlanBackupdestination#retentionperioddays}
        '''
        result = self._values.get("retentionperioddays")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''All_JOBS means SYNCHRONOUS copy type, others are applicable for SELECTIVE copy Type only.

        [All_JOBS, ALL_FULLS, HOURLY_FULLS, DAILY_FULLS, WEEKLY_FULLS, MONTHLY_FULLS, QUARTERLY_FULLS, HALF_YEARLY_FULLS, YEARLY_FULLS, ADVANCED]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#type PlanBackupdestination#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2c327a57c52a3a3815d253cc5324ba4966fcd0fb0d7e48a084a51af3da80e83)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4960c3665373e343fe96ace4a37e281a30a0165fbd0174f629c4729262764d19)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09651842093cb6d6e011621bf6bd9f771244a8f334e5a990450f8ffa53216321)
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
            type_hints = typing.get_type_hints(_typecheckingstub__998e3eb4826db3aa28a84183585c5814fc283582b530bc51b8cc03a33a9bf3ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b88a7bbc9db9f821a568189e979a442714c00b903b38771ec9e263749c6deaa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54b815b1b71789c11c3d9ffc0d6888e417faf4323a49179020edbd54249ac6a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d25ec892b150ac7a82bf1051f7bcdd9db06ebd0f54c3ebd204cce9647e614490)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7348f60caf4b6027c4b651180cb5742c1b79d1839d6f4f8f4de6164f3bfb83b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isinfiniteretention", value)

    @builtins.property
    @jsii.member(jsii_name="retentionperioddays")
    def retentionperioddays(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionperioddays"))

    @retentionperioddays.setter
    def retentionperioddays(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534436972bdd9fb615cbb50efff60a89db77060c4467b9dce0b67abe7ea1e1eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionperioddays", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89cea937898ae83975e631867a9d5b15593b1171558e2855c21d4616bdd182fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75e0a82e1b3b39a8a0a79250e681ac34fcf2895e479f86aabf58ac83eda9f0f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappings",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "sourcevendor": "sourcevendor",
        "target": "target",
        "targetvendor": "targetvendor",
        "vendor": "vendor",
    },
)
class PlanBackupdestinationMappings:
    def __init__(
        self,
        *,
        source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsSource", typing.Dict[builtins.str, typing.Any]]]]] = None,
        sourcevendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsSourcevendor", typing.Dict[builtins.str, typing.Any]]]]] = None,
        target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsTarget", typing.Dict[builtins.str, typing.Any]]]]] = None,
        targetvendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsTargetvendor", typing.Dict[builtins.str, typing.Any]]]]] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: source block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#source PlanBackupdestination#source}
        :param sourcevendor: sourcevendor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#sourcevendor PlanBackupdestination#sourcevendor}
        :param target: target block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#target PlanBackupdestination#target}
        :param targetvendor: targetvendor block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#targetvendor PlanBackupdestination#targetvendor}
        :param vendor: Snapshot vendors available for Snap Copy mappings [NETAPP, AMAZON, PURE]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#vendor PlanBackupdestination#vendor}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7909ff14527e08bc928ddf0e49f6d8cdda2f37114c5fa710e31941e0cd67aefd)
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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSource"]]]:
        '''source block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#source PlanBackupdestination#source}
        '''
        result = self._values.get("source")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSource"]]], result)

    @builtins.property
    def sourcevendor(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSourcevendor"]]]:
        '''sourcevendor block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#sourcevendor PlanBackupdestination#sourcevendor}
        '''
        result = self._values.get("sourcevendor")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSourcevendor"]]], result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTarget"]]]:
        '''target block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#target PlanBackupdestination#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTarget"]]], result)

    @builtins.property
    def targetvendor(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTargetvendor"]]]:
        '''targetvendor block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#targetvendor PlanBackupdestination#targetvendor}
        '''
        result = self._values.get("targetvendor")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTargetvendor"]]], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''Snapshot vendors available for Snap Copy mappings [NETAPP, AMAZON, PURE].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#vendor PlanBackupdestination#vendor}
        '''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationMappings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationMappingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__45e92a209e0324b3bec820f9352f1f7ac5a7d6ab687fb7a652e1177a470a2e06)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanBackupdestinationMappingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709f297d14373ebdcd6225cca98390f0c07c8941287f533bfb7ffe3c1a8290f8)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationMappingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e76c48345526856c1c3983780b845f994156a5e85c4c4839a08b339189cfed3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fedfad6d4b981cef00985a1310c32699ecd79c5673880125aead8b38e1af788e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9e9b618c53953b5f27b9e698eaf3b04ff6abaec3ded42f07e8dbb16b4a2b4f48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc8df61627d76e56c072e1bfffd60f30527d1b47d28e31bd04ed1c7a94af93c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationMappingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e36c6d60edfeb4d1cd9439972525dce503a43429b78086b145d6b699ad1f0da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putSource")
    def put_source(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsSource", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0f93d1ae4c0cad3eaf2630f5b876dc306df2f0853364af41d8af8ab04b48087)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSource", [value]))

    @jsii.member(jsii_name="putSourcevendor")
    def put_sourcevendor(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsSourcevendor", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a16269d750f263a3dc5a0cb53cd0a06d1e62a3727e753098d6ddb1ada066d524)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourcevendor", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsTarget", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45eda72686840da1defc2a79b8ec233550ee95cb1767dfad08148b280f9c51c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTarget", [value]))

    @jsii.member(jsii_name="putTargetvendor")
    def put_targetvendor(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["PlanBackupdestinationMappingsTargetvendor", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__268171d1f9577326b705fc67d58a07aa4f38fb77167c47b7da2832a1ae41a991)
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
    def source(self) -> "PlanBackupdestinationMappingsSourceList":
        return typing.cast("PlanBackupdestinationMappingsSourceList", jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="sourcevendor")
    def sourcevendor(self) -> "PlanBackupdestinationMappingsSourcevendorList":
        return typing.cast("PlanBackupdestinationMappingsSourcevendorList", jsii.get(self, "sourcevendor"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> "PlanBackupdestinationMappingsTargetList":
        return typing.cast("PlanBackupdestinationMappingsTargetList", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="targetvendor")
    def targetvendor(self) -> "PlanBackupdestinationMappingsTargetvendorList":
        return typing.cast("PlanBackupdestinationMappingsTargetvendorList", jsii.get(self, "targetvendor"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSource"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSource"]]], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcevendorInput")
    def sourcevendor_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSourcevendor"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsSourcevendor"]]], jsii.get(self, "sourcevendorInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTarget"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTarget"]]], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="targetvendorInput")
    def targetvendor_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTargetvendor"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["PlanBackupdestinationMappingsTargetvendor"]]], jsii.get(self, "targetvendorInput"))

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
            type_hints = typing.get_type_hints(_typecheckingstub__6e85537e80d944f7ec67251d728eb9a985da156725650d3a1353a7ea3af0d8df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9db6bc3e452691b4d023926955b4163bd8a580b1b572208862a0436d0171d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsSource",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationMappingsSource:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05ccae52ad5f061dc8963f35a7843e7650418a94edd450ea06577e0baa0104e3)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationMappingsSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationMappingsSourceList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsSourceList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f43d492633947506aa4450ab050cfb57c262dbd2bb6799eb4eb962b00888e126)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationMappingsSourceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de3c64eb445f4117803e8ac457c8bc3bd7c8a71de90c9065df1fb44350786b42)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationMappingsSourceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93166004eb7c94c73ed0e2f5d8bafd719ff4cb6b19f3b0a44a9ffa960a6025b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ced1026aabad55d060436113a56a6f61ef0d85a71cab0ae62b78ad950bc2e7d9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1e81f816f065a7f1a86743b59f6bf904544e41fb290b9d5b19aa4636453fc9cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSource]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSource]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSource]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb766415e463e62e21725b92eef929e95faf8dcfa8cd6869dd4b74208f28dce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationMappingsSourceOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsSourceOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d432bf8c8d8646ae6c26d41aa123fb87335645300b17533209a06aad1c11025)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1330f93d6dd6c619e427738ae51d3f2b8cf683b9e8d85081fc811f36b821faa7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a059f8b9e515a2cc336ed5d2437875d1299bffe03600fd8052dc5b25f02351b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSource]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSource]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSource]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9678234503be0ab467c8a411455994db9fc832ec7f8d2b51ea01fe8e1e60faf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsSourcevendor",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationMappingsSourcevendor:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb67a0f4f14686b4dba2267125c6ebe8dc1812c9df19097f053343605b55bf2)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationMappingsSourcevendor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationMappingsSourcevendorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsSourcevendorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cf7aee2118f6b53fb9199f27f7710f50d0388d265afae839059d86b360e8ce8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationMappingsSourcevendorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__facda5db15f5e656df8495c6f51b385c0d007e9386ff9c5163757c2dbd058088)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationMappingsSourcevendorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa51c2c652d8b97f9e021039ffd8a12299af5ed0a6ba458d012dc05adeedb489)
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
            type_hints = typing.get_type_hints(_typecheckingstub__531839bed798ca5c585c85382621fa43eff851577fb8044692b888f6603cc20e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d03986fcdcfc9bb01c80f70a57bcb10a481469d66d4d2b8a1ffa85d6ec92b8e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSourcevendor]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSourcevendor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSourcevendor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20de747d0aa30648227bedd8c191228bd858272ae272edb75c702c96d772a22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationMappingsSourcevendorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsSourcevendorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__679296ddad5659c6e074228c3999a879ec7743e336c7dd6a68f63e60e530dc09)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8679ebcc1d822ce93c98898df48f0536751a37dc3ea5a14588fcb92b4c002ecc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b183633c14e5778f783a4f1a3f929ee10997141b30df7a5f642e03096e290ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSourcevendor]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSourcevendor]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSourcevendor]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66fc89d34f27f1888512b77be198e42047a9a666baa62122f5dfbde6bd449572)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsTarget",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationMappingsTarget:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766d045b03c7082a4c53d8de903f0983a61cd1443d43dd10affce4b85d71c102)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationMappingsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationMappingsTargetList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsTargetList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8be7a03ea4d9a543be90d6624359bcf037416f2b89fd5281720ade8c68e84c5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationMappingsTargetOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acdcf39c388dbfb15b6bfc5e808a5852d11c9e737d4df1594996b530e2f6cd71)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationMappingsTargetOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d14a9abefdb5ac35224bf2cdd1f572258d358855df30312a5a6fd5ca2225c03)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fb01886bd478f45341cc4511d602adbcc382054fa159dffd5b9ec439e2011e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e6297f3f1dff71627f318edbc5a85968cdee8df78a939f2fc539554e7ee0c0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTarget]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTarget]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTarget]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c803e0e46254d89c37e115dc92453315668c0a19ecefd36f45c5c0eff6a54c44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationMappingsTargetOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsTargetOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__968f41dac465a3e5b7f65f94b4de5365529862f166b7da448d802ea0cc3decf2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e5f3b457040a05a94406b04d5c7533957813a2644e0dd0fba1a0f25b42dc6201)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450a2ac9b0e1f2724126e26d312ebf4d2bd143fface5081629b9efa08adfe663)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTarget]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTarget]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTarget]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5801a19f72c9cc58d0568c7de0a9bfb5272cb44eac617b9d9f01bd394e8ea98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsTargetvendor",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationMappingsTargetvendor:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d869f85225ae025e94d7d1747adb90a6a1da2784dfe80251395693bb9081399b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationMappingsTargetvendor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationMappingsTargetvendorList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsTargetvendorList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0ddd34342edb193dff5579565b2bb4e05a9b28114603e27b8dfb17bb2e00a353)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationMappingsTargetvendorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ffdfc96b970186bc7374f677b7e84ed592974c12a0ea763cfccb90d68d931faa)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationMappingsTargetvendorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__098169b924de444afe228f9c19d6b54e3751b2005976af8724132e799430a0d1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__edf5c008a4aa50d16d1bb1d514c87d8695efd39630bb80bf7ce1e59271a81b38)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8f8c31b91e5a6dd3bca5cce9c5b918e10500cad33db476aa25b1c8a69a81585b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTargetvendor]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTargetvendor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTargetvendor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d92a3ff19930646543523a426dae5e9a2021345b3d7acf48933f85075b315648)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationMappingsTargetvendorOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationMappingsTargetvendorOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d6864c02612242333fc0c14d8a5f88ac392c0f01e9726468227eb187e8dc5955)
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
            type_hints = typing.get_type_hints(_typecheckingstub__027d744b670904c7b79fe6374e7f9d386bf6a6ef470e913b5e3d60227017962c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__773c776925b15775bf387a2293760dd7b8c6d33c34c902892d0ad725facae369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTargetvendor]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTargetvendor]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTargetvendor]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45392576926d7a0cf282606b5979320061eaa00445cc5f87de04c07c85e8519d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationRegion",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationRegion:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__128722c24a1054f6e09c2a032fb42deae7e18db1d07676a77484ebb715331afd)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationRegionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationRegionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e13c35b4102e4ad60d530dffdf5a3210ae5af8c661e25cb1c51272460aa4fbc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PlanBackupdestinationRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3187411cdd91d572327c0b755cba4afc92cfb5f83ef3aef9d68c61ddbc8ef0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationRegionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79806aaaf0ff0ebcce2bc06540b11d4671183e91b3b6f6fad5e53ba9726bd487)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dbad8321c600e895dd4b9e56b68fb9e4f47599e7633c5de92c8bfff68ce31bef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__257e1c1676e9524453f76dfa909cbb400abb73632fc267a4a59d4bcffbf9c7fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationRegion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationRegion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b62939294570763de65dc29f6c827656be22dd25075f6f85d075d1d07d21ae5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationRegionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationRegionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffae901dbd1c94bee5a9cd7f536e8bcf2f614393ce468e69271800d19d085c22)
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
            type_hints = typing.get_type_hints(_typecheckingstub__eb3fb3a665209d49cbf50881cda14023b28a2923fd5d9fbc01c8bb6df8167d37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__399b5401d472bb4a0f861097dcd86f3843059530bc0132fe8eee852bc01053c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationRegion]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationRegion]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationRegion]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22dd9b6ebbb2e006de9483f0d5e2ddde3a6fd4255b87a70d062f9bc642bdec81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationSourcecopy",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationSourcecopy:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__502edb42094d4a4805c3e25519fddbd48f80bca612eb62c4ac9a9e5d29dbcef7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationSourcecopy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationSourcecopyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationSourcecopyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f218eedf06bb3c3cd2b78787ef32a9f75abee9ea8fd6b800e11ce7c0ed49bef)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationSourcecopyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c22928d9fb60d17c20867a27bbdaca08e680fccf99d7e44602da02722712f87)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationSourcecopyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2539ac794204bc21240333d5f9dc92577fa289c6fd4a8bac7af71152f289697d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__41b59b16a4f01752120aefd17488589ffbe5de5aad72756bc061d2a14e59eeb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48e2a54e19b59c076a59385b19e8be22c0c647e213701d78731c37edd204b9aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationSourcecopy]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationSourcecopy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationSourcecopy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01bc79eac9258bb2d7e6f6b3c9d1cbc36edb4980d940be189c4b2b8961bf022b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationSourcecopyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationSourcecopyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6edd522d5b5c7906b7883e760a55a6b906db76971c3de0a95d25f6276cbe931)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96fe013c563d981b4e36f53e7f3f13af7f6748fb6ffbcacec35c3b658c675696)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3558b7806ff056c8ff28a5dd779ea6c30f4c7ac603b35263d93fa4f88e49afe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationSourcecopy]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationSourcecopy]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationSourcecopy]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f0006ea19311462bc9b4d3aa28c7c0554ed5cb01953b16395628a6deb409135)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationStoragepool",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class PlanBackupdestinationStoragepool:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__436f9b9eb6cc38545830ef09384fed655dc45dca1fa7272d15d84f19bcb235e7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#id PlanBackupdestination#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/plan_backupdestination#name PlanBackupdestination#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanBackupdestinationStoragepool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PlanBackupdestinationStoragepoolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationStoragepoolList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5e883943503292661ea84f1a4e2ecbf6c3e6f4a7729960a7f0e1959b63f047fa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PlanBackupdestinationStoragepoolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__499f2e594bd690c711bf3d7973e079f0d91975855d5816c7f74f6746e2b14d6a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PlanBackupdestinationStoragepoolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ef16b907ae627053d1a229a6589b0707d2c72c20bafb6c1aef9c983bd06deed)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd8d149ae47350983d161017e2fc81fa9e6138e672d67a0ed5b1de4ba0eb317d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e467a07f355416a33f534b87ad209ef2a5d41532e859f1f9fc6c9d548bcb985c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationStoragepool]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationStoragepool]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationStoragepool]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63f204819d57a2d7ffdcea687ced3736e7b9a76ca380b7e2f54bbffc106e637f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PlanBackupdestinationStoragepoolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.planBackupdestination.PlanBackupdestinationStoragepoolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__830afb6121d2eb7b2a13c12195e20cd7fa6e519029335b3c48b9b2ccfef574f3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c566987ec535ea5157a714b416257e549aa998dc1ccdf4460934ea4eec27c82a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22fd9de459ca9bf2d79b5a2e34c7fc6915828c55f31f8f6935b5122cad7be076)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationStoragepool]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationStoragepool]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationStoragepool]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b288265124f89def8b0836fa306303aa4d0d49ce7390753507c702666344470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PlanBackupdestination",
    "PlanBackupdestinationConfig",
    "PlanBackupdestinationExtendedretentionrules",
    "PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule",
    "PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleList",
    "PlanBackupdestinationExtendedretentionrulesFirstextendedretentionruleOutputReference",
    "PlanBackupdestinationExtendedretentionrulesList",
    "PlanBackupdestinationExtendedretentionrulesOutputReference",
    "PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule",
    "PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleList",
    "PlanBackupdestinationExtendedretentionrulesSecondextendedretentionruleOutputReference",
    "PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule",
    "PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleList",
    "PlanBackupdestinationExtendedretentionrulesThirdextendedretentionruleOutputReference",
    "PlanBackupdestinationMappings",
    "PlanBackupdestinationMappingsList",
    "PlanBackupdestinationMappingsOutputReference",
    "PlanBackupdestinationMappingsSource",
    "PlanBackupdestinationMappingsSourceList",
    "PlanBackupdestinationMappingsSourceOutputReference",
    "PlanBackupdestinationMappingsSourcevendor",
    "PlanBackupdestinationMappingsSourcevendorList",
    "PlanBackupdestinationMappingsSourcevendorOutputReference",
    "PlanBackupdestinationMappingsTarget",
    "PlanBackupdestinationMappingsTargetList",
    "PlanBackupdestinationMappingsTargetOutputReference",
    "PlanBackupdestinationMappingsTargetvendor",
    "PlanBackupdestinationMappingsTargetvendorList",
    "PlanBackupdestinationMappingsTargetvendorOutputReference",
    "PlanBackupdestinationRegion",
    "PlanBackupdestinationRegionList",
    "PlanBackupdestinationRegionOutputReference",
    "PlanBackupdestinationSourcecopy",
    "PlanBackupdestinationSourcecopyList",
    "PlanBackupdestinationSourcecopyOutputReference",
    "PlanBackupdestinationStoragepool",
    "PlanBackupdestinationStoragepoolList",
    "PlanBackupdestinationStoragepoolOutputReference",
]

publication.publish()

def _typecheckingstub__afe9afc89a50b677d21bd6eb16161b18e0c0d440740fd0ed9aca7c7f6cbdc5a8(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    storagepool: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationStoragepool, typing.Dict[builtins.str, typing.Any]]]],
    backupstarttime: typing.Optional[jsii.Number] = None,
    backupstocopy: typing.Optional[builtins.str] = None,
    enabledataaging: typing.Optional[builtins.str] = None,
    extendedretentionrules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrules, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fullbackuptypestocopy: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ismirrorcopy: typing.Optional[builtins.str] = None,
    issnapcopy: typing.Optional[builtins.str] = None,
    mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    netappcloudtarget: typing.Optional[builtins.str] = None,
    optimizeforinstantclone: typing.Optional[builtins.str] = None,
    overrideretentionsettings: typing.Optional[builtins.str] = None,
    region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationRegion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    retentionruletype: typing.Optional[builtins.str] = None,
    snaprecoverypoints: typing.Optional[jsii.Number] = None,
    sourcecopy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationSourcecopy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    storagetype: typing.Optional[builtins.str] = None,
    useextendedretentionrules: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__d5cac8905fd1485b17c65726e4401d43dc62dc3136cdb60df184e2f676fa4b15(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da6726e44ad816469f1829d87cedc859cb7dae95846b1ee5d9f749d223d7774(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrules, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1edf1dd826e5f547b33c41c2eb03b71fdd1db9623fe8c088024cb20ea7dd8091(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d2917c9848c038127e495695e18358a1ea04d84b35afc878bccc59f0a294c1(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationRegion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9e658391caa819cf5b91ff2afde5f876034b2dd77fa2459edcab22e03845c8b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationSourcecopy, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bddafe8bbad1303c00bcd451c7ac55cfa5d2c7560fb40962dc83bd72846dc0a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationStoragepool, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__273d2102d7b98dcd60a322978b963e33552a78d039f3771dbd47e01a7bb14d12(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4e950e9c69bc3651acff0d7f19d0cdb7114d0b5a8a5c66ba5691879287424f3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4a1ec6ad054a3270c2fad2131b92cd1f5374a7a33f29bf4b710a3da26899b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcab93742a123a19bd20ab4576c15ca0f6ffc105df47be9e1ec3a9655f93d9ea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3439701104bc3d2d91e95349b40a908c244cfc1828a389941931de3c5f78731a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea2e711afae1d85754eef1f352ca5f10b6617766199c5da3a5d6410c15e7546b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__429617ede57a62a0f655e5641a2a34dd5fc1e172efafcf15cc3cef2f7582e7ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62d1161c804b7ef227d217a3b5ea1762a6779846ada41f69ad15728c561ba7c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8974b972dc431a1960fb0e5c71f0e26aae3cfca8efd246512acd38d716143e82(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5507715a3b00a1c9dccc92388cc6ece343e839a4fa698557254d20a06679ede7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e5600d4f64c11a38526014cc447cf2063f486a5f1486ada6d3ba0a47265fae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ffdfecec6194b75a5ef9271af21523e33255d1cffbf480116bff299c7c7be1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551cbdc7dd4c8bd9cbde21fa21d050b37b0323839918d0417865da5c147ee3c0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9035efd0e0d7467c643ba8ff3d756b78a271a59be6f3428dcc462ae38ab959c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5ddc4b2a02617c1bc4839f5aed478070cf771f5edfd11ef8cbc3cc0b01d966b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d160dea90b969ff92391a9569deac06a89d655697e0337e4f92787dc2fd3c384(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759ca3f594fe25b1fa13767693b603067e17393c98d863c9f43c36cbf0008d63(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    storagepool: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationStoragepool, typing.Dict[builtins.str, typing.Any]]]],
    backupstarttime: typing.Optional[jsii.Number] = None,
    backupstocopy: typing.Optional[builtins.str] = None,
    enabledataaging: typing.Optional[builtins.str] = None,
    extendedretentionrules: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrules, typing.Dict[builtins.str, typing.Any]]]]] = None,
    fullbackuptypestocopy: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    ismirrorcopy: typing.Optional[builtins.str] = None,
    issnapcopy: typing.Optional[builtins.str] = None,
    mappings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: typing.Optional[builtins.str] = None,
    netappcloudtarget: typing.Optional[builtins.str] = None,
    optimizeforinstantclone: typing.Optional[builtins.str] = None,
    overrideretentionsettings: typing.Optional[builtins.str] = None,
    region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationRegion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    retentionruletype: typing.Optional[builtins.str] = None,
    snaprecoverypoints: typing.Optional[jsii.Number] = None,
    sourcecopy: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationSourcecopy, typing.Dict[builtins.str, typing.Any]]]]] = None,
    storagetype: typing.Optional[builtins.str] = None,
    useextendedretentionrules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cf1d11dc9b915468793146efa58d8c847edac3dec7e87d1ee39334d02611b23(
    *,
    firstextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    secondextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]]] = None,
    thirdextendedretentionrule: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7deeaef569f6ab6ed9f9af54d4591d1391e00ee2b3bfcf7caec63b7d053cfdb6(
    *,
    isinfiniteretention: typing.Optional[builtins.str] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d68ce0543409be10600bd6ce721b19271b182b34f25a66b419f9f388694d00(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__537e71e278825e8bb3fba830e22f700fe5ee92f7daad3c3c7d7ffb3c7ba8f0b0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435b60a04d69d51882478c8af316b7946f8ad8ac14ab146017f1e4d4aaa1287d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e705ccb621bceb1ec40944b5ee0304f213a41a46964d9e0ee1599f74049e01e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97db0bc65e986f86cb95516a43cc02ebcfb73c1e8b93f47e897e0bd1a56b260c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3c4fda4e17accad08393c10ed3f3e5f140f62265f7ec111888d217fb942777(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41f131f8472f355a7171113fbae340a41fdf5d44ded20ebb8b28341d2e25c69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__624753575cebe0c1757ab35e0d7c76fb5958c4ac56257d06a9fcee6361f4250f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56728a38a5342dc0df99612495bc44d7b8d0364538b9d285b7ff616af7df7056(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__247e62cec15dc3c23c9b6e66f79d1c2d6b7e706a11b305a6e3f473b1bbb9ff1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__318d849f17f4c6de68d9649c9d104fdabb6fb7c90490e6f98c7dd019870678c5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cf2ebc87aab8fea051d1390d9d6c8cd4d360e5340c4a274f3061282493479e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb4adf419d30240db461ff628588666cdde9eff75266f53d1f7cbfd2bc96b7d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0005214713661ef33e86412bcdb3dd45861527ebaff97393d3ae2abcc7041618(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1885eaf163d2db8c8c48ebec806313c13063900be74a129d8a924e5b0e8a6eb5(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77bcf8b0e83e8073394b146d3cb3f648666e4fbdc8c8a823f301a0c6670974cf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5cc5cf9c28989605931d8ce17bbbc6c3871ee163c3c808ebe3a38ed85ba2b9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrules]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93609181fcc46a045be938645746ee716c6ee450c093d1ffabe8067726a7bf69(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5de32bd0c12bfeb8a684b6bab8a24e17d9105cf53cc5ee124573a499f3c08847(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesFirstextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33e5a9e2479f3bb88282fe2289c8d2d811470ad7c89b4cf6d0531289eea87ca(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac9fc0503d99fa733784ebab70af4d98f9e3844115960a01ae6fc6341cb92925(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4caf87273b71ee08fcf4bb0396cebdbc46221fd3e34e65afee70aea582b8b2b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrules]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2a7296928bdb4803bc66c704d9101ebfe57f3d49188989ae694fd89a1dd355(
    *,
    isinfiniteretention: typing.Optional[builtins.str] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__437361456ae9118e0e805b01c8ebb95bc89972e548f3e019c05ce18cd08e1917(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae3a69ce40d9d22e7d8fa7cb0ff06acd44bd51f29db6ed846022a3bc4f2c0f6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0908f48f9614ec7d230bbcd762a032388839ad137ee2469cad8757eca5b50db(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57245266060482e7c191ab14471d8442b29a1666f52a7d65abafde25b59ffdda(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb47da0450d77ad5b5e6c2a11908081abb7192932edfcd5d3ea933a531258a30(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ffbefb60fcdb8bfe26e301e8de061bfd5787f888c8a0d1be36ed6cff05dd528(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1a34af8df9b3dedf682e5d283c98b65919f3613303d2b0c4cd0dfbe60487891(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167d01d713e52c5f1e34d2637de5201d4f5b0cf92b44a52088552f594d96c678(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e0e6fa1c38895eeb67bb5b4e3d42cd874940df2e5d036b16ea48065b6d7cccb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61b76a8d5678d4041412af42975cf90c083234afe45118bf71314295017135bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931a30c3a715b81655524db87b2a7fe59ec7c70b8e7e46b12e2d4effdede919d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesSecondextendedretentionrule]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc71c68690963151149b51e696e15ee3cfd296650e48a4b32a93cc5872d8d86(
    *,
    isinfiniteretention: typing.Optional[builtins.str] = None,
    retentionperioddays: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c327a57c52a3a3815d253cc5324ba4966fcd0fb0d7e48a084a51af3da80e83(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4960c3665373e343fe96ace4a37e281a30a0165fbd0174f629c4729262764d19(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09651842093cb6d6e011621bf6bd9f771244a8f334e5a990450f8ffa53216321(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__998e3eb4826db3aa28a84183585c5814fc283582b530bc51b8cc03a33a9bf3ea(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88a7bbc9db9f821a568189e979a442714c00b903b38771ec9e263749c6deaa1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54b815b1b71789c11c3d9ffc0d6888e417faf4323a49179020edbd54249ac6a9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d25ec892b150ac7a82bf1051f7bcdd9db06ebd0f54c3ebd204cce9647e614490(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7348f60caf4b6027c4b651180cb5742c1b79d1839d6f4f8f4de6164f3bfb83b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534436972bdd9fb615cbb50efff60a89db77060c4467b9dce0b67abe7ea1e1eb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89cea937898ae83975e631867a9d5b15593b1171558e2855c21d4616bdd182fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75e0a82e1b3b39a8a0a79250e681ac34fcf2895e479f86aabf58ac83eda9f0f3(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationExtendedretentionrulesThirdextendedretentionrule]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7909ff14527e08bc928ddf0e49f6d8cdda2f37114c5fa710e31941e0cd67aefd(
    *,
    source: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsSource, typing.Dict[builtins.str, typing.Any]]]]] = None,
    sourcevendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsSourcevendor, typing.Dict[builtins.str, typing.Any]]]]] = None,
    target: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsTarget, typing.Dict[builtins.str, typing.Any]]]]] = None,
    targetvendor: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsTargetvendor, typing.Dict[builtins.str, typing.Any]]]]] = None,
    vendor: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e92a209e0324b3bec820f9352f1f7ac5a7d6ab687fb7a652e1177a470a2e06(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709f297d14373ebdcd6225cca98390f0c07c8941287f533bfb7ffe3c1a8290f8(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e76c48345526856c1c3983780b845f994156a5e85c4c4839a08b339189cfed3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fedfad6d4b981cef00985a1310c32699ecd79c5673880125aead8b38e1af788e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e9b618c53953b5f27b9e698eaf3b04ff6abaec3ded42f07e8dbb16b4a2b4f48(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc8df61627d76e56c072e1bfffd60f30527d1b47d28e31bd04ed1c7a94af93c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e36c6d60edfeb4d1cd9439972525dce503a43429b78086b145d6b699ad1f0da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0f93d1ae4c0cad3eaf2630f5b876dc306df2f0853364af41d8af8ab04b48087(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsSource, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a16269d750f263a3dc5a0cb53cd0a06d1e62a3727e753098d6ddb1ada066d524(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsSourcevendor, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45eda72686840da1defc2a79b8ec233550ee95cb1767dfad08148b280f9c51c0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsTarget, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__268171d1f9577326b705fc67d58a07aa4f38fb77167c47b7da2832a1ae41a991(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[PlanBackupdestinationMappingsTargetvendor, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e85537e80d944f7ec67251d728eb9a985da156725650d3a1353a7ea3af0d8df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c9db6bc3e452691b4d023926955b4163bd8a580b1b572208862a0436d0171d9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05ccae52ad5f061dc8963f35a7843e7650418a94edd450ea06577e0baa0104e3(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43d492633947506aa4450ab050cfb57c262dbd2bb6799eb4eb962b00888e126(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de3c64eb445f4117803e8ac457c8bc3bd7c8a71de90c9065df1fb44350786b42(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93166004eb7c94c73ed0e2f5d8bafd719ff4cb6b19f3b0a44a9ffa960a6025b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ced1026aabad55d060436113a56a6f61ef0d85a71cab0ae62b78ad950bc2e7d9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e81f816f065a7f1a86743b59f6bf904544e41fb290b9d5b19aa4636453fc9cb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb766415e463e62e21725b92eef929e95faf8dcfa8cd6869dd4b74208f28dce2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSource]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d432bf8c8d8646ae6c26d41aa123fb87335645300b17533209a06aad1c11025(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1330f93d6dd6c619e427738ae51d3f2b8cf683b9e8d85081fc811f36b821faa7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a059f8b9e515a2cc336ed5d2437875d1299bffe03600fd8052dc5b25f02351b2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9678234503be0ab467c8a411455994db9fc832ec7f8d2b51ea01fe8e1e60faf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSource]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb67a0f4f14686b4dba2267125c6ebe8dc1812c9df19097f053343605b55bf2(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cf7aee2118f6b53fb9199f27f7710f50d0388d265afae839059d86b360e8ce8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facda5db15f5e656df8495c6f51b385c0d007e9386ff9c5163757c2dbd058088(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa51c2c652d8b97f9e021039ffd8a12299af5ed0a6ba458d012dc05adeedb489(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__531839bed798ca5c585c85382621fa43eff851577fb8044692b888f6603cc20e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03986fcdcfc9bb01c80f70a57bcb10a481469d66d4d2b8a1ffa85d6ec92b8e7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20de747d0aa30648227bedd8c191228bd858272ae272edb75c702c96d772a22(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsSourcevendor]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__679296ddad5659c6e074228c3999a879ec7743e336c7dd6a68f63e60e530dc09(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8679ebcc1d822ce93c98898df48f0536751a37dc3ea5a14588fcb92b4c002ecc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b183633c14e5778f783a4f1a3f929ee10997141b30df7a5f642e03096e290ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66fc89d34f27f1888512b77be198e42047a9a666baa62122f5dfbde6bd449572(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsSourcevendor]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766d045b03c7082a4c53d8de903f0983a61cd1443d43dd10affce4b85d71c102(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be7a03ea4d9a543be90d6624359bcf037416f2b89fd5281720ade8c68e84c5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdcf39c388dbfb15b6bfc5e808a5852d11c9e737d4df1594996b530e2f6cd71(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d14a9abefdb5ac35224bf2cdd1f572258d358855df30312a5a6fd5ca2225c03(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb01886bd478f45341cc4511d602adbcc382054fa159dffd5b9ec439e2011e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6297f3f1dff71627f318edbc5a85968cdee8df78a939f2fc539554e7ee0c0b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c803e0e46254d89c37e115dc92453315668c0a19ecefd36f45c5c0eff6a54c44(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTarget]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__968f41dac465a3e5b7f65f94b4de5365529862f166b7da448d802ea0cc3decf2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5f3b457040a05a94406b04d5c7533957813a2644e0dd0fba1a0f25b42dc6201(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450a2ac9b0e1f2724126e26d312ebf4d2bd143fface5081629b9efa08adfe663(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5801a19f72c9cc58d0568c7de0a9bfb5272cb44eac617b9d9f01bd394e8ea98(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTarget]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d869f85225ae025e94d7d1747adb90a6a1da2784dfe80251395693bb9081399b(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ddd34342edb193dff5579565b2bb4e05a9b28114603e27b8dfb17bb2e00a353(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffdfc96b970186bc7374f677b7e84ed592974c12a0ea763cfccb90d68d931faa(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__098169b924de444afe228f9c19d6b54e3751b2005976af8724132e799430a0d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edf5c008a4aa50d16d1bb1d514c87d8695efd39630bb80bf7ce1e59271a81b38(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8c31b91e5a6dd3bca5cce9c5b918e10500cad33db476aa25b1c8a69a81585b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d92a3ff19930646543523a426dae5e9a2021345b3d7acf48933f85075b315648(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationMappingsTargetvendor]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6864c02612242333fc0c14d8a5f88ac392c0f01e9726468227eb187e8dc5955(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__027d744b670904c7b79fe6374e7f9d386bf6a6ef470e913b5e3d60227017962c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__773c776925b15775bf387a2293760dd7b8c6d33c34c902892d0ad725facae369(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45392576926d7a0cf282606b5979320061eaa00445cc5f87de04c07c85e8519d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationMappingsTargetvendor]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128722c24a1054f6e09c2a032fb42deae7e18db1d07676a77484ebb715331afd(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e13c35b4102e4ad60d530dffdf5a3210ae5af8c661e25cb1c51272460aa4fbc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3187411cdd91d572327c0b755cba4afc92cfb5f83ef3aef9d68c61ddbc8ef0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79806aaaf0ff0ebcce2bc06540b11d4671183e91b3b6f6fad5e53ba9726bd487(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbad8321c600e895dd4b9e56b68fb9e4f47599e7633c5de92c8bfff68ce31bef(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__257e1c1676e9524453f76dfa909cbb400abb73632fc267a4a59d4bcffbf9c7fb(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b62939294570763de65dc29f6c827656be22dd25075f6f85d075d1d07d21ae5c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationRegion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffae901dbd1c94bee5a9cd7f536e8bcf2f614393ce468e69271800d19d085c22(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3fb3a665209d49cbf50881cda14023b28a2923fd5d9fbc01c8bb6df8167d37(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__399b5401d472bb4a0f861097dcd86f3843059530bc0132fe8eee852bc01053c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22dd9b6ebbb2e006de9483f0d5e2ddde3a6fd4255b87a70d062f9bc642bdec81(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationRegion]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__502edb42094d4a4805c3e25519fddbd48f80bca612eb62c4ac9a9e5d29dbcef7(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f218eedf06bb3c3cd2b78787ef32a9f75abee9ea8fd6b800e11ce7c0ed49bef(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c22928d9fb60d17c20867a27bbdaca08e680fccf99d7e44602da02722712f87(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2539ac794204bc21240333d5f9dc92577fa289c6fd4a8bac7af71152f289697d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b59b16a4f01752120aefd17488589ffbe5de5aad72756bc061d2a14e59eeb7(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e2a54e19b59c076a59385b19e8be22c0c647e213701d78731c37edd204b9aa(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01bc79eac9258bb2d7e6f6b3c9d1cbc36edb4980d940be189c4b2b8961bf022b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationSourcecopy]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6edd522d5b5c7906b7883e760a55a6b906db76971c3de0a95d25f6276cbe931(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fe013c563d981b4e36f53e7f3f13af7f6748fb6ffbcacec35c3b658c675696(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3558b7806ff056c8ff28a5dd779ea6c30f4c7ac603b35263d93fa4f88e49afe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0006ea19311462bc9b4d3aa28c7c0554ed5cb01953b16395628a6deb409135(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationSourcecopy]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__436f9b9eb6cc38545830ef09384fed655dc45dca1fa7272d15d84f19bcb235e7(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e883943503292661ea84f1a4e2ecbf6c3e6f4a7729960a7f0e1959b63f047fa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__499f2e594bd690c711bf3d7973e079f0d91975855d5816c7f74f6746e2b14d6a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef16b907ae627053d1a229a6589b0707d2c72c20bafb6c1aef9c983bd06deed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8d149ae47350983d161017e2fc81fa9e6138e672d67a0ed5b1de4ba0eb317d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e467a07f355416a33f534b87ad209ef2a5d41532e859f1f9fc6c9d548bcb985c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f204819d57a2d7ffdcea687ced3736e7b9a76ca380b7e2f54bbffc106e637f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[PlanBackupdestinationStoragepool]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__830afb6121d2eb7b2a13c12195e20cd7fa6e519029335b3c48b9b2ccfef574f3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c566987ec535ea5157a714b416257e549aa998dc1ccdf4460934ea4eec27c82a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22fd9de459ca9bf2d79b5a2e34c7fc6915828c55f31f8f6935b5122cad7be076(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b288265124f89def8b0836fa306303aa4d0d49ce7390753507c702666344470(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, PlanBackupdestinationStoragepool]],
) -> None:
    """Type checking stubs"""
    pass
