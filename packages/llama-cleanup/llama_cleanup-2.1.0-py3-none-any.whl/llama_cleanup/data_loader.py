import pandas as pd

def load_data(canadian_postal_codes_path, us_zip_codes_path):
    """
    Loads Canadian and U.S. postal code data from CSV files.

    Args:
        canadian_postal_codes_path (str): Path to the Canadian postal codes CSV file.
        us_zip_codes_path (str): Path to the U.S. zip codes CSV file.

    Returns:
        tuple: DataFrames for Canadian and U.S. postal code data.
    """
    try:
        # Load Canadian postal code data
        canadian_postal_codes = pd.read_csv(canadian_postal_codes_path)
        # Load U.S. zip code data
        us_zip_codes = pd.read_csv(us_zip_codes_path)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None, None
    except pd.errors.EmptyDataError:
        print("One or more CSV files are empty.")
        return None, None
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None, None
    
    return canadian_postal_codes, us_zip_codes


def load_state_province_abbreviations():
    """
    Provides a dictionary mapping of full state/province names to their abbreviations for Canada and the U.S.

    Returns:
        dict: A dictionary with full names as keys and abbreviations as values.
    """
    # Canadian provinces and territories
    province_abbreviations = {
        'ALBERTA': 'AB',
        'BRITISH COLUMBIA': 'BC',
        'MANITOBA': 'MB',
        'NEW BRUNSWICK': 'NB',
        'NEWFOUNDLAND AND LABRADOR': 'NL',
        'NOVA SCOTIA': 'NS',
        'ONTARIO': 'ON',
        'PRINCE EDWARD ISLAND': 'PE',
        'QUEBEC': 'QC',
        'SASKATCHEWAN': 'SK',
        'NORTHWEST TERRITORIES': 'NT',
        'NUNAVUT': 'NU',
        'YUKON': 'YT',
        # U.S. states
        'ALABAMA': 'AL',
        'ALASKA': 'AK',
        'ARIZONA': 'AZ',
        'ARKANSAS': 'AR',
        'CALIFORNIA': 'CA',
        'COLORADO': 'CO',
        'CONNECTICUT': 'CT',
        'DELAWARE': 'DE',
        'FLORIDA': 'FL',
        'GEORGIA': 'GA',
        'HAWAII': 'HI',
        'IDAHO': 'ID',
        'ILLINOIS': 'IL',
        'INDIANA': 'IN',
        'IOWA': 'IA',
        'KANSAS': 'KS',
        'KENTUCKY': 'KY',
        'LOUISIANA': 'LA',
        'MAINE': 'ME',
        'MARYLAND': 'MD',
        'MASSACHUSETTS': 'MA',
        'MICHIGAN': 'MI',
        'MINNESOTA': 'MN',
        'MISSISSIPPI': 'MS',
        'MISSOURI': 'MO',
        'MONTANA': 'MT',
        'NEBRASKA': 'NE',
        'NEVADA': 'NV',
        'NEW HAMPSHIRE': 'NH',
        'NEW JERSEY': 'NJ',
        'NEW MEXICO': 'NM',
        'NEW YORK': 'NY',
        'NORTH CAROLINA': 'NC',
        'NORTH DAKOTA': 'ND',
        'OHIO': 'OH',
        'OKLAHOMA': 'OK',
        'OREGON': 'OR',
        'PENNSYLVANIA': 'PA',
        'RHODE ISLAND': 'RI',
        'SOUTH CAROLINA': 'SC',
        'SOUTH DAKOTA': 'SD',
        'TENNESSEE': 'TN',
        'TEXAS': 'TX',
        'UTAH': 'UT',
        'VERMONT': 'VT',
        'VIRGINIA': 'VA',
        'WASHINGTON': 'WA',
        'WEST VIRGINIA': 'WV',
        'WISCONSIN': 'WI',
        'WYOMING': 'WY',
        # District of Columbia
        'DISTRICT OF COLUMBIA': 'DC',
    }
    
    abbreviation_to_fullname = {abbr: full for full, abbr in province_abbreviations.items()}
    return province_abbreviations, abbreviation_to_fullname
