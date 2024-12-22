from .fileops import FileMv, FilePath, MkDir

NODE_CLASS_MAPPINGS = {
    "File Mv": FileMv,
    "File Path": FilePath,
    "Make Dir": MkDir,
}

__all__ = ['NODE_CLASS_MAPPINGS']