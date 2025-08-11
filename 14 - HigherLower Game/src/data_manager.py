import src.lib.game_data as game_data
import random

class DataManager(object):
    def __init__(self):
        self.data = game_data.data.copy()
        self.accounts = []
    
    def get_accounts(self):
        """Gets 2 accounts from the dataset as list [account1, account2]"""
        a1 = self.data.pop(random.randint(0,len(self.data)-1))
        a2 = self.data.pop(random.randint(0,len(self.data)-1))
        self.accounts = [a1, a2]
    
    def is_guess_correct(self, guess):
        """Compares guess and returns if user is correct"""
        a_followers = self.accounts[0]['follower_count']
        b_followers = self.accounts[1]['follower_count']
        if (a_followers > b_followers and guess == 'a') or (b_followers > a_followers and guess == 'b'):
            return True
        return False
    
    def is_win(self):
        return len(self.data) < 1


"""
SAMPLE DATA
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    }
"""