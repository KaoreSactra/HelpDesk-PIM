def choose_recipient(category: str) -> str:
    category = category.lower()
    if category == "hardware":
        return "hardware_support@example.com"
    elif category == "software":
        return "software_support@example.com"
    else:
        return None