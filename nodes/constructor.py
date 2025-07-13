import json

        
class PromptConstructor:
    

    @classmethod
    def INPUT_TYPES(cls):

        path = './custom_nodes/ComfyUI-Prompt-Worker/settings/'

        with open(path + 'scene.json', 'r', encoding='utf-8') as file:
            scene = json.load(file)

        with open(path + 'photography.json', 'r', encoding='utf-8') as file:
            Photography_Styles = json.load(file)         

        with open(path + 'cinematography.json', 'r', encoding='utf-8') as file:
            Cinematography_Styles = json.load(file)   

        with open(path + 'colors.json', 'r', encoding='utf-8') as file:
            colors = json.load(file)         

        with open(path + 'body.json', 'r', encoding='utf-8') as file:
            body = json.load(file)                    
                          
              
        return {"required": {
                    "scene": (scene,),
                    "photography_style": (Photography_Styles,),
                    "Cinematography_Styles": (Cinematography_Styles,),
                    "colors": (colors,),
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

        for i in styles:
            constructor_string+= i + ',' 

        return (constructor_string,)