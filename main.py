import requests
from bs4 import BeautifulSoup
from coloreflection import Color

C = Color()


def get_title_by_tag(tag):
    if tag.h1:
        return tag.h1.string
    return tag.img.get("alt", False)


def get_info_about_game_by_cusa(cusa):
    response = requests.get(f"https://orbispatches.com/en/CUSA{cusa}")
    soup = BeautifulSoup(response.text, "html.parser")

    if soup.find("h3", string="Whoops, 404!"):
        return False

    title = get_title_by_tag(soup.find("div", class_="flex-fill"))
    return title


def main():
    print(C.border(" Чтобы завершить работу приложения, нажмите Enter (введите пустую строку) \n"))
    while cusa := input(C.FG.purple("Введите код CUSA: ")):
        cusa = cusa.split("CUSA")[-1]
        title = get_info_about_game_by_cusa(cusa)

        if not title:
            print(C.FG.red("Не удалось найти игру с таким CUSA"))
            continue

        print(f"{C.FG.lightgreen('Название игры')}: {C.bold(title)} ({C.italic('CUSA' + cusa)})")


if __name__ == "__main__":
    main()
