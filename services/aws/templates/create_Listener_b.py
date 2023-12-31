from pulumi import export, Output
from typing import Dict, List

from ..resources.alb import(
    ListenerArgs,
    ListenerBuild,
    getListener
)

from ..resources.region_zone import GetRegionShortAWSNew

class CreateListenerB:
     def pulumi_builder(data_conf: Dict) -> List[Output[object]]:
        
         ### VARS ###
        listenerArgs = data_conf["listenerArgs"]
        region_short = GetRegionShortAWSNew.get_regionshort(data_conf["region"])

        ### VARS TO EXPORT ###
        aws_listener = None

        ### GENERATE Listener ### 
        if listenerArgs["listenerId"] is None:
            listener = ListenerBuild(
                "aws Listener",
                ListenerArgs(
                    project_name= data_conf["project_name"], 
                    region_short= region_short,
                    environment= data_conf["environment"], 
                    resource_name = listenerArgs["resource_name"],
                    opts = listenerArgs["opts"],
                    alpn_policy = listenerArgs["alpn_policy"],
                    certificate_arn = listenerArgs["certificate_arn"],
                    default_actions = listenerArgs["default_actions"],
                    load_balancer_arn = listenerArgs["load_balancer_arn"],
                    port = listenerArgs["port"],
                    protocol = listenerArgs["protocol"],
                    ssl_policy = listenerArgs["ssl_policy"],
                    tags = listenerArgs["tags"],
                    )
            ).aws_listener

            aws_listener = Output.format("{0} | {1}", listener.id, listener.arn )
        
        else:
            listener = getListener(
                id = listenerArgs["listenerId"],
                resource_name = "aws listener"
            )
        
        export("AWS Listener: ", aws_listener)
        return listener, aws_listener