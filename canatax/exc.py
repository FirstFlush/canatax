from canatax.enums import ProvinceOrTerritory


class InvalidProvinceError(Exception):
    """Raised when ProvinceOrTerritory enum is passed an invalid value."""
    
    def __init__(self, province:str|ProvinceOrTerritory):
        message = f"Invalid province or territory: `{province}`. Value must be two-letter string: AB,BC,MB,NB,NL,NS,NT,NU,ON,PE,QC,SK,YK."
        super().__init__(message)