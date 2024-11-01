import os

def get_group_info(group_name):
    """
    Handles fetching group information based on the OS.
    
    Parameters:
    - group_name (str): The name of the group to fetch information for.

    Returns:
    - grp.getgrnam(group_name) on Unix-based systems if the group exists.
    - None on Windows or if the group doesn't exist on Unix-based systems.
    """
    if os.name == 'nt':
        # On Windows, return None since 'grp' is not available.
        print(f"grp module not available on Windows. Skipping group info for: {group_name}")
        return None
    else:
        try:
            import grp  # Import 'grp' on Unix-based systems
            group_info = grp.getgrnam(group_name)
            return group_info
        except KeyError:
            print(f"Group '{group_name}' not found.")
            return None

# Example usage
# info = get_group_info('your_group_name')
# print(info)
