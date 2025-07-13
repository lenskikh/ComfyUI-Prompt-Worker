import json
import os

# Получаем путь к текущему файлу ноды

        
class BodyConstructor:
    

    @classmethod
    def INPUT_TYPES(cls):


        path = os.path.dirname(os.path.realpath(__file__)) + '/lists_of_types/'

        with open(path + 'hair_types.json', 'r') as file:
            hair_types = json.load(file)

        with open(path + 'body.json', 'r') as file:
            body = json.load(file)              

        with open(path + 'eyes.json', 'r') as file:
            eyes = json.load(file)

        with open(path + 'skins.json', 'r') as file:
            skins = json.load(file)

        with open(path + 'cut.json', 'r') as file:
            haircut = json.load(file)   

        with open(path + 'nose.json', 'r') as file:
            nose = json.load(file)    

        with open(path + 'cheekbones.json', 'r') as file:
            cheekbones = json.load(file)

        with open(path + 'makeup.json', 'r') as file:
            makeup = json.load(file)                
            
                          
              
        return {"required": {
                    "hairstyle": (hair_types,),
                    "haircut": (haircut,),
                    "body": (body,),
                    "eyes": (eyes,),
                    "skin": (skins,),
                    "nose": (nose,),
                    "cheekbones": (cheekbones,),
                    "makeup": (makeup,),
                }, 
            }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "constructor"
    CATEGORY = "Prompt Worker"

  
    def constructor(self,hairstyle,haircut,body,eyes,skin,nose,cheekbones,makeup,):

        styles = list()
        constructor_string = ""

        if hairstyle != "Off":
            styles.append(hairstyle)    

        if haircut != "Off":
            styles.append(haircut)

        if body != "Off":
            styles.append(body)  

        if eyes != "Off":
            styles.append(eyes)    

        if skin != "Off":
            styles.append(skin)  

        if nose != "Off":
            styles.append(nose)

        if cheekbones != "Off":
            styles.append(cheekbones)
        
        if makeup != "Off":
            styles.append(makeup)

        for i in styles:
            constructor_string+= i + ',' 

        return (constructor_string,)