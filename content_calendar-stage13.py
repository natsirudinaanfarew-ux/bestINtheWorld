# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: ContentCalendar
class SearchEngine:
    def __init__(self, db):
        self.db = db
    
    def search(self, query, fields=None):
        if not fields:
            fields = ['title', 'channel_name', 'topic_name', 'status']
        
        results = []
        for item in self.db.items:
            match_found = False
            lower_query = query.lower()
            
            for field in fields:
                value = getattr(item, field)
                if isinstance(value, str):
                    if lower_query in value.lower():
                        match_found = True
                        break
            
            if match_found:
                results.append(item)
        
        return results
