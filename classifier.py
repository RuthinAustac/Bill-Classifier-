def classify_bill(text):
    t = text.lower()

    # Electricity Bill
    if any(k in t for k in ["electricity", "meter", "kwh", "consumer no", "energy charges"]):
        return "Electricity"

    # Grocery
    if any(k in t for k in ["grocery", "supermarket", "mart", "provision"]):
        return "Grocery"

    # Restaurant / Food
    if any(k in t for k in ["restaurant", "dine", "food", "invoice no", "table no"]):
        return "Restaurant"

    # Mobile Recharge
    if any(k in t for k in ["airtel", "jio", "vi recharge", "prepaid", "postpaid", "recharge"]):
        return "MobileRecharge"

    # Fastag
    if any(k in t for k in ["fastag", "toll", "nhai", "vehicle", "plaza"]):
        return "Fastag"

    # Online Order
    if any(k in t for k in ["amazon", "flipkart", "order id", "shipped", "delivered"]):
        return "OnlineOrder"

    # UPI / Bank Message
    if any(k in t for k in ["upi", "utr", "credited", "debited", "txn"]):
        return "UPI_Bank"

    # Notes / Study Images
    if any(k in t for k in ["chapter", "exercise", "notes", "handwritten", "assignment"]):
        return "Notes"

    # Screenshots
    if "screenshot" in t or "screen shot" in t:
        return "Screenshots"

    # Fallback
    return "Others"
