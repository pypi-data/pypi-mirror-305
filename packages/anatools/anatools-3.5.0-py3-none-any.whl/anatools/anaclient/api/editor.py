"""
Channels API calls.
"""

def createRemoteDevelopment(self, organizationId=None, channelId=None, channelVersion=None, verbose=False):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "createRemoteDevelopment",
            "variables": {
                "organizationId": organizationId,
                "channelId": channelId,
                "channelVersion": channelVersion
            },
            "query": """mutation
                createRemoteDevelopment($organizationId: String!, $channelId: String!, $channelVersion: String) {
                    createRemoteDevelopment(organizationId: $organizationId, channelId: $channelId, channelVersion: $channelVersion) {
                        organizationId
                        channelId
                        editorUrl
                        editorSessionId
                    }
                }"""})
    return self.errorhandler(response, "createRemoteDevelopment")

def deleteRemoteDevelopment(self, editorSessionId, organizationId=None, verbose=False):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "deleteRemoteDevelopment",
            "variables": {
                "organizationId": organizationId,
                "editorSessionId": editorSessionId,
            },
            "query": """mutation
                deleteRemoteDevelopment($organizationId: String!, $editorSessionId: String!) {
                    deleteRemoteDevelopment(organizationId: $organizationId, editorSessionId: $editorSessionId) {
                        organizationId
                        editorSessionId
                        status
                    }
                }"""})
    return self.errorhandler(response, "deleteRemoteDevelopment")

def listRemoteDevelopment(self, organizationId=None, verbose=False):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "listRemoteDevelopment",
            "variables": {
                "organizationId": organizationId
            },
            "query": """query
                listRemoteDevelopment($organizationId: String!) {
                    listRemoteDevelopment(organizationId: $organizationId) {
                        organizationId
                        channelId
                        editorUrl
                        editorSessionId
                    }
                }"""})
    return self.errorhandler(response, "listRemoteDevelopment")

