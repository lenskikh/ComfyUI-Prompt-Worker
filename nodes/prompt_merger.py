class PromptMerger:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
        },
            "optional": {
                "prompt1": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt2": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt3": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt4": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt5": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt6": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt7": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
                "prompt8": ("STRING", {"multiline": False, "default": "", "forceInput": True}),

            },
        }
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("prompt", )
    FUNCTION = "merger"
    CATEGORY = "Prompt Worker"

    def merger(self, separator=",", prompt1="", prompt2="", prompt3="", prompt4="",prompt5="", prompt6="", prompt7="", prompt8=""):

        return (prompt1 + separator + prompt2 + separator + prompt3 + separator + 
                prompt4 + separator + prompt5 + separator + prompt6 + separator + 
                prompt7 + separator + prompt8 + separator,)  