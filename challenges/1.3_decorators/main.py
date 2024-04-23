class User:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions


class PermissionError(Exception):
    pass


def requires_permission(permission):
    # TODO: Implement me
    pass


# Example function using the decorator
@requires_permission('edit')
def edit_document(user, document):
    return f"Document {document} edited by {user.name}."


# Example user and function call
user = User("John Doe", ['view'])
try:
    print(edit_document(user, "Sample Document"))
except PermissionError as e:
    print(e)
