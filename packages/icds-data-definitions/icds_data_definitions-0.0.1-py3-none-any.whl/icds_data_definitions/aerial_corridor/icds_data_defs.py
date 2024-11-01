from pydantic import BaseModel
from enum import Enum, auto

# Version: 0.0.1
DATA_DEFINITIONS_VERSION = 0.0.1
class AvailabilityEnum(str, Enum):
    unknown = auto()
    healthy = auto()
    unhealthy = auto()


class VersionAvailabilityRead(BaseModel):
    "A class to hold version and availability of DSS"
    
    version: str
    availability: AvailabilityEnum

