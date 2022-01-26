from plyer import notification
import time
title="Medicine Remainder"
message="Take your medicine Now"
notification.notify(
	title=title,
	message=message,
	timeout=20,
	app_icon="C:/Users/Nandu/OneDrive/Documents/GitHub/Python/python_/project/medicine.ico",
	)
time.sleep(86400)