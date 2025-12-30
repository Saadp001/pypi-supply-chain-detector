from datetime import datetime

def compute_risk(similarity, upload_time):
    risk = 0

    if similarity > 0.85:
        risk += 0.4

    upload_date = datetime.fromisoformat(upload_time.replace("Z", ""))
    days_old = (datetime.utcnow() - upload_date).days

    if days_old < 30:
        risk += 0.3

    if similarity > 0.9 and days_old < 7:
        risk += 0.3

    return round(risk, 2)
