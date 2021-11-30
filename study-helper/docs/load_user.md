#def load_user(id):
    '''Login Manager function to loads users'''
    return User.query.get(int(id))
