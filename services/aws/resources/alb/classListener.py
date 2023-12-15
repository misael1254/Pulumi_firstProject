from pulumi.output import Inputs
import pulumi_aws as aws
from pulumi import ComponentResource, ResourceOptions
from typing import Mapping, Optional, Sequence
from pulumi_aws.alb import AwaitableGetListenerResult
#from ..lb.classListenerDefaultActionArgs import ListenerDefaultActionArgs
from  pulumi_aws.alb import ListenerDefaultActionArgs 



class ListenerArgs:
    def __init__(self,
                project_name: str, 
                region_short: str,
                environment: str,
                cloudbuddies: str = "True",
                department: str = "nonprod",
                resource_name: str = None,
                opts: Optional[ResourceOptions] = None,
                alpn_policy: Optional[str] = None,
                certificate_arn: Optional[str] = None,
                default_actions: Optional[Sequence[ListenerDefaultActionArgs]] = None,
                load_balancer_arn: Optional[str] = None,
                port: Optional[int] = None,
                protocol: Optional[str] = None,
                ssl_policy: Optional[str] = None,
                tags: Optional[Mapping[str, str]] = None
                 ) -> None:
        
        self.project_name = project_name
        self.region_short = region_short
        self.cloudbuddies = cloudbuddies
        self.department = department
        self.environment = environment
        self.resource_name = resource_name
        self.opts = opts
        self.alpn_policy = alpn_policy
        self.certificate_arn = certificate_arn
        self.default_actions = default_actions
        self.load_balancer_arn = load_balancer_arn
        self.port = port
        self.protocol = protocol
        self.ssl_policy = ssl_policy
        self.tags = tags


class ListenerBuild(ComponentResource):
    def __init__(
            self,
            nameResource: str,
            args: ListenerArgs,
            opts: ResourceOptions = None
        ):
        super().__init__('custom:resource:LISTENER', nameResource, {}, opts)

        if args.resource_name is None:
            args.resource_name = f"listener-{args.project_name}-{args.environment}-{args.region_short}"
        
        if args.tags is None:
            args.tags = {
                'Name': args.resource_name,
                'Project': args.project_name,
                'Department': args.department,
                'Cloudbuddies Archie': args.cloudbuddies,
                'Environment': args.environment
                }

        self.aws_listener = aws.lb.Listener(
            resource_name = args.resource_name,
            opts= args.opts or ResourceOptions(parent=self),
            alpn_policy= args.alpn_policy,
            certificate_arn= args.certificate_arn,
            default_actions= args.default_actions,
            load_balancer_arn= args.load_balancer_arn,
            port= args.port,
            protocol= args.protocol,
            ssl_policy= args.ssl_policy,
            tags= args.tags,
        )
            
        self.register_outputs({})


def getListener(resource_name: str,
        id: str,
        opts: Optional[ResourceOptions] = None,
        alpn_policy: Optional[str] = None,
        arn: Optional[str] = None,
        certificate_arn: Optional[str] = None,
        default_actions: Optional[Sequence[ListenerDefaultActionArgs]] = None,
        load_balancer_arn: Optional[str] = None,
        port: Optional[int] = None,
        protocol: Optional[str] = None,
        ssl_policy: Optional[str] = None,
        tags: Optional[Mapping[str, str]] = None,
        tags_all: Optional[Mapping[str, str]] = None) -> AwaitableGetListenerResult:
    
    return aws.alb.get_listener(
        resource_name = resource_name,
        id = id,
        opts = opts,
        alpn_policy = alpn_policy,
        arn = arn,
        certificate_arn = certificate_arn,
        default_actions = default_actions,
        load_balancer_arn = load_balancer_arn,
        port = port,
        protocol = protocol,
        ssl_policy = ssl_policy,
        tags = tags,
        tags_all = tags_all,
    )