'''
# `commvault_company`

Refer to the Terraform Registry for docs: [`commvault_company`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company).
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


class Company(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.company.Company",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company commvault_company}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        company_alias: builtins.str,
        company_name: builtins.str,
        contact_name: builtins.str,
        email: builtins.str,
        associated_smtp: typing.Optional[builtins.str] = None,
        company_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        plans: typing.Optional[typing.Sequence[builtins.str]] = None,
        send_email: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company commvault_company} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param company_alias: Specifies the Alias name for the company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_alias Company#company_alias}
        :param company_name: Specifies the name of the Company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_name Company#company_name}
        :param contact_name: Specifies Name of the tenant administrator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#contact_name Company#contact_name}
        :param email: Specifies Email address for the tenant administrator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#email Company#email}
        :param associated_smtp: Specifies the SMTP address of the company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#associated_smtp Company#associated_smtp}
        :param company_id: Specifies the company id to which the child company should be associated with. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_id Company#company_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#id Company#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param plans: Specifies the data protection plans to use for the company. The plans you select are the plans that the tenant administrator can choose from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#plans Company#plans}
        :param send_email: Specifies whether email needs to be sent ot not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#send_email Company#send_email}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5de9fd7ee3a4c69998a1809602a88b7782c83f0dc15b1837e1fa9957b9f6f7d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CompanyConfig(
            company_alias=company_alias,
            company_name=company_name,
            contact_name=contact_name,
            email=email,
            associated_smtp=associated_smtp,
            company_id=company_id,
            id=id,
            plans=plans,
            send_email=send_email,
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
        '''Generates CDKTF code for importing a Company resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Company to import.
        :param import_from_id: The id of the existing Company that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Company to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f94295fa89b679c794fcee52f0aeca7ad45f18ccf8bc61d561e6941975347efb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="resetAssociatedSmtp")
    def reset_associated_smtp(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociatedSmtp", []))

    @jsii.member(jsii_name="resetCompanyId")
    def reset_company_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompanyId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPlans")
    def reset_plans(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlans", []))

    @jsii.member(jsii_name="resetSendEmail")
    def reset_send_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSendEmail", []))

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
    @jsii.member(jsii_name="associatedSmtpInput")
    def associated_smtp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associatedSmtpInput"))

    @builtins.property
    @jsii.member(jsii_name="companyAliasInput")
    def company_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "companyAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="companyIdInput")
    def company_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "companyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="companyNameInput")
    def company_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "companyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="contactNameInput")
    def contact_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactNameInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="plansInput")
    def plans_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "plansInput"))

    @builtins.property
    @jsii.member(jsii_name="sendEmailInput")
    def send_email_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "sendEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="associatedSmtp")
    def associated_smtp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedSmtp"))

    @associated_smtp.setter
    def associated_smtp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b463ba3a685de85be63d48f3a9f2dd75d8311cb9b5b5fedc50efb103747eec78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedSmtp", value)

    @builtins.property
    @jsii.member(jsii_name="companyAlias")
    def company_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "companyAlias"))

    @company_alias.setter
    def company_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f6335c3360f2c8aa9a2ba5befb986e10b7bd65ed5dba4c28fed9d49ffad9b7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyAlias", value)

    @builtins.property
    @jsii.member(jsii_name="companyId")
    def company_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "companyId"))

    @company_id.setter
    def company_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__269ff97757f2f0c1b3cec4852c605b6791f049106dc6928ec13ce07c91f84a35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyId", value)

    @builtins.property
    @jsii.member(jsii_name="companyName")
    def company_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "companyName"))

    @company_name.setter
    def company_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3831fae63c4795f75b40b4d984d2061e76fc5e268c446a973d8fbc5ad9a06649)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "companyName", value)

    @builtins.property
    @jsii.member(jsii_name="contactName")
    def contact_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contactName"))

    @contact_name.setter
    def contact_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__296ff15a3db79f9b49f1fa660cc08970fdda56b26e039ac3e4d025a38389957e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactName", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f61f612c65f6a068f8951b46e8881d150a58135e7a0d13227a469efd5301387)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74b0104f3d81e898d89bd30aff959290e3a3faede8730bdc012e2b0afb9144a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="plans")
    def plans(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "plans"))

    @plans.setter
    def plans(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a496363535824ac43c15a198a8c6f6724e0c7704fa10cb22733d5e7c0fb606f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plans", value)

    @builtins.property
    @jsii.member(jsii_name="sendEmail")
    def send_email(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "sendEmail"))

    @send_email.setter
    def send_email(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d11fe3c2cc666ceaf37646ed48b6466ca87b2e8d6f2883d2105de01b7154413a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendEmail", value)


@jsii.data_type(
    jsii_type="commvault.company.CompanyConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "company_alias": "companyAlias",
        "company_name": "companyName",
        "contact_name": "contactName",
        "email": "email",
        "associated_smtp": "associatedSmtp",
        "company_id": "companyId",
        "id": "id",
        "plans": "plans",
        "send_email": "sendEmail",
    },
)
class CompanyConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        company_alias: builtins.str,
        company_name: builtins.str,
        contact_name: builtins.str,
        email: builtins.str,
        associated_smtp: typing.Optional[builtins.str] = None,
        company_id: typing.Optional[jsii.Number] = None,
        id: typing.Optional[builtins.str] = None,
        plans: typing.Optional[typing.Sequence[builtins.str]] = None,
        send_email: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param company_alias: Specifies the Alias name for the company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_alias Company#company_alias}
        :param company_name: Specifies the name of the Company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_name Company#company_name}
        :param contact_name: Specifies Name of the tenant administrator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#contact_name Company#contact_name}
        :param email: Specifies Email address for the tenant administrator. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#email Company#email}
        :param associated_smtp: Specifies the SMTP address of the company. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#associated_smtp Company#associated_smtp}
        :param company_id: Specifies the company id to which the child company should be associated with. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_id Company#company_id}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#id Company#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param plans: Specifies the data protection plans to use for the company. The plans you select are the plans that the tenant administrator can choose from. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#plans Company#plans}
        :param send_email: Specifies whether email needs to be sent ot not. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#send_email Company#send_email}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93df22fc1f98fb05faa12c9e8ace2305bd617942695b7505295bb7ba7259a016)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument company_alias", value=company_alias, expected_type=type_hints["company_alias"])
            check_type(argname="argument company_name", value=company_name, expected_type=type_hints["company_name"])
            check_type(argname="argument contact_name", value=contact_name, expected_type=type_hints["contact_name"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument associated_smtp", value=associated_smtp, expected_type=type_hints["associated_smtp"])
            check_type(argname="argument company_id", value=company_id, expected_type=type_hints["company_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument plans", value=plans, expected_type=type_hints["plans"])
            check_type(argname="argument send_email", value=send_email, expected_type=type_hints["send_email"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "company_alias": company_alias,
            "company_name": company_name,
            "contact_name": contact_name,
            "email": email,
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
        if associated_smtp is not None:
            self._values["associated_smtp"] = associated_smtp
        if company_id is not None:
            self._values["company_id"] = company_id
        if id is not None:
            self._values["id"] = id
        if plans is not None:
            self._values["plans"] = plans
        if send_email is not None:
            self._values["send_email"] = send_email

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
    def company_alias(self) -> builtins.str:
        '''Specifies the Alias name for the company.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_alias Company#company_alias}
        '''
        result = self._values.get("company_alias")
        assert result is not None, "Required property 'company_alias' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def company_name(self) -> builtins.str:
        '''Specifies the name of the Company.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_name Company#company_name}
        '''
        result = self._values.get("company_name")
        assert result is not None, "Required property 'company_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def contact_name(self) -> builtins.str:
        '''Specifies Name of the tenant administrator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#contact_name Company#contact_name}
        '''
        result = self._values.get("contact_name")
        assert result is not None, "Required property 'contact_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''Specifies Email address for the tenant administrator.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#email Company#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def associated_smtp(self) -> typing.Optional[builtins.str]:
        '''Specifies the SMTP address of the company.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#associated_smtp Company#associated_smtp}
        '''
        result = self._values.get("associated_smtp")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company_id(self) -> typing.Optional[jsii.Number]:
        '''Specifies  the company id to which the child company should be associated with.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#company_id Company#company_id}
        '''
        result = self._values.get("company_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#id Company#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plans(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the data protection plans to use for the company.

        The plans you select are the plans that the tenant administrator can choose from.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#plans Company#plans}
        '''
        result = self._values.get("plans")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def send_email(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Specifies whether  email needs to be sent ot not.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/company#send_email Company#send_email}
        '''
        result = self._values.get("send_email")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompanyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Company",
    "CompanyConfig",
]

publication.publish()

def _typecheckingstub__c5de9fd7ee3a4c69998a1809602a88b7782c83f0dc15b1837e1fa9957b9f6f7d(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    company_alias: builtins.str,
    company_name: builtins.str,
    contact_name: builtins.str,
    email: builtins.str,
    associated_smtp: typing.Optional[builtins.str] = None,
    company_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    plans: typing.Optional[typing.Sequence[builtins.str]] = None,
    send_email: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
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

def _typecheckingstub__f94295fa89b679c794fcee52f0aeca7ad45f18ccf8bc61d561e6941975347efb(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b463ba3a685de85be63d48f3a9f2dd75d8311cb9b5b5fedc50efb103747eec78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f6335c3360f2c8aa9a2ba5befb986e10b7bd65ed5dba4c28fed9d49ffad9b7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269ff97757f2f0c1b3cec4852c605b6791f049106dc6928ec13ce07c91f84a35(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3831fae63c4795f75b40b4d984d2061e76fc5e268c446a973d8fbc5ad9a06649(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296ff15a3db79f9b49f1fa660cc08970fdda56b26e039ac3e4d025a38389957e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f61f612c65f6a068f8951b46e8881d150a58135e7a0d13227a469efd5301387(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74b0104f3d81e898d89bd30aff959290e3a3faede8730bdc012e2b0afb9144a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a496363535824ac43c15a198a8c6f6724e0c7704fa10cb22733d5e7c0fb606f3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d11fe3c2cc666ceaf37646ed48b6466ca87b2e8d6f2883d2105de01b7154413a(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93df22fc1f98fb05faa12c9e8ace2305bd617942695b7505295bb7ba7259a016(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    company_alias: builtins.str,
    company_name: builtins.str,
    contact_name: builtins.str,
    email: builtins.str,
    associated_smtp: typing.Optional[builtins.str] = None,
    company_id: typing.Optional[jsii.Number] = None,
    id: typing.Optional[builtins.str] = None,
    plans: typing.Optional[typing.Sequence[builtins.str]] = None,
    send_email: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass
