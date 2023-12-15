from pulumi.output import Inputs
import pulumi_aws as aws
from pulumi import ComponentResource, ResourceOptions
from typing import Mapping, Optional, Sequence
from pulumi_aws.alb import TargetGroupHealthCheckArgs, TargetGroupStickinessArgs, TargetGroupTargetFailoverArgs, TargetGroupTargetHealthStateArgs, AwaitableGetTargetGroupResult

class TargetGroupArgs():
    def __init__(self,
            project_name: str, 
            region_short: str,
            environment: str,
            cloudbuddies: str = "True",
            department: str = "nonprod", 
            #resource_name: str,
            opts: Optional[ResourceOptions] = None,
            connection_termination: Optional[bool] = None,
            deregistration_delay: Optional[int] = None,
            health_check: Optional[TargetGroupHealthCheckArgs] = None,
            ip_address_type: Optional[str] = None,
            lambda_multi_value_headers_enabled: Optional[bool] = None,
            load_balancing_algorithm_type: Optional[str] = None,
            load_balancing_cross_zone_enabled: Optional[str] = None,
            name: Optional[str] = None,
            name_prefix: Optional[str] = None,
            port: Optional[int] = None,
            preserve_client_ip: Optional[str] = None,
            protocol: Optional[str] = None,
            protocol_version: Optional[str] = None,
            proxy_protocol_v2: Optional[bool] = None,
            slow_start: Optional[int] = None,
            stickiness: Optional[TargetGroupStickinessArgs] = None,
            tags: Optional[Mapping[str, str]] = None,
            target_failovers: Optional[Sequence[TargetGroupTargetFailoverArgs]] = None,
            target_health_states: Optional[Sequence[TargetGroupTargetHealthStateArgs]] = None,
            target_type: Optional[str] = None,
            vpc_id: Optional[str] = None
            ) -> None:
        
        self.project_name = project_name
        self.region_short = region_short
        self.cloudbuddies = cloudbuddies
        self.department = department
        self.environment = environment
        #self.resource_name = resource_name
        self.opts = opts
        self.connection_termination = connection_termination
        self.deregistration_delay = deregistration_delay
        self.health_check = health_check
        self.ip_address_type = ip_address_type
        self.lambda_multi_value_headers_enabled = lambda_multi_value_headers_enabled
        self.load_balancing_algorithm_type = load_balancing_algorithm_type
        self.load_balancing_cross_zone_enabled = load_balancing_cross_zone_enabled
        self.name = name
        self.name_prefix = name_prefix
        self.port = port
        self.preserve_client_ip = preserve_client_ip
        self.protocol = protocol
        self.protocol_version = protocol_version
        self.proxy_protocol_v2 = proxy_protocol_v2
        self.slow_start = slow_start
        self.stickiness = stickiness
        self.tags = tags
        self.target_failovers = target_failovers
        self.target_health_states = target_health_states
        self.target_type = target_type
        self.vpc_id = vpc_id



class TargetGroupBuild(ComponentResource):
    def __init__(self,
                nameResource: str,
                args: TargetGroupArgs,
                opts: ResourceOptions = None
                ):
        
        super().__init__('custom:resource:TARGETGROUP', nameResource, {}, opts) # inicializa la clase padre

        
        if args.name is None:
            args.name = f"tg-{args.project_name}-{args.environment}-{args.region_short}"
        
        if args.tags is None:
            args.tags = {
                'Name': args.name,
                'Project': args.project_name,
                'Department': args.department,
                'Cloudbuddies Archie': args.cloudbuddies,
                'Environment': args.environment
                }
            
        self.targetGroup = aws.lb.TargetGroup(
            args.name,
            opts = args.opts or ResourceOptions(parent=self),
            connection_termination = args.connection_termination,
            deregistration_delay = args.deregistration_delay,
            health_check = args.health_check,
            ip_address_type = args.ip_address_type,
            lambda_multi_value_headers_enabled = args.lambda_multi_value_headers_enabled,
            load_balancing_algorithm_type = args.load_balancing_algorithm_type,
            load_balancing_cross_zone_enabled = args.load_balancing_cross_zone_enabled,
            name = args.name,
            name_prefix = args.name_prefix,
            port = args.port,
            preserve_client_ip = args.preserve_client_ip,
            protocol = args.protocol,
            protocol_version = args.protocol_version,
            proxy_protocol_v2 = args.proxy_protocol_v2,
            slow_start = args.slow_start,
            stickiness = args.stickiness,
            tags = args.tags,
            target_failovers = args.target_failovers,
            target_health_states = args.target_health_states,
            target_type = args.target_type,
            vpc_id = args.vpc_id,
        )

        self.register_outputs({})


def getTargetGroup(
        resource_name: str,
        id: str,
        opts: Optional[ResourceOptions] = None,
        arn: Optional[str] = None,
        arn_suffix: Optional[str] = None,
        connection_termination: Optional[bool] = None,
        deregistration_delay: Optional[int] = None,
        health_check: Optional[TargetGroupHealthCheckArgs] = None,
        ip_address_type: Optional[str] = None,
        lambda_multi_value_headers_enabled: Optional[bool] = None,
        load_balancing_algorithm_type: Optional[str] = None,
        load_balancing_cross_zone_enabled: Optional[str] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        port: Optional[int] = None,
        preserve_client_ip: Optional[str] = None,
        protocol: Optional[str] = None,
        protocol_version: Optional[str] = None,
        proxy_protocol_v2: Optional[bool] = None,
        slow_start: Optional[int] = None,
        stickiness: Optional[TargetGroupStickinessArgs] = None,
        tags: Optional[Mapping[str, str]] = None,
        tags_all: Optional[Mapping[str, str]] = None,
        target_failovers: Optional[Sequence[TargetGroupTargetFailoverArgs]] = None,
        target_health_states: Optional[Sequence[TargetGroupTargetHealthStateArgs]] = None,
        target_type: Optional[str] = None,
        vpc_id: Optional[str] = None) -> AwaitableGetTargetGroupResult:
    
    return aws.alb.get_target_group(
        resource_name = resource_name,
        id = id,
        opts = opts,
        arn = arn,
        arn_suffix = arn_suffix,
        connection_termination = connection_termination,
        deregistration_delay = deregistration_delay,
        health_check = health_check,
        ip_address_type = ip_address_type,
        lambda_multi_value_headers_enabled = lambda_multi_value_headers_enabled,
        load_balancing_algorithm_type = load_balancing_algorithm_type,
        load_balancing_cross_zone_enabled = load_balancing_cross_zone_enabled,
        name = name,
        name_prefix = name_prefix,
        port = port,
        preserve_client_ip = preserve_client_ip,
        protocol = protocol,
        protocol_version = protocol_version,
        proxy_protocol_v2 = proxy_protocol_v2,
        slow_start = slow_start,
        stickiness = stickiness,
        tags = tags,
        tags_all = tags_all,
        target_failovers = target_failovers,
        target_health_states = target_health_states,
        target_type = target_type,
        vpc_id = vpc_id,
    )