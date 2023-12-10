from .create_Listener_b import CreateListenerB

class createListenerA:
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
                "default_actions" : None,
                "load_balancer_arn" : None,
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