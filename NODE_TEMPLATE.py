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
