import json
import os

        
class ClothesConstructor:
    

    @classmethod
    def INPUT_TYPES(cls):


        path = os.path.dirname(os.path.realpath(__file__)) + '/lists_of_types/'

        with open(path + 'outerwear.json', 'r', encoding='utf-8') as file:
            outerwear = json.load(file)

        with open(path + 'tops.json', 'r', encoding='utf-8') as file:
            tops = json.load(file)      

        with open(path + 'bottoms.json', 'r', encoding='utf-8') as file:
            bottoms = json.load(file)  

        with open(path + 'dresses.json', 'r', encoding='utf-8') as file:
            dresses = json.load(file)          

        with open(path + 'underwear.json', 'r', encoding='utf-8') as file:
            underwear = json.load(file)

        with open(path + 'sportswear.json', 'r', encoding='utf-8') as file:
            sportswear = json.load(file)

        with open(path + 'footwear.json', 'r', encoding='utf-8') as file:
            footwear = json.load(file)    

        with open(path + 'headwear.json', 'r', encoding='utf-8') as file:
            headwear = json.load(file)    

        with open(path + 'accessories.json', 'r', encoding='utf-8') as file:
            accessories = json.load(file)     

        with open(path + 'traditional.json', 'r', encoding='utf-8') as file:
            traditional = json.load(file)                                
                          
              
        return {"required": {
                    "outerwear": (outerwear,),
                    "tops": (tops,),
                    "bottoms": (bottoms,),
                    "dresses": (dresses,),
                    "underwear": (underwear,),
                    "sportswear": (sportswear,),
                    "footwear": (footwear,),
                    "headwear": (headwear,),
                    "accessories": (accessories,),
                    "traditional": (traditional,),
                }, 
            }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "constructor"
    CATEGORY = "Prompt Worker"

  
    def constructor(self,outerwear,tops,bottoms,dresses,underwear,sportswear,footwear,headwear,accessories,traditional):


        styles = list()
        constructor_string = ""

        if outerwear != "Off":
            styles.append(outerwear)            

        if tops != "Off":
            styles.append(tops)  

        if bottoms != "Off":
            styles.append(bottoms)         

        if dresses != "Off":
            styles.append(dresses)  

        if underwear != "Off":
            styles.append(underwear)    

        if sportswear != "Off":
            styles.append(sportswear)   

        if footwear != "Off":
            styles.append(footwear)    

        if headwear != "Off":
            styles.append(headwear)   

        if accessories != "Off":
            styles.append(accessories)     

        if traditional != "Off":
            styles.append(traditional)                                                                                      

        for i in styles:
            constructor_string+= i + ',' 

        return (constructor_string,)