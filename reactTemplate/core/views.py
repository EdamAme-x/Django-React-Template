from django.shortcuts import render

def index(request):
    context = {
        "title": "Django x React",
        "ReactRuntime": '<script crossorigin src="https://unpkg.com/react/umd/react.production.min.js"></script>' +
  '<script crossorigin src="https://unpkg.com/react-dom/umd/react-dom.production.min.js"></script>' +
  '<script crossorigin src="https://unpkg.com/@mui/material/umd/material-ui.production.min.js"></script>' +
  '<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>'
    }
    return render(request, "index.html", context)
