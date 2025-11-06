class AppError(Exception):
    """General application error."""
    pass

class NotFoundError(AppError):
    """ The server cannot find the requested resource. """

class AccessDeniedError(AppError):
    """ The client does not have access rights to the content """