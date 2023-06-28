import requests
from coloreflection import Color

C = Color()


def get_info_about_game_by_cusa(cusa):
    response = requests.get(f"https://orbispatches.com/en/CUSA{cusa}")

    if "Whoops, 404!" in response.text:
        return False

    title = response.text.split("<title>")[-1].split("</title>")[0]
    title = title.split(":", 1)[-1].split("|")[0].strip()
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
