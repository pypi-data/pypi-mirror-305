'''
# `commvault_storage_cloud_bucket_s3`

Refer to the Terraform Registry for docs: [`commvault_storage_cloud_bucket_s3`](https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3).
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


class StorageCloudBucketS3(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3",
):
    '''Represents a {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3 commvault_storage_cloud_bucket_s3}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        authentication: builtins.str,
        bucket: builtins.str,
        cloudstorageid: jsii.Number,
        mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Mediaagent", typing.Dict[builtins.str, typing.Any]]]],
        servicehost: builtins.str,
        storageclass: builtins.str,
        access: typing.Optional[builtins.str] = None,
        arnrole: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Configuration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Credentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        proxyaddress: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3 commvault_storage_cloud_bucket_s3} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param authentication: Authentication type for the cloud storage server [Access and secret keys, AWS IAM role policy, AWS STS assume role, AWS STS assume role with IAM role policy]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#authentication StorageCloudBucketS3#authentication}
        :param bucket: Name of bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#bucket StorageCloudBucketS3#bucket}
        :param cloudstorageid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#cloudstorageid StorageCloudBucketS3#cloudstorageid}.
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#mediaagent StorageCloudBucketS3#mediaagent}
        :param servicehost: IP address or fully qualified domain name or URL for the cloud library based on cloud vendor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#servicehost StorageCloudBucketS3#servicehost}
        :param storageclass: Appropriate storage class for your account [Standard, Reduced Redundancy Storage, Standard - Infrequent access, One zone - Infrequent access, Intelligent tiering, S3 Glacier, Standard/Glacier (Combined Storage Tiers), Standard-IA/Glacier (Combined Storage Tiers), One Zone-IA/Glacier (Combined Storage Tiers), Intelligent-Tiering/Glacier (Combined Storage Tiers), S3 Glacier Deep Archive, Standard/Deep Archive (Combined Storage Tiers), Standard-IA/Deep Archive (Combined Storage Tiers), One Zone-IA/Deep Archive (Combined Storage Tiers), Intelligent-Tiering/Deep Archive (Combined Storage Tiers)]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#storageclass StorageCloudBucketS3#storageclass}
        :param access: The access type for the access path can be either read (writing to path not allowed) or read and write (writing to path allowed). [READ_AND_WRITE, READ] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#access StorageCloudBucketS3#access}
        :param arnrole: Needed for AWS STS assume role and AWS STS assume role with IAM role policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#arnrole StorageCloudBucketS3#arnrole}
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#configuration StorageCloudBucketS3#configuration}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#credentials StorageCloudBucketS3#credentials}
        :param enable: Enable/Disable access of bucket to a media Agent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#enable StorageCloudBucketS3#enable}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Password for proxy configuration (Should be in Base64 format). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#password StorageCloudBucketS3#password}
        :param port: Port for proxy configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#port StorageCloudBucketS3#port}
        :param proxyaddress: If the MediaAgent accesses the mount path using a proxy then proxy server address needs to be provided. If you want to remove proxy information, pass empty string in proxyAddress. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#proxyaddress StorageCloudBucketS3#proxyaddress}
        :param username: Username for proxy configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#username StorageCloudBucketS3#username}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2710751f842ad7cd8d762840ad946e51dc541cc940e42901e434dc7e897714e6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageCloudBucketS3Config(
            authentication=authentication,
            bucket=bucket,
            cloudstorageid=cloudstorageid,
            mediaagent=mediaagent,
            servicehost=servicehost,
            storageclass=storageclass,
            access=access,
            arnrole=arnrole,
            configuration=configuration,
            credentials=credentials,
            enable=enable,
            id=id,
            password=password,
            port=port,
            proxyaddress=proxyaddress,
            username=username,
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
        '''Generates CDKTF code for importing a StorageCloudBucketS3 resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the StorageCloudBucketS3 to import.
        :param import_from_id: The id of the existing StorageCloudBucketS3 that should be imported. Refer to the {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the StorageCloudBucketS3 to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7a808b5c90085d269b026545898e3348298374bf564e1977da13103923ab9bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putConfiguration")
    def put_configuration(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Configuration", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c6c7e8e61090d3ab9836b623162a95ca2b1be331eb3fa31fb4c9c254fe2a606)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConfiguration", [value]))

    @jsii.member(jsii_name="putCredentials")
    def put_credentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Credentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23e74084d4bb2608ebe8a99cf6d7a52f3576da774f4f8d5d43ba2df1a2d9551)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCredentials", [value]))

    @jsii.member(jsii_name="putMediaagent")
    def put_mediaagent(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Mediaagent", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52fcff3541a9e29550852e4bd7400e3d68cd28a72e5b8d4d4ad7e4b03fe28665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMediaagent", [value]))

    @jsii.member(jsii_name="resetAccess")
    def reset_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccess", []))

    @jsii.member(jsii_name="resetArnrole")
    def reset_arnrole(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArnrole", []))

    @jsii.member(jsii_name="resetConfiguration")
    def reset_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfiguration", []))

    @jsii.member(jsii_name="resetCredentials")
    def reset_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCredentials", []))

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetProxyaddress")
    def reset_proxyaddress(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxyaddress", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

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
    @jsii.member(jsii_name="configuration")
    def configuration(self) -> "StorageCloudBucketS3ConfigurationList":
        return typing.cast("StorageCloudBucketS3ConfigurationList", jsii.get(self, "configuration"))

    @builtins.property
    @jsii.member(jsii_name="credentials")
    def credentials(self) -> "StorageCloudBucketS3CredentialsList":
        return typing.cast("StorageCloudBucketS3CredentialsList", jsii.get(self, "credentials"))

    @builtins.property
    @jsii.member(jsii_name="mediaagent")
    def mediaagent(self) -> "StorageCloudBucketS3MediaagentList":
        return typing.cast("StorageCloudBucketS3MediaagentList", jsii.get(self, "mediaagent"))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="arnroleInput")
    def arnrole_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "arnroleInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationInput")
    def authentication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketInput")
    def bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudstorageidInput")
    def cloudstorageid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cloudstorageidInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationInput")
    def configuration_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Configuration"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Configuration"]]], jsii.get(self, "configurationInput"))

    @builtins.property
    @jsii.member(jsii_name="credentialsInput")
    def credentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Credentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Credentials"]]], jsii.get(self, "credentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="mediaagentInput")
    def mediaagent_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Mediaagent"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Mediaagent"]]], jsii.get(self, "mediaagentInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="proxyaddressInput")
    def proxyaddress_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "proxyaddressInput"))

    @builtins.property
    @jsii.member(jsii_name="servicehostInput")
    def servicehost_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicehostInput"))

    @builtins.property
    @jsii.member(jsii_name="storageclassInput")
    def storageclass_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageclassInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "access"))

    @access.setter
    def access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__575f5262e262f756b30253f208378d52e93507359897e1240ff0cae015d0978b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="arnrole")
    def arnrole(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arnrole"))

    @arnrole.setter
    def arnrole(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__907ecddd03d7757595d4bf7ea2c0cbf4159911b0a3f664f4685d189b703eec7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "arnrole", value)

    @builtins.property
    @jsii.member(jsii_name="authentication")
    def authentication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authentication"))

    @authentication.setter
    def authentication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d673474ba9fe1778362f08b4159c2d728bf1439488bd4753f71e33c62230ac56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authentication", value)

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucket"))

    @bucket.setter
    def bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8063971343171579097683f6556221e977359aa01596d5da8815e88dd404bab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucket", value)

    @builtins.property
    @jsii.member(jsii_name="cloudstorageid")
    def cloudstorageid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cloudstorageid"))

    @cloudstorageid.setter
    def cloudstorageid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8354b70e80319500ff810a97b0ac49fe4d1f5a498ca754b07505eec12af66b7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cloudstorageid", value)

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b893b46fd646e0eeb28863bd6e418af8fbcaacb77b801e7c1e5ec56498a1b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3699d937099d2c2a238f4ea320a2da9855c78d29bc8fccd5b81981b565cb87fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f28604f4d27f6303853e9cf584c20f337e3a2694918c5c62523daaa4ad0be02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0027076e1bc0bfb5274d3cdc45f684623c2cefac8ce60179114ac16959231f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="proxyaddress")
    def proxyaddress(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proxyaddress"))

    @proxyaddress.setter
    def proxyaddress(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__680ce2e9e250f7d3bd24cad65a1a9a16dbe8886941868eb582de3f18ca157aad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyaddress", value)

    @builtins.property
    @jsii.member(jsii_name="servicehost")
    def servicehost(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicehost"))

    @servicehost.setter
    def servicehost(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36101af172941b422e09efa024ed803b5324f61aec2494191eb287c307307197)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicehost", value)

    @builtins.property
    @jsii.member(jsii_name="storageclass")
    def storageclass(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageclass"))

    @storageclass.setter
    def storageclass(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__107fc49eca3b16964f2006090ede6d10e31cb29b3c73c3406e619be63b190f19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageclass", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0edaa837d5f541c6c4906ef418b70359b1b98d205959a1ca6febe1234cac4b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3Config",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "authentication": "authentication",
        "bucket": "bucket",
        "cloudstorageid": "cloudstorageid",
        "mediaagent": "mediaagent",
        "servicehost": "servicehost",
        "storageclass": "storageclass",
        "access": "access",
        "arnrole": "arnrole",
        "configuration": "configuration",
        "credentials": "credentials",
        "enable": "enable",
        "id": "id",
        "password": "password",
        "port": "port",
        "proxyaddress": "proxyaddress",
        "username": "username",
    },
)
class StorageCloudBucketS3Config(_cdktf_9a9027ec.TerraformMetaArguments):
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
        authentication: builtins.str,
        bucket: builtins.str,
        cloudstorageid: jsii.Number,
        mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Mediaagent", typing.Dict[builtins.str, typing.Any]]]],
        servicehost: builtins.str,
        storageclass: builtins.str,
        access: typing.Optional[builtins.str] = None,
        arnrole: typing.Optional[builtins.str] = None,
        configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Configuration", typing.Dict[builtins.str, typing.Any]]]]] = None,
        credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3Credentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
        enable: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        proxyaddress: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param authentication: Authentication type for the cloud storage server [Access and secret keys, AWS IAM role policy, AWS STS assume role, AWS STS assume role with IAM role policy]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#authentication StorageCloudBucketS3#authentication}
        :param bucket: Name of bucket. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#bucket StorageCloudBucketS3#bucket}
        :param cloudstorageid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#cloudstorageid StorageCloudBucketS3#cloudstorageid}.
        :param mediaagent: mediaagent block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#mediaagent StorageCloudBucketS3#mediaagent}
        :param servicehost: IP address or fully qualified domain name or URL for the cloud library based on cloud vendor. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#servicehost StorageCloudBucketS3#servicehost}
        :param storageclass: Appropriate storage class for your account [Standard, Reduced Redundancy Storage, Standard - Infrequent access, One zone - Infrequent access, Intelligent tiering, S3 Glacier, Standard/Glacier (Combined Storage Tiers), Standard-IA/Glacier (Combined Storage Tiers), One Zone-IA/Glacier (Combined Storage Tiers), Intelligent-Tiering/Glacier (Combined Storage Tiers), S3 Glacier Deep Archive, Standard/Deep Archive (Combined Storage Tiers), Standard-IA/Deep Archive (Combined Storage Tiers), One Zone-IA/Deep Archive (Combined Storage Tiers), Intelligent-Tiering/Deep Archive (Combined Storage Tiers)]. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#storageclass StorageCloudBucketS3#storageclass}
        :param access: The access type for the access path can be either read (writing to path not allowed) or read and write (writing to path allowed). [READ_AND_WRITE, READ] Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#access StorageCloudBucketS3#access}
        :param arnrole: Needed for AWS STS assume role and AWS STS assume role with IAM role policy. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#arnrole StorageCloudBucketS3#arnrole}
        :param configuration: configuration block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#configuration StorageCloudBucketS3#configuration}
        :param credentials: credentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#credentials StorageCloudBucketS3#credentials}
        :param enable: Enable/Disable access of bucket to a media Agent. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#enable StorageCloudBucketS3#enable}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param password: Password for proxy configuration (Should be in Base64 format). Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#password StorageCloudBucketS3#password}
        :param port: Port for proxy configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#port StorageCloudBucketS3#port}
        :param proxyaddress: If the MediaAgent accesses the mount path using a proxy then proxy server address needs to be provided. If you want to remove proxy information, pass empty string in proxyAddress. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#proxyaddress StorageCloudBucketS3#proxyaddress}
        :param username: Username for proxy configuration. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#username StorageCloudBucketS3#username}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__625d0ff100073a920556560d6338556bdd4d75849bf3a080bd6c37b5c4aa7685)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument authentication", value=authentication, expected_type=type_hints["authentication"])
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument cloudstorageid", value=cloudstorageid, expected_type=type_hints["cloudstorageid"])
            check_type(argname="argument mediaagent", value=mediaagent, expected_type=type_hints["mediaagent"])
            check_type(argname="argument servicehost", value=servicehost, expected_type=type_hints["servicehost"])
            check_type(argname="argument storageclass", value=storageclass, expected_type=type_hints["storageclass"])
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument arnrole", value=arnrole, expected_type=type_hints["arnrole"])
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument credentials", value=credentials, expected_type=type_hints["credentials"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument proxyaddress", value=proxyaddress, expected_type=type_hints["proxyaddress"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication": authentication,
            "bucket": bucket,
            "cloudstorageid": cloudstorageid,
            "mediaagent": mediaagent,
            "servicehost": servicehost,
            "storageclass": storageclass,
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
        if access is not None:
            self._values["access"] = access
        if arnrole is not None:
            self._values["arnrole"] = arnrole
        if configuration is not None:
            self._values["configuration"] = configuration
        if credentials is not None:
            self._values["credentials"] = credentials
        if enable is not None:
            self._values["enable"] = enable
        if id is not None:
            self._values["id"] = id
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if proxyaddress is not None:
            self._values["proxyaddress"] = proxyaddress
        if username is not None:
            self._values["username"] = username

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
    def authentication(self) -> builtins.str:
        '''Authentication type for the cloud storage server [Access and secret keys, AWS IAM role policy, AWS STS assume role, AWS STS assume role with IAM role policy].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#authentication StorageCloudBucketS3#authentication}
        '''
        result = self._values.get("authentication")
        assert result is not None, "Required property 'authentication' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bucket(self) -> builtins.str:
        '''Name of bucket.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#bucket StorageCloudBucketS3#bucket}
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloudstorageid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#cloudstorageid StorageCloudBucketS3#cloudstorageid}.'''
        result = self._values.get("cloudstorageid")
        assert result is not None, "Required property 'cloudstorageid' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def mediaagent(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Mediaagent"]]:
        '''mediaagent block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#mediaagent StorageCloudBucketS3#mediaagent}
        '''
        result = self._values.get("mediaagent")
        assert result is not None, "Required property 'mediaagent' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Mediaagent"]], result)

    @builtins.property
    def servicehost(self) -> builtins.str:
        '''IP address or fully qualified domain name or URL for the cloud library based on cloud vendor.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#servicehost StorageCloudBucketS3#servicehost}
        '''
        result = self._values.get("servicehost")
        assert result is not None, "Required property 'servicehost' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storageclass(self) -> builtins.str:
        '''Appropriate storage class for your account [Standard, Reduced Redundancy Storage, Standard - Infrequent access, One zone - Infrequent access, Intelligent tiering, S3 Glacier, Standard/Glacier (Combined Storage Tiers), Standard-IA/Glacier (Combined Storage Tiers), One Zone-IA/Glacier (Combined Storage Tiers), Intelligent-Tiering/Glacier (Combined Storage Tiers), S3 Glacier Deep Archive, Standard/Deep Archive (Combined Storage Tiers), Standard-IA/Deep Archive (Combined Storage Tiers), One Zone-IA/Deep Archive (Combined Storage Tiers), Intelligent-Tiering/Deep Archive (Combined Storage Tiers)].

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#storageclass StorageCloudBucketS3#storageclass}
        '''
        result = self._values.get("storageclass")
        assert result is not None, "Required property 'storageclass' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access(self) -> typing.Optional[builtins.str]:
        '''The access type for the access path can be either read (writing to path not allowed) or read and write (writing to path allowed).

        [READ_AND_WRITE, READ]

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#access StorageCloudBucketS3#access}
        '''
        result = self._values.get("access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def arnrole(self) -> typing.Optional[builtins.str]:
        '''Needed for AWS STS assume role and AWS STS assume role with IAM role policy.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#arnrole StorageCloudBucketS3#arnrole}
        '''
        result = self._values.get("arnrole")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def configuration(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Configuration"]]]:
        '''configuration block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#configuration StorageCloudBucketS3#configuration}
        '''
        result = self._values.get("configuration")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Configuration"]]], result)

    @builtins.property
    def credentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Credentials"]]]:
        '''credentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#credentials StorageCloudBucketS3#credentials}
        '''
        result = self._values.get("credentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3Credentials"]]], result)

    @builtins.property
    def enable(self) -> typing.Optional[builtins.str]:
        '''Enable/Disable access of bucket to a media Agent.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#enable StorageCloudBucketS3#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Password for proxy configuration (Should be in Base64 format).

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#password StorageCloudBucketS3#password}
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Port for proxy configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#port StorageCloudBucketS3#port}
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def proxyaddress(self) -> typing.Optional[builtins.str]:
        '''If the MediaAgent accesses the mount path using a proxy then proxy server address needs to be provided.

        If you want to remove proxy information, pass empty string in proxyAddress.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#proxyaddress StorageCloudBucketS3#proxyaddress}
        '''
        result = self._values.get("proxyaddress")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Username for proxy configuration.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#username StorageCloudBucketS3#username}
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudBucketS3Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3Configuration",
    jsii_struct_bases=[],
    name_mapping={
        "disablebackuplocationforfuturebackups": "disablebackuplocationforfuturebackups",
        "enable": "enable",
        "prepareforretirement": "prepareforretirement",
        "storageacceleratorcredentials": "storageacceleratorcredentials",
    },
)
class StorageCloudBucketS3Configuration:
    def __init__(
        self,
        *,
        disablebackuplocationforfuturebackups: typing.Optional[builtins.str] = None,
        enable: typing.Optional[builtins.str] = None,
        prepareforretirement: typing.Optional[builtins.str] = None,
        storageacceleratorcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3ConfigurationStorageacceleratorcredentials", typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param disablebackuplocationforfuturebackups: When true, prevents new data writes to backup location by changing number of writers to zero. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#disablebackuplocationforfuturebackups StorageCloudBucketS3#disablebackuplocationforfuturebackups}
        :param enable: When true, means mount path is enabled. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#enable StorageCloudBucketS3#enable}
        :param prepareforretirement: When true, the deduplicated blocks in the mount path will not be referenced when there are multiple mount paths in the library. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#prepareforretirement StorageCloudBucketS3#prepareforretirement}
        :param storageacceleratorcredentials: storageacceleratorcredentials block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#storageacceleratorcredentials StorageCloudBucketS3#storageacceleratorcredentials}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68fb28b75211819bbdf1dc3a6b3dc100815186cce434b8ca09d702fec8ef0803)
            check_type(argname="argument disablebackuplocationforfuturebackups", value=disablebackuplocationforfuturebackups, expected_type=type_hints["disablebackuplocationforfuturebackups"])
            check_type(argname="argument enable", value=enable, expected_type=type_hints["enable"])
            check_type(argname="argument prepareforretirement", value=prepareforretirement, expected_type=type_hints["prepareforretirement"])
            check_type(argname="argument storageacceleratorcredentials", value=storageacceleratorcredentials, expected_type=type_hints["storageacceleratorcredentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if disablebackuplocationforfuturebackups is not None:
            self._values["disablebackuplocationforfuturebackups"] = disablebackuplocationforfuturebackups
        if enable is not None:
            self._values["enable"] = enable
        if prepareforretirement is not None:
            self._values["prepareforretirement"] = prepareforretirement
        if storageacceleratorcredentials is not None:
            self._values["storageacceleratorcredentials"] = storageacceleratorcredentials

    @builtins.property
    def disablebackuplocationforfuturebackups(self) -> typing.Optional[builtins.str]:
        '''When true, prevents new data writes to backup location by changing number of writers to zero.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#disablebackuplocationforfuturebackups StorageCloudBucketS3#disablebackuplocationforfuturebackups}
        '''
        result = self._values.get("disablebackuplocationforfuturebackups")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable(self) -> typing.Optional[builtins.str]:
        '''When true, means mount path is enabled.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#enable StorageCloudBucketS3#enable}
        '''
        result = self._values.get("enable")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prepareforretirement(self) -> typing.Optional[builtins.str]:
        '''When true, the deduplicated blocks in the mount path will not be referenced when there are multiple mount paths in the library.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#prepareforretirement StorageCloudBucketS3#prepareforretirement}
        '''
        result = self._values.get("prepareforretirement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storageacceleratorcredentials(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3ConfigurationStorageacceleratorcredentials"]]]:
        '''storageacceleratorcredentials block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#storageacceleratorcredentials StorageCloudBucketS3#storageacceleratorcredentials}
        '''
        result = self._values.get("storageacceleratorcredentials")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3ConfigurationStorageacceleratorcredentials"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudBucketS3Configuration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudBucketS3ConfigurationList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3ConfigurationList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c90bec667d5bf0861cb17ee5d79b629f24f5f3bc093ac6db4344e7e1d571aafa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudBucketS3ConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c6375bfe7b7458da929b65473c79cb875b58a671aae4bdd0dcec75b58c793d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudBucketS3ConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e6ccd7b94b5b8d2bd1f411d678aae57fe1cb76ae33a5088e576990bd14f4e8d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__242b6e3864f25480342ab20daa1e0d7c2f7aae80bbdd1a9f7a2f5280a160e39d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c0e4414b23fed117560d72267b01c5dafcd3bf4d116136646fb73d23d44de996)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Configuration]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Configuration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Configuration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1891715e23304707f9aad7d974412c492998c0a7052c5414fad0711d5281d91f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudBucketS3ConfigurationOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3ConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__36a105504c709b18a3f7b0ecc7582fe50038c481180ce16038f38703f0d9a56b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putStorageacceleratorcredentials")
    def put_storageacceleratorcredentials(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["StorageCloudBucketS3ConfigurationStorageacceleratorcredentials", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c77a2c386e2ae0d539a8d22411f07dbef665e36b6ef654a53aab052130778d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorageacceleratorcredentials", [value]))

    @jsii.member(jsii_name="resetDisablebackuplocationforfuturebackups")
    def reset_disablebackuplocationforfuturebackups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisablebackuplocationforfuturebackups", []))

    @jsii.member(jsii_name="resetEnable")
    def reset_enable(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnable", []))

    @jsii.member(jsii_name="resetPrepareforretirement")
    def reset_prepareforretirement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrepareforretirement", []))

    @jsii.member(jsii_name="resetStorageacceleratorcredentials")
    def reset_storageacceleratorcredentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageacceleratorcredentials", []))

    @builtins.property
    @jsii.member(jsii_name="storageacceleratorcredentials")
    def storageacceleratorcredentials(
        self,
    ) -> "StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsList":
        return typing.cast("StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsList", jsii.get(self, "storageacceleratorcredentials"))

    @builtins.property
    @jsii.member(jsii_name="disablebackuplocationforfuturebackupsInput")
    def disablebackuplocationforfuturebackups_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "disablebackuplocationforfuturebackupsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableInput")
    def enable_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableInput"))

    @builtins.property
    @jsii.member(jsii_name="prepareforretirementInput")
    def prepareforretirement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prepareforretirementInput"))

    @builtins.property
    @jsii.member(jsii_name="storageacceleratorcredentialsInput")
    def storageacceleratorcredentials_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3ConfigurationStorageacceleratorcredentials"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["StorageCloudBucketS3ConfigurationStorageacceleratorcredentials"]]], jsii.get(self, "storageacceleratorcredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="disablebackuplocationforfuturebackups")
    def disablebackuplocationforfuturebackups(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "disablebackuplocationforfuturebackups"))

    @disablebackuplocationforfuturebackups.setter
    def disablebackuplocationforfuturebackups(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07986ecc26d47205410d78d0a9de657e27817c3bf61cef956e001538f707db1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disablebackuplocationforfuturebackups", value)

    @builtins.property
    @jsii.member(jsii_name="enable")
    def enable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enable"))

    @enable.setter
    def enable(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__432d1918980ff078a68e5e1465a9036f6b33fcdbfb946e20da5f6e532c0bcb33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enable", value)

    @builtins.property
    @jsii.member(jsii_name="prepareforretirement")
    def prepareforretirement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prepareforretirement"))

    @prepareforretirement.setter
    def prepareforretirement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__311327d87453bbd8bc16834485aa43b24233c46462b74666e5f4214c6a71c88f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prepareforretirement", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Configuration]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Configuration]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Configuration]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843859ccb795bb5c3c5892cc4548be8298c9fdb1a37033143af27d22d41478e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3ConfigurationStorageacceleratorcredentials",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudBucketS3ConfigurationStorageacceleratorcredentials:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#name StorageCloudBucketS3#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903968a347af26ba2404cfcc54956aaf777f736a955eea00942dd70b528e8c69)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#name StorageCloudBucketS3#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudBucketS3ConfigurationStorageacceleratorcredentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dc03e982b7683797670b5bd13bcc3835e34167eef1241dcfe401aaa0c6e19c24)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f7921e7804bd97c74c7aec9d20ebce684b4077af1d422344e445a39e31d423)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a81ba43ad733f0f74af2178758cab525e849b3d84a56deca63d5c72aa36f17ae)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85f8ca763926f49eaadffc69d3bc721b12399bfe5124f2e1851d11149b93a5e0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cdfbf42b034b16ab320fe777ef8f05f1a41effd856146728fc4793651bf04bf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a59aa15bf36b7a1add37b2acd8edadddd12343717a8fed7b9f1361d892c06060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__0e4339b870bb9069381c3bafffca36076932ade6503a1295ba5eccf313a542b0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a2c06b5842a8743f9c4b8adba321cbef4ae01007105cbd5f1f4174c3d5ab5611)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75ac0ed4785bc83a4b8d66eb60530f992fc4bf6595d901eec8d8112d3d5adc79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c99b55c510f7075df95be0946cc1e678f0bb4f63908b2a8cb470cc10241bb4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3Credentials",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudBucketS3Credentials:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#name StorageCloudBucketS3#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e04ffa618eccbca7e5c78edc3e001755e9ee7fc25bc01ebc100e0bda125bfef7)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#name StorageCloudBucketS3#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudBucketS3Credentials(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudBucketS3CredentialsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3CredentialsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__dbd87e85be23159155033bd772e02be147a4be0fccf3702d8bf075e86f2994a0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudBucketS3CredentialsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f6f2b503d4416ba66d7b2fd5461b98577af97ef4366d42df033649154f8d0ab)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudBucketS3CredentialsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__076c7851e246d9c4a0add90ea153bc7fb5380b319bb445644281bfbea5657b31)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f562849208824cbc5405d77ca619252a1f1adb863a7e93467d5f9eb1d0972dd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__791e01dbc1e43f5f00495dc5f31f89e51507d4eb33b54d8dca6d14893bf4d913)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Credentials]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Credentials]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Credentials]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74ed0b5bf4971277b69fb78128b47a13bea156cf73f912e792eaca7af007af6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudBucketS3CredentialsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3CredentialsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__802330c7016dedbcf4a3abea8883e35fd67e273e142d07acf04fec7774881d58)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2f2efe26ef0331008e6eba6279bca3aace4a6b503b763011b08c3bd13f367a62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdaa0a379b33efcd42a2d118d8fe3b6c362ac1f4de06fe40b0e1774cc36f0437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Credentials]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Credentials]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Credentials]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1afda9fce42e326cae816a960bc8e962511f18ac945c44e4d33a58922ea118)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3Mediaagent",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "name": "name"},
)
class StorageCloudBucketS3Mediaagent:
    def __init__(
        self,
        *,
        id: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#name StorageCloudBucketS3#name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40847f933029993fe3c5fe00b4124654a765e914ed85f671cc3ff08d636bcb71)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def id(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#id StorageCloudBucketS3#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/commvault/commvault/1.2.10/docs/resources/storage_cloud_bucket_s3#name StorageCloudBucketS3#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageCloudBucketS3Mediaagent(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloudBucketS3MediaagentList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3MediaagentList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a3253ed9af7302d925f9ec6a9c3e001fffef91c44d0e221358a6eccff8235e65)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "StorageCloudBucketS3MediaagentOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__250b06a447cf65cb14e7935857399e98b6d42bd9117e03461f450e5b332c6ff7)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("StorageCloudBucketS3MediaagentOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__379ffb9cbf106b95b2becbb47a3ca51696aea4650625f64246073911aa838edd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d214df1086fb96022c5fd0bafe134b852968c0d1c97279f42cd8b70c812f2ac9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fdbf975c00ec205626df10a475775355da7b8c01a2fa6ea175dd60505387b3e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Mediaagent]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Mediaagent]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Mediaagent]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3633696eef5c6fa7d2050aad7cb149bc3cb48a6e420baac0370300b83b6794e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class StorageCloudBucketS3MediaagentOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="commvault.storageCloudBucketS3.StorageCloudBucketS3MediaagentOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__82919a42f77d74e077a4c027bf791f9828d7a4fde83c60e1dd612a3a87f695da)
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
            type_hints = typing.get_type_hints(_typecheckingstub__77d71df40f18875bdac6f80d38bda6edb6d32130277242194b720372569572fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6ece608cb192c35fe8ce10cf61f331cadca43974cefd56e191bf5ec5079109f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Mediaagent]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Mediaagent]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Mediaagent]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34cc7ad8a39208848328c11a0a13b04e9fbc3eec2e50e4975e87cbfdce12aed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "StorageCloudBucketS3",
    "StorageCloudBucketS3Config",
    "StorageCloudBucketS3Configuration",
    "StorageCloudBucketS3ConfigurationList",
    "StorageCloudBucketS3ConfigurationOutputReference",
    "StorageCloudBucketS3ConfigurationStorageacceleratorcredentials",
    "StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsList",
    "StorageCloudBucketS3ConfigurationStorageacceleratorcredentialsOutputReference",
    "StorageCloudBucketS3Credentials",
    "StorageCloudBucketS3CredentialsList",
    "StorageCloudBucketS3CredentialsOutputReference",
    "StorageCloudBucketS3Mediaagent",
    "StorageCloudBucketS3MediaagentList",
    "StorageCloudBucketS3MediaagentOutputReference",
]

publication.publish()

def _typecheckingstub__2710751f842ad7cd8d762840ad946e51dc541cc940e42901e434dc7e897714e6(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    authentication: builtins.str,
    bucket: builtins.str,
    cloudstorageid: jsii.Number,
    mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Mediaagent, typing.Dict[builtins.str, typing.Any]]]],
    servicehost: builtins.str,
    storageclass: builtins.str,
    access: typing.Optional[builtins.str] = None,
    arnrole: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Configuration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Credentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enable: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    proxyaddress: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__a7a808b5c90085d269b026545898e3348298374bf564e1977da13103923ab9bd(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c6c7e8e61090d3ab9836b623162a95ca2b1be331eb3fa31fb4c9c254fe2a606(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Configuration, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23e74084d4bb2608ebe8a99cf6d7a52f3576da774f4f8d5d43ba2df1a2d9551(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Credentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52fcff3541a9e29550852e4bd7400e3d68cd28a72e5b8d4d4ad7e4b03fe28665(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Mediaagent, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__575f5262e262f756b30253f208378d52e93507359897e1240ff0cae015d0978b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__907ecddd03d7757595d4bf7ea2c0cbf4159911b0a3f664f4685d189b703eec7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d673474ba9fe1778362f08b4159c2d728bf1439488bd4753f71e33c62230ac56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8063971343171579097683f6556221e977359aa01596d5da8815e88dd404bab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8354b70e80319500ff810a97b0ac49fe4d1f5a498ca754b07505eec12af66b7e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b893b46fd646e0eeb28863bd6e418af8fbcaacb77b801e7c1e5ec56498a1b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3699d937099d2c2a238f4ea320a2da9855c78d29bc8fccd5b81981b565cb87fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f28604f4d27f6303853e9cf584c20f337e3a2694918c5c62523daaa4ad0be02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0027076e1bc0bfb5274d3cdc45f684623c2cefac8ce60179114ac16959231f0(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__680ce2e9e250f7d3bd24cad65a1a9a16dbe8886941868eb582de3f18ca157aad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36101af172941b422e09efa024ed803b5324f61aec2494191eb287c307307197(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__107fc49eca3b16964f2006090ede6d10e31cb29b3c73c3406e619be63b190f19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0edaa837d5f541c6c4906ef418b70359b1b98d205959a1ca6febe1234cac4b3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625d0ff100073a920556560d6338556bdd4d75849bf3a080bd6c37b5c4aa7685(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    authentication: builtins.str,
    bucket: builtins.str,
    cloudstorageid: jsii.Number,
    mediaagent: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Mediaagent, typing.Dict[builtins.str, typing.Any]]]],
    servicehost: builtins.str,
    storageclass: builtins.str,
    access: typing.Optional[builtins.str] = None,
    arnrole: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Configuration, typing.Dict[builtins.str, typing.Any]]]]] = None,
    credentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3Credentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
    enable: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    proxyaddress: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68fb28b75211819bbdf1dc3a6b3dc100815186cce434b8ca09d702fec8ef0803(
    *,
    disablebackuplocationforfuturebackups: typing.Optional[builtins.str] = None,
    enable: typing.Optional[builtins.str] = None,
    prepareforretirement: typing.Optional[builtins.str] = None,
    storageacceleratorcredentials: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3ConfigurationStorageacceleratorcredentials, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90bec667d5bf0861cb17ee5d79b629f24f5f3bc093ac6db4344e7e1d571aafa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c6375bfe7b7458da929b65473c79cb875b58a671aae4bdd0dcec75b58c793d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e6ccd7b94b5b8d2bd1f411d678aae57fe1cb76ae33a5088e576990bd14f4e8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242b6e3864f25480342ab20daa1e0d7c2f7aae80bbdd1a9f7a2f5280a160e39d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0e4414b23fed117560d72267b01c5dafcd3bf4d116136646fb73d23d44de996(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1891715e23304707f9aad7d974412c492998c0a7052c5414fad0711d5281d91f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Configuration]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a105504c709b18a3f7b0ecc7582fe50038c481180ce16038f38703f0d9a56b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c77a2c386e2ae0d539a8d22411f07dbef665e36b6ef654a53aab052130778d5(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[StorageCloudBucketS3ConfigurationStorageacceleratorcredentials, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07986ecc26d47205410d78d0a9de657e27817c3bf61cef956e001538f707db1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432d1918980ff078a68e5e1465a9036f6b33fcdbfb946e20da5f6e532c0bcb33(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__311327d87453bbd8bc16834485aa43b24233c46462b74666e5f4214c6a71c88f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843859ccb795bb5c3c5892cc4548be8298c9fdb1a37033143af27d22d41478e5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Configuration]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903968a347af26ba2404cfcc54956aaf777f736a955eea00942dd70b528e8c69(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc03e982b7683797670b5bd13bcc3835e34167eef1241dcfe401aaa0c6e19c24(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f7921e7804bd97c74c7aec9d20ebce684b4077af1d422344e445a39e31d423(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a81ba43ad733f0f74af2178758cab525e849b3d84a56deca63d5c72aa36f17ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f8ca763926f49eaadffc69d3bc721b12399bfe5124f2e1851d11149b93a5e0(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdfbf42b034b16ab320fe777ef8f05f1a41effd856146728fc4793651bf04bf6(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a59aa15bf36b7a1add37b2acd8edadddd12343717a8fed7b9f1361d892c06060(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e4339b870bb9069381c3bafffca36076932ade6503a1295ba5eccf313a542b0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c06b5842a8743f9c4b8adba321cbef4ae01007105cbd5f1f4174c3d5ab5611(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75ac0ed4785bc83a4b8d66eb60530f992fc4bf6595d901eec8d8112d3d5adc79(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c99b55c510f7075df95be0946cc1e678f0bb4f63908b2a8cb470cc10241bb4c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3ConfigurationStorageacceleratorcredentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04ffa618eccbca7e5c78edc3e001755e9ee7fc25bc01ebc100e0bda125bfef7(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbd87e85be23159155033bd772e02be147a4be0fccf3702d8bf075e86f2994a0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f6f2b503d4416ba66d7b2fd5461b98577af97ef4366d42df033649154f8d0ab(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__076c7851e246d9c4a0add90ea153bc7fb5380b319bb445644281bfbea5657b31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f562849208824cbc5405d77ca619252a1f1adb863a7e93467d5f9eb1d0972dd(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791e01dbc1e43f5f00495dc5f31f89e51507d4eb33b54d8dca6d14893bf4d913(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74ed0b5bf4971277b69fb78128b47a13bea156cf73f912e792eaca7af007af6e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Credentials]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802330c7016dedbcf4a3abea8883e35fd67e273e142d07acf04fec7774881d58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f2efe26ef0331008e6eba6279bca3aace4a6b503b763011b08c3bd13f367a62(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdaa0a379b33efcd42a2d118d8fe3b6c362ac1f4de06fe40b0e1774cc36f0437(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1afda9fce42e326cae816a960bc8e962511f18ac945c44e4d33a58922ea118(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Credentials]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40847f933029993fe3c5fe00b4124654a765e914ed85f671cc3ff08d636bcb71(
    *,
    id: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3253ed9af7302d925f9ec6a9c3e001fffef91c44d0e221358a6eccff8235e65(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__250b06a447cf65cb14e7935857399e98b6d42bd9117e03461f450e5b332c6ff7(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__379ffb9cbf106b95b2becbb47a3ca51696aea4650625f64246073911aa838edd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d214df1086fb96022c5fd0bafe134b852968c0d1c97279f42cd8b70c812f2ac9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdbf975c00ec205626df10a475775355da7b8c01a2fa6ea175dd60505387b3e4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3633696eef5c6fa7d2050aad7cb149bc3cb48a6e420baac0370300b83b6794e2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[StorageCloudBucketS3Mediaagent]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82919a42f77d74e077a4c027bf791f9828d7a4fde83c60e1dd612a3a87f695da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d71df40f18875bdac6f80d38bda6edb6d32130277242194b720372569572fa(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6ece608cb192c35fe8ce10cf61f331cadca43974cefd56e191bf5ec5079109f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34cc7ad8a39208848328c11a0a13b04e9fbc3eec2e50e4975e87cbfdce12aed8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, StorageCloudBucketS3Mediaagent]],
) -> None:
    """Type checking stubs"""
    pass
