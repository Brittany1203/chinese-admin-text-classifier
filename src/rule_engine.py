COMMON_COLUMNS = {
    "首页",
    "政策解读",
    "政府信息公开",
    "规范性文件",
    "网站地图",
    "通知公告",
    "领导信息",
}

PROVINCIAL_KEYWORDS = ["省", "广东省", "省能源局", "省教育厅"]
CITY_LEVEL_KEYWORDS = ["市投资促进局", "市医疗保障局", "市发展和改革局"]


def detect_site_level(site_name: str) -> str:
    if "镇" in site_name:
        return "town"
    if "区" in site_name:
        return "district"
    if "县" in site_name:
        return "county"
    if "市" in site_name:
        return "city"
    if "省" in site_name:
        return "province"
    return "unknown"


def classify_column(site_name: str, parent_column_name: str, column_name: str) -> dict:
    site_level = detect_site_level(site_name)

    if column_name in COMMON_COLUMNS:
        return {
            "label": 1,
            "rule_type": "common_column",
            "reason": "Common government column name is treated as valid.",
        }

    if site_level == "town":
        for keyword in CITY_LEVEL_KEYWORDS + PROVINCIAL_KEYWORDS:
            if keyword in column_name:
                return {
                    "label": 0,
                    "rule_type": "hierarchy_mismatch",
                    "reason": "Town-level site contains city-level or provincial-level institution keyword.",
                }

    if site_level in {"district", "county"}:
        for keyword in PROVINCIAL_KEYWORDS:
            if keyword in column_name:
                return {
                    "label": 0,
                    "rule_type": "province_level_mismatch",
                    "reason": "District/county-level site contains provincial-level institution keyword.",
                }

    for keyword in CITY_LEVEL_KEYWORDS:
        if keyword in column_name and site_level in {"district", "county", "town"}:
            return {
                "label": 0,
                "rule_type": "city_level_mismatch",
                "reason": "Lower-level government site contains city-level bureau keyword.",
            }

    return {
        "label": 1,
        "rule_type": "default_valid",
        "reason": "No mismatch rule was triggered.",
    }