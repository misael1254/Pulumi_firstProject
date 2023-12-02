from pulumi import export, Output
from typing import Dict, List

from ..resources.rds import (
    SubnetGroupArgs,
    SubnetGroupBuild,
    get_subnet_group
    )

from ..resources.region_zone import GetRegionShortAWSNew

class createSubnetGroupB: 
    def pulumi_builder(data_conf: Dict) -> List[Output[object]]:
        
        ### VARS ###
        subnetGroup_conf = data_conf["subnet_group"]
        region_short = GetRegionShortAWSNew.get_regionshort(data_conf["region"])

        ### VARS TO EXPORT ###
        aws_subnetGroup = None

        ### GENERATE SUBNET GROUP ### 
        if subnetGroup_conf["subnetGroup_id"] is None:
            subnetGroup = SubnetGroupBuild(
                "Subnet Group",
                SubnetGroupArgs(
                    project_name= data_conf["project_name"], 
                    region_short= region_short,
                    environment= data_conf["environment"], 
                    opts= subnetGroup_conf["opts"], 
                    name= subnetGroup_conf["name"], 
                    name_prefix= subnetGroup_conf["name_prefix"], 
                    subnet_ids= subnetGroup_conf["subnet_ids"], 
                    tags= subnetGroup_conf["tags"], 
                )
            ).subnetGroup

            aws_subnetGroup = Output.format("{0} | {1}", subnetGroup.id, subnetGroup.arn )
        
        else:
            subnetGroup = get_subnet_group(
                id = subnetGroup_conf["subnetGroup_id"],
                name = "Subnet Group"
            )
        
        export("AWS Subnet Group: ", aws_subnetGroup)
        return subnetGroup, aws_subnetGroup