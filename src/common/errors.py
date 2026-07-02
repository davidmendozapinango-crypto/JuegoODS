class JuegoODSError(Exception):
    pass


class DuplicateCedulaError(JuegoODSError):
    pass


class PlayerNotFoundError(JuegoODSError):
    pass


class ValidationError(JuegoODSError):
    pass


class CorruptedDataError(JuegoODSError):
    pass
