from datetime import datetime , timedelta
tomorrow = datetime.now() + timedelta(days=1)
date=tomorrow.strftime("%d/%m/%y")
print(date)