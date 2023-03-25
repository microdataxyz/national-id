from copy import copy
from typing import Optional, Tuple
from ..constant import Citizenship

from ..yugoslavia import ParseResult, UniqueMasterCitizenNumber as YugoslaviaJMBG

MNE_METADATA = copy(YugoslaviaJMBG.METADATA)
MNE_METADATA.iso3166_alpha2 = 'ME'


class UniqueMasterCitizenNumber(YugoslaviaJMBG):
    """
    Montenegro Unique Master Citizen Number format, JMBG
    https://en.wikipedia.org/wiki/Unique_Master_Citizen_Number
    """
    METADATA = MNE_METADATA

    @staticmethod
    def parse(id_number: str) -> Optional[ParseResult]:
        """parse the value"""
        result = YugoslaviaJMBG.parse(id_number)
        if not result:
            return None
        loc_citizenship = UniqueMasterCitizenNumber.check_location(result['location'])
        if not loc_citizenship:
            return None
        citizenship, location = loc_citizenship
        result['citizenship'] = citizenship
        return result

    @staticmethod
    def check_location(location: str) -> Optional[Tuple[Citizenship, str]]:
        result = YugoslaviaJMBG.check_location(location)
        if not result:
            return None
        """
        Since the North Macedonia is an independent country, they share the same id code base. So, the citizenship
        is 20 < location < 30
        """
        if 20 < int(location) < 30:
            return Citizenship.CITIZEN, location
        return Citizenship.RESIDENT, location


JMBG = UniqueMasterCitizenNumber
"""
Alias of UniqueMasterCitizenNumber
"""
