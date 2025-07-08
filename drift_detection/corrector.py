def suggest_corrections(drift):
    suggestions = {}
    for key, values in drift.items():
        suggestions[key] = {
            "from": values["prod"],         
            "to": values["dev"]            
        }
    return suggestions
