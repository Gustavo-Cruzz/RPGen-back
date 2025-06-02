from flask import Blueprint
from controllers import character_controller
from middlewares.auth_middleware import token_required

character_bp = Blueprint('characters', __name__, url_prefix='/my-characters')

character_bp.route('', methods=['POST'], strict_slashes=False)(token_required(character_controller.create))
character_bp.route('', methods=['GET'], strict_slashes=False)(token_required(character_controller.read_all))
character_bp.route('/<character_id>', methods=['GET'], strict_slashes=False)(token_required(character_controller.read_one))
character_bp.route('/<character_id>', methods=['PUT', 'PATCH'], strict_slashes=False)(token_required(character_controller.update))
character_bp.route('/<character_id>', methods=['DELETE'], strict_slashes=False)(token_required(character_controller.delete))
