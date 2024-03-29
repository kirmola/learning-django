from aiohttp import ClientSession
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.
class DictionaryView(View):
    async def fetch_data(self, word):
        baseurl = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        # try:
        async with ClientSession() as session:
            async with session.get(baseurl) as response:
                if response.status == 200:
                    data = await response.json()
                    return render(self.request, "dict/define.html", {
                        "data": data[0]
                    })
                    # return JsonResponse(data[0])
                else:
                    return HttpResponse("Can't find the meaning of this", status=404)
        # except Exception as e:
        #     return HttpResponse("An error occurred: " + str(e), status=500)

    async def get(self, request, word):
        data = await self.fetch_data(word)
        return data


def home(request):
    return render(request, "dict/home.html")