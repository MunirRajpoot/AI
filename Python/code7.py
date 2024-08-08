# Current Time UK 

from datetime import datetime
import pytz

# Define the UK timezone
uk_timezone = pytz.timezone('Europe/London')

# Get the current time in the UK timezone
current_time_uk = datetime.now(uk_timezone)

# Print the current time
print("Current time in the UK:", current_time_uk.strftime('%Y-%m-%d %H:%M:%S'))
