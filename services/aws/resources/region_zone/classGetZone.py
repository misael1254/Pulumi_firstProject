import pulumi_aws as aws
import pulumi
from typing import List

"""
Gets the Zones based on provided region
Parameters to provide in the main file :
   region
"""

class GetAzAWSNew():
    def get_zones() -> List[str]:
        zones = aws.get_availability_zones(state="available")
        azNameList = zones.names
        return azNameList
