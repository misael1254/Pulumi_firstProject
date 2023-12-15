from .create_Listener_b import CreateListenerB

#FOR EXAMPLE PORPUSE
#import pulumi_aws as aws

#front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
# ...
#front_end_target_group = aws.lb.TargetGroup("frontEndTargetGroup")
# ...

class CreateListenerA:
    def pulumi_program(data: dict = None ) -> None:
        
        data_conf = {
            "project_name": "subnetgroup",
            "region": "us-east-1",
            "environment": "nonprod",
            "department" : "department test",
            "cloudbuddies" : "deployed by archie",
            "listenerArgs": {
                "resource_name" : None,
                "opts" : None,
                "alpn_policy" : None,
                "certificate_arn" : None,
                "default_actions": None, #:[aws.lb.ListenerDefaultActionArgs(type="forward",target_group_arn=front_end_target_group.arn,)], #
                "load_balancer_arn" :None,# front_end_load_balancer.arn,#
                "port" : None,
                "protocol" : None,
                "ssl_policy" : None,
                "tags" : None,
                "listenerId": None
                },
            }

        if data is not None:
            data_conf.update(data)

        CreateListenerB.pulumi_builder(data_conf)