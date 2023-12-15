from pulumi import export, Output
from typing import Dict, List

from ..resources.alb import(
    LoadBalancerArgs,
    LoadBalancerBuild,
    getLoadBalancer
)

from ..resources.region_zone import GetRegionShortAWSNew

class CreateLoadBalancerB:
     def pulumi_builder(data_conf: Dict) -> List[Output[object]]:
          
        ### VARS ###
        loadBalancerArgs = data_conf["loadBalancerArgs"]
        region_short = GetRegionShortAWSNew.get_regionshort(data_conf["region"])

        ### VARS TO EXPORT ###
        aws_loadBalancer = None

        ### GENERATE Load Balancer ### 
        if loadBalancerArgs["loadBalancerId"] is None:
            loadBalancer = LoadBalancerBuild(
                "aws loadbalancer",
                LoadBalancerArgs(
                    project_name= data_conf["project_name"], 
                    region_short= region_short,
                    environment= data_conf["environment"], 
                    #resource_name = loadBalancerArgs["resource_name"],
                    opts = loadBalancerArgs["opts"],
                    access_logs = loadBalancerArgs["access_logs"],
                    customer_owned_ipv4_pool = loadBalancerArgs["customer_owned_ipv4_pool"],
                    desync_mitigation_mode = loadBalancerArgs["desync_mitigation_mode"],
                    dns_record_client_routing_policy = loadBalancerArgs["dns_record_client_routing_policy"],
                    drop_invalid_header_fields = loadBalancerArgs["drop_invalid_header_fields"],
                    enable_cross_zone_load_balancing = loadBalancerArgs["enable_cross_zone_load_balancing"],
                    enable_deletion_protection = loadBalancerArgs["enable_deletion_protection"],
                    enable_http2 = loadBalancerArgs["enable_http2"],
                    enable_tls_version_and_cipher_suite_headers = loadBalancerArgs["enable_tls_version_and_cipher_suite_headers"],
                    enable_waf_fail_open = loadBalancerArgs["enable_waf_fail_open"],
                    enable_xff_client_port = loadBalancerArgs["enable_xff_client_port"],
                    idle_timeout = loadBalancerArgs["idle_timeout"],
                    internal = loadBalancerArgs["internal"],
                    ip_address_type = loadBalancerArgs["ip_address_type"],
                    load_balancer_type = loadBalancerArgs["load_balancer_type"],
                    name = loadBalancerArgs["name"],
                    name_prefix = loadBalancerArgs["name_prefix"],
                    preserve_host_header = loadBalancerArgs["preserve_host_header"],
                    security_groups = loadBalancerArgs["security_groups"],
                    subnet_mappings = loadBalancerArgs["subnet_mappings"],
                    subnets = loadBalancerArgs["subnets"],
                    tags = loadBalancerArgs["tags"],
                    xff_header_processing_mode = loadBalancerArgs["xff_header_processing_mode"],
                    )
            ).aws_loadBalancer

            aws_loadBalancer = Output.format("{0} | {1}", loadBalancer.id, loadBalancer.arn )
        
        else:
            loadBalancer = getLoadBalancer(
                id = loadBalancerArgs["loadBalancerId"],
                resource_name = "aws loadbalancer"
            )
        
        export("AWS Load Balancer: ", aws_loadBalancer)
        return loadBalancer, aws_loadBalancer