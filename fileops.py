class FileMv:
  
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "origin": ("STRING", {"forceInput": True, "default": "", "dynamicPrompts": False}),
                # Dropdown for regex or extension
                "destination": ("STRING", {"default": "extension"}),
            }
        }

    # Outputs the index and filename
    RETURN_TYPES = ("STRING")
    RETURN_NAMES = ("Terminal Output")

    OUTPUT_NODE = True

    FUNCTION = "mv_file"
    CATEGORY = "ic/fileops"
