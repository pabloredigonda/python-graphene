import graphene


class MutationResultType(graphene.ObjectType):
    success = graphene.Boolean(required=True)
    errorCode = graphene.String(required=False)
    errorMessage = graphene.String(required=False)


class SuccessMutationResultType(MutationResultType):
    def __init__(self):
        MutationResultType.__init__(self, success=True)
