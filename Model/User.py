class User():
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.dict_recipes = {}           
        self.wish_list = []
        
        
    def add_recipe(self, id_recipe, rating, is_favorite):
        
        self.dict_recipes[id_recipe] = {
            "rating": rating, 
            "is_favorite": is_favorite
        }
        
        if id_recipe in self.wish_list:
            self.remove_wish_list(id_recipe)
        
    def remove_recipe(self, id_recipe):
        del self.dict_recipes[id_recipe]
        
    def add_wish_list(self, id_recipe):
        
        #TODO nao permitir adicionar repetidos na lista de receitas
        
        self.wish_list.append(id_recipe)
        
    def remove_wish_list(self, id_recipe):
        self.wish_list.remove(id_recipe)   
        
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
        
    #TODO adicionar gets & sets para todos os atributos
    
    def get_wish_list_index(index):
        return self.wish_list[index]