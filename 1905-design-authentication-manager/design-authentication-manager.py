class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.tokens = {}
        # tokenID: expiry time

    def generate(self, tokenId: str, currentTime: int) -> None:
        # generate new token with tokenId at currentTime
        self.tokens[tokenId] = currentTime + self.ttl


    def renew(self, tokenId: str, currentTime: int) -> None:
        # if tokenId exists renew time
        # or else ignore
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime+ self.ttl


    def countUnexpiredTokens(self, currentTime: int) -> int:
        # count the expired tokens, but also remove them. This is not told in the question
        expired = [token for token, expiry in self.tokens.items() if expiry <= currentTime]
        for token in expired:
            del self.tokens[token]
        return len(self.tokens)

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)