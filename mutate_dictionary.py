user_preferences = {"language": "Spanish", "font_size": "14px", "timezone": "GMT", "currency": "USD",
                    "enable_location": False, "volume_level": 50, "date_format": "MM/DD/YYYY",
                    "highlight_color": "yellow"}

del user_preferences["currency"]
removed_item = user_preferences.pop("date_format", "N/A")
print(user_preferences)
