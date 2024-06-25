from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
    <head><title>Cloud&SRE </title></head>
    <body>
        <h1>Mateus Neves Merçon</h1>
        <h2>Cloud Computing & Site Reliability Engineering</h2>
    </body>
    </html>
    """
    return HttpResponse(html_content)
