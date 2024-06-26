# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verify Humans</title>
    <link rel="stylesheet" type="text/css" href="./css/index.css">
</head>
<style>
    body {
    line-height: 1.4;
    font-size: 16px;
    padding: 0 25px;
    margin: 25px auto;
    max-width: 650px;
    }

    ul {
        margin-top: 0px;
    }

    #maincontent {
        max-width: 38em;
        margin: 15 auto;
        margin-top: 70px;
    }

    h2 {
        margin-bottom: 0px;
    }

    p {

     font-weight: 100;
     font-style: italic;
    }
</style>
<body>
    <div id="maincontent">
        <h2 style="text-align: center;"> Verify Humans <br>Fact checker for the entire internet</br></h2>
    </div>
    <hr>
    <ul>
        <!-- Adding options here with an intro-->
        <p> The first great threat AI will bring to humanity, will not be the replacement of jobs (both white collar or blue), rather the distribution of misinformation generated by AI </p>
        <li>
            We exist to be a platform that indexes and labels information and disinformation. This catalog exists for the world to gather and find truth. Truth is not subjective its objective and it should not be placed in the hands of a single power or entity. Rather the people. 
        </li>
        <br>
        <li>
           In order to protect humanity from the dangerous consequences of disinformation, we must be able to label disinformation faster than in can be generated.
        </li>
        <br>
        <li>
          Verify Humans exists to do exactly that, we create a clear and obvious border between Human generated and AI generated content where one has not yet previously existed.
        </li>
        <br>
    </ul>
    <p style="text-align: center; font-style: italic;">
        email us here for more information: founders@verifyhumans.com
    </p>
    <footer>
        <p style="text-align: center;">&copy; 2024 Verified Humans</p>
    </footer>
</body>
</html>
    </html>
    '''
    return HttpResponse(html)