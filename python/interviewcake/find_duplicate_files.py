def find_duplicate_files():
    """
    Simple enough.

    * walk through local filesystem
    * build hash table with k: filesize and v: files
    * in case of collision, don't create linked list - just add tuple to list
    """
