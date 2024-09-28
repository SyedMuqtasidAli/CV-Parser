class APIRotation:
    def __init__(self, api_keys):
        """
        Initialize the APIRotation class with a list of API keys.
        
        :param api_keys: A list of API keys to rotate through.
        """
        self.api_keys = api_keys
        self.current_index = 0

    def get_next_key(self):
        """
        Get the next API key in rotation.
        
        :return: The next API key.
        """
        key = self.api_keys[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.api_keys)
        return key

    def add_key(self, new_key):
        """
        Add a new API key to the rotation list.
        
        :param new_key: The new API key to be added.
        """
        self.api_keys.append(new_key)

# Example usage:
api_keys = ['API_KEY_1', 'API_KEY_2', 'API_KEY_3']
api_rotation = APIRotation(api_keys)

# Rotate through keys
print(api_rotation.get_next_key())  # Output: API_KEY_1
print(api_rotation.get_next_key())  # Output: API_KEY_2

# Add new key
api_rotation.add_key('API_KEY_4')
print(api_rotation.get_next_key())  # Output: API_KEY_3
