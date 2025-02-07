# Write your solution here
def file_to_list(filename: str):
    file_list = [] #convert file to list
    with open(filename) as file:
        for line in file:
            parts = line.replace("\n","")
            file_list.append(parts)

    return file_list

def number_list():
    minutes = [] #create a list up to 100 minutes
    for i in range(100):
        minutes.append(str(i))
    return minutes

def search_by_name(filename: str, word: str):
    recipe_parts_list = file_to_list(filename)
    
    minutes=number_list()

    recipe_names = [] #list with only the names
    for i in range(len(recipe_parts_list)-1):
        if recipe_parts_list[i+1] != "" and recipe_parts_list[i+1] in minutes:
            recipe_names.append(recipe_parts_list[i])
    
    #find name in recipe names
    recipe = []
    for name in recipe_names:
        if word.lower() in name.lower():
            recipe.append(name)
    
    return recipe

def search_by_time(filename: str, prep_time: int):
    recipe_parts_list = file_to_list(filename)

    minutes=number_list()


    string_list = []
    for i in range(len(recipe_parts_list)):
        if recipe_parts_list[i] != "" and recipe_parts_list[i] in minutes:
            convert_int = int(recipe_parts_list[i])
            if convert_int <= prep_time:
                string_list.append(f"{recipe_parts_list[i-1]}, preparation time {recipe_parts_list[i]} min")
        
    return string_list    
    
def search_by_ingredient(filename: str, ingredient: str):
    
    recipe_parts_list = file_to_list(filename)
    minutes=number_list()
    
    recipes = {}
    name = ""
    for i in range(len(recipe_parts_list)):
        if recipe_parts_list[i] in minutes:
            name = recipe_parts_list[i-1]
            time = recipe_parts_list[i]
        elif recipe_parts_list[i].lower() == ingredient.lower():
            recipes[name] = time

    printing_list = []
    for name, time in recipes.items():
        printing_list.append(f"{name}, preparation time {time} min")

    return printing_list

if __name__=="__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")



    for recipe in found_recipes:
        print(recipe)