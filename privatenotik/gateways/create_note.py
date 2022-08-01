from gateways.base_gateway import BaseGatewayAPI


class CreateNoteGateway(BaseGatewayAPI):

    query = '/notes/note'
    method = 'POST'
