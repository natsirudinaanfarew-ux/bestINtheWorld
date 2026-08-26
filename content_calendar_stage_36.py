# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: ContentCalendar
def repair_simple_issues(data):
    issues = []
    if not isinstance(data, dict):
        return data, ["data is not a dict"]
    for key, value in data.items():
        if key == "publications" and not isinstance(value, list):
            data["publications"] = []
            issues.append("publications is not a list, converted to []")
        for i, pub in enumerate(data.get("publications", [])):
            if not isinstance(pub, dict):
                data["publications"][i] = {}
                issues.append(f"publication at index {i} is not a dict, converted to {{}}")
            if "title" in pub and not isinstance(pub["title"], str):
                pub["title"] = str(pub["title"])
                issues.append(f"publication title is not a string, converted to str")
            if "channels" in pub and not isinstance(pub["channels"], list):
                pub["channels"] = []
                issues.append(f"publication channels is not a list, converted to []")
            if "channels" in pub and len(pub["channels"]) > 0 and not all(isinstance(c, str) for c in pub["channels"]):
                pub["channels"] = [str(c) for c in pub["channels"]]
                issues.append(f"publication channels contains non-string elements, converted to str")
            if "status" in pub and pub["status"] not in ["draft", "scheduled", "published", "archived"]:
                pub["status"] = "draft"
                issues.append(f"publication status is invalid, set to 'draft'")
    return data, issues
