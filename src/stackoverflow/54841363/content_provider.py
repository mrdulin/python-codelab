class ContentUser():
    def getUserRef(self, username):
        userRef = ''
        return userRef


class ContentReportGeneralSearch():
    def getReport(self, username, search_text, search_type='0'):
        user = ContentUser()
        user.getUserRef(username=username)
