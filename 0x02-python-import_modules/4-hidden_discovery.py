#!/usr/bin/python3
if __name__ == "__main__":
    """Print hidden files in sorted order"""
    import hidden_4

    names = dir(hidden_4)

    if name in names:
        if name[:2] != "__":
            print(name)
