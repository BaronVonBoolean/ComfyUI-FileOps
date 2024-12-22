import subprocess

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
  RETURN_TYPES = ("STRING","STRING",)
  RETURN_NAMES = ("Terminal Output","Terminal Error",)

  FUNCTION = "main"
  
  def main(self, origin="", destination=""):
    result = subprocess.run(["mv", origin, destination], capture_output=True, text=True)
    print(result.stdout)
    return (result.stdout,result.stderr)
  
class FilePath:
  CATEGORY = "ic/fileops"
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "path": ("STRING",),
      }
    }

  # Outputs the index and filename
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("Filepath")

  FUNCTION = "main"
  
  def main(self, path=""):
    print("Loading path {}".format(path))
    return (path,)
  
class MkDir:
  CATEGORY = "ic/fileops"
  @classmethod
  def INPUT_TYPES(cls):
    return {
      "required": {
        "parent_path": ("STRING",),
        "dir_name": ("STRING",),
      }
    }

  # Outputs the index and filename
  RETURN_TYPES = ("STRING",)
  RETURN_NAMES = ("dirpath",)

  FUNCTION = "main"
  
  def main(self, dir_name="", parent_path=""):
    print("Making directory {}".format(dir_name))
    result = subprocess.run(["mkdir", "-p", "{}/{}".format(parent_path, dir_name)], capture_output=True, text=True)
    return ("{}/{}".format(parent_path, dir_name),)


NODE_DISPLAY_NAME_MAPPINGS = {
    "FileMv": "ComfyUI FileMv",
}