from flask import Blueprint
from controllers import auth_controller
from middlewares.auth_middleware import token_required

auth_bp = Blueprint('auth', __name__)

auth_bp.route('/register', methods=['POST'])(auth_controller.register)
auth_bp.route('/login', methods=['POST'])(auth_controller.login)
auth_bp.route('/me', methods=['GET'])(token_required(auth_controller.me))
