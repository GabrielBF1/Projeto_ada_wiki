import os
import json
from airium import Airium


page = Airium()
page('<!DOCTYPE html>')

for file in os.listdir("./json_files/"):
    if file.endswith(".json"):
        f = open("./json_files/" + file)
        data = json.load(f)
        print(data["titulo"])
        with page.html():
            with page.head():
                page.meta(charset="utf-8")
                page.title(_t=data["titulo"])
            with page.body():
                with page.h1(style="font-family:Abadi;"):
                    page(data["titulo"])
            with page.p(style="font-family:Abadi;"):
                page(data["descricao"])
            with page.p(style="font-size: 14px; font-family:Abadi;", align="center"):
                page("<br><br>Autor: " + data["autor"])
        html = str(page)
        html_file = open("./html_files/" + file.replace(".json", ".html"), "w")
        html_file.write(html)
        page = Airium()
        page('<!DOCTYPE html>')