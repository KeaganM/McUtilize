import requests

class Requester:
    '''
    Requester is a simple wrapper around the requests that has some examples in the doc string on how to structure a
    request.

    --------------------------------------------------------------------------------------------------------------------
    # Get request is designed like so:

        url = http://mywebsite.com/
        params = {key1:value1,key2:value2}
        r = request.get(url = url, params = params)

        resulting url: http://mywebsite.com/get?key2=value2&key1=value1

       -----------------------------------------------------------------------------------------------------------------
    # Post request is designed like so:

        url = http://mywebsite.com/
        data = {key1:value1,key2:value2}
        r = request.post(url = url, data = data)

        resulting url: http://mywebsite.com/

        data remains hidden and is sent as a post request
    '''
    types = {
        'GET': lambda url,payload=None: requests.get(url, payload),
        'POST': lambda url,data=None: requests.post(url,data)
    }

    response_types = {
        'raw': lambda x: x.raw,
        'json':lambda x:x.json(),
        'text':lambda x:x.text,
        'none':lambda x:x,
        'binary_response_content':lambda x:x.content
    }

    def __init__(self, url: str, type: str, response_type:str = 'json', *args, **kwargs):
        self.url = url
        self.type = type
        self.response_type = response_type

        self.request_function = Requester.types[type]

        self.args = args
        self.kwargs = kwargs

    def make_request(self):
        r = None
        try:
            r = self.request_function(self.url,*self.args,**self.kwargs)
        except Exception as e:
            print(e)
            print('Do help(Requester) for more info on types of requests')
        return Requester.response_types[self.response_type](r)


    def __repr__(self):
        return f'URL: {self.url}\nTYPE: {self.type} '

if __name__ == '__main__':

    # url_root = 'https://api/stripe.com'


    # url_root = 'https://reqres.in'
    # # get request
    # url = f"{url_root}/api/users?page=2"
    # type = 'GET'
    #
    # r = Requester(url, type).make_request()
    # print(r)
    # # print(help(Requester))
    #
    # # post request
    # url = f'{url_root}/api/users'
    # type = 'POST'
    # data = {
    #     'id':'1809998'
    # }
    # r = Requester(url,type,data=data).make_request()
    # print(r)

    url = 'https://jsonplaceholder.typicode.com/posts'

    r = Requester(url,'GET')
    results = r.make_request()
    print(results)
