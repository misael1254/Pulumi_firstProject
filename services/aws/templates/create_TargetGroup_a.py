from .create_TargetGroup_b import CreateTargetGroupB

class CreateTargetGroupA:
    def pulumi_program(data: dict = None ) -> None:

        data_conf = {
            "project_name": "subnetgroup",
            "region": "us-east-1",
            "environment": "nonprod",
            "department" : "department test",
            "cloudbuddies" : "deployed by archie",
            "targetGroupArgs": {
                    "opts" : None,
                    "connection_termination" : None,
                    "deregistration_delay" : None,
                    "health_check" : None,
                    "ip_address_type" : None,
                    "lambda_multi_value_headers_enabled" : None,
                    "load_balancing_algorithm_type" : None,
                    "load_balancing_cross_zone_enabled" : None,
                    "name" : None,
                    "name_prefix" : None,
                    "port" : 80,#None,
                    "preserve_client_ip" : None,
                    "protocol" : "HTTP",#None,
                    "protocol_version" : None,
                    "proxy_protocol_v2" : None,
                    "slow_start" : None,
                    "stickiness" : None,
                    "tags" : None,
                    "target_failovers" : None,
                    "target_health_states" : None,
                    "target_type" : None,
                    "vpc_id" : "vpc-0487e2dbbb0867b92",#None,
                    "targetGroupId": None,
                },
            }

        if data is not None:
            data_conf.update(data)
        
        CreateTargetGroupB.pulumi_builder(data_conf=data_conf)
