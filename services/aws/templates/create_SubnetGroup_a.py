from .create_SubnetGroup_b import createSubnetGroupB

class createSubnetGroupA:
    def pulumi_program(data: dict = None ) -> None:

        data_conf = {
            "project_name": "SubnetGroup_non",
            "region": "us-east-1",
            "environment": "nonprod",
            "department" : "",
            "cloudbuddies" : "Deployed by Archie",
            "subnet_group": {
                "opts": None,
                "description": None,
                "name": None,
                "name_prefix": None,
                "subnet_ids": None,
                "tags": None,
                "subnetGroup_id": None
                },
            }

        if data is not None:
            data_conf.update(data)
        
        createSubnetGroupB.pulumi_builder(data_conf=data_conf)