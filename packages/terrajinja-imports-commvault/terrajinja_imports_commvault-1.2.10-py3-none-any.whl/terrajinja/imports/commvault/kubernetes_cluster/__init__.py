'''
# `commvault_kubernetes_cluster`

Refer to the Terraform Registry for docs: [`commvault_kubernetes_cluster`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster).
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


class KubernetesCluster(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesCluster",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster commvault_kubernetes_cluster}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterAccessnodes", typing.Dict[builtins.str, typing.Any]]]]] = None,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterActivitycontrol", typing.Dict[builtins.str, typing.Any]]]]] = None,
        apiserver: typing.Optional[builtins.str] = None,
        etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterEtcdprotection", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterRegion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        serviceaccount: typing.Optional[builtins.str] = None,
        servicetoken: typing.Optional[builtins.str] = None,
        servicetype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster commvault_kubernetes_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param accessnodes: accessnodes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#accessnodes KubernetesCluster#accessnodes}
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#activitycontrol KubernetesCluster#activitycontrol}
        :param apiserver: API Server Endpoint of the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#apiserver KubernetesCluster#apiserver}
        :param etcdprotection: etcdprotection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#etcdprotection KubernetesCluster#etcdprotection}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Name of the Kubernetes Cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#options KubernetesCluster#options}
        :param region: region block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#region KubernetesCluster#region}
        :param serviceaccount: Name of the Service Account to authenticate with the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#serviceaccount KubernetesCluster#serviceaccount}
        :param servicetoken: Secret token to authenticate with the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#servicetoken KubernetesCluster#servicetoken}
        :param servicetype: The Service Type of the Kubernetes cluster [ONPREM, AKS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#servicetype KubernetesCluster#servicetype}
        :param tags: tags block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17cb1c80c475e6e7bc8bf99cd39cf975884c7cf42a1db2d6da4c1de13fbf2a31)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KubernetesClusterConfig(
            accessnodes=accessnodes,
            activitycontrol=activitycontrol,
            apiserver=apiserver,
            etcdprotection=etcdprotection,
            id=id,
            name=name,
            options=options,
            region=region,
            serviceaccount=serviceaccount,
            servicetoken=servicetoken,
            servicetype=servicetype,
            tags=tags,
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
        '''Generates CDKTF code for importing a KubernetesCluster resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the KubernetesCluster to import.
        :param import_from_id: The id of the existing KubernetesCluster that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the KubernetesCluster to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__311f5f9c70858b93b154d1bfa9e6e87cca1b53f76bd2280f3aaca04566c7ef0f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAccessnodes")
    def put_accessnodes(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterAccessnodes", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__856699ce4045a14a2777f72ff87fceec8b841eafebc844fcb3c15dcf61f0147a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessnodes", [value]))

    @jsii.member(jsii_name="putActivitycontrol")
    def put_activitycontrol(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterActivitycontrol", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355d1e63d9a4ca873d0d24b0461b1e1595d66877481ec189399d06844f9eb7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putActivitycontrol", [value]))

    @jsii.member(jsii_name="putEtcdprotection")
    def put_etcdprotection(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterEtcdprotection", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d60805ec53478ce887a478485d01a11ce6ec00a23e0fa604af538fed1a8facd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEtcdprotection", [value]))

    @jsii.member(jsii_name="putOptions")
    def put_options(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterOptions", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf7ea84c530b6ebd477e92dfdb2ddcdd8ed2ca0ea7e1e4e93ca518d2f4395a58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOptions", [value]))

    @jsii.member(jsii_name="putRegion")
    def put_region(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterRegion", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7b783af2f70b9ab69a81eee7501652a7e212ca0c1a19b1e72f5af4b4bef12c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegion", [value]))

    @jsii.member(jsii_name="putTags")
    def put_tags(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterTags", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__474a217a2a6b960fe68efaec8d274d8b7c695cf21da5ad11cbace46943ecb9e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTags", [value]))

    @jsii.member(jsii_name="resetAccessnodes")
    def reset_accessnodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessnodes", []))

    @jsii.member(jsii_name="resetActivitycontrol")
    def reset_activitycontrol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetActivitycontrol", []))

    @jsii.member(jsii_name="resetApiserver")
    def reset_apiserver(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiserver", []))

    @jsii.member(jsii_name="resetEtcdprotection")
    def reset_etcdprotection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEtcdprotection", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetServiceaccount")
    def reset_serviceaccount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceaccount", []))

    @jsii.member(jsii_name="resetServicetoken")
    def reset_servicetoken(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicetoken", []))

    @jsii.member(jsii_name="resetServicetype")
    def reset_servicetype(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicetype", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    def accessnodes(self) -> "KubernetesClusterAccessnodesList":
        return typing.cast("KubernetesClusterAccessnodesList", jsii.get(self, "accessnodes"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrol")
    def activitycontrol(self) -> "KubernetesClusterActivitycontrolList":
        return typing.cast("KubernetesClusterActivitycontrolList", jsii.get(self, "activitycontrol"))

    @builtins.property
    @jsii.member(jsii_name="etcdprotection")
    def etcdprotection(self) -> "KubernetesClusterEtcdprotectionList":
        return typing.cast("KubernetesClusterEtcdprotectionList", jsii.get(self, "etcdprotection"))

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> "KubernetesClusterOptionsList":
        return typing.cast("KubernetesClusterOptionsList", jsii.get(self, "options"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> "KubernetesClusterRegionList":
        return typing.cast("KubernetesClusterRegionList", jsii.get(self, "region"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "KubernetesClusterTagsList":
        return typing.cast("KubernetesClusterTagsList", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="accessnodesInput")
    def accessnodes_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterAccessnodes"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterAccessnodes"]]], jsii.get(self, "accessnodesInput"))

    @builtins.property
    @jsii.member(jsii_name="activitycontrolInput")
    def activitycontrol_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterActivitycontrol"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterActivitycontrol"]]], jsii.get(self, "activitycontrolInput"))

    @builtins.property
    @jsii.member(jsii_name="apiserverInput")
    def apiserver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiserverInput"))

    @builtins.property
    @jsii.member(jsii_name="etcdprotectionInput")
    def etcdprotection_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotection"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotection"]]], jsii.get(self, "etcdprotectionInput"))

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
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterOptions"]]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterRegion"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterRegion"]]], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceaccountInput")
    def serviceaccount_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceaccountInput"))

    @builtins.property
    @jsii.member(jsii_name="servicetokenInput")
    def servicetoken_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicetokenInput"))

    @builtins.property
    @jsii.member(jsii_name="servicetypeInput")
    def servicetype_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicetypeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterTags"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterTags"]]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiserver")
    def apiserver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiserver"))

    @apiserver.setter
    def apiserver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d30b7b43026a7b5aec3af9db6a53f4def18f652ecdd74568dca751afd5d985d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiserver", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d9db187b552c39082b97467c47f7a792b9f5b7e862ba79a5a48ba8a27255447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fa7f4791fdf7d4d574641a122a78d44c5cf2d13b68575de496d91bdda0673e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="serviceaccount")
    def serviceaccount(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceaccount"))

    @serviceaccount.setter
    def serviceaccount(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd4e83efd6094bf89a5b54c881032f5ba5a9c9f109931adf8007f8f6ec2180a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceaccount", value)

    @builtins.property
    @jsii.member(jsii_name="servicetoken")
    def servicetoken(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicetoken"))

    @servicetoken.setter
    def servicetoken(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a86aec8c134acc1a5bedcb50bd92478ea7e18718711b9c537bdd6f522eea1fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicetoken", value)

    @builtins.property
    @jsii.member(jsii_name="servicetype")
    def servicetype(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicetype"))

    @servicetype.setter
    def servicetype(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bad11ff336f7f1c51a7ce7c53e5f6572f994b6ae51af1fec4bbfca697c786c9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicetype", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterAccessnodes",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "type": "type"},
)
class KubernetesClusterAccessnodes:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#type KubernetesCluster#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b9ab6e76632d4788d34f07af6db65661ea5ace18a16f8531097008d00feedc)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#type KubernetesCluster#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterAccessnodes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterAccessnodesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterAccessnodesList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0cb21fa2753346384db112381cb8413e619b15db543b9279368acbeb48f43588)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesClusterAccessnodesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d725dddbf7008233ca2f7a53e49f9b427e87af14b551a9e804dc1edf535b20)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterAccessnodesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35dea32ad677836ed7383f2c073eddbd5cf1e71f54aab84a0650031aa10a42b6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__67be32dcde77a72eadd82cd748638b5dc220e33e98ef9719ec5513dabfdff411)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d7c0317d2873d87fa00745d955ac83e1a495f28faa3058263f374f4e6c52a23f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterAccessnodes]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterAccessnodes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterAccessnodes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6e01bea844b0522ca593eb509fb4d03f6719cb2ab4b5007cc990607ad6dbe1e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterAccessnodesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterAccessnodesOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__98acd42155592411ac98792a9f3cf45d43766c5800735e242dfe2ee60bcb5195)
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
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @id.setter
    def id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6b8b667e7b66796183ac1ea8f13a73346b8b409898939b5a1744f4348df9507)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a54f60669b402a88dde230c9838cc571cb69e6c2c03fcc797a8217a1e474330)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterAccessnodes]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterAccessnodes]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterAccessnodes]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce4bba16e73ec6a51454bf2f73d5f494925d71a307f2adaad46dbacbb9943739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterActivitycontrol",
    jsii_struct_bases=[],
    name_mapping={
        "enablebackup": "enablebackup",
        "enablebackupafteradelay": "enablebackupafteradelay",
        "enablerestore": "enablerestore",
        "enablerestoreafteradelay": "enablerestoreafteradelay",
    },
)
class KubernetesClusterActivitycontrol:
    def __init__(
        self,
        *,
        enablebackup: typing.Optional[builtins.str] = None,
        enablebackupafteradelay: typing.Optional[jsii.Number] = None,
        enablerestore: typing.Optional[builtins.str] = None,
        enablerestoreafteradelay: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param enablebackup: Enable or disable backup for cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablebackup KubernetesCluster#enablebackup}
        :param enablebackupafteradelay: Enabling backup after a delay. Provide UTC Time in Unix format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablebackupafteradelay KubernetesCluster#enablebackupafteradelay}
        :param enablerestore: Enable or disable restore for cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablerestore KubernetesCluster#enablerestore}
        :param enablerestoreafteradelay: Enabling restore after a delay. Provide UTC Time in Unix format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablerestoreafteradelay KubernetesCluster#enablerestoreafteradelay}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8f3900158f58566012c7a1ae5a4ce94db7ef5c47517ce5ca0c80a72aef06e67)
            check_type(argname="argument enablebackup", value=enablebackup, expected_type=type_hints["enablebackup"])
            check_type(argname="argument enablebackupafteradelay", value=enablebackupafteradelay, expected_type=type_hints["enablebackupafteradelay"])
            check_type(argname="argument enablerestore", value=enablerestore, expected_type=type_hints["enablerestore"])
            check_type(argname="argument enablerestoreafteradelay", value=enablerestoreafteradelay, expected_type=type_hints["enablerestoreafteradelay"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enablebackup is not None:
            self._values["enablebackup"] = enablebackup
        if enablebackupafteradelay is not None:
            self._values["enablebackupafteradelay"] = enablebackupafteradelay
        if enablerestore is not None:
            self._values["enablerestore"] = enablerestore
        if enablerestoreafteradelay is not None:
            self._values["enablerestoreafteradelay"] = enablerestoreafteradelay

    @builtins.property
    def enablebackup(self) -> typing.Optional[builtins.str]:
        '''Enable or disable backup for cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablebackup KubernetesCluster#enablebackup}
        '''
        result = self._values.get("enablebackup")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enablebackupafteradelay(self) -> typing.Optional[jsii.Number]:
        '''Enabling backup after a delay. Provide UTC Time in Unix format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablebackupafteradelay KubernetesCluster#enablebackupafteradelay}
        '''
        result = self._values.get("enablebackupafteradelay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enablerestore(self) -> typing.Optional[builtins.str]:
        '''Enable or disable restore for cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablerestore KubernetesCluster#enablerestore}
        '''
        result = self._values.get("enablerestore")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enablerestoreafteradelay(self) -> typing.Optional[jsii.Number]:
        '''Enabling restore after a delay. Provide UTC Time in Unix format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enablerestoreafteradelay KubernetesCluster#enablerestoreafteradelay}
        '''
        result = self._values.get("enablerestoreafteradelay")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterActivitycontrol(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterActivitycontrolList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterActivitycontrolList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__415527d830c504a43f527d29e25a63c98085dc80da6d8e9a0827b4fbef592099)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterActivitycontrolOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52beafd2d0634a7459db44d1943bad22ffd37f46c337406c4906f69e97b85d7f)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterActivitycontrolOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fa233ac46138d61c356e222b0699d721288870c1b6145212b259c176a515d36)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5c68aa2f81aeb16902ac52bfd11bf5fb64ef4f06e626783ada4dfddd18c7a928)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bc20f054e784cb511a4da96d868df8b31adf156e01aeff1e35705faaf31cb72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterActivitycontrol]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterActivitycontrol]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterActivitycontrol]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2931fb64023c0d726125d2c9eeccc60d311adb9dc32791a27603a57cb2549a9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterActivitycontrolOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterActivitycontrolOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__5cd57a8cc23fa70dfbd1c2812e6327ef896c8dda24d95fcfee2c808d01187b73)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnablebackup")
    def reset_enablebackup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablebackup", []))

    @jsii.member(jsii_name="resetEnablebackupafteradelay")
    def reset_enablebackupafteradelay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablebackupafteradelay", []))

    @jsii.member(jsii_name="resetEnablerestore")
    def reset_enablerestore(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablerestore", []))

    @jsii.member(jsii_name="resetEnablerestoreafteradelay")
    def reset_enablerestoreafteradelay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnablerestoreafteradelay", []))

    @builtins.property
    @jsii.member(jsii_name="enablebackupafteradelayInput")
    def enablebackupafteradelay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enablebackupafteradelayInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackupInput")
    def enablebackup_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablebackupInput"))

    @builtins.property
    @jsii.member(jsii_name="enablerestoreafteradelayInput")
    def enablerestoreafteradelay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "enablerestoreafteradelayInput"))

    @builtins.property
    @jsii.member(jsii_name="enablerestoreInput")
    def enablerestore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enablerestoreInput"))

    @builtins.property
    @jsii.member(jsii_name="enablebackup")
    def enablebackup(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablebackup"))

    @enablebackup.setter
    def enablebackup(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d262de690260d9f2990fe21bec8fb07b8807845e3e3b19efeade589494f3c66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackup", value)

    @builtins.property
    @jsii.member(jsii_name="enablebackupafteradelay")
    def enablebackupafteradelay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enablebackupafteradelay"))

    @enablebackupafteradelay.setter
    def enablebackupafteradelay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25e6bf721b62ff11040fd41347f93242774f94b6312d261ce461b8ffa4c61bd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablebackupafteradelay", value)

    @builtins.property
    @jsii.member(jsii_name="enablerestore")
    def enablerestore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enablerestore"))

    @enablerestore.setter
    def enablerestore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd1da442f56e809b67f5cff905dbe9b181cfbca90c322391203051e5712d721)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablerestore", value)

    @builtins.property
    @jsii.member(jsii_name="enablerestoreafteradelay")
    def enablerestoreafteradelay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "enablerestoreafteradelay"))

    @enablerestoreafteradelay.setter
    def enablerestoreafteradelay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ebdddb64e3eff485e7ed880069b02d2b4c021416ba5981316c5c8304c6d1983)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enablerestoreafteradelay", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterActivitycontrol]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterActivitycontrol]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterActivitycontrol]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c62bc322a262523e1eef4b6a5970dffba5387f4f25e725439a871aaf43c768c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "accessnodes": "accessnodes",
        "activitycontrol": "activitycontrol",
        "apiserver": "apiserver",
        "etcdprotection": "etcdprotection",
        "id": "id",
        "name": "name",
        "options": "options",
        "region": "region",
        "serviceaccount": "serviceaccount",
        "servicetoken": "servicetoken",
        "servicetype": "servicetype",
        "tags": "tags",
    },
)
class KubernetesClusterConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
        activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
        apiserver: typing.Optional[builtins.str] = None,
        etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterEtcdprotection", typing.Dict[builtins.str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterOptions", typing.Dict[builtins.str, typing.Any]]]]] = None,
        region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterRegion", typing.Dict[builtins.str, typing.Any]]]]] = None,
        serviceaccount: typing.Optional[builtins.str] = None,
        servicetoken: typing.Optional[builtins.str] = None,
        servicetype: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterTags", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param accessnodes: accessnodes block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#accessnodes KubernetesCluster#accessnodes}
        :param activitycontrol: activitycontrol block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#activitycontrol KubernetesCluster#activitycontrol}
        :param apiserver: API Server Endpoint of the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#apiserver KubernetesCluster#apiserver}
        :param etcdprotection: etcdprotection block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#etcdprotection KubernetesCluster#etcdprotection}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Name of the Kubernetes Cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}
        :param options: options block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#options KubernetesCluster#options}
        :param region: region block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#region KubernetesCluster#region}
        :param serviceaccount: Name of the Service Account to authenticate with the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#serviceaccount KubernetesCluster#serviceaccount}
        :param servicetoken: Secret token to authenticate with the cluster. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#servicetoken KubernetesCluster#servicetoken}
        :param servicetype: The Service Type of the Kubernetes cluster [ONPREM, AKS]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#servicetype KubernetesCluster#servicetype}
        :param tags: tags block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d1b0bee98ecec17fd74c059eecdd73143fb72f20a9ca82103df82d5496c8181)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument accessnodes", value=accessnodes, expected_type=type_hints["accessnodes"])
            check_type(argname="argument activitycontrol", value=activitycontrol, expected_type=type_hints["activitycontrol"])
            check_type(argname="argument apiserver", value=apiserver, expected_type=type_hints["apiserver"])
            check_type(argname="argument etcdprotection", value=etcdprotection, expected_type=type_hints["etcdprotection"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument serviceaccount", value=serviceaccount, expected_type=type_hints["serviceaccount"])
            check_type(argname="argument servicetoken", value=servicetoken, expected_type=type_hints["servicetoken"])
            check_type(argname="argument servicetype", value=servicetype, expected_type=type_hints["servicetype"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
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
        if accessnodes is not None:
            self._values["accessnodes"] = accessnodes
        if activitycontrol is not None:
            self._values["activitycontrol"] = activitycontrol
        if apiserver is not None:
            self._values["apiserver"] = apiserver
        if etcdprotection is not None:
            self._values["etcdprotection"] = etcdprotection
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if options is not None:
            self._values["options"] = options
        if region is not None:
            self._values["region"] = region
        if serviceaccount is not None:
            self._values["serviceaccount"] = serviceaccount
        if servicetoken is not None:
            self._values["servicetoken"] = servicetoken
        if servicetype is not None:
            self._values["servicetype"] = servicetype
        if tags is not None:
            self._values["tags"] = tags

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
    def accessnodes(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterAccessnodes]]]:
        '''accessnodes block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#accessnodes KubernetesCluster#accessnodes}
        '''
        result = self._values.get("accessnodes")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterAccessnodes]]], result)

    @builtins.property
    def activitycontrol(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterActivitycontrol]]]:
        '''activitycontrol block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#activitycontrol KubernetesCluster#activitycontrol}
        '''
        result = self._values.get("activitycontrol")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterActivitycontrol]]], result)

    @builtins.property
    def apiserver(self) -> typing.Optional[builtins.str]:
        '''API Server Endpoint of the cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#apiserver KubernetesCluster#apiserver}
        '''
        result = self._values.get("apiserver")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def etcdprotection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotection"]]]:
        '''etcdprotection block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#etcdprotection KubernetesCluster#etcdprotection}
        '''
        result = self._values.get("etcdprotection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotection"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the Kubernetes Cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterOptions"]]]:
        '''options block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#options KubernetesCluster#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterOptions"]]], result)

    @builtins.property
    def region(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterRegion"]]]:
        '''region block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#region KubernetesCluster#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterRegion"]]], result)

    @builtins.property
    def serviceaccount(self) -> typing.Optional[builtins.str]:
        '''Name of the Service Account to authenticate with the cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#serviceaccount KubernetesCluster#serviceaccount}
        '''
        result = self._values.get("serviceaccount")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servicetoken(self) -> typing.Optional[builtins.str]:
        '''Secret token to authenticate with the cluster.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#servicetoken KubernetesCluster#servicetoken}
        '''
        result = self._values.get("servicetoken")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def servicetype(self) -> typing.Optional[builtins.str]:
        '''The Service Type of the Kubernetes cluster [ONPREM, AKS].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#servicetype KubernetesCluster#servicetype}
        '''
        result = self._values.get("servicetype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterTags"]]]:
        '''tags block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#tags KubernetesCluster#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterTags"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterEtcdprotection",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled", "plan": "plan"},
)
class KubernetesClusterEtcdprotection:
    def __init__(
        self,
        *,
        enabled: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterEtcdprotectionPlan", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param enabled: Denote if etcd protection is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enabled KubernetesCluster#enabled}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#plan KubernetesCluster#plan}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__152ef28cfeb821719014e006fb7cbdb080d12b8750869276f71de6c85c184b7d)
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

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#enabled KubernetesCluster#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotectionPlan"]]]:
        '''plan block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#plan KubernetesCluster#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotectionPlan"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterEtcdprotection(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterEtcdprotectionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterEtcdprotectionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__263ef028bfb24eee4cf1ad5a9dea8d8a37b6dca924b6b515cce3e726f1d03fab)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterEtcdprotectionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7beffdad28da705d0f71aefcddd493d87c0350b23705733b741450c1d44c9965)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterEtcdprotectionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228060e2406262f91ababdeecba713835cb26874dd5d5fb6225e103b97d0df8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ac391be550affe4bdd532f8bc6d862c4db1e3653fdcb48a961b80097aac3e7f9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3b5ff9c3c6937dfcdc41ae071cf57b55618ba5098659ee0e14b9b479c9a80861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotection]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotection]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotection]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b46a85a2d63ae58bf63c8b5216a017152b84158585282dcd5979e9c3f0ac095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterEtcdprotectionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterEtcdprotectionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0c067fadf3daa94bc87fdf0c61c8d5774dc9a38795c8136e96a3c4b1cc9c7baf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterEtcdprotectionPlan", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88ac5976ca93ca70f08ae15d941c6716125cc84584e9e2c9f8854cbae8b9128d)
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
    def plan(self) -> "KubernetesClusterEtcdprotectionPlanList":
        return typing.cast("KubernetesClusterEtcdprotectionPlanList", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotectionPlan"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterEtcdprotectionPlan"]]], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69ea5c73769f5ad7d3d05802c03b6f4862d0c3779eddba349b87152f11930fcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotection]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotection]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotection]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5589ba56203eb82d762b5019117cf80eecd637b213cd1eabffee368fccc92c7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterEtcdprotectionPlan",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class KubernetesClusterEtcdprotectionPlan:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3796ad5554710946a67fbf3bb15bbd62f6ee055f1d6ac6a22fc9aade52f0a6a9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterEtcdprotectionPlan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterEtcdprotectionPlanList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterEtcdprotectionPlanList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c879702fb33ef6dd0884028c86c0724f4a20a83b9e4e69c7dd55bbad237183de)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterEtcdprotectionPlanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__019da69f427bee7e2a6362705c44b6812b27decd5d2ab89170a4a2efaeeaec8b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterEtcdprotectionPlanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__456ba874fb4f262a4255ec0cf15571bfe35f2de14075ae336ad9470b65b92d72)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cfff0f48eeff86822f438ca7edffa8b6ec131e4b32db47bc0c9db07566dbc120)
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
            type_hints = typing.get_type_hints(_typecheckingstub__300cde92261c44e98a864b993943576c1eb6c912c4b1676f11e0ffb9fd9de423)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotectionPlan]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotectionPlan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotectionPlan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c02d22a9d4ea7f7456a0279b70e9a10fd8fb1342b68eb6fe46e96bf9508db77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterEtcdprotectionPlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterEtcdprotectionPlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__354a95d0956ddcd902e2b10e175a1ac37b4ff1a51877f4b519eea60e758abe24)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d78d169eecbc320411888ccfbb9a9f1b5bb985fb73e514a4cf634e1f07a98119)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa11c6fc30e58c5e1c53c52cb5071597cccb50438973c07774434f67e6d0a21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotectionPlan]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotectionPlan]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotectionPlan]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a741beaa7fa21413ce9229c64c59f4c5eee8f25e721a7fccdd658db8ac08ee89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterOptions",
    jsii_struct_bases=[],
    name_mapping={"imageregistry": "imageregistry"},
)
class KubernetesClusterOptions:
    def __init__(
        self,
        *,
        imageregistry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["KubernetesClusterOptionsImageregistry", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param imageregistry: imageregistry block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#imageregistry KubernetesCluster#imageregistry}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24d0be4f341a62097f8cf02601f6d217c92cf00674012719569c88daa8e1490c)
            check_type(argname="argument imageregistry", value=imageregistry, expected_type=type_hints["imageregistry"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if imageregistry is not None:
            self._values["imageregistry"] = imageregistry

    @builtins.property
    def imageregistry(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterOptionsImageregistry"]]]:
        '''imageregistry block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#imageregistry KubernetesCluster#imageregistry}
        '''
        result = self._values.get("imageregistry")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["KubernetesClusterOptionsImageregistry"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterOptionsImageregistry",
    jsii_struct_bases=[],
    name_mapping={"imagepullsecret": "imagepullsecret", "registryurl": "registryurl"},
)
class KubernetesClusterOptionsImageregistry:
    def __init__(
        self,
        *,
        imagepullsecret: typing.Optional[builtins.str] = None,
        registryurl: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param imagepullsecret: Specify image pull secret to authenticate with the image repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#imagepullsecret KubernetesCluster#imagepullsecret}
        :param registryurl: Specify image registry URL for internal image repository. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#registryurl KubernetesCluster#registryurl}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3dc8d1fc5ae4a08758a65233c558473a7ca8392299512ee325d2e808348b39e)
            check_type(argname="argument imagepullsecret", value=imagepullsecret, expected_type=type_hints["imagepullsecret"])
            check_type(argname="argument registryurl", value=registryurl, expected_type=type_hints["registryurl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if imagepullsecret is not None:
            self._values["imagepullsecret"] = imagepullsecret
        if registryurl is not None:
            self._values["registryurl"] = registryurl

    @builtins.property
    def imagepullsecret(self) -> typing.Optional[builtins.str]:
        '''Specify image pull secret to authenticate with the image repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#imagepullsecret KubernetesCluster#imagepullsecret}
        '''
        result = self._values.get("imagepullsecret")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registryurl(self) -> typing.Optional[builtins.str]:
        '''Specify image registry URL for internal image repository.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#registryurl KubernetesCluster#registryurl}
        '''
        result = self._values.get("registryurl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterOptionsImageregistry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterOptionsImageregistryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterOptionsImageregistryList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__11b5693237cd05527565d1998d665cb838f7432c34734f07e57410291545ef5b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "KubernetesClusterOptionsImageregistryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fc5688e14b3e42c4d29b80ef52014058cd975392a3f62ce1872c2002494eb6b)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterOptionsImageregistryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__589b6759ddf7d16a623bfa4a970c78775f4700d3c191a778e9002da4fe554580)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77075da1166b72cc9bdbb248a8854e2fdc6cf922ffdf4c2ddd857a67710aa28e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__59e086f083b992727ae157d6a6b2b30bc2aa79ef230a13c2a25fa88231cc93f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptionsImageregistry]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptionsImageregistry]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptionsImageregistry]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f63c25809ad79a479d23ec807f0a6bb558cea1d68069a22f198334786913852b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterOptionsImageregistryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterOptionsImageregistryOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a5cf336669d79eaeafcca8defcb5b41ab279f5a43b2ef75c47716c02be37e4e9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImagepullsecret")
    def reset_imagepullsecret(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImagepullsecret", []))

    @jsii.member(jsii_name="resetRegistryurl")
    def reset_registryurl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryurl", []))

    @builtins.property
    @jsii.member(jsii_name="imagepullsecretInput")
    def imagepullsecret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imagepullsecretInput"))

    @builtins.property
    @jsii.member(jsii_name="registryurlInput")
    def registryurl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryurlInput"))

    @builtins.property
    @jsii.member(jsii_name="imagepullsecret")
    def imagepullsecret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imagepullsecret"))

    @imagepullsecret.setter
    def imagepullsecret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd019a6cd63303906f244a7b09939a26e5863ef12c680c4125c8e1b90d8916d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imagepullsecret", value)

    @builtins.property
    @jsii.member(jsii_name="registryurl")
    def registryurl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryurl"))

    @registryurl.setter
    def registryurl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9efc3e78236ee11809c1060f09daa6fa34f892bc37f9ff5cec88632ab8762afb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryurl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptionsImageregistry]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptionsImageregistry]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptionsImageregistry]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68108763b5d9d4e220fa1e7508063ce403c503e2cdf80001c70c849e1c20543a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterOptionsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterOptionsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7274d2cffbd5b95569bcfc0a4bacd29ea710ed4e88c6fe57726c982d596f9576)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesClusterOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3359de6f1b0d010508367ce0a04cabc200f7a2f4f31cfda6f2d78a9cf594b555)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f8c346896aa96e649d39874f691dd3f889d314fa89647e33e3d155a8e77adb8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__92764dafc48c4e4fddac60aa9e93cadd5c3bc906fe2d8a9c81977c28c26c2bb6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91d3736e01b3916702107ee34e9e20a719ba1b7f1c4a202c085810f6ebba3ed7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptions]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c57b870776829c29c5659bf72bf3b57dac6db4a045d24fd0e29f801bb24c059)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterOptionsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterOptionsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__7992214d9a786196c0275d79a43f7d51a83e90689dcb8ea1edc222fd2bc1da2d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putImageregistry")
    def put_imageregistry(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterOptionsImageregistry, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13994500a6022755eb470d400cb7a2e7543a8a6ccb728cd9c41cf810e1701bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putImageregistry", [value]))

    @jsii.member(jsii_name="resetImageregistry")
    def reset_imageregistry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageregistry", []))

    @builtins.property
    @jsii.member(jsii_name="imageregistry")
    def imageregistry(self) -> KubernetesClusterOptionsImageregistryList:
        return typing.cast(KubernetesClusterOptionsImageregistryList, jsii.get(self, "imageregistry"))

    @builtins.property
    @jsii.member(jsii_name="imageregistryInput")
    def imageregistry_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptionsImageregistry]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptionsImageregistry]]], jsii.get(self, "imageregistryInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptions]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptions]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptions]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad36a379043454ff175159c4ebf5283b1340681b0257c55a0547beb352fc86cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterRegion",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class KubernetesClusterRegion:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fcc6956700856f02b74495e74296705f5fbd29a6d56bb613ede477ce04e1493)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#id KubernetesCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterRegion(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterRegionList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterRegionList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f7bbbd05ac909cf282295c229ae5079402c6b21b91b147f2a5996260004f79d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesClusterRegionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd5b88d76dd30feacac5a871b49a69652ed40f3b5cbac6eaaf5e2cc25556eff0)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterRegionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9edc55580b131cd7ba6f1ca8f325a2bb17dfabb37c4f9db90228786524deb84a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffa23f8aee8c17dd70882dc84d84ff796cb06f4de301445b5e4b752038f2a2fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dfa68c853884e2088f6bebdbc0fd1666e23df6ba037e36459ab7212c988daac9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterRegion]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterRegion]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterRegion]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6acf9c07c26b6f890b6cdb433619c98b84a604a6157faaa3ae683ac4f46671c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterRegionOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterRegionOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c83b99fb231d196b141054aba0dfcfe964be156c65c3cab65500fbb74eea5784)
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
            type_hints = typing.get_type_hints(_typecheckingstub__aed0e4a1a79614e38ead2b852dad7414eeb3c88b0e97c6f8962258f0ca42fa13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e675cd408219495f7d5fd0d4e250a6dc911b355f2b52f178a00c6eb5a942bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterRegion]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterRegion]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterRegion]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f9c59c5fe0f177f6523618b9815d1417a4a2313621e472c55666fb1ecaab67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.kubernetesCluster.KubernetesClusterTags",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class KubernetesClusterTags:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.
        :param value: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#value KubernetesCluster#value}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__777ccdd75f7280699814caac681fdfad9770b7556b60d37b97a60e281c4c3d2f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#name KubernetesCluster#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/kubernetes_cluster#value KubernetesCluster#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesClusterTags(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class KubernetesClusterTagsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterTagsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1049a656ad55717699041ab3567a173d43c6e36bdb289a74f843adb7815c5783)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "KubernetesClusterTagsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__078ef0d93547179c8ddf240260108ec2d35f8b98f314fbbe969d3e11038555f6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("KubernetesClusterTagsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3de07e3026a49748bb73465e3705ee7c42b479e2296e90b5c8b49f2c5707dc4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9680c37cd9a05b094d1cce047895ff0f890190762715f4fbff58e1fbc9820049)
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
            type_hints = typing.get_type_hints(_typecheckingstub__31d140f02d336d2d660849e20816e12d2f14a5b84be43c0849b7ed9448e049e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterTags]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterTags]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterTags]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7058417d8318409271e6efc74e0176f7548ed316e121780ff24b95b18f63e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class KubernetesClusterTagsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.kubernetesCluster.KubernetesClusterTagsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2d0a52fdcb5aa6e5b5fee2319d4d6b1f29e77a338083749cfc46a89ebc4bbd3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90dc43a6aad191fef848359ca677b40ec139def6bb621e5700d5be071d17d37f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598de56fff4716cb42a093d46b84cf45e0b38e575f3593a87d21d278822e2ea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTags]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTags]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTags]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7dff3ad2e1049157840f6f42a3c15578a97b15db8946a786537da4bdfc8f60bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "KubernetesCluster",
    "KubernetesClusterAccessnodes",
    "KubernetesClusterAccessnodesList",
    "KubernetesClusterAccessnodesOutputReference",
    "KubernetesClusterActivitycontrol",
    "KubernetesClusterActivitycontrolList",
    "KubernetesClusterActivitycontrolOutputReference",
    "KubernetesClusterConfig",
    "KubernetesClusterEtcdprotection",
    "KubernetesClusterEtcdprotectionList",
    "KubernetesClusterEtcdprotectionOutputReference",
    "KubernetesClusterEtcdprotectionPlan",
    "KubernetesClusterEtcdprotectionPlanList",
    "KubernetesClusterEtcdprotectionPlanOutputReference",
    "KubernetesClusterOptions",
    "KubernetesClusterOptionsImageregistry",
    "KubernetesClusterOptionsImageregistryList",
    "KubernetesClusterOptionsImageregistryOutputReference",
    "KubernetesClusterOptionsList",
    "KubernetesClusterOptionsOutputReference",
    "KubernetesClusterRegion",
    "KubernetesClusterRegionList",
    "KubernetesClusterRegionOutputReference",
    "KubernetesClusterTags",
    "KubernetesClusterTagsList",
    "KubernetesClusterTagsOutputReference",
]

