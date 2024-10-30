import pandas as pd

def lookup_lat_long_canada(canadian_postal_codes: pd.DataFrame, city: str, province_abbr: str):
    """
    Lookup latitude and longitude for Canadian addresses.

    Args:
        canadian_postal_codes (pd.DataFrame): DataFrame containing Canadian postal code data.
        city (str): The city name.
        province_abbr (str): The province abbreviation.

    Returns:
        tuple: (latitude, longitude) if found, otherwise (None, None).
    """
    city_upper = city.upper()
    province_abbr_upper = province_abbr.upper()

    # Attempt to find a matching city and province abbreviation in the DataFrame
    result = canadian_postal_codes[
        (canadian_postal_codes['PROVINCE_ABBR'] == province_abbr_upper) &
        (canadian_postal_codes['CITY'].str.upper() == city_upper)
    ]

    if not result.empty:
        latitude = float(result.iloc[0]['LATITUDE'])
        longitude = float(result.iloc[0]['LONGITUDE'])
        return latitude, longitude
    else:
        return None, None


def lookup_lat_long_us(us_zip_codes: pd.DataFrame, city: str, state_abbr: str):
    """
    Lookup latitude and longitude for U.S. addresses.

    Args:
        us_zip_codes (pd.DataFrame): DataFrame containing U.S. zip code data.
        city (str): The city name.
        state_abbr (str): The state abbreviation.

    Returns:
        tuple: (latitude, longitude) if found, otherwise (None, None).
    """
    city_upper = city.upper()
    state_abbr_upper = state_abbr.upper()

    # Attempt to find a matching city and state abbreviation in the DataFrame
    result = us_zip_codes[
        (us_zip_codes['State'] == state_abbr_upper) &
        (us_zip_codes['City'].str.upper() == city_upper)
    ]

    if not result.empty:
        latitude = float(result.iloc[0]['ZipLatitude'])
        longitude = float(result.iloc[0]['ZipLongitude'])
        return latitude, longitude
    else:
        return None, None

