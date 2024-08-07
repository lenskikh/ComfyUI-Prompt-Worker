import re
        
class PromptWorker:

    text2 = ""

    @classmethod
    def INPUT_TYPES(cls):
               
        return {"required": {
                    "positive": ("STRING", {"forceInput": True}),
                    "negative_char": ("STRING", {"forceInput": True}),
                    "blacklist": ("STRING", {"forceInput": True}),
                    "alphabetical_sorting": (["False", "True"],),
                    }
                }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "clean_prompt"
    CATEGORY = "Prompt Worker"

    def clean_prompt(self, positive, negative_char, blacklist, alphabetical_sorting):

        #delete any weight like 1.3 and etc.
        if ":" in positive:
            positive = re.sub(r':\d+\.\d+', '', positive)
        # weight 1 without digit after
        if ":" in positive:
            positive = re.sub(r':\d+', '', positive)
        # with space symbol token: 1.3
        if ":" in positive:
            positive = re.sub(r':\s*\d+\.\d+', '', positive)           

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

        self.unique(positive, alphabetical_sorting)
        return (PromptWorker.text2,)
    
 
    def unique(self, positive, alphabetical_sorting):
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

        if alphabetical_sorting == "True":
            unique_list.sort()

        for i in unique_list:
            PromptWorker.text2+= i + ", "           