publication.publish()

def _typecheckingstub__17cb1c80c475e6e7bc8bf99cd39cf975884c7cf42a1db2d6da4c1de13fbf2a31(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    apiserver: typing.Optional[builtins.str] = None,
    etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterEtcdprotection, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterRegion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    serviceaccount: typing.Optional[builtins.str] = None,
    servicetoken: typing.Optional[builtins.str] = None,
    servicetype: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
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

def _typecheckingstub__311f5f9c70858b93b154d1bfa9e6e87cca1b53f76bd2280f3aaca04566c7ef0f(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__856699ce4045a14a2777f72ff87fceec8b841eafebc844fcb3c15dcf61f0147a(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterAccessnodes, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355d1e63d9a4ca873d0d24b0461b1e1595d66877481ec189399d06844f9eb7c0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterActivitycontrol, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60805ec53478ce887a478485d01a11ce6ec00a23e0fa604af538fed1a8facd4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterEtcdprotection, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7ea84c530b6ebd477e92dfdb2ddcdd8ed2ca0ea7e1e4e93ca518d2f4395a58(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterOptions, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7b783af2f70b9ab69a81eee7501652a7e212ca0c1a19b1e72f5af4b4bef12c8(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterRegion, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__474a217a2a6b960fe68efaec8d274d8b7c695cf21da5ad11cbace46943ecb9e0(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterTags, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d30b7b43026a7b5aec3af9db6a53f4def18f652ecdd74568dca751afd5d985d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d9db187b552c39082b97467c47f7a792b9f5b7e862ba79a5a48ba8a27255447(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fa7f4791fdf7d4d574641a122a78d44c5cf2d13b68575de496d91bdda0673e9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4e83efd6094bf89a5b54c881032f5ba5a9c9f109931adf8007f8f6ec2180a3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a86aec8c134acc1a5bedcb50bd92478ea7e18718711b9c537bdd6f522eea1fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bad11ff336f7f1c51a7ce7c53e5f6572f994b6ae51af1fec4bbfca697c786c9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b9ab6e76632d4788d34f07af6db65661ea5ace18a16f8531097008d00feedc(
    *,
    id: typing.Optional[jsii.Number] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb21fa2753346384db112381cb8413e619b15db543b9279368acbeb48f43588(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d725dddbf7008233ca2f7a53e49f9b427e87af14b551a9e804dc1edf535b20(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35dea32ad677836ed7383f2c073eddbd5cf1e71f54aab84a0650031aa10a42b6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67be32dcde77a72eadd82cd748638b5dc220e33e98ef9719ec5513dabfdff411(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7c0317d2873d87fa00745d955ac83e1a495f28faa3058263f374f4e6c52a23f(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6e01bea844b0522ca593eb509fb4d03f6719cb2ab4b5007cc990607ad6dbe1e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterAccessnodes]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98acd42155592411ac98792a9f3cf45d43766c5800735e242dfe2ee60bcb5195(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6b8b667e7b66796183ac1ea8f13a73346b8b409898939b5a1744f4348df9507(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a54f60669b402a88dde230c9838cc571cb69e6c2c03fcc797a8217a1e474330(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce4bba16e73ec6a51454bf2f73d5f494925d71a307f2adaad46dbacbb9943739(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterAccessnodes]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8f3900158f58566012c7a1ae5a4ce94db7ef5c47517ce5ca0c80a72aef06e67(
    *,
    enablebackup: typing.Optional[builtins.str] = None,
    enablebackupafteradelay: typing.Optional[jsii.Number] = None,
    enablerestore: typing.Optional[builtins.str] = None,
    enablerestoreafteradelay: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__415527d830c504a43f527d29e25a63c98085dc80da6d8e9a0827b4fbef592099(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52beafd2d0634a7459db44d1943bad22ffd37f46c337406c4906f69e97b85d7f(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fa233ac46138d61c356e222b0699d721288870c1b6145212b259c176a515d36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c68aa2f81aeb16902ac52bfd11bf5fb64ef4f06e626783ada4dfddd18c7a928(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bc20f054e784cb511a4da96d868df8b31adf156e01aeff1e35705faaf31cb72(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2931fb64023c0d726125d2c9eeccc60d311adb9dc32791a27603a57cb2549a9f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterActivitycontrol]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cd57a8cc23fa70dfbd1c2812e6327ef896c8dda24d95fcfee2c808d01187b73(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d262de690260d9f2990fe21bec8fb07b8807845e3e3b19efeade589494f3c66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25e6bf721b62ff11040fd41347f93242774f94b6312d261ce461b8ffa4c61bd1(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd1da442f56e809b67f5cff905dbe9b181cfbca90c322391203051e5712d721(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ebdddb64e3eff485e7ed880069b02d2b4c021416ba5981316c5c8304c6d1983(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c62bc322a262523e1eef4b6a5970dffba5387f4f25e725439a871aaf43c768c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterActivitycontrol]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d1b0bee98ecec17fd74c059eecdd73143fb72f20a9ca82103df82d5496c8181(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    accessnodes: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterAccessnodes, typing.Dict[builtins.str, typing.Any]]]]] = None,
    activitycontrol: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterActivitycontrol, typing.Dict[builtins.str, typing.Any]]]]] = None,
    apiserver: typing.Optional[builtins.str] = None,
    etcdprotection: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterEtcdprotection, typing.Dict[builtins.str, typing.Any]]]]] = None,
    id: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    options: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterOptions, typing.Dict[builtins.str, typing.Any]]]]] = None,
    region: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterRegion, typing.Dict[builtins.str, typing.Any]]]]] = None,
    serviceaccount: typing.Optional[builtins.str] = None,
    servicetoken: typing.Optional[builtins.str] = None,
    servicetype: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterTags, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__152ef28cfeb821719014e006fb7cbdb080d12b8750869276f71de6c85c184b7d(
    *,
    enabled: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterEtcdprotectionPlan, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__263ef028bfb24eee4cf1ad5a9dea8d8a37b6dca924b6b515cce3e726f1d03fab(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7beffdad28da705d0f71aefcddd493d87c0350b23705733b741450c1d44c9965(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228060e2406262f91ababdeecba713835cb26874dd5d5fb6225e103b97d0df8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac391be550affe4bdd532f8bc6d862c4db1e3653fdcb48a961b80097aac3e7f9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b5ff9c3c6937dfcdc41ae071cf57b55618ba5098659ee0e14b9b479c9a80861(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b46a85a2d63ae58bf63c8b5216a017152b84158585282dcd5979e9c3f0ac095(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotection]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c067fadf3daa94bc87fdf0c61c8d5774dc9a38795c8136e96a3c4b1cc9c7baf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ac5976ca93ca70f08ae15d941c6716125cc84584e9e2c9f8854cbae8b9128d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterEtcdprotectionPlan, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69ea5c73769f5ad7d3d05802c03b6f4862d0c3779eddba349b87152f11930fcc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5589ba56203eb82d762b5019117cf80eecd637b213cd1eabffee368fccc92c7b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotection]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3796ad5554710946a67fbf3bb15bbd62f6ee055f1d6ac6a22fc9aade52f0a6a9(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c879702fb33ef6dd0884028c86c0724f4a20a83b9e4e69c7dd55bbad237183de(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__019da69f427bee7e2a6362705c44b6812b27decd5d2ab89170a4a2efaeeaec8b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__456ba874fb4f262a4255ec0cf15571bfe35f2de14075ae336ad9470b65b92d72(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfff0f48eeff86822f438ca7edffa8b6ec131e4b32db47bc0c9db07566dbc120(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__300cde92261c44e98a864b993943576c1eb6c912c4b1676f11e0ffb9fd9de423(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c02d22a9d4ea7f7456a0279b70e9a10fd8fb1342b68eb6fe46e96bf9508db77(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterEtcdprotectionPlan]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__354a95d0956ddcd902e2b10e175a1ac37b4ff1a51877f4b519eea60e758abe24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78d169eecbc320411888ccfbb9a9f1b5bb985fb73e514a4cf634e1f07a98119(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa11c6fc30e58c5e1c53c52cb5071597cccb50438973c07774434f67e6d0a21(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a741beaa7fa21413ce9229c64c59f4c5eee8f25e721a7fccdd658db8ac08ee89(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterEtcdprotectionPlan]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24d0be4f341a62097f8cf02601f6d217c92cf00674012719569c88daa8e1490c(
    *,
    imageregistry: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterOptionsImageregistry, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3dc8d1fc5ae4a08758a65233c558473a7ca8392299512ee325d2e808348b39e(
    *,
    imagepullsecret: typing.Optional[builtins.str] = None,
    registryurl: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11b5693237cd05527565d1998d665cb838f7432c34734f07e57410291545ef5b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fc5688e14b3e42c4d29b80ef52014058cd975392a3f62ce1872c2002494eb6b(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__589b6759ddf7d16a623bfa4a970c78775f4700d3c191a778e9002da4fe554580(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77075da1166b72cc9bdbb248a8854e2fdc6cf922ffdf4c2ddd857a67710aa28e(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e086f083b992727ae157d6a6b2b30bc2aa79ef230a13c2a25fa88231cc93f6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f63c25809ad79a479d23ec807f0a6bb558cea1d68069a22f198334786913852b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptionsImageregistry]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5cf336669d79eaeafcca8defcb5b41ab279f5a43b2ef75c47716c02be37e4e9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd019a6cd63303906f244a7b09939a26e5863ef12c680c4125c8e1b90d8916d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9efc3e78236ee11809c1060f09daa6fa34f892bc37f9ff5cec88632ab8762afb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68108763b5d9d4e220fa1e7508063ce403c503e2cdf80001c70c849e1c20543a(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptionsImageregistry]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7274d2cffbd5b95569bcfc0a4bacd29ea710ed4e88c6fe57726c982d596f9576(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3359de6f1b0d010508367ce0a04cabc200f7a2f4f31cfda6f2d78a9cf594b555(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f8c346896aa96e649d39874f691dd3f889d314fa89647e33e3d155a8e77adb8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92764dafc48c4e4fddac60aa9e93cadd5c3bc906fe2d8a9c81977c28c26c2bb6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d3736e01b3916702107ee34e9e20a719ba1b7f1c4a202c085810f6ebba3ed7(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c57b870776829c29c5659bf72bf3b57dac6db4a045d24fd0e29f801bb24c059(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterOptions]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7992214d9a786196c0275d79a43f7d51a83e90689dcb8ea1edc222fd2bc1da2d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13994500a6022755eb470d400cb7a2e7543a8a6ccb728cd9c41cf810e1701bce(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[KubernetesClusterOptionsImageregistry, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad36a379043454ff175159c4ebf5283b1340681b0257c55a0547beb352fc86cf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterOptions]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fcc6956700856f02b74495e74296705f5fbd29a6d56bb613ede477ce04e1493(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f7bbbd05ac909cf282295c229ae5079402c6b21b91b147f2a5996260004f79d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd5b88d76dd30feacac5a871b49a69652ed40f3b5cbac6eaaf5e2cc25556eff0(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9edc55580b131cd7ba6f1ca8f325a2bb17dfabb37c4f9db90228786524deb84a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffa23f8aee8c17dd70882dc84d84ff796cb06f4de301445b5e4b752038f2a2fb(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa68c853884e2088f6bebdbc0fd1666e23df6ba037e36459ab7212c988daac9(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6acf9c07c26b6f890b6cdb433619c98b84a604a6157faaa3ae683ac4f46671c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterRegion]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c83b99fb231d196b141054aba0dfcfe964be156c65c3cab65500fbb74eea5784(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aed0e4a1a79614e38ead2b852dad7414eeb3c88b0e97c6f8962258f0ca42fa13(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e675cd408219495f7d5fd0d4e250a6dc911b355f2b52f178a00c6eb5a942bf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f9c59c5fe0f177f6523618b9815d1417a4a2313621e472c55666fb1ecaab67(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterRegion]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__777ccdd75f7280699814caac681fdfad9770b7556b60d37b97a60e281c4c3d2f(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1049a656ad55717699041ab3567a173d43c6e36bdb289a74f843adb7815c5783(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078ef0d93547179c8ddf240260108ec2d35f8b98f314fbbe969d3e11038555f6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3de07e3026a49748bb73465e3705ee7c42b479e2296e90b5c8b49f2c5707dc4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9680c37cd9a05b094d1cce047895ff0f890190762715f4fbff58e1fbc9820049(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d140f02d336d2d660849e20816e12d2f14a5b84be43c0849b7ed9448e049e0(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7058417d8318409271e6efc74e0176f7548ed316e121780ff24b95b18f63e25(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[KubernetesClusterTags]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0a52fdcb5aa6e5b5fee2319d4d6b1f29e77a338083749cfc46a89ebc4bbd3f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90dc43a6aad191fef848359ca677b40ec139def6bb621e5700d5be071d17d37f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598de56fff4716cb42a093d46b84cf45e0b38e575f3593a87d21d278822e2ea6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7dff3ad2e1049157840f6f42a3c15578a97b15db8946a786537da4bdfc8f60bf(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, KubernetesClusterTags]],
) -> None:
    """Type checking stubs"""
    pass
