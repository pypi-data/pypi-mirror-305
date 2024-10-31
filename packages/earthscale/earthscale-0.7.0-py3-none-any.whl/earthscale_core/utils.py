import datetime
import re

from earthscale.constants import (
    GOOGLE_DRIVE_RASTER_EXTENSIONS,
    GOOGLE_DRIVE_VECTOR_EXTENSIONS,
)
from earthscale.datasets.dataset import DatasetType


def infer_dataset_type_from_extension(url: str) -> DatasetType:
    extension = f".{url.split('.')[-1]}"
    if extension in GOOGLE_DRIVE_RASTER_EXTENSIONS:
        return DatasetType.RASTER
    if extension in GOOGLE_DRIVE_VECTOR_EXTENSIONS:
        return DatasetType.VECTOR
    raise ValueError(
        f"Could not infer dataset type from extension {extension} for url {url}. Valid"
        f" extensions are "
        f"{GOOGLE_DRIVE_RASTER_EXTENSIONS + GOOGLE_DRIVE_VECTOR_EXTENSIONS}"
    )


def parse_supabase_datetime_string(datetime_string: str) -> datetime.datetime:
    """Sometimes supabase drops one digit of the milliseconds

    This creates an invalid ISO-string (5 instead of 6 digits). This functions appends
    a zero to the end of the milliseconds to make it valid

    """
    pattern = r"(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2})\.(\d+)([+-]\d{2}:\d{2})"
    match = re.match(pattern, datetime_string)

    if not match:
        raise ValueError(f"Could not parse {datetime_string} into a datetime object")

    date_part = match.group(1)
    time_part = match.group(2)
    fractional_seconds = match.group(3)[:6]  # Truncate to 6 digits
    tz_part = match.group(4)

    # Combine the date and time parts
    dt_string = f"{date_part} {time_part}"
    dt = datetime.datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")

    # Add the fractional seconds
    microseconds = int(fractional_seconds.ljust(6, "0"))
    dt = dt.replace(microsecond=microseconds)

    # Handle the timezone offset
    hours_offset, minutes_offset = map(int, tz_part.split(":"))
    tz_offset = datetime.timedelta(hours=hours_offset, minutes=minutes_offset)
    dt = dt.replace(tzinfo=datetime.timezone(tz_offset))
    return dt
