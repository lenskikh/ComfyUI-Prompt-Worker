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

            },
        }
    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("prompt", )
    FUNCTION = "merger"
    CATEGORY = "Prompt Worker"

    def merger(self, separator=",", prompt1="", prompt2="", prompt3="", prompt4=""):

        return (prompt1 + separator + prompt2 + separator + prompt3 + separator + prompt4 + separator,)  