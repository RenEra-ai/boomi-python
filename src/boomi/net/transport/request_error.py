
from typing import Optional


class RequestError(Exception):
    """
    Class representing a Request Error.
    """

    def __init__(
        self,
        message: str,
        stack: Optional["RequestError"] = None,
    ):
        """
        Initialize a new instance of RequestError.

        :param str message: The error message.
        """
        super().__init__(message)
        self.stack = stack

    def __str__(self):
        """
        Get the string representation of the error.

        :return: The string representation of the error.
        :rtype: str
        """
        error_stack = []
        current_error = self
        while current_error is not None:
            error_stack.append(f"Error: {super().__str__()}")
            current_error = current_error.stack
        return "\n".join(error_stack)


class UnsafeComponentXmlSerializationError(RequestError):
    """Raised when a Component XML operation is given a non-raw payload.

    Boomi Component XML is treated as an opaque payload: the SDK only accepts a
    raw ``str`` or ``bytes`` body and never parses, hydrates, or re-serializes
    it, so transmission is byte-for-byte identical to a direct API call. Passing
    a ``Component`` model, ``dict``, ``ElementTree.Element``, or any object that
    exposes ``to_xml``/``_map`` would require the SDK to re-serialize XML, which
    silently corrupts component structure (namespaces, CDATA, comments,
    attribute order, unknown attributes). Export the exact XML with
    ``get_component`` and pass it back unchanged.

    It subclasses :class:`RequestError` (a client-side usage error), so existing
    ``except RequestError`` / ``except Exception`` handlers still catch it.
    """

    def __init__(self, received_type: str):
        """
        :param str received_type: The disallowed type name that was passed.
        """
        super().__init__(
            "Component XML must be passed as a raw 'str' or 'bytes' payload; got "
            f"'{received_type}'. The SDK will not re-serialize Component models, "
            "dicts, or ElementTree elements because doing so silently corrupts "
            "component XML. Obtain the exact XML via get_component(...) and pass "
            "it back unchanged."
        )
        self.received_type = received_type
