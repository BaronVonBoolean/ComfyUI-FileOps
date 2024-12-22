from .fileops import FileMv, FilePath

NODE_CLASS_MAPPINGS = {
    "File Mv": FileMv,
    "File Path": FilePath,
}

__all__ = ['NODE_CLASS_MAPPINGS']