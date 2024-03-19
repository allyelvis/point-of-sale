from odoo import http
from odoo.http import request

class MyController(http.Controller):

    @http.route('/my_api/auth', type='json', auth='public', methods=['POST'], csrf=False)
    def api_auth(self, **post):
        username = post.get('username')
        password = post.get('password')

        uid = request.session.authenticate(request.session.db, username, password)
        if uid is not False:
            return {
                'status': 'success',
                'message': 'Authentication successful',
                'uid': uid,
            }
        else:
            return {
                'status': 'error',
                'message': 'Authentication failed',
            }
