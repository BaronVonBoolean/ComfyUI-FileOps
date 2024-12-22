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
  
class FilePath:
  CATEGORY = "ic/fileops"
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "path": ("STRING",),
        # Dropdown for regex or extension
      }
    }

  # Outputs the index and filename
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("Filepath (string)")

  FUNCTION = "main"
  
  def main(self, path=""):
    print(path)
    return (path,)

NODE_DISPLAY_NAME_MAPPINGS = {
    "FileMv": "ComfyUI FileMv",
}