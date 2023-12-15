from .create_LoadBalancer_b import CreateLoadBalancerB

class CreateLoadBalancerA:
    def pulumi_program(data: dict = None ) -> None:
        
        data_conf = {
            "project_name": "subnetgroup",
            "region": "us-east-1",
            "environment": "nonprod",
            "department" : "department test",
            "cloudbuddies" : "deployed by archie",
            "loadBalancerArgs": {
                "opts" : None,
                "access_logs" : None,
                "customer_owned_ipv4_pool" : None,
                "desync_mitigation_mode" : None,
                "dns_record_client_routing_policy" : None,
                "drop_invalid_header_fields" : None,
                "enable_cross_zone_load_balancing" : None,
                "enable_deletion_protection" : None,
                "enable_http2" : None,
                "enable_tls_version_and_cipher_suite_headers" : None,
                "enable_waf_fail_open" : None,
                "enable_xff_client_port" : None,
                "idle_timeout" : None,
                "internal" : None,
                "ip_address_type" : None,
                "load_balancer_type" : None,
                "name" : None,
                "name_prefix" : None,
                "preserve_host_header" : None,
                "security_groups" : None,
                "subnet_mappings" : None,
                "subnets" : None,
                "tags" : None,
                "xff_header_processing_mode" : None,
                "loadBalancerId" : None,
            },
        }

        if data is not None:
            data_conf.update(data)

        CreateLoadBalancerB.pulumi_builder(data_conf)