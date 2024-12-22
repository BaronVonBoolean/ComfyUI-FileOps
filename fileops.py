class FileMv:
  CATEGORY = "ic/fileops"
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "origin": ("STRING",),
        # Dropdown for regex or extension
        "destination": ("STRING",),
      }
    }

  # Outputs the index and filename
  RETURN_TYPES = ("STRING",)
  # RETURN_NAMES = ("Terminal Output")

  FUNCTION = "main"
  
  def main(self, origin="", destination=""):
    print(origin, destination)
    return (destination,)
  
NODE_CLASS_MAPPINGS = {
    "FileMv": FileMv,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FileMv": "ComfyUI FileMv",
}