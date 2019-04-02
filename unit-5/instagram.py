

class InstagramAccount:
    def __init__(self, user, passw):
        self.account = user
        self.passw = passw
        self.followers = []
        self.photos = []

    def follow(self, another_account):
        if isinstance(another_account, InstagramAccount):
            another_account.followers.append(self.account)
        else:
            print('not a valid instagram account')
        ''''
        try:
            another_account.followers.append(self.account)
        except:
            print('not a valid instagram account')
        '''

    def add_photo(self, photo):
        if isinstance(photo, dict):
            self.photos.append(photo)

    def get_followers(self):
        return self.followers
    
    def __repr__(self):
        return '<username: {}, password: {}'.format(self.account, self.passw)


account_1 = InstagramAccount('john', 'secure')

account_2 = InstagramAccount('jane', 'password')



'''
my_account = InstagramAccount('john', 'pass')
second_account = InstagramAccount('mary', '1234')

my_account.follow(second_account)

my_account.add_photo({'photo_id': 1, 'url': 'http://teste.com', 'likes': 0})

second_account.get_followers
my_account.get_followers

print(second_account)

'''


