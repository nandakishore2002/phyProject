from plyer import notification
import time
title="Drinking Water remider"
message="It's been an hour you drank water so, have some water now"
notification.notify(
	title=title,
	message=message,
	timeout=20,
	app_icon="C:/Users/Nandu/OneDrive/Documents/GitHub/Python/python_/project/water_logo.ico",
	)
time.sleep(3600)