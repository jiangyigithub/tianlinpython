favorite_languages={
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',
}
survey_0=['jen','jiang yi','tian lin','sarah','edward','phil']
for survey in sorted(survey_0):    #在for 循环中按字母表进行排序
    if survey in favorite_languages.keys():
        print(f"{survey.title()},Thank you for taking the poll!")
    else:
        print(f'{survey.title()}.Sorry,please take our poll!')
