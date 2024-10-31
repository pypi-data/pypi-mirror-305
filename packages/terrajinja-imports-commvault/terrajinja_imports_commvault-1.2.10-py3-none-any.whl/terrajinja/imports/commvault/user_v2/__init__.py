'''
# `commvault_user_v2`

Refer to the Terraform Registry for docs: [`commvault_user_v2`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2).
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


class UserV2(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.userV2.UserV2",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2 commvault_user_v2}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        email: builtins.str,
        authenticationmethod: typing.Optional[builtins.str] = None,
        company: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UserV2Company", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[builtins.str] = None,
        fullname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inviteuser: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UserV2Plan", typing.Dict[builtins.str, typing.Any]]]]] = None,
        userprincipalname: typing.Optional[builtins.str] = None,
        usesystemgeneratepassword: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2 commvault_user_v2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param email: Used to provide an email-id to the new user. This email-id is used for logging in the user. Please note that email ids are compulsory for company and local users and optional for external users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#email UserV2#email}
        :param authenticationmethod: Change the current authentication method of user. SAML user association can be removed using this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#authenticationmethod UserV2#authenticationmethod}
        :param company: company block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#company UserV2#company}
        :param enabled: enable or disable the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#enabled UserV2#enabled}
        :param fullname: Used to provide a name to the new user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#fullname UserV2#fullname}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inviteuser: User will receive an email to install backup software package on their device if this is set to true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#inviteuser UserV2#inviteuser}
        :param name: Used to provide the new user with a username. This username can be used for logging in the user instead of email-id when duplicate email-ids are present. For external user, it is necessary to provide the domain name along with the username (domainName\\username). To create a company user, the company id or name needs to be provided in the company entity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}
        :param password: Used to provide a password to the user being created. This will be accepted when the useSystemGeneratePassword tag is false. The password has to be provided in Base64 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#password UserV2#password}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#plan UserV2#plan}
        :param userprincipalname: Change User Principal Name(UPN) for existing user. This User Principal Name can be used for logging-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#userprincipalname UserV2#userprincipalname}
        :param usesystemgeneratepassword: Choose to provide a system generated password to the user instead of providing your own password. An email will be sent to the user to reset the password. If it is set to true, password tag need not be provided. If it is set to false, password needs to be provided in the password tag in Base64 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#usesystemgeneratepassword UserV2#usesystemgeneratepassword}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3351b8e5c7e784ab14026c479c5531336945aac1b10b64d0c72cb592f534073a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = UserV2Config(
            email=email,
            authenticationmethod=authenticationmethod,
            company=company,
            enabled=enabled,
            fullname=fullname,
            id=id,
            inviteuser=inviteuser,
            name=name,
            password=password,
            plan=plan,
            userprincipalname=userprincipalname,
            usesystemgeneratepassword=usesystemgeneratepassword,
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
        '''Generates CDKTF code for importing a UserV2 resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the UserV2 to import.
        :param import_from_id: The id of the existing UserV2 that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the UserV2 to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__150d8139ebf4df5af5d29f28fa1f1910b1b8b7b11016b810ac2beedbddad19f6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putCompany")
    def put_company(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UserV2Company", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88846c19ee0582093560f49ccf26fca37d97f7d86351a66e575131cb840ea01b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCompany", [value]))

    @jsii.member(jsii_name="putPlan")
    def put_plan(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UserV2Plan", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a73fd81ce2481dcb3ad5acb62cf0795e716bb13fa420a65411d3cf0d51e9f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlan", [value]))

    @jsii.member(jsii_name="resetAuthenticationmethod")
    def reset_authenticationmethod(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationmethod", []))

    @jsii.member(jsii_name="resetCompany")
    def reset_company(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompany", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFullname")
    def reset_fullname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFullname", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInviteuser")
    def reset_inviteuser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInviteuser", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPlan")
    def reset_plan(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlan", []))

    @jsii.member(jsii_name="resetUserprincipalname")
    def reset_userprincipalname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserprincipalname", []))

    @jsii.member(jsii_name="resetUsesystemgeneratepassword")
    def reset_usesystemgeneratepassword(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsesystemgeneratepassword", []))

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
    @jsii.member(jsii_name="company")
    def company(self) -> "UserV2CompanyList":
        return typing.cast("UserV2CompanyList", jsii.get(self, "company"))

    @builtins.property
    @jsii.member(jsii_name="plan")
    def plan(self) -> "UserV2PlanList":
        return typing.cast("UserV2PlanList", jsii.get(self, "plan"))

    @builtins.property
    @jsii.member(jsii_name="authenticationmethodInput")
    def authenticationmethod_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationmethodInput"))

    @builtins.property
    @jsii.member(jsii_name="companyInput")
    def company_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserV2Company"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserV2Company"]]], jsii.get(self, "companyInput"))

    @builtins.property
    @jsii.member(jsii_name="emailInput")
    def email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="fullnameInput")
    def fullname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fullnameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inviteuserInput")
    def inviteuser_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inviteuserInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="planInput")
    def plan_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserV2Plan"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserV2Plan"]]], jsii.get(self, "planInput"))

    @builtins.property
    @jsii.member(jsii_name="userprincipalnameInput")
    def userprincipalname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userprincipalnameInput"))

    @builtins.property
    @jsii.member(jsii_name="usesystemgeneratepasswordInput")
    def usesystemgeneratepassword_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usesystemgeneratepasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationmethod")
    def authenticationmethod(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationmethod"))

    @authenticationmethod.setter
    def authenticationmethod(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__990bd641ead4350203fa22ec2bb5b782672534fbeeac8ed9858031ed42ac95d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationmethod", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82efd334dd5401da7a2a6b5346392865ac08b308b2f8665f2776585aa17d5a0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8505a3f92d9d68fc559d7a845e2d58bfddbd612746d1aafa2dba64f64d9ff8b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="fullname")
    def fullname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fullname"))

    @fullname.setter
    def fullname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f738e6e2823ed5e24a9eb857ce65b716b4ccdfcbf59cc9744a996e48cd1239d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fullname", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4702539bf8744be683fe18f3af94f8ee7b50471e8b555039cc4d29ad28cf82e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inviteuser")
    def inviteuser(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inviteuser"))

    @inviteuser.setter
    def inviteuser(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f44cdc71782c460d8c26f62f00f4fef6d8e3a8b3af0fbea37f85a52e3d9c449)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inviteuser", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6241c023f5082a44e204ec5152a7c1cbe431848ea6541679f864ab16ddf069e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4fb56bc86a748b85fd4dd6faa7d0065cff6700e684216e239bb8b6adc621c65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="userprincipalname")
    def userprincipalname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userprincipalname"))

    @userprincipalname.setter
    def userprincipalname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__297e0a19519794fc9ab18a4a6ff414a74fc710516e79dc909dba5df013d98c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userprincipalname", value)

    @builtins.property
    @jsii.member(jsii_name="usesystemgeneratepassword")
    def usesystemgeneratepassword(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "usesystemgeneratepassword"))

    @usesystemgeneratepassword.setter
    def usesystemgeneratepassword(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48e255f1d45c12c665db441a33abf034d0d8fde124f003c1b36c0675c83a10ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usesystemgeneratepassword", value)


@jsii.data_type(
    jsii_type="commvault.userV2.UserV2Company",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class UserV2Company:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa0bb211e071c059b41a40fa2d6f65dfb4dd3d5471b12651bc1429d3a4da39b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserV2Company(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserV2CompanyList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.userV2.UserV2CompanyList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2726ec494a8a9b70797cdc354356f75b5348a65d05f28b5264034d0cf127106e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserV2CompanyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8be786ed995a78656d43579fe904b57e10a396cfacf30334489457550db6c509)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserV2CompanyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afe02ce95cd636f7b16195d325aab3142850b3b69d9aa2ee4f26f31343f0e31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__48b3f3a93e64c7fbe96c1f92023d40a930280d18cc06d5ff9cd84bbff46db692)
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
            type_hints = typing.get_type_hints(_typecheckingstub__16d690a34f46648f14e0267ef7be54f14aa1814dc2a701ce788dab010722cbe8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Company]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Company]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Company]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6bcdbd527167480936de05de43139fef4e3d3573b8f3801a430c2958eb4e6ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserV2CompanyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.userV2.UserV2CompanyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e51e3274ec4dfd373b2f2b601d9781bc746a7b7ba45cd5e7333e752b3ab81a44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c211b66fe86b35b318fad90cb0c77e3ed5fddab3a220761a5fa70425037f8c3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52f3158f7e6f94107c72370ecc70f7484199e2327228a1b437ea962d8ada88e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Company]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Company]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Company]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30d9297250b18d423588fafa2b7aceb1fc70e11c22aa19567ec0d8427c0a645b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.userV2.UserV2Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "email": "email",
        "authenticationmethod": "authenticationmethod",
        "company": "company",
        "enabled": "enabled",
        "fullname": "fullname",
        "id": "id",
        "inviteuser": "inviteuser",
        "name": "name",
        "password": "password",
        "plan": "plan",
        "userprincipalname": "userprincipalname",
        "usesystemgeneratepassword": "usesystemgeneratepassword",
    },
)
class UserV2Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        email: builtins.str,
        authenticationmethod: typing.Optional[builtins.str] = None,
        company: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Company, typing.Dict[builtins.str, typing.Any]]]]] = None,
        enabled: typing.Optional[builtins.str] = None,
        fullname: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        inviteuser: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["UserV2Plan", typing.Dict[builtins.str, typing.Any]]]]] = None,
        userprincipalname: typing.Optional[builtins.str] = None,
        usesystemgeneratepassword: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param email: Used to provide an email-id to the new user. This email-id is used for logging in the user. Please note that email ids are compulsory for company and local users and optional for external users. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#email UserV2#email}
        :param authenticationmethod: Change the current authentication method of user. SAML user association can be removed using this. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#authenticationmethod UserV2#authenticationmethod}
        :param company: company block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#company UserV2#company}
        :param enabled: enable or disable the user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#enabled UserV2#enabled}
        :param fullname: Used to provide a name to the new user. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#fullname UserV2#fullname}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inviteuser: User will receive an email to install backup software package on their device if this is set to true. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#inviteuser UserV2#inviteuser}
        :param name: Used to provide the new user with a username. This username can be used for logging in the user instead of email-id when duplicate email-ids are present. For external user, it is necessary to provide the domain name along with the username (domainName\\username). To create a company user, the company id or name needs to be provided in the company entity. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}
        :param password: Used to provide a password to the user being created. This will be accepted when the useSystemGeneratePassword tag is false. The password has to be provided in Base64 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#password UserV2#password}
        :param plan: plan block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#plan UserV2#plan}
        :param userprincipalname: Change User Principal Name(UPN) for existing user. This User Principal Name can be used for logging-in. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#userprincipalname UserV2#userprincipalname}
        :param usesystemgeneratepassword: Choose to provide a system generated password to the user instead of providing your own password. An email will be sent to the user to reset the password. If it is set to true, password tag need not be provided. If it is set to false, password needs to be provided in the password tag in Base64 format. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#usesystemgeneratepassword UserV2#usesystemgeneratepassword}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c8455bff84f0f8f951e6e4b4da5ee107cb71132489100a107cc2ca59df52a3a)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument authenticationmethod", value=authenticationmethod, expected_type=type_hints["authenticationmethod"])
            check_type(argname="argument company", value=company, expected_type=type_hints["company"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument fullname", value=fullname, expected_type=type_hints["fullname"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inviteuser", value=inviteuser, expected_type=type_hints["inviteuser"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument plan", value=plan, expected_type=type_hints["plan"])
            check_type(argname="argument userprincipalname", value=userprincipalname, expected_type=type_hints["userprincipalname"])
            check_type(argname="argument usesystemgeneratepassword", value=usesystemgeneratepassword, expected_type=type_hints["usesystemgeneratepassword"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
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
        if authenticationmethod is not None:
            self._values["authenticationmethod"] = authenticationmethod
        if company is not None:
            self._values["company"] = company
        if enabled is not None:
            self._values["enabled"] = enabled
        if fullname is not None:
            self._values["fullname"] = fullname
        if id is not None:
            self._values["id"] = id
        if inviteuser is not None:
            self._values["inviteuser"] = inviteuser
        if name is not None:
            self._values["name"] = name
        if password is not None:
            self._values["password"] = password
        if plan is not None:
            self._values["plan"] = plan
        if userprincipalname is not None:
            self._values["userprincipalname"] = userprincipalname
        if usesystemgeneratepassword is not None:
            self._values["usesystemgeneratepassword"] = usesystemgeneratepassword

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
    def email(self) -> builtins.str:
        '''Used to provide an email-id to the new user.

        This email-id is used for logging in the user. Please note that email ids are compulsory for company and local users and optional for external users.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#email UserV2#email}
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authenticationmethod(self) -> typing.Optional[builtins.str]:
        '''Change the current authentication method of user. SAML user association can be removed using this.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#authenticationmethod UserV2#authenticationmethod}
        '''
        result = self._values.get("authenticationmethod")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def company(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Company]]]:
        '''company block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#company UserV2#company}
        '''
        result = self._values.get("company")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Company]]], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.str]:
        '''enable or disable the user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#enabled UserV2#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fullname(self) -> typing.Optional[builtins.str]:
        '''Used to provide a name to the new user.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#fullname UserV2#fullname}
        '''
        result = self._values.get("fullname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inviteuser(self) -> typing.Optional[builtins.str]:
        '''User will receive an email to install backup software package on their device if this is set to true.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#inviteuser UserV2#inviteuser}
        '''
        result = self._values.get("inviteuser")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Used to provide the new user with a username.

        This username can be used for logging in the user instead of email-id when duplicate email-ids are present. For external user, it is necessary to provide the domain name along with the username (domainName\\username). To create a company user, the company id or name needs to be provided in the company entity.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Used to provide a password to the user being created.

        This will be accepted when the useSystemGeneratePassword tag is false. The password has to be provided in Base64 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#password UserV2#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def plan(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserV2Plan"]]]:
        '''plan block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#plan UserV2#plan}
        '''
        result = self._values.get("plan")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["UserV2Plan"]]], result)

    @builtins.property
    def userprincipalname(self) -> typing.Optional[builtins.str]:
        '''Change User Principal Name(UPN) for existing user. This User Principal Name can be used for logging-in.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#userprincipalname UserV2#userprincipalname}
        '''
        result = self._values.get("userprincipalname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def usesystemgeneratepassword(self) -> typing.Optional[builtins.str]:
        '''Choose to provide a system generated password to the user instead of providing your own password.

        An email will be sent to the user to reset the password. If it is set to true, password tag need not be provided. If it is set to false, password needs to be provided in the password tag in Base64 format.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#usesystemgeneratepassword UserV2#usesystemgeneratepassword}
        '''
        result = self._values.get("usesystemgeneratepassword")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserV2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.userV2.UserV2Plan",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class UserV2Plan:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f3f95d00ac38e0a556ad046ba44bfaed6d06c7d06a8c423c107092a0e7d469a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#id UserV2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/user_v2#name UserV2#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserV2Plan(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class UserV2PlanList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.userV2.UserV2PlanList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1431d9a18f47adee3c5f1e3da4e16312501659e160e0260f08eec55a20842916)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "UserV2PlanOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ae9eb45f4aafff632444a3386eb4c28b838584b7470d7722df7254cc2388662)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("UserV2PlanOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__179023d3f6e7b8f6e9c6ab38c3a532ccaf203c5f999b7f83c84b3a87ba1ba01b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6c154e587d3ea6fe5e92b24e0e6241b430e125fc2c8d3d5e2c700cb15b9263d6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__23bc97150047395de57ca721f8d9670f95496b35f4891e9a4bf283eb483f4545)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Plan]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Plan]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Plan]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4718f53448fea4bc808d2a0f5bab01b7f079e9132e36611ea621bf6c3a8959ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class UserV2PlanOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.userV2.UserV2PlanOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__699e88fb385f51330388304f2f146c8f29a18ced2f035a8ecf38b0fded9f219b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__61d0743dea483af0647cf9a0c7468c602a63c377e2159ff2d05edd4630ef914a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af91290e5b145c3e0da19b2fcaec4a4dfe5581dfd0c941ab2b4ca6b1f58dd87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Plan]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Plan]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Plan]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dec192db4840a5dbb3426f4d3188dfc3095afb4b3f05f478d77c51276d613227)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "UserV2",
    "UserV2Company",
    "UserV2CompanyList",
    "UserV2CompanyOutputReference",
    "UserV2Config",
    "UserV2Plan",
    "UserV2PlanList",
    "UserV2PlanOutputReference",
]

publication.publish()

def _typecheckingstub__3351b8e5c7e784ab14026c479c5531336945aac1b10b64d0c72cb592f534073a(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    email: builtins.str,
    authenticationmethod: typing.Optional[builtins.str] = None,
    company: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Company, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[builtins.str] = None,
    fullname: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inviteuser: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Plan, typing.Dict[builtins.str, typing.Any]]]]] = None,
    userprincipalname: typing.Optional[builtins.str] = None,
    usesystemgeneratepassword: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__150d8139ebf4df5af5d29f28fa1f1910b1b8b7b11016b810ac2beedbddad19f6(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88846c19ee0582093560f49ccf26fca37d97f7d86351a66e575131cb840ea01b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Company, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a73fd81ce2481dcb3ad5acb62cf0795e716bb13fa420a65411d3cf0d51e9f4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Plan, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990bd641ead4350203fa22ec2bb5b782672534fbeeac8ed9858031ed42ac95d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82efd334dd5401da7a2a6b5346392865ac08b308b2f8665f2776585aa17d5a0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8505a3f92d9d68fc559d7a845e2d58bfddbd612746d1aafa2dba64f64d9ff8b9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f738e6e2823ed5e24a9eb857ce65b716b4ccdfcbf59cc9744a996e48cd1239d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4702539bf8744be683fe18f3af94f8ee7b50471e8b555039cc4d29ad28cf82e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f44cdc71782c460d8c26f62f00f4fef6d8e3a8b3af0fbea37f85a52e3d9c449(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6241c023f5082a44e204ec5152a7c1cbe431848ea6541679f864ab16ddf069e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4fb56bc86a748b85fd4dd6faa7d0065cff6700e684216e239bb8b6adc621c65(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__297e0a19519794fc9ab18a4a6ff414a74fc710516e79dc909dba5df013d98c53(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48e255f1d45c12c665db441a33abf034d0d8fde124f003c1b36c0675c83a10ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa0bb211e071c059b41a40fa2d6f65dfb4dd3d5471b12651bc1429d3a4da39b(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2726ec494a8a9b70797cdc354356f75b5348a65d05f28b5264034d0cf127106e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8be786ed995a78656d43579fe904b57e10a396cfacf30334489457550db6c509(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afe02ce95cd636f7b16195d325aab3142850b3b69d9aa2ee4f26f31343f0e31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b3f3a93e64c7fbe96c1f92023d40a930280d18cc06d5ff9cd84bbff46db692(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d690a34f46648f14e0267ef7be54f14aa1814dc2a701ce788dab010722cbe8(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6bcdbd527167480936de05de43139fef4e3d3573b8f3801a430c2958eb4e6ef(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Company]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e51e3274ec4dfd373b2f2b601d9781bc746a7b7ba45cd5e7333e752b3ab81a44(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c211b66fe86b35b318fad90cb0c77e3ed5fddab3a220761a5fa70425037f8c3d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52f3158f7e6f94107c72370ecc70f7484199e2327228a1b437ea962d8ada88e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30d9297250b18d423588fafa2b7aceb1fc70e11c22aa19567ec0d8427c0a645b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Company]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8455bff84f0f8f951e6e4b4da5ee107cb71132489100a107cc2ca59df52a3a(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    email: builtins.str,
    authenticationmethod: typing.Optional[builtins.str] = None,
    company: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Company, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enabled: typing.Optional[builtins.str] = None,
    fullname: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    inviteuser: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    plan: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[UserV2Plan, typing.Dict[builtins.str, typing.Any]]]]] = None,
    userprincipalname: typing.Optional[builtins.str] = None,
    usesystemgeneratepassword: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f3f95d00ac38e0a556ad046ba44bfaed6d06c7d06a8c423c107092a0e7d469a(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1431d9a18f47adee3c5f1e3da4e16312501659e160e0260f08eec55a20842916(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ae9eb45f4aafff632444a3386eb4c28b838584b7470d7722df7254cc2388662(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__179023d3f6e7b8f6e9c6ab38c3a532ccaf203c5f999b7f83c84b3a87ba1ba01b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c154e587d3ea6fe5e92b24e0e6241b430e125fc2c8d3d5e2c700cb15b9263d6(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23bc97150047395de57ca721f8d9670f95496b35f4891e9a4bf283eb483f4545(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4718f53448fea4bc808d2a0f5bab01b7f079e9132e36611ea621bf6c3a8959ba(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[UserV2Plan]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699e88fb385f51330388304f2f146c8f29a18ced2f035a8ecf38b0fded9f219b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d0743dea483af0647cf9a0c7468c602a63c377e2159ff2d05edd4630ef914a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af91290e5b145c3e0da19b2fcaec4a4dfe5581dfd0c941ab2b4ca6b1f58dd87b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dec192db4840a5dbb3426f4d3188dfc3095afb4b3f05f478d77c51276d613227(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, UserV2Plan]],
) -> None:
    """Type checking stubs"""
    pass
