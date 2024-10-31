'''
# `commvault_kubernetes_appgroup`

Refer to the Terraform Registry for docs: [`commvault_kubernetes_appgroup`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup).
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


class KubernetesAppgroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroup",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup commvault_kubernetes_appgroup}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupActivitycontrol", typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupCluster", typing.Dict[builtins.str, typing.Any]]]]] = None,
        content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupContent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupFilters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupPlan", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup commvault_kubernetes_appgroup} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#activitycontrol KubernetesAppgroup#activitycontrol}
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cluster KubernetesAppgroup#cluster}
        :param content: content block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#content KubernetesAppgroup#content}
        :param filters: filters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#filters KubernetesAppgroup#filters}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Specify new name to rename an Application Group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#options KubernetesAppgroup#options}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#plan KubernetesAppgroup#plan}
        :param tags: tags block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#tags KubernetesAppgroup#tags}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#timezone KubernetesAppgroup#timezone}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7589979f6ff1fc3754c3c89584a95d4277d658c8974a2e80b24e0d1fef75c91)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KubernetesAppgroupConfig(
            activitycontrol=activitycontrol,
            cluster=cluster,
            content=content,
            filters=filters,
            id=id,
            name=name,
            options=options,
            plan=plan,
            tags=tags,
            timezone=timezone,
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
        '''Generates CDKTF code for importing a KubernetesAppgroup resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the KubernetesAppgroup to import.
        :param import_from_id: The id of the existing KubernetesAppgroup that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the KubernetesAppgroup to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36d412414dc3e0bdb924f69e5fe254035cabcbcf38b3019a2f8ac25c2a2e9091)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putActivitycontrol")
    def put_activitycontrol(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupActivitycontrol", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0a793de2f9d98b0fb4d8bfe167d0c88a13c82e0baa16b89ea5c27992037801d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActivitycontrol", [value]))

    @jsii.member(jsii_name="putCluster")
    def put_cluster(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupCluster", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4ed074395297caac911405e8c71733955245c7d8c591a170a756f45e264da64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCluster", [value]))

    @jsii.member(jsii_name="putContent")
    def put_content(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupContent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e8b88f9c870adf6b7ab719b50601882f83bdda8838fa4eed6ab872a3fb70ead)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContent", [value]))

    @jsii.member(jsii_name="putFilters")
    def put_filters(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupFilters", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d14126c7a6d791ed53a0d5fe8a77ec0b0656fe78c589346ad4352648da134e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFilters", [value]))

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5055fa4579d73d0a749d9277340a1f1bdf35f68dc773a6260c01ef8fbb22afdb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOptions", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupPlan", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aa59ae1fa90b20eda6c0d1b1e444afbf93cedc86c8f3047b94aa19e7962232d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cec767fc2e748035ca9e4a1aa2aad1bfa4e9ea5f7f921592f8eb01c6aafaa4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="putTimezone")
    def put_timezone(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupTimezone", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2501ca895e5d25225b5b6844e645377bb7b24f9df123bd3b32a063b63f7e42c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTimezone", [value]))

    @jsii.member(jsii_name="resetActivitycontrol")
    def reset_activitycontrol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivitycontrol", []))

    @jsii.member(jsii_name="resetCluster")
    def reset_cluster(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCluster", []))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetFilters")
    def reset_filters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilters", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTimezone")
    def reset_timezone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimezone", []))

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
    @jsii.member(jsii_name="activitycontrol")
    def activitycontrol(self) -> "KubernetesAppgroupActivitycontrolList":
        return typing.cast("KubernetesAppgroupActivitycontrolList", jsii.get(self, "activitycontrol"))

    @builtins.property
    @jsii.member(jsii_name="cluster")
    def cluster(self) -> "KubernetesAppgroupClusterList":
        return typing.cast("KubernetesAppgroupClusterList", jsii.get(self, "cluster"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> "KubernetesAppgroupContentList":
        return typing.cast("KubernetesAppgroupContentList", jsii.get(self, "content"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(self) -> "KubernetesAppgroupFiltersList":
        return typing.cast("KubernetesAppgroupFiltersList", jsii.get(self, "filters"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> "KubernetesAppgroupOptionsList":
        return typing.cast("KubernetesAppgroupOptionsList", jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "KubernetesAppgroupPlanList":
        return typing.cast("KubernetesAppgroupPlanList", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "KubernetesAppgroupTagsList":
        return typing.cast("KubernetesAppgroupTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="timezone")
    def timezone(self) -> "KubernetesAppgroupTimezoneList":
        return typing.cast("KubernetesAppgroupTimezoneList", jsii.get(self, "timezone"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrolInput")
    def activitycontrol_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupActivitycontrol"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupActivitycontrol"]]], jsii.get(self, "activitycontrolInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterInput")
    def cluster_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupCluster"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupCluster"]]], jsii.get(self, "clusterInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContent"]]], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="filtersInput")
    def filters_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFilters"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFilters"]]], jsii.get(self, "filtersInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptions"]]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupPlan"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupPlan"]]], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timezoneInput")
    def timezone_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTimezone"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTimezone"]]], jsii.get(self, "timezoneInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a384204abc17cfde459f037c2a586188a47ec22425c4917a8018f258ffddf64c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52779712bc5a21342fd9278c4034908a34fd7714b63ffab8c65f05d99dd1cc04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupActivitycontrol",
    jsii_struct_bases=[],
    name_mapping={"enablebackup": "enablebackup"},
)
class KubernetesAppgroupActivitycontrol:
    def __init__(self, *, enablebackup: typing.Optional[builtins.str] = None) -> None:
        '''
        :param enablebackup: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#enablebackup KubernetesAppgroup#enablebackup}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7d2068153accbe0cecb62ce2d40d25bcdf52f6979a684c9bcf4f27bb81204a3)
            check_type(argname="argument enablebackup", value=enablebackup, expected_type=type_hints["enablebackup"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enablebackup is not None:
            self._values["enablebackup"] = enablebackup

    @builtins.property
    def enablebackup(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#enablebackup KubernetesAppgroup#enablebackup}.'''
        result = self._values.get("enablebackup")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupActivitycontrol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupActivitycontrolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupActivitycontrolList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e40b06fb24338eb019a12773f44bb240dc907ba6d0129cf511d1bc801494fe6b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesAppgroupActivitycontrolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0bada9def581e8ed2e7058727fff60d6ca6ed5ab8775ad9c118d7bfd352b849)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupActivitycontrolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8314b36a54de4af85791da0857a6555bb2506cdc830de4410894b48d91baa01)
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
            type_hints = typing.get_type_hints(_typecheckingstub__26ccfdd8a758c5a1ea88e46afa60b01d02910136272d8d98353e6ef78dfa8a90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__889b5128450f5dfc2f013558c9b18b9b3d5dc671c9acfc27b048f913be0305dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupActivitycontrol]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupActivitycontrol]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupActivitycontrol]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ff62c1b6249067aac317e82e353e4ae397173e15e51fb122186cdf53ce555b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupActivitycontrolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupActivitycontrolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__64ce1c3d5347f7e5976167561ed574361af96a9d831bbff98442286c3af51267)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnablebackup")
    def reset_enablebackup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablebackup", []))

    @builtins.property
    @jsii.member(jsii_name="enablebackupInput")
    def enablebackup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablebackupInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackup")
    def enablebackup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablebackup"))

    @enablebackup.setter
    def enablebackup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20d9889c9e4a68004fd71d153786e4a4f222f72d28cf93b596dc0a74a2901a09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupActivitycontrol]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupActivitycontrol]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupActivitycontrol]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889d291a66bc3706888aa7c552affb47a8ad12e728de058224286fb275ecf670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupCluster",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class KubernetesAppgroupCluster:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__922ac818d70136da3d5f6c0705a9aba5ba57ee512ef3fefeaac27ccc3306c43c)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupCluster(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupClusterList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupClusterList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e639585bde6b9300718682ead99690aecb830dbe7e11050f0432e85399ccfe48)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupClusterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a581240bf45701f41882ca36f029882f1cfb102223ca56cfb4ac9e0bedfdade6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupClusterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8609f321a36cc37173bdc025ca7744f4d34751ea6b3f68d74dfe636baa178f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__de7b0c1dac82966d9a9af0bc985c2a66d7076ff37f7890806b4c15bc462a94fe)
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
            type_hints = typing.get_type_hints(_typecheckingstub__47d57f57968c69c877ac4b09fef35730d798cb6534067f8ad01a08676dc39cb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupCluster]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupCluster]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupCluster]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4e89281e80e72ce2cffdc3a4e68e6abd69e9cdc8189011f8685d9b216d92059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupClusterOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupClusterOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__b94eba0c0b6897f0ea102d02b821d5d6e5f6e4d0af64d4caeca5a80ef5963642)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98f0eee3269c4cfdffefefda994bb470ba3cc1255b22a1dbf44bf391f19cb6cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11f89acd2309cb5b9a1a6e41c44bd5cc1dbf3e72b5ba1419806d88c13b0c0ef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupCluster]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupCluster]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupCluster]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cdf30c244ab587be07d8aceb096170cdeb28c7e7f6ec5149bae6647f7105faa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "activitycontrol": "activitycontrol",
        "cluster": "cluster",
        "content": "content",
        "filters": "filters",
        "id": "id",
        "name": "name",
        "options": "options",
        "plan": "plan",
        "tags": "tags",
        "timezone": "timezone",
    },
)
class KubernetesAppgroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
        cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
        content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupContent", typing.Dict[builtins.str, typing.Any]]]]] = None,
        filters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupFilters", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupPlan", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupTimezone", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#activitycontrol KubernetesAppgroup#activitycontrol}
        :param cluster: cluster block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cluster KubernetesAppgroup#cluster}
        :param content: content block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#content KubernetesAppgroup#content}
        :param filters: filters block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#filters KubernetesAppgroup#filters}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Specify new name to rename an Application Group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#options KubernetesAppgroup#options}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#plan KubernetesAppgroup#plan}
        :param tags: tags block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#tags KubernetesAppgroup#tags}
        :param timezone: timezone block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#timezone KubernetesAppgroup#timezone}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdaef67727f0167580336f887651110ef5ef60fadaf84fd91a146d1ae45836e6)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument activitycontrol", value=activitycontrol, expected_type=type_hints["activitycontrol"])
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timezone", value=timezone, expected_type=type_hints["timezone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
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
        if activitycontrol is not None:
            self._values["activitycontrol"] = activitycontrol
        if cluster is not None:
            self._values["cluster"] = cluster
        if content is not None:
            self._values["content"] = content
        if filters is not None:
            self._values["filters"] = filters
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if options is not None:
            self._values["options"] = options
        if plan is not None:
            self._values["plan"] = plan
        if tags is not None:
            self._values["tags"] = tags
        if timezone is not None:
            self._values["timezone"] = timezone

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
    def activitycontrol(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupActivitycontrol]]]:
        '''activitycontrol block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#activitycontrol KubernetesAppgroup#activitycontrol}
        '''
        result = self._values.get("activitycontrol")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupActivitycontrol]]], result)

    @builtins.property
    def cluster(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupCluster]]]:
        '''cluster block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cluster KubernetesAppgroup#cluster}
        '''
        result = self._values.get("cluster")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupCluster]]], result)

    @builtins.property
    def content(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContent"]]]:
        '''content block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#content KubernetesAppgroup#content}
        '''
        result = self._values.get("content")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContent"]]], result)

    @builtins.property
    def filters(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFilters"]]]:
        '''filters block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#filters KubernetesAppgroup#filters}
        '''
        result = self._values.get("filters")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFilters"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Specify new name to rename an Application Group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptions"]]]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#options KubernetesAppgroup#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptions"]]], result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupPlan"]]]:
        '''plan block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#plan KubernetesAppgroup#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupPlan"]]], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#tags KubernetesAppgroup#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTags"]]], result)

    @builtins.property
    def timezone(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTimezone"]]]:
        '''timezone block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#timezone KubernetesAppgroup#timezone}
        '''
        result = self._values.get("timezone")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupTimezone"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContent",
    jsii_struct_bases=[],
    name_mapping={"applications": "applications", "labelselectors": "labelselectors"},
)
class KubernetesAppgroupContent:
    def __init__(
        self,
        *,
        applications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupContentApplications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        labelselectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupContentLabelselectors", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param applications: applications block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#applications KubernetesAppgroup#applications}
        :param labelselectors: labelselectors block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#labelselectors KubernetesAppgroup#labelselectors}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ccecb2865c0d73679ae5cb1a78102c6f596e7586d844a878e4a9bc608f70a9)
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument labelselectors", value=labelselectors, expected_type=type_hints["labelselectors"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if applications is not None:
            self._values["applications"] = applications
        if labelselectors is not None:
            self._values["labelselectors"] = labelselectors

    @builtins.property
    def applications(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContentApplications"]]]:
        '''applications block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#applications KubernetesAppgroup#applications}
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContentApplications"]]], result)

    @builtins.property
    def labelselectors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContentLabelselectors"]]]:
        '''labelselectors block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#labelselectors KubernetesAppgroup#labelselectors}
        '''
        result = self._values.get("labelselectors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupContentLabelselectors"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupContent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentApplications",
    jsii_struct_bases=[],
    name_mapping={"guid": "guid", "type": "type", "name": "name"},
)
class KubernetesAppgroupContentApplications:
    def __init__(
        self,
        *,
        guid: builtins.str,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param guid: GUID value of the Kubernetes Application to be associated as content. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#guid KubernetesAppgroup#guid}
        :param type: Type of the Kubernetes application [NAMESPACE, APPLICATION, PVC, LABELS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#type KubernetesAppgroup#type}
        :param name: Name of the application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__071dc462fc0e3dfb237a2ea13201227330433dac935442aab1d0813d8774b288)
            check_type(argname="argument guid", value=guid, expected_type=type_hints["guid"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "guid": guid,
            "type": type,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def guid(self) -> builtins.str:
        '''GUID value of the Kubernetes Application to be associated as content.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#guid KubernetesAppgroup#guid}
        '''
        result = self._values.get("guid")
        assert result is not None, "Required property 'guid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the Kubernetes application [NAMESPACE, APPLICATION, PVC, LABELS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#type KubernetesAppgroup#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupContentApplications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupContentApplicationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentApplicationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__10742edb978014b30549a6554b0b90ee995c4fc48b9158905c62b960066bb633)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesAppgroupContentApplicationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec1f8caadfdceb78276e82cdd247e89bdb4c51bab26f44ae4a855a859861b25c)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupContentApplicationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a4b86840434045b3200d6831bba81281a96bb06f8ad087cceb80659c676679)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6b736af98de1d9bdc0ed8246f03e25e2147283a7b697c0f3bd5d7c31cb32ad85)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ccc0a1a7e038c0279f6831f1f174c26aa79d20c2c84e9aea2c3aa049bd2f30bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentApplications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentApplications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentApplications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c300dbe93f9b0c52abc2277e7d24695d05feaebcdc7e6755123365d8fb4067a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupContentApplicationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentApplicationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__d43b8cae651eab972aff05760278cf4739ad45a7ced8eb412d3424b481b51c56)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="guidInput")
    def guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guidInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @guid.setter
    def guid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9becdc95ed7b49c582958cc6009b6797f00db11dd9ac2890a327ba1bf2bfbaf4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guid", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ce85ddc60886f99ebf2698a0f536574e84541ad788d7b53d1d1613b34833e1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba0b99ad30076a08373db86b537073adf7d1f09f40a5b39345e76dbd267c1f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentApplications]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentApplications]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentApplications]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6171a7cf58e0189047d12dbec1edb9ba935d54d3e7060a8b39aba6523aedc9fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentLabelselectors",
    jsii_struct_bases=[],
    name_mapping={"selectorlevel": "selectorlevel", "selectorvalue": "selectorvalue"},
)
class KubernetesAppgroupContentLabelselectors:
    def __init__(
        self,
        *,
        selectorlevel: builtins.str,
        selectorvalue: builtins.str,
    ) -> None:
        '''
        :param selectorlevel: Selector level of the label selector [Application, Volumes, Namespace]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorlevel KubernetesAppgroup#selectorlevel}
        :param selectorvalue: Value of the label selector in key=value format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorvalue KubernetesAppgroup#selectorvalue}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb16c20d75ac27d6850aa2b1242de7ae227a8487007de261d943a08fff250ed)
            check_type(argname="argument selectorlevel", value=selectorlevel, expected_type=type_hints["selectorlevel"])
            check_type(argname="argument selectorvalue", value=selectorvalue, expected_type=type_hints["selectorvalue"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "selectorlevel": selectorlevel,
            "selectorvalue": selectorvalue,
        }

    @builtins.property
    def selectorlevel(self) -> builtins.str:
        '''Selector level of the label selector [Application, Volumes, Namespace].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorlevel KubernetesAppgroup#selectorlevel}
        '''
        result = self._values.get("selectorlevel")
        assert result is not None, "Required property 'selectorlevel' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selectorvalue(self) -> builtins.str:
        '''Value of the label selector in key=value format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorvalue KubernetesAppgroup#selectorvalue}
        '''
        result = self._values.get("selectorvalue")
        assert result is not None, "Required property 'selectorvalue' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupContentLabelselectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupContentLabelselectorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentLabelselectorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__08d34b0a6f5758b335e5dfe492478dc5fd4746943f8d16bf28fe3d93f68de5de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesAppgroupContentLabelselectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a259c6b2f9f9d3ed5a69a2c2247819aa2ee8ab15755e099a11150c7b7306798f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupContentLabelselectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30ba58f4c311b06504b64e5dbf67d1b60755526d8652e1f5a5abff3ef169b90d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8f3bdc5502af51cb950872bf6daa7c0613a7ff9af408a83a6ef201fe275fde8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9aa4b6a9014398683335efad4140a89b1c37003af32a69fec0203c54f59daf59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentLabelselectors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentLabelselectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentLabelselectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3000c958d18cd6df4dcaf6c76743ca5a83cbc96b508a8a2cbb1479d6eda41153)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupContentLabelselectorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentLabelselectorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4a907121ad6be8aef156717e28c8e2d8163894fdce690b1a23fdc04df796ff3a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="selectorlevelInput")
    def selectorlevel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorlevelInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorvalueInput")
    def selectorvalue_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorvalueInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorlevel")
    def selectorlevel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectorlevel"))

    @selectorlevel.setter
    def selectorlevel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__321e71b7422f25161851e976e6313e5bdf1d0de338e6f9f6f30f90e9e0cd8aad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectorlevel", value)

    @builtins.property
    @jsii.member(jsii_name="selectorvalue")
    def selectorvalue(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectorvalue"))

    @selectorvalue.setter
    def selectorvalue(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8db60f173133de2d80d682d1fd2c91f7aaebd85d971860da6f27c9703bd9d06b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectorvalue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentLabelselectors]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentLabelselectors]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentLabelselectors]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94308ab6bd739a7619d0550623e46dc13666b4e2fc8a88ed1bfd415ba038761c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupContentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a6f91d407933bffce7c67e426cdec116acd080837b0edbddf73d20e4a3ff0c79)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupContentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6529b432eb9bc84a78e555544864ebd70c14948d72806ad459a2e26f95c7751)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupContentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6562daeccdb4e52ed87dd71446245007cba2692d37d10deb207e140c469f62)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70e4316bc329d64a97e3317d6c2961f6bb05f904e91defa537766237c6ea4977)
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
            type_hints = typing.get_type_hints(_typecheckingstub__03e8b338de38073aecdfd303e1341774ab86483d8541f755f2223cce26f1bd26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d5fcebf4ded2c4ec2a942672b26928a6a84e1922077214bb89ab3a662585879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupContentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupContentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__90bd82d08dc1f058485ff600c91022e359b9216ec655f900aae0ed2426cae322)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putApplications")
    def put_applications(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContentApplications, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b4b3068b2225bf88eb8575aa98953cf99606808a7c58ac75f6f82d442ca142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplications", [value]))

    @jsii.member(jsii_name="putLabelselectors")
    def put_labelselectors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContentLabelselectors, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90bf0594c21ca221a770fc1a39335c6ab869796a8f9c25b112258ef40fb480c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabelselectors", [value]))

    @jsii.member(jsii_name="resetApplications")
    def reset_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplications", []))

    @jsii.member(jsii_name="resetLabelselectors")
    def reset_labelselectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelselectors", []))

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(self) -> KubernetesAppgroupContentApplicationsList:
        return typing.cast(KubernetesAppgroupContentApplicationsList, jsii.get(self, "applications"))

    @builtins.property
    @jsii.member(jsii_name="labelselectors")
    def labelselectors(self) -> KubernetesAppgroupContentLabelselectorsList:
        return typing.cast(KubernetesAppgroupContentLabelselectorsList, jsii.get(self, "labelselectors"))

    @builtins.property
    @jsii.member(jsii_name="applicationsInput")
    def applications_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentApplications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentApplications]]], jsii.get(self, "applicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelselectorsInput")
    def labelselectors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentLabelselectors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentLabelselectors]]], jsii.get(self, "labelselectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__331a6e6c502d0972a52274197e8824050c0ee233b84164e7d139d25fc71ca31a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFilters",
    jsii_struct_bases=[],
    name_mapping={
        "applications": "applications",
        "labelselectors": "labelselectors",
        "skipstatelessapps": "skipstatelessapps",
    },
)
class KubernetesAppgroupFilters:
    def __init__(
        self,
        *,
        applications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupFiltersApplications", typing.Dict[builtins.str, typing.Any]]]]] = None,
        labelselectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupFiltersLabelselectors", typing.Dict[builtins.str, typing.Any]]]]] = None,
        skipstatelessapps: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param applications: applications block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#applications KubernetesAppgroup#applications}
        :param labelselectors: labelselectors block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#labelselectors KubernetesAppgroup#labelselectors}
        :param skipstatelessapps: Specify whether to skip backup of stateless applications. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#skipstatelessapps KubernetesAppgroup#skipstatelessapps}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3344364fc5deed19a38888224e4afb483e76aec5e6b719a421c51037dc0f537)
            check_type(argname="argument applications", value=applications, expected_type=type_hints["applications"])
            check_type(argname="argument labelselectors", value=labelselectors, expected_type=type_hints["labelselectors"])
            check_type(argname="argument skipstatelessapps", value=skipstatelessapps, expected_type=type_hints["skipstatelessapps"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if applications is not None:
            self._values["applications"] = applications
        if labelselectors is not None:
            self._values["labelselectors"] = labelselectors
        if skipstatelessapps is not None:
            self._values["skipstatelessapps"] = skipstatelessapps

    @builtins.property
    def applications(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFiltersApplications"]]]:
        '''applications block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#applications KubernetesAppgroup#applications}
        '''
        result = self._values.get("applications")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFiltersApplications"]]], result)

    @builtins.property
    def labelselectors(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFiltersLabelselectors"]]]:
        '''labelselectors block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#labelselectors KubernetesAppgroup#labelselectors}
        '''
        result = self._values.get("labelselectors")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupFiltersLabelselectors"]]], result)

    @builtins.property
    def skipstatelessapps(self) -> typing.Optional[builtins.str]:
        '''Specify whether to skip backup of stateless applications.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#skipstatelessapps KubernetesAppgroup#skipstatelessapps}
        '''
        result = self._values.get("skipstatelessapps")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupFilters(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersApplications",
    jsii_struct_bases=[],
    name_mapping={"guid": "guid", "type": "type", "name": "name"},
)
class KubernetesAppgroupFiltersApplications:
    def __init__(
        self,
        *,
        guid: builtins.str,
        type: builtins.str,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param guid: GUID value of the Kubernetes Application to be associated as content. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#guid KubernetesAppgroup#guid}
        :param type: Type of the Kubernetes application [NAMESPACE, APPLICATION, PVC, LABELS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#type KubernetesAppgroup#type}
        :param name: Name of the application. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e34c5c2946a87d6aadd9ce9e86d060b15227fd22090d0ff021331f08dabaaea)
            check_type(argname="argument guid", value=guid, expected_type=type_hints["guid"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "guid": guid,
            "type": type,
        }
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def guid(self) -> builtins.str:
        '''GUID value of the Kubernetes Application to be associated as content.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#guid KubernetesAppgroup#guid}
        '''
        result = self._values.get("guid")
        assert result is not None, "Required property 'guid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the Kubernetes application [NAMESPACE, APPLICATION, PVC, LABELS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#type KubernetesAppgroup#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the application.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupFiltersApplications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupFiltersApplicationsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersApplicationsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__01534c0ea326c1c32288134f384018d5864ee8de9080a32b9c6df7557033439c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesAppgroupFiltersApplicationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__138f7de9b2a9b721b61f06c2426386f100957b504ded22aefae6e1a666e66ccc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupFiltersApplicationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1124599fed44e868da5544f2ffe0bcaee9a68b8cc70a73f7010514ee2d0d1e7c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__07a9823dbb1c9c638e44e2596382e41c618ab884a9db15713201d0c989709f0b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6b6c3cee9dac9194c4e591265e6f92af693ae8eb012c63ade2d07fd4240ffad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersApplications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersApplications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersApplications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fa4a4fdf3efb850d29bdac24224dcfb189d8a1f9e5aed6457bd3aef39dd3a37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupFiltersApplicationsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersApplicationsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2bcb9d18ddf6b3f87aacc6bc533cb0f3f9a1025a30b6e456f35a5ef0d541120f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="guidInput")
    def guid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "guidInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="guid")
    def guid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "guid"))

    @guid.setter
    def guid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__728780fde284c3c511739e9552cff549f6bead79440f3aff51912d0b4d80a580)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guid", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__409b750bc5e28e085e7821d150863dbe6d5bd6e1caee7df80c4599fa03eccfa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bd97ed6a57bec35d581675973e8b3b18957932b672899f89ccd9e041b386d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersApplications]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersApplications]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersApplications]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5dbbd78a608a5de55afe5539728b9210463462f60d2a6f0a027350f21a6f2a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersLabelselectors",
    jsii_struct_bases=[],
    name_mapping={"selectorlevel": "selectorlevel", "selectorvalue": "selectorvalue"},
)
class KubernetesAppgroupFiltersLabelselectors:
    def __init__(
        self,
        *,
        selectorlevel: builtins.str,
        selectorvalue: builtins.str,
    ) -> None:
        '''
        :param selectorlevel: Selector level of the label selector [Application, Volumes, Namespace]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorlevel KubernetesAppgroup#selectorlevel}
        :param selectorvalue: Value of the label selector in key=value format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorvalue KubernetesAppgroup#selectorvalue}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d534d420af60cc01a248e9fa094ff417dfa905fe5ac4dfb0e262e9074329c5f3)
            check_type(argname="argument selectorlevel", value=selectorlevel, expected_type=type_hints["selectorlevel"])
            check_type(argname="argument selectorvalue", value=selectorvalue, expected_type=type_hints["selectorvalue"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "selectorlevel": selectorlevel,
            "selectorvalue": selectorvalue,
        }

    @builtins.property
    def selectorlevel(self) -> builtins.str:
        '''Selector level of the label selector [Application, Volumes, Namespace].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorlevel KubernetesAppgroup#selectorlevel}
        '''
        result = self._values.get("selectorlevel")
        assert result is not None, "Required property 'selectorlevel' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selectorvalue(self) -> builtins.str:
        '''Value of the label selector in key=value format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#selectorvalue KubernetesAppgroup#selectorvalue}
        '''
        result = self._values.get("selectorvalue")
        assert result is not None, "Required property 'selectorvalue' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupFiltersLabelselectors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupFiltersLabelselectorsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersLabelselectorsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__975717bc1af918bf96823f184eee5931df2f1444812f493366461e5f84c6d1e8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesAppgroupFiltersLabelselectorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__813ee924615754d0107e1fcc89f2f69aff24fb4e6b904560c0a59d05a21583ba)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupFiltersLabelselectorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8afb25a93c1d24b4c619a293f1a19efe20d8719f63976a396bdfd5942c43587)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cb4fa81bb46b8aad2c44e510d2b107a6fa8e2b8d0b97f557b58c321925c0f1c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c507c0d1957fd459be30dd88a1061ccf4f9504f9ac6c2366b9d637720926bff5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersLabelselectors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersLabelselectors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersLabelselectors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51e202038afbbcd0f2a666b2d260cca3b5b4409cbb11ce3ddefddbd4a3c77939)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupFiltersLabelselectorsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersLabelselectorsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4fb9009fc02cd893b79e0d2130178a6cbe12c3c0450b93db13bdc1992aaa2902)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="selectorlevelInput")
    def selectorlevel_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorlevelInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorvalueInput")
    def selectorvalue_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectorvalueInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorlevel")
    def selectorlevel(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectorlevel"))

    @selectorlevel.setter
    def selectorlevel(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076fbe1d6c8ee2fb4ebd09d60238e7744cb60ae181ee75bd4be268c81788e1a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectorlevel", value)

    @builtins.property
    @jsii.member(jsii_name="selectorvalue")
    def selectorvalue(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectorvalue"))

    @selectorvalue.setter
    def selectorvalue(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e10a55ec16ccbc64244446abaddcb5ab886797d3699e03ef2ab14bb95716e1e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectorvalue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersLabelselectors]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersLabelselectors]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersLabelselectors]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54031cf5641f166ff537f4f0aa4f78938aad85e498b7eb8782b01e9206608095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupFiltersList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f050bde3e2e3c417f6e8e43d06eb09b599e6186c0e33ab09bb78cb6c745efba3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupFiltersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c71cf63a4d12b0b5460c9b93555f349ceb78249c03421e023a29e9a577490b22)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupFiltersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e775389458fe2c198d8f266cd66ab43893bb9024696ccfdb82eb26cbba325803)
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
            type_hints = typing.get_type_hints(_typecheckingstub__622af09e2eb8cf644b671c1e834e507c899fed9fc2bbcc737538269ffca7a974)
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
            type_hints = typing.get_type_hints(_typecheckingstub__42e5a44c274b82352f2f4b02f2c7f61a1c32e722d8757fb7b25e215ce0c3c8c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFilters]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFilters]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFilters]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f0da0295b89268788f7524dced58fc482ad3b151c7e7669dd2f98c8ad0ae25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupFiltersOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupFiltersOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__293f28622c149c94d623a095dd22d2afc49eba6813672ae655cfd759ed23378d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putApplications")
    def put_applications(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFiltersApplications, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c0d56ee9bf7e9dec77bb4c24647d7780615ae623ea6730c3477be36f48351a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApplications", [value]))

    @jsii.member(jsii_name="putLabelselectors")
    def put_labelselectors(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFiltersLabelselectors, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca9f7821f5dc92b58608f3e85584c443b0093111b5c815e947bd26ff560558b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLabelselectors", [value]))

    @jsii.member(jsii_name="resetApplications")
    def reset_applications(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApplications", []))

    @jsii.member(jsii_name="resetLabelselectors")
    def reset_labelselectors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabelselectors", []))

    @jsii.member(jsii_name="resetSkipstatelessapps")
    def reset_skipstatelessapps(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipstatelessapps", []))

    @builtins.property
    @jsii.member(jsii_name="applications")
    def applications(self) -> KubernetesAppgroupFiltersApplicationsList:
        return typing.cast(KubernetesAppgroupFiltersApplicationsList, jsii.get(self, "applications"))

    @builtins.property
    @jsii.member(jsii_name="labelselectors")
    def labelselectors(self) -> KubernetesAppgroupFiltersLabelselectorsList:
        return typing.cast(KubernetesAppgroupFiltersLabelselectorsList, jsii.get(self, "labelselectors"))

    @builtins.property
    @jsii.member(jsii_name="applicationsInput")
    def applications_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersApplications]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersApplications]]], jsii.get(self, "applicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelselectorsInput")
    def labelselectors_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersLabelselectors]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersLabelselectors]]], jsii.get(self, "labelselectorsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipstatelessappsInput")
    def skipstatelessapps_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skipstatelessappsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipstatelessapps")
    def skipstatelessapps(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "skipstatelessapps"))

    @skipstatelessapps.setter
    def skipstatelessapps(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__969c05feeafb46b68d1ce10bc73325f9cf6bfc75d36e1b899c3aa2713d6913a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipstatelessapps", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFilters]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFilters]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFilters]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92c528df889e2d6bb3075321591cd65a9c5fc35468ac01e2bd4b546be8d4724d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupOptions",
    jsii_struct_bases=[],
    name_mapping={
        "backupstreams": "backupstreams",
        "cvnamespacescheduling": "cvnamespacescheduling",
        "jobstarttime": "jobstarttime",
        "snapfallbacktolivevolumebackup": "snapfallbacktolivevolumebackup",
        "workerresources": "workerresources",
    },
)
class KubernetesAppgroupOptions:
    def __init__(
        self,
        *,
        backupstreams: typing.Optional[jsii.Number] = None,
        cvnamespacescheduling: typing.Optional[builtins.str] = None,
        jobstarttime: typing.Optional[jsii.Number] = None,
        snapfallbacktolivevolumebackup: typing.Optional[builtins.str] = None,
        workerresources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupOptionsWorkerresources", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backupstreams: Define number of parallel data readers. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#backupstreams KubernetesAppgroup#backupstreams}
        :param cvnamespacescheduling: Define setting to enable scheduling worker Pods to CV Namespace for CSI-Snapshot enabled backups. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cvnamespacescheduling KubernetesAppgroup#cvnamespacescheduling}
        :param jobstarttime: Define the backup job start time in epochs. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#jobstarttime KubernetesAppgroup#jobstarttime}
        :param snapfallbacktolivevolumebackup: Define setting to enable fallback to live volume backup in case of snap failure. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#snapfallbacktolivevolumebackup KubernetesAppgroup#snapfallbacktolivevolumebackup}
        :param workerresources: workerresources block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#workerresources KubernetesAppgroup#workerresources}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f044735ae2d83c81f938d28ca13347293aa574837695b09cb562757aabd36217)
            check_type(argname="argument backupstreams", value=backupstreams, expected_type=type_hints["backupstreams"])
            check_type(argname="argument cvnamespacescheduling", value=cvnamespacescheduling, expected_type=type_hints["cvnamespacescheduling"])
            check_type(argname="argument jobstarttime", value=jobstarttime, expected_type=type_hints["jobstarttime"])
            check_type(argname="argument snapfallbacktolivevolumebackup", value=snapfallbacktolivevolumebackup, expected_type=type_hints["snapfallbacktolivevolumebackup"])
            check_type(argname="argument workerresources", value=workerresources, expected_type=type_hints["workerresources"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if backupstreams is not None:
            self._values["backupstreams"] = backupstreams
        if cvnamespacescheduling is not None:
            self._values["cvnamespacescheduling"] = cvnamespacescheduling
        if jobstarttime is not None:
            self._values["jobstarttime"] = jobstarttime
        if snapfallbacktolivevolumebackup is not None:
            self._values["snapfallbacktolivevolumebackup"] = snapfallbacktolivevolumebackup
        if workerresources is not None:
            self._values["workerresources"] = workerresources

    @builtins.property
    def backupstreams(self) -> typing.Optional[jsii.Number]:
        '''Define number of parallel data readers.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#backupstreams KubernetesAppgroup#backupstreams}
        '''
        result = self._values.get("backupstreams")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cvnamespacescheduling(self) -> typing.Optional[builtins.str]:
        '''Define setting to enable scheduling worker Pods to CV Namespace for CSI-Snapshot enabled backups.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cvnamespacescheduling KubernetesAppgroup#cvnamespacescheduling}
        '''
        result = self._values.get("cvnamespacescheduling")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jobstarttime(self) -> typing.Optional[jsii.Number]:
        '''Define the backup job start time in epochs.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#jobstarttime KubernetesAppgroup#jobstarttime}
        '''
        result = self._values.get("jobstarttime")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def snapfallbacktolivevolumebackup(self) -> typing.Optional[builtins.str]:
        '''Define setting to enable fallback to live volume backup in case of snap failure.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#snapfallbacktolivevolumebackup KubernetesAppgroup#snapfallbacktolivevolumebackup}
        '''
        result = self._values.get("snapfallbacktolivevolumebackup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def workerresources(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptionsWorkerresources"]]]:
        '''workerresources block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#workerresources KubernetesAppgroup#workerresources}
        '''
        result = self._values.get("workerresources")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptionsWorkerresources"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3d5833f565916644b3abe77f91c5dfcbc3e4c446b93880da88eddc933c5cb2d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace512425d19824db1f62c886b723c6862ba6032f4cb3967f7b294a2c3e6d56d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac11c34d9783dfd5071f3093adfa1ded08950eaa05ad4294c7cfac0ed57ba65a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3829b53e8cefbd1c56450d1ca23f234b98923030155ce352a2e24f95895e5acd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a5e355817ebfc874175f94f97542b6f73013e437c2f7a7a2203163114680baf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb3923d508e6e0890ea2d120e2af570810c3fdf4fce9488e5dac1f1e23e109b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__3c78c0ef61d13d19d8dc5f6828dd3bc4a96ae6e36ef9b1829b7cc34cd6f5c23e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putWorkerresources")
    def put_workerresources(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesAppgroupOptionsWorkerresources", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a071b78b24e5941acc264f250e696831281a15b5f36152efd38a9bf620539a13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWorkerresources", [value]))

    @jsii.member(jsii_name="resetBackupstreams")
    def reset_backupstreams(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupstreams", []))

    @jsii.member(jsii_name="resetCvnamespacescheduling")
    def reset_cvnamespacescheduling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCvnamespacescheduling", []))

    @jsii.member(jsii_name="resetJobstarttime")
    def reset_jobstarttime(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobstarttime", []))

    @jsii.member(jsii_name="resetSnapfallbacktolivevolumebackup")
    def reset_snapfallbacktolivevolumebackup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapfallbacktolivevolumebackup", []))

    @jsii.member(jsii_name="resetWorkerresources")
    def reset_workerresources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkerresources", []))

    @builtins.property
    @jsii.member(jsii_name="workerresources")
    def workerresources(self) -> "KubernetesAppgroupOptionsWorkerresourcesList":
        return typing.cast("KubernetesAppgroupOptionsWorkerresourcesList", jsii.get(self, "workerresources"))

    @builtins.property
    @jsii.member(jsii_name="backupstreamsInput")
    def backupstreams_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backupstreamsInput"))

    @builtins.property
    @jsii.member(jsii_name="cvnamespaceschedulingInput")
    def cvnamespacescheduling_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cvnamespaceschedulingInput"))

    @builtins.property
    @jsii.member(jsii_name="jobstarttimeInput")
    def jobstarttime_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "jobstarttimeInput"))

    @builtins.property
    @jsii.member(jsii_name="snapfallbacktolivevolumebackupInput")
    def snapfallbacktolivevolumebackup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "snapfallbacktolivevolumebackupInput"))

    @builtins.property
    @jsii.member(jsii_name="workerresourcesInput")
    def workerresources_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptionsWorkerresources"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesAppgroupOptionsWorkerresources"]]], jsii.get(self, "workerresourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="backupstreams")
    def backupstreams(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backupstreams"))

    @backupstreams.setter
    def backupstreams(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeef9bb1b50c11e7eefb49463b18a1d846cc63ad1fa0b03fbf62f64b7dc3d614)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backupstreams", value)

    @builtins.property
    @jsii.member(jsii_name="cvnamespacescheduling")
    def cvnamespacescheduling(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cvnamespacescheduling"))

    @cvnamespacescheduling.setter
    def cvnamespacescheduling(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf9d853eb2055101b8733a77281b6ba659f0aedc92d589d6df47d5b20b02cda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cvnamespacescheduling", value)

    @builtins.property
    @jsii.member(jsii_name="jobstarttime")
    def jobstarttime(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "jobstarttime"))

    @jobstarttime.setter
    def jobstarttime(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7764fedcfea0d1a7883b69499682c7a58794e824fd716d20ef150c76edc717f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobstarttime", value)

    @builtins.property
    @jsii.member(jsii_name="snapfallbacktolivevolumebackup")
    def snapfallbacktolivevolumebackup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "snapfallbacktolivevolumebackup"))

    @snapfallbacktolivevolumebackup.setter
    def snapfallbacktolivevolumebackup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35eec9b412e2d95025ebf251542d3df2125681dd56da4f12e9b28b5cc061d761)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snapfallbacktolivevolumebackup", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3317759bf42c5ced4a2795e551694c73792da2f0891d5bcadeab41f3bfa9f5e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupOptionsWorkerresources",
    jsii_struct_bases=[],
    name_mapping={
        "cpulimits": "cpulimits",
        "cpurequests": "cpurequests",
        "memorylimits": "memorylimits",
        "memoryrequests": "memoryrequests",
    },
)
class KubernetesAppgroupOptionsWorkerresources:
    def __init__(
        self,
        *,
        cpulimits: typing.Optional[builtins.str] = None,
        cpurequests: typing.Optional[builtins.str] = None,
        memorylimits: typing.Optional[builtins.str] = None,
        memoryrequests: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cpulimits: Define limits.cpu to set on the worker Pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cpulimits KubernetesAppgroup#cpulimits}
        :param cpurequests: Define requests.cpu to set on the worker Pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cpurequests KubernetesAppgroup#cpurequests}
        :param memorylimits: Define limits.memory to set on the worker Pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#memorylimits KubernetesAppgroup#memorylimits}
        :param memoryrequests: Define requests.memory to set on the worker Pod. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#memoryrequests KubernetesAppgroup#memoryrequests}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b531368a5bb0dcbdaf5d3ccd586dc47aeac711f0549c465811e450c26e66773)
            check_type(argname="argument cpulimits", value=cpulimits, expected_type=type_hints["cpulimits"])
            check_type(argname="argument cpurequests", value=cpurequests, expected_type=type_hints["cpurequests"])
            check_type(argname="argument memorylimits", value=memorylimits, expected_type=type_hints["memorylimits"])
            check_type(argname="argument memoryrequests", value=memoryrequests, expected_type=type_hints["memoryrequests"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cpulimits is not None:
            self._values["cpulimits"] = cpulimits
        if cpurequests is not None:
            self._values["cpurequests"] = cpurequests
        if memorylimits is not None:
            self._values["memorylimits"] = memorylimits
        if memoryrequests is not None:
            self._values["memoryrequests"] = memoryrequests

    @builtins.property
    def cpulimits(self) -> typing.Optional[builtins.str]:
        '''Define limits.cpu to set on the worker Pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cpulimits KubernetesAppgroup#cpulimits}
        '''
        result = self._values.get("cpulimits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cpurequests(self) -> typing.Optional[builtins.str]:
        '''Define requests.cpu to set on the worker Pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#cpurequests KubernetesAppgroup#cpurequests}
        '''
        result = self._values.get("cpurequests")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memorylimits(self) -> typing.Optional[builtins.str]:
        '''Define limits.memory to set on the worker Pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#memorylimits KubernetesAppgroup#memorylimits}
        '''
        result = self._values.get("memorylimits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memoryrequests(self) -> typing.Optional[builtins.str]:
        '''Define requests.memory to set on the worker Pod.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#memoryrequests KubernetesAppgroup#memoryrequests}
        '''
        result = self._values.get("memoryrequests")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupOptionsWorkerresources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupOptionsWorkerresourcesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupOptionsWorkerresourcesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd14aa5c4956065a9bbcec26d6de222e1a18d4d49eee44c41e3104a537e4e199)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesAppgroupOptionsWorkerresourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e7039d60863a2bfe006ca76d80a91f99276bfc795553d559d4f3630f6f47034)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupOptionsWorkerresourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b398e97967c2c781562f781f4587585b26af825b9e803e6a5bcad7d4ba0c9241)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a24227f1f68e8b34ce3726dc93ae1b9a800745ef46259fdb86d31ea5c6f4f8f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d02928be86883aabf2303e8e490d1b9a9100d5a66f57d20035978802c9ce88f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptionsWorkerresources]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptionsWorkerresources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptionsWorkerresources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d1ffdb5869946d3769269ab188ed7ad323b523943c9723cd5bbf3456cc6d9ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupOptionsWorkerresourcesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupOptionsWorkerresourcesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f95ff685cd44a888fbd4ca3efa25351f244ee84d94971c8821eacf4b2c8bb62)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCpulimits")
    def reset_cpulimits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpulimits", []))

    @jsii.member(jsii_name="resetCpurequests")
    def reset_cpurequests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCpurequests", []))

    @jsii.member(jsii_name="resetMemorylimits")
    def reset_memorylimits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemorylimits", []))

    @jsii.member(jsii_name="resetMemoryrequests")
    def reset_memoryrequests(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMemoryrequests", []))

    @builtins.property
    @jsii.member(jsii_name="cpulimitsInput")
    def cpulimits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpulimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpurequestsInput")
    def cpurequests_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cpurequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="memorylimitsInput")
    def memorylimits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memorylimitsInput"))

    @builtins.property
    @jsii.member(jsii_name="memoryrequestsInput")
    def memoryrequests_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryrequestsInput"))

    @builtins.property
    @jsii.member(jsii_name="cpulimits")
    def cpulimits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpulimits"))

    @cpulimits.setter
    def cpulimits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef46437a1231afa99fa57df2097c37da279e761b065e03e193ca47b995bada2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpulimits", value)

    @builtins.property
    @jsii.member(jsii_name="cpurequests")
    def cpurequests(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cpurequests"))

    @cpurequests.setter
    def cpurequests(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1af33256fa0428aea70158664db92bd05708b331fe08a7b82b6f61d59da6a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cpurequests", value)

    @builtins.property
    @jsii.member(jsii_name="memorylimits")
    def memorylimits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memorylimits"))

    @memorylimits.setter
    def memorylimits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f26730f3de48157d1b527b4aa348bb79f9d49a942b0027cef93b9aaf8462667f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorylimits", value)

    @builtins.property
    @jsii.member(jsii_name="memoryrequests")
    def memoryrequests(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "memoryrequests"))

    @memoryrequests.setter
    def memoryrequests(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b9eedd357bf5ad503ae579f9abd978dff4244c40cb227de45ba58b32f7d06b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryrequests", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptionsWorkerresources]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptionsWorkerresources]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptionsWorkerresources]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89e1b472246f3dfeded285418582af32ebe1ac485c45412854450ec9d300298)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupPlan",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class KubernetesAppgroupPlan:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16c080ceefb0f87173615ad210ca15613785082afb2d7ab2fd3216dfbfccf2b9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupPlanList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupPlanList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__95f86aae0b58dba003838a174224b8f37214ebbd3881200f55c46be0bab15c26)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupPlanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6adecedb27403dd1caf40572bb3f07110970335d33dbedb8171abb122ad1a9bc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupPlanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a2016db468c0bb6101df5f17a703588349d3c3ac6d891a4d5c6ed7231003251)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9209e0af633dae9096d8c03abfa6647454c7f238c1befe56bba3cfe964ae0d69)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f3ff39f88df03b8b1eca4d3a5145eb20c7f6400992286b9118466882cd044875)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupPlan]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupPlan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupPlan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__498b4df98a4dc28e4d5e910ce56eb8fdcbe762bbfc69669be458ee0de0a41346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupPlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupPlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fa05b7c1a5176d5175c0c7a66ac97aa76ff35c3728ae65c500e2b4fe78dc6ecb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2a2efcc90c0c0342bd26d92988a8b9369006b32ad0c1176390a2c3cc82fcdd6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54d763436fc746b2a5ba201396bed5a7b62b50036b802bc75a403377c67d0192)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupPlan]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupPlan]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupPlan]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e4af414072059151f4884ea8eae2af2020602cf0274776ef20bf17c9840de31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupTags",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class KubernetesAppgroupTags:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#value KubernetesAppgroup#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__185f114adc41a465c4f3a8174a9e5e648dcfb787beb92d6f9d48cc6ec9c80cff)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#value KubernetesAppgroup#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c1537f5f65e94af8fd1b54a7413fdd9355aa4f9d5ebdb3f2b1b201d7b1825c0c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c9ea3a2a7e481e81955308739e8a999121b91bd349d4578dc23a3f41533a290)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320d56a6487c3737967fb6ba196a684d3d562a0d852a81e22eb8ba8f071cec8a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c00fc46b10d228e3b25eec1a5f2662679defdc63091655cfce15e90d8402f0cb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db569c8ea6e38bfd393317ef774093cd253f0f64a3824572ef522f34817ac84b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efffdb3a8ba8464735abcb18bb9efbc7027629e8938cfa58b0df6cd2894054cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c39b1ea023e5b91766d2324c3c3678f7ff255bae3fdc95395ff77187ec7747b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53d4b0117bbd3785e33c3171fe4d88b4613f49874241bff0bd70f2c0f22ca92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30dd3a96f7d39176c6bb88f90a2e194ff14fff3b7d0a96a30ce10fceb67017a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTags]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTags]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTags]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d7453f63263aa23f821f780a378c9612fa0e4a266b208492e2521cbe0519c10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupTimezone",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class KubernetesAppgroupTimezone:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad6d8abef1b66db36b1d2d98d76dd3c6c0f18e50b28c8d37411970e529666b0)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#id KubernetesAppgroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_appgroup#name KubernetesAppgroup#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAppgroupTimezone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesAppgroupTimezoneList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupTimezoneList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c41847f7fec9e7001199f1451853a4cc090caef28f9be2c8c0eb0747e96c1786)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesAppgroupTimezoneOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d9fe519289f88435d626792b6966884eea782d3c4d69e9d81ad9f66fecc072)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesAppgroupTimezoneOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9680813f3ab6e7e3e4817b9454066852d7538062eb1ccfaedd6a104bb02fcbef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6a0dd53732d73b8f81973271326fee183864a81ef67e63f1c70eda72fb27fdff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfac9fd0a3f8564cc8eb15b37b5a649d76ac2016acef53a9ae8b34d44c104575)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTimezone]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTimezone]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTimezone]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b05063e8ef3b1508d4ea60663c4313e471aa7a852fc0cdcb89c07c8d6b09bfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesAppgroupTimezoneOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesAppgroup.KubernetesAppgroupTimezoneOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a937c2008e4bb440da13fec8780f36828a61983f9174e914792c259eec8c419)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e69b3e130b1263155bfb1f4bd24539248ea182ee4e62a13778fe7515e506d0dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536c88bc44d634fde6b311ec25f6d5ff8932752138fb23d9c09db2c9874a12b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTimezone]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTimezone]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTimezone]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5b8efa31ba2188fb62192232cb23b3d112b6c5ec9fe7715c387d88de5e4a68)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KubernetesAppgroup",
    "KubernetesAppgroupActivitycontrol",
    "KubernetesAppgroupActivitycontrolList",
    "KubernetesAppgroupActivitycontrolOutputReference",
    "KubernetesAppgroupCluster",
    "KubernetesAppgroupClusterList",
    "KubernetesAppgroupClusterOutputReference",
    "KubernetesAppgroupConfig",
    "KubernetesAppgroupContent",
    "KubernetesAppgroupContentApplications",
    "KubernetesAppgroupContentApplicationsList",
    "KubernetesAppgroupContentApplicationsOutputReference",
    "KubernetesAppgroupContentLabelselectors",
    "KubernetesAppgroupContentLabelselectorsList",
    "KubernetesAppgroupContentLabelselectorsOutputReference",
    "KubernetesAppgroupContentList",
    "KubernetesAppgroupContentOutputReference",
    "KubernetesAppgroupFilters",
    "KubernetesAppgroupFiltersApplications",
    "KubernetesAppgroupFiltersApplicationsList",
    "KubernetesAppgroupFiltersApplicationsOutputReference",
    "KubernetesAppgroupFiltersLabelselectors",
    "KubernetesAppgroupFiltersLabelselectorsList",
    "KubernetesAppgroupFiltersLabelselectorsOutputReference",
    "KubernetesAppgroupFiltersList",
    "KubernetesAppgroupFiltersOutputReference",
    "KubernetesAppgroupOptions",
    "KubernetesAppgroupOptionsList",
    "KubernetesAppgroupOptionsOutputReference",
    "KubernetesAppgroupOptionsWorkerresources",
    "KubernetesAppgroupOptionsWorkerresourcesList",
    "KubernetesAppgroupOptionsWorkerresourcesOutputReference",
    "KubernetesAppgroupPlan",
    "KubernetesAppgroupPlanList",
    "KubernetesAppgroupPlanOutputReference",
    "KubernetesAppgroupTags",
    "KubernetesAppgroupTagsList",
    "KubernetesAppgroupTagsOutputReference",
    "KubernetesAppgroupTimezone",
    "KubernetesAppgroupTimezoneList",
    "KubernetesAppgroupTimezoneOutputReference",
]

publication.publish()

def _typecheckingstub__d7589979f6ff1fc3754c3c89584a95d4277d658c8974a2e80b24e0d1fef75c91(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
    content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFilters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupPlan, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__36d412414dc3e0bdb924f69e5fe254035cabcbcf38b3019a2f8ac25c2a2e9091(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0a793de2f9d98b0fb4d8bfe167d0c88a13c82e0baa16b89ea5c27992037801d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupActivitycontrol, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4ed074395297caac911405e8c71733955245c7d8c591a170a756f45e264da64(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupCluster, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e8b88f9c870adf6b7ab719b50601882f83bdda8838fa4eed6ab872a3fb70ead(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d14126c7a6d791ed53a0d5fe8a77ec0b0656fe78c589346ad4352648da134e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFilters, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5055fa4579d73d0a749d9277340a1f1bdf35f68dc773a6260c01ef8fbb22afdb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa59ae1fa90b20eda6c0d1b1e444afbf93cedc86c8f3047b94aa19e7962232d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupPlan, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cec767fc2e748035ca9e4a1aa2aad1bfa4e9ea5f7f921592f8eb01c6aafaa4e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2501ca895e5d25225b5b6844e645377bb7b24f9df123bd3b32a063b63f7e42c(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupTimezone, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a384204abc17cfde459f037c2a586188a47ec22425c4917a8018f258ffddf64c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52779712bc5a21342fd9278c4034908a34fd7714b63ffab8c65f05d99dd1cc04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d2068153accbe0cecb62ce2d40d25bcdf52f6979a684c9bcf4f27bb81204a3(
    *,
    enablebackup: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40b06fb24338eb019a12773f44bb240dc907ba6d0129cf511d1bc801494fe6b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0bada9def581e8ed2e7058727fff60d6ca6ed5ab8775ad9c118d7bfd352b849(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8314b36a54de4af85791da0857a6555bb2506cdc830de4410894b48d91baa01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ccfdd8a758c5a1ea88e46afa60b01d02910136272d8d98353e6ef78dfa8a90(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889b5128450f5dfc2f013558c9b18b9b3d5dc671c9acfc27b048f913be0305dd(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ff62c1b6249067aac317e82e353e4ae397173e15e51fb122186cdf53ce555b8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupActivitycontrol]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ce1c3d5347f7e5976167561ed574361af96a9d831bbff98442286c3af51267(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20d9889c9e4a68004fd71d153786e4a4f222f72d28cf93b596dc0a74a2901a09(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889d291a66bc3706888aa7c552affb47a8ad12e728de058224286fb275ecf670(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupActivitycontrol]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__922ac818d70136da3d5f6c0705a9aba5ba57ee512ef3fefeaac27ccc3306c43c(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e639585bde6b9300718682ead99690aecb830dbe7e11050f0432e85399ccfe48(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a581240bf45701f41882ca36f029882f1cfb102223ca56cfb4ac9e0bedfdade6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8609f321a36cc37173bdc025ca7744f4d34751ea6b3f68d74dfe636baa178f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7b0c1dac82966d9a9af0bc985c2a66d7076ff37f7890806b4c15bc462a94fe(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d57f57968c69c877ac4b09fef35730d798cb6534067f8ad01a08676dc39cb3(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e89281e80e72ce2cffdc3a4e68e6abd69e9cdc8189011f8685d9b216d92059(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupCluster]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94eba0c0b6897f0ea102d02b821d5d6e5f6e4d0af64d4caeca5a80ef5963642(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f0eee3269c4cfdffefefda994bb470ba3cc1255b22a1dbf44bf391f19cb6cb(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11f89acd2309cb5b9a1a6e41c44bd5cc1dbf3e72b5ba1419806d88c13b0c0ef9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cdf30c244ab587be07d8aceb096170cdeb28c7e7f6ec5149bae6647f7105faa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupCluster]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdaef67727f0167580336f887651110ef5ef60fadaf84fd91a146d1ae45836e6(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    cluster: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupCluster, typing.Dict[builtins.str, typing.Any]]]]] = None,
    content: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContent, typing.Dict[builtins.str, typing.Any]]]]] = None,
    filters: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFilters, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupPlan, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
    timezone: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupTimezone, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ccecb2865c0d73679ae5cb1a78102c6f596e7586d844a878e4a9bc608f70a9(
    *,
    applications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContentApplications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    labelselectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContentLabelselectors, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__071dc462fc0e3dfb237a2ea13201227330433dac935442aab1d0813d8774b288(
    *,
    guid: builtins.str,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10742edb978014b30549a6554b0b90ee995c4fc48b9158905c62b960066bb633(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec1f8caadfdceb78276e82cdd247e89bdb4c51bab26f44ae4a855a859861b25c(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a4b86840434045b3200d6831bba81281a96bb06f8ad087cceb80659c676679(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b736af98de1d9bdc0ed8246f03e25e2147283a7b697c0f3bd5d7c31cb32ad85(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccc0a1a7e038c0279f6831f1f174c26aa79d20c2c84e9aea2c3aa049bd2f30bf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c300dbe93f9b0c52abc2277e7d24695d05feaebcdc7e6755123365d8fb4067a9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentApplications]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d43b8cae651eab972aff05760278cf4739ad45a7ced8eb412d3424b481b51c56(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9becdc95ed7b49c582958cc6009b6797f00db11dd9ac2890a327ba1bf2bfbaf4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce85ddc60886f99ebf2698a0f536574e84541ad788d7b53d1d1613b34833e1e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba0b99ad30076a08373db86b537073adf7d1f09f40a5b39345e76dbd267c1f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6171a7cf58e0189047d12dbec1edb9ba935d54d3e7060a8b39aba6523aedc9fe(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentApplications]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb16c20d75ac27d6850aa2b1242de7ae227a8487007de261d943a08fff250ed(
    *,
    selectorlevel: builtins.str,
    selectorvalue: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08d34b0a6f5758b335e5dfe492478dc5fd4746943f8d16bf28fe3d93f68de5de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a259c6b2f9f9d3ed5a69a2c2247819aa2ee8ab15755e099a11150c7b7306798f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ba58f4c311b06504b64e5dbf67d1b60755526d8652e1f5a5abff3ef169b90d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f3bdc5502af51cb950872bf6daa7c0613a7ff9af408a83a6ef201fe275fde8(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa4b6a9014398683335efad4140a89b1c37003af32a69fec0203c54f59daf59(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3000c958d18cd6df4dcaf6c76743ca5a83cbc96b508a8a2cbb1479d6eda41153(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContentLabelselectors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a907121ad6be8aef156717e28c8e2d8163894fdce690b1a23fdc04df796ff3a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__321e71b7422f25161851e976e6313e5bdf1d0de338e6f9f6f30f90e9e0cd8aad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8db60f173133de2d80d682d1fd2c91f7aaebd85d971860da6f27c9703bd9d06b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94308ab6bd739a7619d0550623e46dc13666b4e2fc8a88ed1bfd415ba038761c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContentLabelselectors]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6f91d407933bffce7c67e426cdec116acd080837b0edbddf73d20e4a3ff0c79(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6529b432eb9bc84a78e555544864ebd70c14948d72806ad459a2e26f95c7751(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e6562daeccdb4e52ed87dd71446245007cba2692d37d10deb207e140c469f62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70e4316bc329d64a97e3317d6c2961f6bb05f904e91defa537766237c6ea4977(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e8b338de38073aecdfd303e1341774ab86483d8541f755f2223cce26f1bd26(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5fcebf4ded2c4ec2a942672b26928a6a84e1922077214bb89ab3a662585879(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupContent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90bd82d08dc1f058485ff600c91022e359b9216ec655f900aae0ed2426cae322(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b4b3068b2225bf88eb8575aa98953cf99606808a7c58ac75f6f82d442ca142(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContentApplications, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90bf0594c21ca221a770fc1a39335c6ab869796a8f9c25b112258ef40fb480c0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupContentLabelselectors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__331a6e6c502d0972a52274197e8824050c0ee233b84164e7d139d25fc71ca31a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupContent]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3344364fc5deed19a38888224e4afb483e76aec5e6b719a421c51037dc0f537(
    *,
    applications: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFiltersApplications, typing.Dict[builtins.str, typing.Any]]]]] = None,
    labelselectors: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFiltersLabelselectors, typing.Dict[builtins.str, typing.Any]]]]] = None,
    skipstatelessapps: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e34c5c2946a87d6aadd9ce9e86d060b15227fd22090d0ff021331f08dabaaea(
    *,
    guid: builtins.str,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01534c0ea326c1c32288134f384018d5864ee8de9080a32b9c6df7557033439c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138f7de9b2a9b721b61f06c2426386f100957b504ded22aefae6e1a666e66ccc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1124599fed44e868da5544f2ffe0bcaee9a68b8cc70a73f7010514ee2d0d1e7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07a9823dbb1c9c638e44e2596382e41c618ab884a9db15713201d0c989709f0b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6b6c3cee9dac9194c4e591265e6f92af693ae8eb012c63ade2d07fd4240ffad(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fa4a4fdf3efb850d29bdac24224dcfb189d8a1f9e5aed6457bd3aef39dd3a37(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersApplications]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bcb9d18ddf6b3f87aacc6bc533cb0f3f9a1025a30b6e456f35a5ef0d541120f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__728780fde284c3c511739e9552cff549f6bead79440f3aff51912d0b4d80a580(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__409b750bc5e28e085e7821d150863dbe6d5bd6e1caee7df80c4599fa03eccfa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bd97ed6a57bec35d581675973e8b3b18957932b672899f89ccd9e041b386d79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5dbbd78a608a5de55afe5539728b9210463462f60d2a6f0a027350f21a6f2a0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersApplications]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d534d420af60cc01a248e9fa094ff417dfa905fe5ac4dfb0e262e9074329c5f3(
    *,
    selectorlevel: builtins.str,
    selectorvalue: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975717bc1af918bf96823f184eee5931df2f1444812f493366461e5f84c6d1e8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__813ee924615754d0107e1fcc89f2f69aff24fb4e6b904560c0a59d05a21583ba(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8afb25a93c1d24b4c619a293f1a19efe20d8719f63976a396bdfd5942c43587(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb4fa81bb46b8aad2c44e510d2b107a6fa8e2b8d0b97f557b58c321925c0f1c(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c507c0d1957fd459be30dd88a1061ccf4f9504f9ac6c2366b9d637720926bff5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51e202038afbbcd0f2a666b2d260cca3b5b4409cbb11ce3ddefddbd4a3c77939(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFiltersLabelselectors]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fb9009fc02cd893b79e0d2130178a6cbe12c3c0450b93db13bdc1992aaa2902(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076fbe1d6c8ee2fb4ebd09d60238e7744cb60ae181ee75bd4be268c81788e1a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10a55ec16ccbc64244446abaddcb5ab886797d3699e03ef2ab14bb95716e1e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54031cf5641f166ff537f4f0aa4f78938aad85e498b7eb8782b01e9206608095(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFiltersLabelselectors]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f050bde3e2e3c417f6e8e43d06eb09b599e6186c0e33ab09bb78cb6c745efba3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c71cf63a4d12b0b5460c9b93555f349ceb78249c03421e023a29e9a577490b22(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e775389458fe2c198d8f266cd66ab43893bb9024696ccfdb82eb26cbba325803(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622af09e2eb8cf644b671c1e834e507c899fed9fc2bbcc737538269ffca7a974(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42e5a44c274b82352f2f4b02f2c7f61a1c32e722d8757fb7b25e215ce0c3c8c1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f0da0295b89268788f7524dced58fc482ad3b151c7e7669dd2f98c8ad0ae25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupFilters]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__293f28622c149c94d623a095dd22d2afc49eba6813672ae655cfd759ed23378d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c0d56ee9bf7e9dec77bb4c24647d7780615ae623ea6730c3477be36f48351a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFiltersApplications, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca9f7821f5dc92b58608f3e85584c443b0093111b5c815e947bd26ff560558b0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupFiltersLabelselectors, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__969c05feeafb46b68d1ce10bc73325f9cf6bfc75d36e1b899c3aa2713d6913a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92c528df889e2d6bb3075321591cd65a9c5fc35468ac01e2bd4b546be8d4724d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupFilters]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f044735ae2d83c81f938d28ca13347293aa574837695b09cb562757aabd36217(
    *,
    backupstreams: typing.Optional[jsii.Number] = None,
    cvnamespacescheduling: typing.Optional[builtins.str] = None,
    jobstarttime: typing.Optional[jsii.Number] = None,
    snapfallbacktolivevolumebackup: typing.Optional[builtins.str] = None,
    workerresources: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupOptionsWorkerresources, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d5833f565916644b3abe77f91c5dfcbc3e4c446b93880da88eddc933c5cb2d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace512425d19824db1f62c886b723c6862ba6032f4cb3967f7b294a2c3e6d56d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac11c34d9783dfd5071f3093adfa1ded08950eaa05ad4294c7cfac0ed57ba65a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3829b53e8cefbd1c56450d1ca23f234b98923030155ce352a2e24f95895e5acd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a5e355817ebfc874175f94f97542b6f73013e437c2f7a7a2203163114680baf(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb3923d508e6e0890ea2d120e2af570810c3fdf4fce9488e5dac1f1e23e109b2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c78c0ef61d13d19d8dc5f6828dd3bc4a96ae6e36ef9b1829b7cc34cd6f5c23e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a071b78b24e5941acc264f250e696831281a15b5f36152efd38a9bf620539a13(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesAppgroupOptionsWorkerresources, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeef9bb1b50c11e7eefb49463b18a1d846cc63ad1fa0b03fbf62f64b7dc3d614(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf9d853eb2055101b8733a77281b6ba659f0aedc92d589d6df47d5b20b02cda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7764fedcfea0d1a7883b69499682c7a58794e824fd716d20ef150c76edc717f8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35eec9b412e2d95025ebf251542d3df2125681dd56da4f12e9b28b5cc061d761(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3317759bf42c5ced4a2795e551694c73792da2f0891d5bcadeab41f3bfa9f5e0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b531368a5bb0dcbdaf5d3ccd586dc47aeac711f0549c465811e450c26e66773(
    *,
    cpulimits: typing.Optional[builtins.str] = None,
    cpurequests: typing.Optional[builtins.str] = None,
    memorylimits: typing.Optional[builtins.str] = None,
    memoryrequests: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd14aa5c4956065a9bbcec26d6de222e1a18d4d49eee44c41e3104a537e4e199(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e7039d60863a2bfe006ca76d80a91f99276bfc795553d559d4f3630f6f47034(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b398e97967c2c781562f781f4587585b26af825b9e803e6a5bcad7d4ba0c9241(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a24227f1f68e8b34ce3726dc93ae1b9a800745ef46259fdb86d31ea5c6f4f8f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d02928be86883aabf2303e8e490d1b9a9100d5a66f57d20035978802c9ce88f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d1ffdb5869946d3769269ab188ed7ad323b523943c9723cd5bbf3456cc6d9ef(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupOptionsWorkerresources]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f95ff685cd44a888fbd4ca3efa25351f244ee84d94971c8821eacf4b2c8bb62(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef46437a1231afa99fa57df2097c37da279e761b065e03e193ca47b995bada2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1af33256fa0428aea70158664db92bd05708b331fe08a7b82b6f61d59da6a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26730f3de48157d1b527b4aa348bb79f9d49a942b0027cef93b9aaf8462667f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9eedd357bf5ad503ae579f9abd978dff4244c40cb227de45ba58b32f7d06b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89e1b472246f3dfeded285418582af32ebe1ac485c45412854450ec9d300298(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupOptionsWorkerresources]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c080ceefb0f87173615ad210ca15613785082afb2d7ab2fd3216dfbfccf2b9(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95f86aae0b58dba003838a174224b8f37214ebbd3881200f55c46be0bab15c26(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6adecedb27403dd1caf40572bb3f07110970335d33dbedb8171abb122ad1a9bc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a2016db468c0bb6101df5f17a703588349d3c3ac6d891a4d5c6ed7231003251(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9209e0af633dae9096d8c03abfa6647454c7f238c1befe56bba3cfe964ae0d69(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ff39f88df03b8b1eca4d3a5145eb20c7f6400992286b9118466882cd044875(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__498b4df98a4dc28e4d5e910ce56eb8fdcbe762bbfc69669be458ee0de0a41346(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupPlan]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa05b7c1a5176d5175c0c7a66ac97aa76ff35c3728ae65c500e2b4fe78dc6ecb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a2efcc90c0c0342bd26d92988a8b9369006b32ad0c1176390a2c3cc82fcdd6e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54d763436fc746b2a5ba201396bed5a7b62b50036b802bc75a403377c67d0192(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4af414072059151f4884ea8eae2af2020602cf0274776ef20bf17c9840de31(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupPlan]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__185f114adc41a465c4f3a8174a9e5e648dcfb787beb92d6f9d48cc6ec9c80cff(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1537f5f65e94af8fd1b54a7413fdd9355aa4f9d5ebdb3f2b1b201d7b1825c0c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c9ea3a2a7e481e81955308739e8a999121b91bd349d4578dc23a3f41533a290(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320d56a6487c3737967fb6ba196a684d3d562a0d852a81e22eb8ba8f071cec8a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c00fc46b10d228e3b25eec1a5f2662679defdc63091655cfce15e90d8402f0cb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db569c8ea6e38bfd393317ef774093cd253f0f64a3824572ef522f34817ac84b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efffdb3a8ba8464735abcb18bb9efbc7027629e8938cfa58b0df6cd2894054cb(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c39b1ea023e5b91766d2324c3c3678f7ff255bae3fdc95395ff77187ec7747b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53d4b0117bbd3785e33c3171fe4d88b4613f49874241bff0bd70f2c0f22ca92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30dd3a96f7d39176c6bb88f90a2e194ff14fff3b7d0a96a30ce10fceb67017a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d7453f63263aa23f821f780a378c9612fa0e4a266b208492e2521cbe0519c10(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTags]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad6d8abef1b66db36b1d2d98d76dd3c6c0f18e50b28c8d37411970e529666b0(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41847f7fec9e7001199f1451853a4cc090caef28f9be2c8c0eb0747e96c1786(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d9fe519289f88435d626792b6966884eea782d3c4d69e9d81ad9f66fecc072(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9680813f3ab6e7e3e4817b9454066852d7538062eb1ccfaedd6a104bb02fcbef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a0dd53732d73b8f81973271326fee183864a81ef67e63f1c70eda72fb27fdff(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfac9fd0a3f8564cc8eb15b37b5a649d76ac2016acef53a9ae8b34d44c104575(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b05063e8ef3b1508d4ea60663c4313e471aa7a852fc0cdcb89c07c8d6b09bfa(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesAppgroupTimezone]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a937c2008e4bb440da13fec8780f36828a61983f9174e914792c259eec8c419(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e69b3e130b1263155bfb1f4bd24539248ea182ee4e62a13778fe7515e506d0dd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536c88bc44d634fde6b311ec25f6d5ff8932752138fb23d9c09db2c9874a12b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5b8efa31ba2188fb62192232cb23b3d112b6c5ec9fe7715c387d88de5e4a68(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesAppgroupTimezone]],
) -> None:
    """Type checking stubs"""
    pass
