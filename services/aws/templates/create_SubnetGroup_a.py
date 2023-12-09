from .create_SubnetGroup_b import createSubnetGroupB

class createSubnetGroupA:
    def pulumi_program(data: dict = None ) -> None:

        data_conf = {
            "project_name": "subnetgroup",
            "region": "us-east-1",
            "environment": "nonprod",
            "department" : "department test",
            "cloudbuddies" : "deployed by archie",
            "subnet_group": {
                "opts": None,
                "description": None,
                "name": None,
                "name_prefix": None,
                "subnet_ids": ["subnet-0adfb3c282de62df1","subnet-06d5ab12261e02534","subnet-00b1de09d650fa056"],
                "tags": None,
                "subnetGroup_id": None
                },
            }

        if data is not None:
            data_conf.update(data)
        
        createSubnetGroupB.pulumi_builder(data_conf=data_conf)