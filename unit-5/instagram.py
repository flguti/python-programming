

class InstagramAccount:
    def __init__(self, user, passw):
        self.account = user
        self.passw = passw
        self.followers = []
        self.photos = []

    def follow(self, another_account):
        another_account.followers.append(self.account)

    def add_photo(self, photo):
        self.photos.append(photo)

    def get_followers(self):
        return self.followers
    
    def __repr__(self):
        return '<username: {}, password: {}'.format(self.account, self.passw)

my_account = InstagramAccount('john', 'pass')
second_account = InstagramAccount('mary', '1234')

my_account.follow(second_account)

my_account.add_photo({'photo_id': 1, 'url': 'http://teste.com', 'likes': 0})

second_account.get_followers
my_account.get_followers

print(second_account)

