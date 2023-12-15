from pulumi.output import Inputs
import pulumi_aws as aws
from pulumi import ComponentResource, ResourceOptions
from typing import Mapping, Optional, Sequence
from pulumi_aws.alb import LoadBalancerAccessLogsArgs, LoadBalancerSubnetMappingArgs, AwaitableGetLoadBalancerResult


class LoadBalancerArgs:
    def __init__(self,
            project_name: str, 
            region_short: str,
            environment: str,
            cloudbuddies: str = "True",
            department: str = "nonprod",
            resource_name: str = None,
            #resource_name: str,
            opts: Optional[ResourceOptions] = None,
            access_logs: Optional[LoadBalancerAccessLogsArgs] = None,
            customer_owned_ipv4_pool: Optional[str] = None,
            desync_mitigation_mode: Optional[str] = None,
            dns_record_client_routing_policy: Optional[str] = None,
            drop_invalid_header_fields: Optional[bool] = None,
            enable_cross_zone_load_balancing: Optional[bool] = None,
            enable_deletion_protection: Optional[bool] = None,
            enable_http2: Optional[bool] = None,
            enable_tls_version_and_cipher_suite_headers: Optional[bool] = None,
            enable_waf_fail_open: Optional[bool] = None,
            enable_xff_client_port: Optional[bool] = None,
            idle_timeout: Optional[int] = None,
            internal: Optional[bool] = None,
            ip_address_type: Optional[str] = None,
            load_balancer_type: Optional[str] = None,
            name: Optional[str] = None,
            name_prefix: Optional[str] = None,
            preserve_host_header: Optional[bool] = None,
            security_groups: Optional[Sequence[str]] = None,
            subnet_mappings: Optional[Sequence[LoadBalancerSubnetMappingArgs]] = None,
            subnets: Optional[Sequence[str]] = None,
            tags: Optional[Mapping[str, str]] = None,
            xff_header_processing_mode: Optional[str] = None
            ) -> None:
        
        self.project_name = project_name
        self.region_short = region_short
        self.environment =  environment
        self.cloudbuddies = cloudbuddies
        self.department =   department
        self.resource_name = resource_name
        #self.resource_name = resource_name
        self.opts = opts
        self.access_logs = access_logs
        self.customer_owned_ipv4_pool = customer_owned_ipv4_pool
        self.desync_mitigation_mode = desync_mitigation_mode
        self.dns_record_client_routing_policy = dns_record_client_routing_policy
        self.drop_invalid_header_fields = drop_invalid_header_fields
        self.enable_cross_zone_load_balancing = enable_cross_zone_load_balancing
        self.enable_deletion_protection = enable_deletion_protection
        self.enable_http2 = enable_http2
        self.enable_tls_version_and_cipher_suite_headers = enable_tls_version_and_cipher_suite_headers
        self.enable_waf_fail_open = enable_waf_fail_open
        self.enable_xff_client_port = enable_xff_client_port
        self.idle_timeout = idle_timeout
        self.internal = internal
        self.ip_address_type = ip_address_type
        self.load_balancer_type = load_balancer_type
        self.name = name
        self.name_prefix = name_prefix
        self.preserve_host_header = preserve_host_header
        self.security_groups = security_groups
        self.subnet_mappings = subnet_mappings
        self.subnets = subnets
        self.tags = tags
        self.xff_header_processing_mode = xff_header_processing_mode


