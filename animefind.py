import laftel


def findAnime(title):
    animes = []
    for anime in laftel.sync.searchAnime(title):
        ng = []
        ng.append(anime.name)
        ng.append(anime.genres)
        animes.append(ng)
    return animes


print(findAnime("psycho-pass"))


# 장르별 애니 검색이 가능하게 하고 싶었다. 다만 이제 API가 좀 구리고 얘네들 자체 사이트에 있는것도 좀 별로라 뭐 어떻게 해야할지 모르겠다. 이정도면 라프텔 외부에서 애니 검색정도나 좀 가능할듯?
