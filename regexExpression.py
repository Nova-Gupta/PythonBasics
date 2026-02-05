# datetime module
from datetime import datetime, timedelta, date

from arrow import now
now = datetime.now()
print(now)
today = date.today()
print(today)

# This is a sample code file named regexExpression.py
yesterday = today - timedelta(days=1)
print(yesterday)