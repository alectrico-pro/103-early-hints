import re
from workers import Response

CSS = "body { color: red; }"
HTML = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Early Hints test</title>
    <link rel="stylesheet" href="/test.css">
</head>
<body>
    <h1>Early Hints test page</h1>
</body>
</html>
"""
def on_fetch(request):
    if re.search("test.css", request.url):
        headers = {"content-type": "text/css"}
        return Response(CSS, headers=headers)
    else:
        headers = {"content-type": "text/html","link": "</test.css>; rel=preload; as=style"}
        return Response(HTML, headers=headers)
