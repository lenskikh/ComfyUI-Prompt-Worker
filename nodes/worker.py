import re

        
class PromptWorker:

    text2 = ""

    @classmethod
    def INPUT_TYPES(cls):
                        
              
        return {"required": {
                    "positive": ("STRING", {"forceInput": True}),
                    "alphabetical_sorting": (["False", "True"],),
                    "remove_lora": (["False", "True"],),
                    "lower_case": (["False", "True"],),
                    },
                "optional":{
                    "negative_char": ("STRING", {"forceInput": True}), 
                    "blacklist": ("STRING", {"forceInput": True}),
            },                      
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "clean_prompt"
    CATEGORY = "Prompt Worker"

  
    def clean_prompt(self, positive, remove_lora, lower_case, alphabetical_sorting, **kwargs):


        if "-" in positive:
            positive = re.sub(r'-', ' ', positive)

        if "." in positive:
            positive = re.sub(r'\.', ',', positive)  

        #delete any weight like 1.3 and etc.
        if remove_lora == "True":
            
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

        if lower_case == "True":
            #convert to lower case
            positive = positive.lower()
        else:
            positive = positive.strip()
        
        PromptWorker.text2 = ""

        if "negative_char" in kwargs:
            negative_char = kwargs["negative_char"]        
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

        if "blacklist" in kwargs:
            blacklist = kwargs["blacklist"]
            blacklist = blacklist.lower()

            black_list = blacklist.split(",")
            for blackwords in black_list:
                blackwords = blackwords.strip()
                positive = positive.replace(blackwords, "")     
                if "|" in blackwords:
                    replace_words = blackwords.split("|")
                    positive = positive.replace(replace_words[0], replace_words[1]) 

        self.unique(positive, alphabetical_sorting)
    
        return (PromptWorker.text2,)    
 

    def unique(self, positive, alphabetical_sorting):

        word_list = positive.split(",")
        text3 = list()
        
        for word in word_list:
            word = word.strip()
            if "lower_case" == "True":
                word = word.lower() 
                
            if "-" in word:
                pass
            else:
                text3.append(word)

        unique_list = list(dict.fromkeys(text3))
        

        for i in unique_list:
            PromptWorker.text2+= i + ", "           

        if alphabetical_sorting == "True":
            self.sorting(PromptWorker.text2.split(","))     
            
    def sorting(self, text_list):
        processed_list = []
        # Iterate through each item in text_list
        for x in text_list:
            stripped = x.strip()
            if stripped:  # Check if the string is not empty after stripping
                processed_list.append(stripped)

        # Sort the list case-insensitively
        processed_list.sort()

        # Join the sorted list with ", " separator
        PromptWorker.text2 = ", ".join(processed_list)
        return PromptWorker.text2                 

        