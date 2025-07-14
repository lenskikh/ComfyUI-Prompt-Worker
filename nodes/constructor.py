import json
import os

        
class PromptConstructor:
    

    @classmethod
    def INPUT_TYPES(cls):

        path = os.path.dirname(os.path.realpath(__file__)) + '/lists_of_types/'

        with open(path + 'scene.json', 'r', encoding='utf-8') as file:
            scene = json.load(file)

        with open(path + 'photography.json', 'r', encoding='utf-8') as file:
            Photography_Styles = json.load(file)         

        with open(path + 'cinematography.json', 'r', encoding='utf-8') as file:
            Cinematography_Styles = json.load(file)   

        with open(path + 'colors.json', 'r', encoding='utf-8') as file:
            colors = json.load(file)         

        with open(path + 'custom_list.json', 'r', encoding='utf-8') as file:
            custom_list = json.load(file)                    
                          
              
        return {"required": {
                    "scene": (scene,),
                    "photography_style": (Photography_Styles,),
                    "Cinematography_Styles": (Cinematography_Styles,),
                    "colors": (colors,),
                    "custom_list": (custom_list,),
                },
                "optional":{
                    "clothes": ("STRING", {"forceInput": True}), 
                    "body": ("STRING", {"forceInput": True}), 
            },  
            }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "constructor"
    CATEGORY = "Prompt Worker"

  
    def constructor(self, scene, photography_style,Cinematography_Styles, colors,**kwargs):


        styles = list()
        constructor_string = ""
            
        if Cinematography_Styles != "Off":
            styles.append(Cinematography_Styles)

        if scene != "Off":
            styles.append(scene)

        if photography_style != "Off":
            styles.append(photography_style)

        if colors != "Off":
            styles.append(colors)  

        if "clothes" in kwargs:
            styles.append(kwargs['clothes'])   

        if "body" in kwargs:
            styles.append(kwargs['body'])        

        if kwargs['custom_list'] != "Off":
            styles.append(kwargs['custom_list'])   
                        

        for i in styles:
            constructor_string+= i + ',' 

        return (constructor_string,)