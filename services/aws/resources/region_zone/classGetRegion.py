import re

"""
Gets the Region shortcode based on provided region
    :param region: Region entered in fronted
"""


class GetRegionShortAWSNew:

    def get_regionshort(region):
        regionShort = {
            "eu-central-1": "euc1",
            "eu-west-1": "euw1",
            "eu-west-2": "euw2",
            "eu-west-3": "euw3",
            "eu-north-1": "eun1",
            "us-east-1": "use1",
            "us-east-2": "use2",
            "us-west-1": "usw1",
            "us-west-2": "usw2",
            "ap-south-1": "aps1",
            "ap-northeast-2": "apne2",
            "ap-southeast-1": "apse1",
            "ap-southeast-2": "apse2",
            "ap-northeast-1": "apne1",
            "ca-central-1": "cac1",
            "sa-east-1": "sae1",
        }.get(region)
        return regionShort

    def Split_Function(string):
        # split on delimiter(s)
        return re.split(r"[ ,;:_/.]", string)

    def get_azshort(az):
        azShort = {
            "eu-central-1a": "euc1a",
            "eu-central-1b": "euc1b",
            "eu-central-1c": "euc1c",
            "eu-west-1a": "euw1a",
            "eu-west-1b": "euw1b",
            "eu-west-1c": "euw1c",
            "eu-west-2a": "euw2a",
            "eu-west-2b": "euw2b",
            "eu-west-2c": "euw2c",
            "eu-west-3a": "euw3a",
            "eu-west-3b": "euw3b",
            "eu-west-3c": "euw3c",
            "eu-north-1a": "eun1a",
            "eu-north-1b": "eun1b",
            "eu-north-1c": "eun1c",
            "us-east-1a": "use1a",
            "us-east-1b": "use1b",
            "us-east-1c": "use1c",
            "us-east-1d": "use1d",
            "us-east-1e": "use1e",
            "us-east-1f": "use1f",
            "us-east-2a": "use2a",
            "us-east-2b": "use2b",
            "us-east-2c": "use2c",
            "us-west-1a": "usw1a",
            "us-west-1b": "usw1b",
            "us-west-2a": "usw2a",
            "us-west-2b": "usw2b",
            "us-west-2c": "usw2c",
            "us-west-2d": "usw2d",
            "ap-south-1a": "aps1a",
            "ap-south-1b": "aps1b",
            "ap-south-1c": "aps1c",
            "ap-northeast-2a": "apne2a",
            "ap-northeast-2b": "apne2b",
            "ap-northeast-2c": "apne2c",
            "ap-northeast-2d": "apne2d",
            "ap-southeast-1a": "apse1a",
            "ap-southeast-1b": "apse1b",
            "ap-southeast-1c": "apse1c",
            "ap-southeast-2a": "apse2a",
            "ap-southeast-2b": "apse2b",
            "ap-southeast-2c": "apse2c",
            "ap-northeast-1a": "apne1a",
            "ap-northeast-1c": "apne1c",
            "ap-northeast-1d": "apne1d",
            "ca-central-1a": "cac1a",
            "ca-central-1b": "cac1b",
            "ca-central-1d": "cac1d",
            "sa-east-1a": "sae1a",
            "sa-east-1b": "sae1b",
            "sa-east-1c": "sae1c",
        }.get(az)
        return azShort
