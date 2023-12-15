from pulumi import export, Output
from typing import Dict, List

from ..resources.alb import(
    TargetGroupArgs,
    TargetGroupBuild,
    getTargetGroup
)

from ..resources.region_zone import GetRegionShortAWSNew

class CreateTargetGroupB:
    def pulumi_builder(data_conf: Dict) -> List[Output[object]]:
        
         ### VARS ###
        targetGroupArgs = data_conf["targetGroupArgs"]
        region_short = GetRegionShortAWSNew.get_regionshort(data_conf["region"])

        ### VARS TO EXPORT ###
        aws_targetGroup = None

        ### GENERATE Listener ### 
        if targetGroupArgs["targetGroupId"] is None:
            targetGroup = TargetGroupBuild(
                "aws target group",
                TargetGroupArgs(
                    project_name= data_conf["project_name"], 
                    region_short= region_short,
                    environment= data_conf["environment"], 
                    opts = targetGroupArgs["opts"],
                    connection_termination = targetGroupArgs["connection_termination"],
                    deregistration_delay = targetGroupArgs["deregistration_delay"],
                    health_check = targetGroupArgs["health_check"],
                    ip_address_type = targetGroupArgs["ip_address_type"],
                    lambda_multi_value_headers_enabled = targetGroupArgs["lambda_multi_value_headers_enabled"],
                    load_balancing_algorithm_type = targetGroupArgs["load_balancing_algorithm_type"],
                    load_balancing_cross_zone_enabled = targetGroupArgs["load_balancing_cross_zone_enabled"],
                    name = targetGroupArgs["name"],
                    name_prefix = targetGroupArgs["name_prefix"],
                    port = targetGroupArgs["port"],
                    preserve_client_ip = targetGroupArgs["preserve_client_ip"],
                    protocol = targetGroupArgs["protocol"],
                    protocol_version = targetGroupArgs["protocol_version"],
                    proxy_protocol_v2 = targetGroupArgs["proxy_protocol_v2"],
                    slow_start = targetGroupArgs["slow_start"],
                    stickiness = targetGroupArgs["stickiness"],
                    tags = targetGroupArgs["tags"],
                    target_failovers = targetGroupArgs["target_failovers"],
                    target_health_states = targetGroupArgs["target_health_states"],
                    target_type = targetGroupArgs["target_type"],
                    vpc_id = targetGroupArgs["vpc_id"],
                )
            ).targetGroup

            aws_targetGroup = Output.format("{0} | {1}", targetGroup.id, targetGroup.arn )
        
        else:
            targetGroup = getTargetGroup(
                id = targetGroupArgs["targetGroupId"],
                resource_name = "aws target group"
            )
        
        export("AWS Target group: ", aws_targetGroup)
        return targetGroup, aws_targetGroup