init:
    $ prologue = 0

label prologue:

    $ make_names_unknown()

    $ backdrop = "prologue"

    $ new_chapter(-1, u"Пролог")

    $ prolog_time()

    play music music_list["a_promise_from_distant_days_v2"] fadein 3

    $ renpy.pause(3)

    scene anim prolog_1 
    with fade3

    window show

    "Мне опять снился этот сон."
    "{i}Этот{/i} сон..."
    "Я уже и не помню, сколько дней или недель подряд он повторяется."
    "И как всегда, наутро все забудется."
    "Хотя, может быть, оно и к лучшему..."
    "Останутся только туманные воспоминания о каких-то воротах, статуях пионеров и странной девочке...{w} которая постоянно спрашивает меня:"
    window hide

    scene black 
    with fade3

    scene bg ext_camp_entrance_night 
    show owl :
        pos (931, 88)
    show prologue_dream 
    with fade3

    window show
    dreamgirl "Ты пойдешь со мной?"
    "Пойду?.."
    "Но куда?"
    "И зачем?.."
    "Да и где я вообще нахожусь?"
    "Конечно, если бы все происходило на самом деле, наяву, то стоило непременно испугаться."
    "Ну конечно, а как иначе!"
    "Но это – всего лишь сон.{w} Тот самый, который я вижу каждую ночь.{w} Но все равно сон."
    "Однако я здесь не просто так."
    "Необязательно знать {i}где{/i} и {i}почему{/i}, чтобы понять, что что-то происходит."
    "Нечто, отчаянно требующее моего внимания."
    "Ведь здесь все такое реальное."
    "Реальное настолько, насколько реальны вещи в моей квартире – я бы мог открыть ворота, услышать скрип петель, смахнуть рукой осыпающуюся ржавчину, потянуть носом свежий морозный воздух и поежиться от холода."
    "Мог бы, но для этого надо сдвинуться с места, сделать шаг, пошевелить рукой..."
    "А ведь это сон...{w} И даже если я это и понимаю, то сделать ничего не могу."
    "Ведь здесь – словно по ту сторону старого телевизора, из последних сил борющегося с помехами и старающегося показать зрителям все, не упустив ни малейшей детали."
    "Но четкость картинки все меньше...{w} Наверное, скоро просыпаться."
    "..."
    window hide

    with fade2

    window show
    "Может быть, спросить у нее что-то?{w} У той девочки."
    "Как же ее зовут..."
    "Например, про звезды..."
    "Хотя почему звезды..."
    "Можно же спросить про ворота!{w} Да, про ворота!"
    "Вот она удивится."
    "Хотя лучше про букву {i}ё{/i}."
    "Хорошая была буква..."
    "Хотя почему была..."
    "И какое отношение буквы, ворота и звезды имеют к этому месту?"
    "Ведь если мне каждую ночь снится этот сон, а проснувшись, я ничего не помню, то это значит, что надо искать разгадку здесь и сейчас, пусть и во сне..."
    "А вот если присмотреться, то можно совершенно четко разглядеть Магелланово Облако..."
    "Как будто попал в южное полушарие!"
    "..."
    window hide

    with fade2

    window show
    "Во сне всегда больше волнует неестественный цвет травы, невозможная кривизна прямых и отражения в камне, а не реальная опасность, готовая оборвать все здесь и сейчас."
    "Естественно, ведь {i}здесь{/i} нельзя умереть."
    "Я точно знаю – я делал это тысячу раз..."
    "А если нельзя умереть, то нет и стимула жить?"
    "Надо будет спросить у этой девочки – она местная, значит, должна знать."
    "Да, именно!{w} Спросить, например, про сову."
    "Больно уж птица странная..."
    "А впрочем, неважно..."
    "..."
    window hide

    with fade2

    window show
    dreamgirl "Ты пойдешь со мной?"
    "И каждый раз надо отвечать."
    "Иначе никак, иначе сон не закончится, а я – не проснусь."
    window hide

    $ renpy.pause(2)

    menu:
        "Да, я пойду с тобой":
            $ prologue = 1
        "Нет, я останусь здесь":
            pass

    $ renpy.pause(1)

    window show
    "И каждый раз так сложно решить, что же ответить."
    "Где я, что я здесь делаю, кто она такая?.."
    "И почему от ответа на этот вопрос зависит так много в моей жизни?"
    "Или не зависит?.."
    "В конце концов, ведь это просто сон..."

    stop music fadeout 5

    "Ведь так?.."
    window hide

    scene bg black 
    with fade3

    $ renpy.pause(2)

    play sound_loop sfx_keyboard_mouse_computer_noise fadein 3

    scene anim 1 _prologue 
    with fade3

    $ renpy.pause(9.4, hard=True)

    scene anim 2 _prologue 
    with fade3

    $ renpy.pause(9.4, hard=True)

    scene anim 3 _prologue 
    with fade3

    $ renpy.pause(6.2, hard=True)

    window show
    "Экран монитора смотрел на меня словно живой."
    window hide

    show blinking  with dissolve

    $ renpy.pause(3.5)

    window show
    "Иногда мне правда казалось, что он обладает сознанием, своими мыслями и желаниями, стремлениями; умеет чувствовать, любить и страдать."
    hide blinking 
    "Иногда мне казалось, что инструмент, неодушевленный кусок металла и текстолита в наших отношениях не он, а я."
    "Наверное, в этом была доля правды, ведь компьютер на 90%% обеспечивал мое общение с внешним миром."
    "Анонимные имиджборды, иногда какие-то чаты, редко – аська или джаббер, еще реже – форумы."
    window hide
    show blinking  with dissolve

    $ renpy.pause(3.5)

    window show
    "И все люди, сидящие по ту сторону сетевого кабеля: кто-то далеко, за тысячи километров, а кто-то – в соседнем доме, – всего лишь плод его больной фантазии, ошибка в программном коде или баг ядра, зажившего собственной жизнью."
    window hide

    hide blinking 

    $ renpy.pause(3)

    scene anim prolog_15 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_3 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_4 
    with fade
    $ renpy.pause(3, hard=True)

    stop sound_loop fadeout 4

    window show
    "Если посмотреть со стороны на мое существование, то такие мысли покажутся не столь уж бредовыми, хотя какой-нибудь психолог наверняка поставил бы мне кучу заумных диагнозов, а, возможно, и выписал направление в желтый дом."
    window hide

    $ renpy.pause(3)

    scene anim prolog_5 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_14 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim prolog_11 
    with fade
    $ renpy.pause(3, hard=True)

    window show
    "Маленькая квартирка, в которой не наблюдалось не то что следов какого бы то ни было ремонта, но и даже подобия порядка, и всегда одинаковый вид из окна на серый, вечно куда-то бегущий мегаполис, – вот условия моей повседневной жизни."
    window hide

    play music music_list["farewell_to_the_past_edit"] fadein 5

    $ renpy.pause(3)

    scene anim prolog_2 
    with fade
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Конечно, все начиналось далеко не так..."
    "Я, как и все обычные люди, родился, пошел в школу, закончил ее.{w} Не сказать чтобы очень хорошо, но и не плохо."
    "Поступил в институт, где кое-как промучился полтора курса."
    "Работал на паре-тройке разных работ.{w} Иногда даже и неплохо, иногда даже получая за это достойные деньги."
    "Однако все это было чем-то не тем."
    "Я не ощущал полноту жизни – все словно зациклилось на каком-то этапе и продолжало идти по кругу.{w} Как в фильме «День сурка»."
    "Только у меня не было выбора, как именно провести этот день, и каждый раз все повторялось по одной и той же схеме.{w} Схеме пустоты, уныния и отчаяния."
    nvl clear
    window hide

    $ renpy.pause(3)

    window show
    "Последние несколько лет я просто целыми днями сидел за компьютером."
    "Иногда подворачивались какие-то халтурки, иногда помогали родители."
    "В общем, на жизнь хватало."
    "Это и немудрено, ведь потребности у меня были небольшие."
    "На улицу я практически не выходил, а все мое общение с людьми сводилось к интернет-переписке с анонимами, ни имен, ни возраста, ни пола которых я не знал."
    "Короче говоря, достаточно типичная жизнь достаточно типичного асоциального человека своего времени.{w} Этакий Обломов XXI века."
    "Может быть, кто-то с меня когда-нибудь напишет роман, который станет классикой современной литературы.{w} Или напишу я сам…"
    "Впрочем нет, что себя обманывать – уже не раз пытался, но меня не хватало даже на короткий рассказ."
    nvl clear
    "Пытался я также изучить и множество других вещей."
    "Рисовать – не дано от природы.{w} Программирование – надоело.{w} Иностранные языки – долго и скучно…"
    "Любил я разве что читать, но даже при этом никогда бы не смог себя назвать эрудированным человеком."
    "Возможно, я был асом в просмотре аниме и отпускании неумелых шуточек в интернете."
    "Если бы за это платили деньги, это, конечно, меня порадовало (да и заработал бы неплохо), но вряд ли таким образом заполнилась бы пустота в моей душе."
    nvl clear
    window hide

    scene bg semen_room_window 
    with fade

    stop music fadeout 4

    play sound_loop sfx_street_traffic_outside fadein 2

    $ renpy.pause(3)    

    window show
    "Сегодня очередной типичный день моей типичной жизни типичного неудачника."
    "И сегодня мне нужно ехать на встречу институтских товарищей."
    "По правде говоря, желания не было ни малейшего, да и какой смысл, если вместе с ними я отучился всего ничего."
    "Однако меня каким-то образом все же уговорил друг, бывший одногруппник, один из немногих людей, с кем я поддерживал контакт не только в интернете."
    window hide

    $ renpy.pause(4)

    stop sound_loop fadeout 3

    play ambience ambience_cold_wind_loop fadein 3

    $ set_mode_adv()

    play sound sfx_intro_bus_stop_steps

    scene anim intro_1 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_2 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_3 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_4 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_5 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_6 
    with fade
    $ renpy.pause(3, hard=True)

    play sound sfx_intro_bus_stop_sigh

    scene anim intro_8 
    with fade
    $ renpy.pause(3, hard=True)
    scene anim intro_7 
    with fade
    $ renpy.pause(3, hard=True)

    scene bg bus_stop 
    with fade

    window show
    "Вечер. Мороз.{w} Остановка и ожидание автобуса."
    "Я никогда не любил зиму.{w} Впрочем, и жаркое лето тоже не моя стихия."
    "Просто не вижу смысла выделять какое-то одно время года – не столь важно, какая погода на улице, если ты целыми днями сидишь дома."
    "Автобус сегодня задерживался так сильно, что я уже был готов плюнуть на все и потратить последнюю пару сотен на такси (совсем не ехать мне почему-то в голову не пришло)."
    "В голове, как всегда, роились миллионы мыслей, из которых было совершенно невозможно выудить хотя бы одну стоящую."
    "Такую, которую можно закончить, привести в порядок, облечь в форму идеи и претворить в жизнь."
    "Может быть, заняться бизнесом?{w} Но откуда я возьму деньги?"
    "Или пойти опять работать в офис?{w} Нет уж!"
    "Может, стоит попробовать фриланс?{w} Да что я умею, и кому я нужен…"
    window hide

    $ renpy.pause(3)

    scene anim prolog_2 
    with fade
    $ renpy.pause(1)

    $ set_mode_nvl()

    window show
    "Вдруг мне вспомнилось детство…{w} Или скорее юношество – 15-17 лет."
    "Почему именно это время?{w} Я даже и сам не мог ответить на этот вопрос."
    "Наверное, потому что тогда все было проще."
    "Не нужна была лишняя мотивация для принятия таких сложных сейчас и таких простых тогда решений."
    "Проснувшись с утра, ты четко знал, чем будешь заниматься весь день, а выходных ждал с нетерпением, ведь тогда можно будет отдохнуть, заняться любимыми делами – компьютер, футбол, встречи с друзьями."
    "А потом, когда наступит новая неделя, вновь приняться за учебу."
    "Ведь раньше не возникало этих мучительных вопросов «зачем», «кому это надо», «что изменится, если я это сделаю» или «что не изменится»."
    "Простой поток жизни, такой привычный для любого нормального человека и такой чуждый для меня теперешнего."
    nvl clear
    "Время беззаботного детства…{w} Тогда же я и встретил свою первую любовь."
    "Сейчас уже и не вспомнить ее внешность, характер."
    "В памяти осталось разве что имя и те чувства, которые захлестывали меня, когда я был с ней.{w} Теплота, нежность, желание заботиться о ней, защитить…"
    "Жаль, что это продолжалось так недолго…"
    "Сейчас я уже с трудом могу себе представить что-то подобное."
    "Наверное, и хочется познакомиться с девушкой, только не знаю, как начать диалог, о чем вообще с ней говорить, чем ее заинтересовать."
    "Да и по правде говоря, подходящих девушек я давно не встречал.{w} Хотя где бы я их смог встретить…"
    nvl clear
    window hide

    play sound sfx_intro_bus_engine_start

    $ renpy.pause(3)

    play sound_loop sfx_intro_bus_engine_loop fadein 3

    $ set_mode_adv()

    scene anim intro_9 
    with fade2

    window show
    "Звук работающего двигателя вывел меня из размышлений."
    "Подъехал автобус."
    "«Какой-то он не такой» – пронеслось у меня в голове."
    "Впрочем, какая разница – по этому маршруту ходит только 410."
    window hide

    $ renpy.pause(2)

    scene anim intro_10 
    with fade

    play sound sfx_intro_bus_door_open

    $ renpy.pause(3, hard=True)
    scene anim intro_11 
    with fade
    $ renpy.pause(1, hard=True)

    stop sound_loop fadeout 4

    scene anim intro_13 
    with fade2
    $ renpy.pause(3, hard=True)

    scene bg intro_xx 
    with fade

    stop ambience fadeout 2
    play sound_loop sfx_bus_interior_moving fadein 4

    window show
    "Огни пролетают мимо, их холодный свет словно зажигает где-то внутри меня что-то большое и светлое."

    $ volume(0.5, "music")

    play music music_list["lightness_radio_bus"] fadein 7

    "Или не зажигает, а просто пробуждает…"
    "Ведь «это» уже давно сидело внутри, то затихая, то просыпаясь вновь."
    "Какая-то очень известная мелодия играла в радиоприемнике у водителя.{w} Но я ее не слушал."
    "Я смотрел в запотевшее окно автобуса на проезжающие мимо машины."
    "Ведь люди куда-то спешат, ведь им что-то нужно, и, погруженные в свои дела, они не задумываются о вопросах, мучающих меня."
    "Возможно, у них тоже есть свои серьезные проблемы, а может, им живется намного лучше."
    "Знать наверняка нельзя, так как все люди разные.{w} Или не разные?"
    "Бывает, что поступки какого-то человека легко предсказуемы, но, пытаясь заглянуть к нему в душу, видишь только непроглядную тьму."
    "..."
    "Автобус приближался к центру, и мои мысли нарушил яркий свет огней большого города."
    "Сотни горящих рекламных вывесок, тысячи машин, миллионы людей."
    "Я смотрел на это светопреставление, и мне почему-то безумно захотелось спать."
    window hide

    stop music fadeout 3

    show blink  with dissolve
    $ renpy.pause(1.5)

    window show
    "Глаза закрылись всего на полсекунды и…"
    window hide

    stop sound_loop fadeout 3

    scene bg black 
    with fade3

    $ renpy.pause(3)

    $ volume(1.0, "music")

    jump opening

label opening:



    $ renpy.pause(2, hard=True)

    play music music_list["opening"] fadein 5

    scene black 

    $ renpy.pause(3, hard=True)

    scene op_back 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_sl 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_un 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_us 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_dv 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_mi 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show op_uv 
    with dissolve2

    $ renpy.pause(2, hard=True)

    show logo_day :
        pos (400,150)
    with dissolve2

    $ renpy.pause(2, hard=True)

    scene black 
    with dissolve2

    stop music fadeout 5

    $ renpy.pause(5, hard=True)

    jump day1
