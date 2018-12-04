def get_test_add_cart(userId, blockId):
  displayURL = 'http://127.0.0.1:5000'
  json_result = {
    'messages':[
      {
        'attachment': {
          'type': 'template',
          'payload': {
            'template_type': 'generic',
            'image_aspect_ratio': 'square',
            'elements': [{
              'title': 'Welcome ' + str(userId),
              'subtitle': 'Choose your preferences',
              'buttons':[
                {
                  'type': 'web_url',
                  'url': displayURL + '/webview/dynamic-webview?userId={userId}&blockId={blockId}'.format(userId = userId, blockId = blockId),
                  'title': 'Webview',
                  'messenger_extensions': True,
                  'webview_height_ratio': 'tall' # Med view
                }
              ]
            }]
          }
        }
      }
  ]}
  return json_result
