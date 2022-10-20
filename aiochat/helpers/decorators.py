

def login_required(func):
    async def wrapped(self, *args, **kwargs):
        if self.request.user in None:
            pass
        # redirect

        return await func