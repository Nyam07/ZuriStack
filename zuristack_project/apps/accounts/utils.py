from uuid import uuid4
def generate_random_id(length=5):
    """
    Function to get a random id for each user to append to the slug name
    """
    random_id = str(uuid4())
    return random_id[:length]