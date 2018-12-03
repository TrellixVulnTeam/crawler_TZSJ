from flask import redirect,  url_for
def get_test_add_cart(userId):
  displayURL = 'https://crawler-robibot.herokuapp.com'
  json_result = {
    'messages':[
      {
        'attachment': {
          'type': 'template',
          'payload': {
            'template_type': 'generic',
            'image_aspect_ratio': 'square',
            'elements': [{
              'title': 'Welcome! ' + str(userId),
              'subtitle': 'Choose your preferences',
              'buttons':[
                {
                  'type': 'web_url',
                  'url': displayURL + '/webview/show-webview',
                  'title': 'Webview (compact)',
                  'messenger_extensions': True,
                  'webview_height_ratio': 'compact' # Small view
                },
                {
                  'type': 'web_url',
                  'url': displayURL + '/webview/show-webview',
                  'title': 'Webview (tall)',
                  'messenger_extensions': True,
                  'webview_height_ratio': 'tall' # Medium view
                },
                {
                  'type': 'web_url',
                  'url': displayURL + '/webview/show-webview',
                  'title': 'Webview (full)',
                  'messenger_extensions': True,
                  'webview_height_ratio': 'full' # large view
                }
              ]
            }]
          }
        }
      }
  ]}
  return json_result
