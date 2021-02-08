import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')


    try:
        req_body = req.get_json()
    except ValueError:
        pass
    else:
        test = req_body.get('test')

    if test:
        return func.HttpResponse(f"test: {test}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a test in the query string or in the request body for a personalized response.",
             status_code=200
        )

    