class LoadBalancerBuild(ComponentResource):
    def __init__(
            self,
            nameResource: str,
            args: LoadBalancerArgs,
            opts: ResourceOptions = None
        ):

        super().__init__('custom:resource:LOADBALANCER', nameResource, {}, opts)


        if args.name is None:
            args.name = f"lb-{args.project_name}-{args.environment}-{args.region_short}"
        
        if args.tags is None:
            args.tags = {
                'Name': args.name,
                'Project': args.project_name,
                'Department': args.department,
                'Cloudbuddies Archie': args.cloudbuddies,
                'Environment': args.environment
            }
        
        self.aws_loadBalancer = aws.alb.LoadBalancer(
            resource_name = args.name,
            opts = args.opts,
            access_logs = args.access_logs,
            customer_owned_ipv4_pool = args.customer_owned_ipv4_pool,
            desync_mitigation_mode = args.desync_mitigation_mode,
            dns_record_client_routing_policy = args.dns_record_client_routing_policy,
            drop_invalid_header_fields = args.drop_invalid_header_fields,
            enable_cross_zone_load_balancing = args.enable_cross_zone_load_balancing,
            enable_deletion_protection = args.enable_deletion_protection,
            enable_http2 = args.enable_http2,
            enable_tls_version_and_cipher_suite_headers = args.enable_tls_version_and_cipher_suite_headers,
            enable_waf_fail_open = args.enable_waf_fail_open,
            enable_xff_client_port = args.enable_xff_client_port,
            idle_timeout = args.idle_timeout,
            internal = args.internal,
            ip_address_type = args.ip_address_type,
            load_balancer_type = args.load_balancer_type,
            name = args.name,
            name_prefix = args.name_prefix,
            preserve_host_header = args.preserve_host_header,
            security_groups = args.security_groups,
            subnet_mappings = args.subnet_mappings,
            subnets = args.subnets,
            tags = args.tags,
            xff_header_processing_mode = args.xff_header_processing_mode,
        )

        self.register_outputs({})


def getLoadBalancer(resource_name: str,
        id: str,
        opts: Optional[ResourceOptions] = None,
        access_logs: Optional[LoadBalancerAccessLogsArgs] = None,
        arn: Optional[str] = None,
        arn_suffix: Optional[str] = None,
        customer_owned_ipv4_pool: Optional[str] = None,
        desync_mitigation_mode: Optional[str] = None,
        dns_name: Optional[str] = None,
        dns_record_client_routing_policy: Optional[str] = None,
        drop_invalid_header_fields: Optional[bool] = None,
        enable_cross_zone_load_balancing: Optional[bool] = None,
        enable_deletion_protection: Optional[bool] = None,
        enable_http2: Optional[bool] = None,
        enable_tls_version_and_cipher_suite_headers: Optional[bool] = None,
        enable_waf_fail_open: Optional[bool] = None,
        enable_xff_client_port: Optional[bool] = None,
        idle_timeout: Optional[int] = None,
        internal: Optional[bool] = None,
        ip_address_type: Optional[str] = None,
        load_balancer_type: Optional[str] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        preserve_host_header: Optional[bool] = None,
        security_groups: Optional[Sequence[str]] = None,
        subnet_mappings: Optional[Sequence[LoadBalancerSubnetMappingArgs]] = None,
        subnets: Optional[Sequence[str]] = None,
        tags: Optional[Mapping[str, str]] = None,
        tags_all: Optional[Mapping[str, str]] = None,
        vpc_id: Optional[str] = None,
        xff_header_processing_mode: Optional[str] = None,
        zone_id: Optional[str] = None) -> AwaitableGetLoadBalancerResult:

        return aws.alb.get_load_balancer(
            resource_name = resource_name,
            id = id,
            opts = opts,
            access_logs = access_logs,
            arn = arn,
            arn_suffix = arn_suffix,
            customer_owned_ipv4_pool = customer_owned_ipv4_pool,
            desync_mitigation_mode = desync_mitigation_mode,
            dns_name = dns_name,
            dns_record_client_routing_policy = dns_record_client_routing_policy,
            drop_invalid_header_fields = drop_invalid_header_fields,
            enable_cross_zone_load_balancing = enable_cross_zone_load_balancing,
            enable_deletion_protection = enable_deletion_protection,
            enable_http2 = enable_http2,
            enable_tls_version_and_cipher_suite_headers = enable_tls_version_and_cipher_suite_headers,
            enable_waf_fail_open = enable_waf_fail_open,
            enable_xff_client_port = enable_xff_client_port,
            idle_timeout = idle_timeout,
            internal = internal,
            ip_address_type = ip_address_type,
            load_balancer_type = load_balancer_type,
            name = name,
            name_prefix = name_prefix,
            preserve_host_header = preserve_host_header,
            security_groups = security_groups,
            subnet_mappings = subnet_mappings,
            subnets = subnets,
            tags = tags,
            tags_all = tags_all,
            vpc_id = vpc_id,
            xff_header_processing_mode = xff_header_processing_mode,
            zone_id = zone_id,
        )