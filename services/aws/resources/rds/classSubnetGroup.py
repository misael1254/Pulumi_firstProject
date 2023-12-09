from typing import Mapping, Optional, Sequence
import pulumi
import pulumi_aws as aws
from pulumi import ComponentResource, ResourceOptions
from pulumi_aws.rds import AwaitableGetSubnetGroupResult

class SubnetGroupArgs:
    def __init__(self,
                project_name: str, 
                region_short: str,
                environment: str,
                # resource_name: str, # Generalmente se crea el nombre del rucurso con los primeros parámetros
                cloudbuddies: str = "True",
                department: str = "nonprod",
                description: Optional[str] = None,
                name: Optional[str] = None,
                name_prefix: Optional[str] = None,
                subnet_ids: Optional[Sequence[str]] = None,
                opts: Optional[ResourceOptions] = None,
                tags: Optional[Mapping[str, str]] = None
                ) -> None:

        self.project_name = project_name
        self.region_short = region_short
        self.cloudbuddies = cloudbuddies
        self.department = department
        self.environment = environment
        # self.resource_name: resource_name
        self.opts = opts
        self.description = description
        self.name = name
        self.name_prefix = name_prefix
        self.subnet_ids = subnet_ids
        self.tags = tags


class SubnetGroupBuild(ComponentResource):
    def __init__(self,
                nameResource: str,
                args: SubnetGroupArgs,
                opts: ResourceOptions = None
                ):
        super().__init__('custom:resource:SUBNETGROUP', nameResource, {}, opts) # inicializa la clase padre
    
        # if args.name is not None:
        #      name = args.name
        # else:
        #     name = f"subnetGroup-{args.project_name}-{args.environment}-{args.region_short}"
        
        # refactorización del if anterior
        if args.name is None:
            args.name = f"subnetgroup-{args.project_name}-{args.environment}-{args.region_short}"
        

        if args.tags is None:
            args.tags = {
                'Name': args.name,
                'Project': args.project_name,
                'Department': args.department,
                'Cloudbuddies Archie': args.cloudbuddies,
                'Environment': args.environment
                }

        self.subnetGroup = aws.rds.SubnetGroup(
                args.name,
                opts = args.opts or ResourceOptions(parent=self),
                description = args.description,
                name = args.name,
                name_prefix = args.name_prefix,
                subnet_ids = args.subnet_ids,
                tags = args.tags,
                )
        
        self.register_outputs({})

        
def get_subnet_group(resource_name: str,
        id: str,
        opts: Optional[ResourceOptions] = None,
        arn: Optional[str] = None,
        description: Optional[str] = None,
        name: Optional[str] = None,
        name_prefix: Optional[str] = None,
        subnet_ids: Optional[Sequence[str]] = None,
        supported_network_types: Optional[Sequence[str]] = None,
        tags: Optional[Mapping[str, str]] = None,
        tags_all: Optional[Mapping[str, str]] = None,
        vpc_id: Optional[str] = None) -> AwaitableGetSubnetGroupResult : 
    
    return aws.rds.get_subnet_group(
        id=id,
        opts= opts,
        arn= arn,
        description= description,
        name= name,
        name_prefix= name_prefix,
        subnet_ids= subnet_ids,
        supported_network_types= supported_network_types,
        tags= tags,
        tags_all= tags_all,
        vpc_id=vpc_id)