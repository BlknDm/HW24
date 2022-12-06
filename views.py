from typing import Union, Mapping, Any, Optional, List

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from schemas import RequestParamsListSchema
from utils import query_build

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/perform_query', methods=['POST', 'GET'])
def perform_query() -> str | Response:

    try:
        params = RequestParamsListSchema().load(request.json)
    except ValidationError as error:
        return Response(error.messages)

    result: List[str]
    for query in params['queries']:
        result = query_build(
            cmd=query['cmd'],
            param=query['value'],
            filename=params['filename'],
            data=result,
        )

    return jsonify(result)
