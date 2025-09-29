from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .context import usercontext
from .forms import PromptForm
from .output import model_output


@login_required
def index(request):
    context = usercontext(request)
    context.update(
        {
            "titre_onglet": "Démo",
            "titre_presentation": "Démonstration",
            "response": "",
            "request": False,
        }
    )
    form = PromptForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        prompt = form.cleaned_data["prompt"]
        response = model_output(prompt)
        context.update({"prompt": prompt, "response": response, "request": True})

    context.update({"form": form})

    return render(request, "home/index.html", context)
