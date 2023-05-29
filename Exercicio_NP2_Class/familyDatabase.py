class FamilyDatabase:
    def __init__(self, database):
        self.db = database
        
    def get_vivo(self):
        query = "MATCH (p:Person) RETURN p.status AS status"
        results = self.db.execute_query(query)
        return [result["status"] for result in results]
    
    def get_pai(self):
        query = "MATCH (a:name)-[:PAI_DO]->(p:name) RETURN a.name AS name, p.name AS pai_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["pai_name"]) for result in results]
    
    def get_mae(self):
        query = "MATCH (a:name)-[:MAE_DO]->(p:name) RETURN a.name AS name, p.name AS mae_name"
        results = self.db.execute_query(query)
        return [(result["name"], result["mae_name"]) for result in results]
    
    def get_nome(self):
        query = "MATCH (p:Person) RETURN p.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_ranking(self):
        query = "MATCH (p:Pessoa) RETURN p.ranking AS ranking"
        results = self.db.execute_query(query)
        return [result["ranking"] for result in results]