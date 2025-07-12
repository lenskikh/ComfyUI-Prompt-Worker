from .nodes.worker import *
from .nodes.constructor import *
from .nodes.clothes import *
from .nodes.body import *

NODE_CLASS_MAPPINGS = { 

    "Prompt Worker": PromptWorker,
    "Prompt Сonstructor": PromptConstructor,
    "Prompt Clothes": ClothesConstructor,
    "Prompt Body": BodyConstructor,

    }
    
print("\033[34mComfyUI Prompt Worker: \033[92mLoaded\033[0m")
