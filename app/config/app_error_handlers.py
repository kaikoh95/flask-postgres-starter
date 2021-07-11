
def app_error_handlers(app):

    @app.errorhandler(400)
    def bad_request(error):
        error = vars(error)
        message = "The browser (or proxy) sent a request that this server could not understand."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        out = {"error": message}
        if error.get("description"):
            out = {**out, **{"description": error.get("description")}}
        return out, 400

    @app.errorhandler(401)
    def unauthorized(error):
        error = vars(error)
        message = "The server could not verify that you are authorized to" \
                  " access the URL requested. You either supplied the wrong" \
                  " credentials (e.g. a bad password), or your browser " \
                  "doesn't understand how to supply the credentials required."
        if error.get("data") and error.get("data").get('message'):
            message = error["data"]["error"]
        return {'message': message}, 401

    @app.errorhandler(403)
    def forbidden(error):
        error = vars(error)
        message = "You don't have the permission to access the requested " \
                  "resource. It is either read-protected or not readable by " \
                  "the server."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {"error": message}, 403

    @app.errorhandler(404)
    def not_found(error):
        error = vars(error)
        message = "The requested URL was not found on the server. If you" \
                  " entered the URL manually please check your spelling and" \
                  " try again."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {"error": message}, 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        error = vars(error)
        message = "The method is not allowed for the requested URL."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {"error": message}, 405

    @app.errorhandler(422)
    def method_not_allowed(error):
        error = vars(error)
        message = "The request was well-formed but was unable to be followed due to semantic errors."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {"error": message}, 422

    @app.errorhandler(500)
    def internal_server(error):
        error = vars(error)
        message = "The server encountered an internal error and was unable" \
                  " to complete your request. Either the server is" \
                  " overloaded or there is an error in the application."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {"error": message}, 500

    @app.errorhandler(503)
    def service_unavailable(error):
        error = vars(error)
        message = "The server is temporarily unable to service your" \
                  " request due to maintenance downtime or capacity" \
                  " problems. Please try again later."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {'code': 503, "error": message}, 503

    @app.errorhandler(504)
    def gateway_timeout(error):
        error = vars(error)
        message = "The connection to an upstream server timed out."
        if error.get("data") and error.get("data").get("error"):
            message = error["data"]["error"]
        return {"error": message}, 504
