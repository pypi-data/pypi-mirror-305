'''
# `commvault_vm_group`

Refer to the Terraform Registry for docs: [`commvault_vm_group`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group).
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


class VmGroup(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.vmGroup.VmGroup",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group commvault_vm_group}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        client_id: jsii.Number,
        plan_id: jsii.Number,
        vm_group_name: builtins.str,
        company_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        vms: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group commvault_vm_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param client_id: Specifies The ID of the hypervisor client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#client_id VmGroup#client_id}
        :param plan_id: Specifies The ID of the plan that you want to associate with the VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#plan_id VmGroup#plan_id}
        :param vm_group_name: Specifies The name of the VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#vm_group_name VmGroup#vm_group_name}
        :param company_id: Specifies the company id to which the vm group should be associated with. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#company_id VmGroup#company_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#id VmGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Specifies The Tags that you want to back up in a VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#tags VmGroup#tags}
        :param vms: Specifies The VMs that you want to back up in a VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#vms VmGroup#vms}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0b1590755a90eea3e6e36585a1bfece93fe87a43c046808cd22c4585851a782)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VmGroupConfig(
            client_id=client_id,
            plan_id=plan_id,
            vm_group_name=vm_group_name,
            company_id=company_id,
            id=id,
            tags=tags,
            vms=vms,
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
        '''Generates CDKTF code for importing a VmGroup resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the VmGroup to import.
        :param import_from_id: The id of the existing VmGroup that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the VmGroup to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1237154a40cd2068745901ce997c59b9e13abbb764d967e0294925d2fd223da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetCompanyId")
    def reset_company_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompanyId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetVms")
    def reset_vms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVms", []))

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
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="companyIdInput")
    def company_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "companyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="planIdInput")
    def plan_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "planIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmGroupNameInput")
    def vm_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="vmsInput")
    def vms_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vmsInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a57d25c4a88b7af0f90fd91fdec1c771c528727f49eb206a53ed3d58e99c8719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="companyId")
    def company_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "companyId"))

    @company_id.setter
    def company_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c6ab47ae9ac7cf3353c013ed18ec8a8d71ff8755cc8f1e4d60cf7dbfa46536d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__009838c27665e760b6e1bb97d072b7f030594fb20c575a556e55df1759a0f257)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="planId")
    def plan_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "planId"))

    @plan_id.setter
    def plan_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb58d4935de415ebfc9626d53610b4f3c3d39f810a7fa76dfdd8240f8e5e8008)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "planId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9da5668fc018dc6ed5b27a31536b09726e01aa2cf034ca783fe10bf3d52abe8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vmGroupName")
    def vm_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmGroupName"))

    @vm_group_name.setter
    def vm_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af630f77f6c74d25f390feddd118adb30c96e66e1598dda529f7420fd3a4c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="vms")
    def vms(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vms"))

    @vms.setter
    def vms(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__654c1fd5e7643a50cc06cf959e8178389002f66b60cf936be4cb58a3f6e37fba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vms", value)


@jsii.data_type(
    jsii_type="commvault.vmGroup.VmGroupConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "client_id": "clientId",
        "plan_id": "planId",
        "vm_group_name": "vmGroupName",
        "company_id": "companyId",
        "id": "id",
        "tags": "tags",
        "vms": "vms",
    },
)
class VmGroupConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        client_id: jsii.Number,
        plan_id: jsii.Number,
        vm_group_name: builtins.str,
        company_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        vms: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param client_id: Specifies The ID of the hypervisor client. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#client_id VmGroup#client_id}
        :param plan_id: Specifies The ID of the plan that you want to associate with the VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#plan_id VmGroup#plan_id}
        :param vm_group_name: Specifies The name of the VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#vm_group_name VmGroup#vm_group_name}
        :param company_id: Specifies the company id to which the vm group should be associated with. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#company_id VmGroup#company_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#id VmGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Specifies The Tags that you want to back up in a VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#tags VmGroup#tags}
        :param vms: Specifies The VMs that you want to back up in a VM group. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#vms VmGroup#vms}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba0651932a3bf77da252bcc7b4652df2624a1067be8c9b6be8b69fbf7e2d4b58)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument plan_id", value=plan_id, expected_type=type_hints["plan_id"])
            check_type(argname="argument vm_group_name", value=vm_group_name, expected_type=type_hints["vm_group_name"])
            check_type(argname="argument company_id", value=company_id, expected_type=type_hints["company_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vms", value=vms, expected_type=type_hints["vms"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "plan_id": plan_id,
            "vm_group_name": vm_group_name,
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
        if company_id is not None:
            self._values["company_id"] = company_id
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
        if vms is not None:
            self._values["vms"] = vms

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
    def client_id(self) -> jsii.Number:
        '''Specifies The ID of the hypervisor client.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#client_id VmGroup#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def plan_id(self) -> jsii.Number:
        '''Specifies The ID of the plan that you want to associate with the VM group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#plan_id VmGroup#plan_id}
        '''
        result = self._values.get("plan_id")
        assert result is not None, "Required property 'plan_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def vm_group_name(self) -> builtins.str:
        '''Specifies The name of the VM group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#vm_group_name VmGroup#vm_group_name}
        '''
        result = self._values.get("vm_group_name")
        assert result is not None, "Required property 'vm_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def company_id(self) -> typing.Optional[jsii.Number]:
        '''Specifies the company id to which the vm group should be associated with.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#company_id VmGroup#company_id}
        '''
        result = self._values.get("company_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#id VmGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies The Tags that you want to back up in a VM group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#tags VmGroup#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def vms(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies The VMs that you want to back up in a VM group.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/vm_group#vms VmGroup#vms}
        '''
        result = self._values.get("vms")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VmGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VmGroup",
    "VmGroupConfig",
]

publication.publish()

def _typecheckingstub__e0b1590755a90eea3e6e36585a1bfece93fe87a43c046808cd22c4585851a782(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    client_id: jsii.Number,
    plan_id: jsii.Number,
    vm_group_name: builtins.str,
    company_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    vms: typing.Optional[typing.Sequence[builtins.str]] = None,
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

def _typecheckingstub__d1237154a40cd2068745901ce997c59b9e13abbb764d967e0294925d2fd223da(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a57d25c4a88b7af0f90fd91fdec1c771c528727f49eb206a53ed3d58e99c8719(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c6ab47ae9ac7cf3353c013ed18ec8a8d71ff8755cc8f1e4d60cf7dbfa46536d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009838c27665e760b6e1bb97d072b7f030594fb20c575a556e55df1759a0f257(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb58d4935de415ebfc9626d53610b4f3c3d39f810a7fa76dfdd8240f8e5e8008(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da5668fc018dc6ed5b27a31536b09726e01aa2cf034ca783fe10bf3d52abe8d(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af630f77f6c74d25f390feddd118adb30c96e66e1598dda529f7420fd3a4c7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__654c1fd5e7643a50cc06cf959e8178389002f66b60cf936be4cb58a3f6e37fba(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba0651932a3bf77da252bcc7b4652df2624a1067be8c9b6be8b69fbf7e2d4b58(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    client_id: jsii.Number,
    plan_id: jsii.Number,
    vm_group_name: builtins.str,
    company_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    vms: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
