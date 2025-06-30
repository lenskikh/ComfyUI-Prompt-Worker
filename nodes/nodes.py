import re

        
class PromptWorker:

    text2 = ""

    @classmethod
    def INPUT_TYPES(cls):

        type_of_weather = ("Off", "cloudy", "foggy", "hail", "partly cloudy", "rainy", "sleet", "snowy", "stormy", "sunny", "windy")
        Photography_Styles = ("Off", "abstract photography", "artistic photography", "black and white", "documentary photography", 
                              "fashion photography", "high contrast", "landscape photography", "low contrast", "macro photography", 
                              "minimalist photography", "night photography", "portrait photography", "street photography")
        Cinematography_Styles = ("Off","blockbuster style", "dramatic shadows", "dreamlike", "dynamic shots", "emotional", 
                                 "exaggerated shadows", "experimental style", "film noir", "illogical visuals", "jump cuts style", 
                                 "lighting and framing", "neo-noir", "new wave style", "pastel colors", "raw", "surrealism", 
                                 "symmetrical framing", "unfiltered storytelling", "wes anderson style" )
              
        return {"required": {
                    "positive": ("STRING", {"forceInput": True}),
                    "negative_char": ("STRING", {"forceInput": True}),
                    "blacklist": ("STRING", {"forceInput": True}),
                    "alphabetical_sorting": (["False", "True"],),
                    "lora": (["False", "True"],),
                    "weather": ([type_of_weather]),
                    "photography_style": (Photography_Styles,),
                    "Cinematography_Styles": (Cinematography_Styles,),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "clean_prompt"
    CATEGORY = "Prompt Worker"

  
    def clean_prompt(self, positive, negative_char, blacklist, lora, alphabetical_sorting, weather, photography_style,Cinematography_Styles):

        blacklist = blacklist.lower()

        #delete any weight like 1.3 and etc.
        if lora == "True":
            
            if ":" in positive:
                positive = re.sub(r':\d+\.\d+', '', positive)
            # weight 1 without digit after
            if ":" in positive:
                positive = re.sub(r':\d+', '', positive)
            # with space symbol token: 1.3
            if ":" in positive:
                positive = re.sub(r':\s*\d+\.\d+', '', positive)  
            if "lora" in positive:
                positive = re.sub(r'<lora:[^>]*>', '', positive)                        

        positive = positive.lower().strip()
        
        PromptWorker.text2 = ""

        negative_char = negative_char.split(",")

        for negative_symbol in negative_char:
            #remove space
            negative_symbol = negative_symbol.strip()

            #check if one symbol is
            if len(negative_symbol) == 1:
                if negative_symbol == "'":
                    positive = positive.replace("'", "")             
                if negative_symbol in positive:
                    negative_symbol_for_replace = eval("r'" + "["+negative_symbol+"]" + "'")
                    positive =  re.sub(negative_symbol_for_replace,'', positive)

        black_list = blacklist.split(",")
        for blackwords in black_list:
            blackwords = blackwords.strip()
            positive = positive.replace(blackwords, "")     
            if "|" in blackwords:
                replace_words = blackwords.split("|")
                positive = positive.replace(replace_words[0], replace_words[1]) 

        self.unique(positive, alphabetical_sorting,weather,photography_style,Cinematography_Styles)
    
        return (PromptWorker.text2,)    
 

    def unique(self, positive, alphabetical_sorting, weather,photography_style, Cinematography_Styles):

        word_list = positive.split(",")
        text3 = list()
        
        for word in word_list:
            word = word.strip()
            word = word.lower()
            if "-" in word:
                pass
            else:
                text3.append(word)

        unique_list = list(dict.fromkeys(text3))
            
        if Cinematography_Styles != "Off":
            unique_list.append(Cinematography_Styles)

        if weather != "Off":
            unique_list.append(weather)

        if photography_style != "Off":
            unique_list.append(photography_style)

        for i in unique_list:
            PromptWorker.text2+= i + ", "           

        if alphabetical_sorting == "True":
            self.sorting(PromptWorker.text2.split(","))     
            
    def sorting(self, text_list):
        PromptWorker.text2 = ", ".join(sorted([x.strip() for x in text_list if x.strip()], key=lambda x: x.lower()))
        return PromptWorker.text2                 

        