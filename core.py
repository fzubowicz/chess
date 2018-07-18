import fun

### białe

## pionki [x,y]
b_p_1 = [1, 2, 1, 'p']
b_p_2 = [2, 2, 1, 'p']
b_p_3 = [3, 2, 1, 'p']
b_p_4 = [4, 2, 1, 'p']
b_p_5 = [5, 2, 1, 'p']
b_p_6 = [6, 2, 1, 'p']
b_p_7 = [7, 2, 1, 'p']
b_p_8 = [8, 2, 1, 'p']

## figury [x,y]

# wieża
b_wie_l = [1, 1, 1, 'w']
b_wie_p = [8, 1, 1, 'w']

# Skoczek
b_skocz_l = [2, 1, 1, 's']
b_skocz_p = [7, 1, 1, 's']

# goniec

b_gon_l = [3, 1, 1, 'g']
b_gon_p = [6, 1, 1, 'g']

# król królowa
b_hetman = [4, 1, 1, 'h']
b_krol = [5, 1, 1, 'k']

biale_lista = ([b_krol] + [b_hetman]
               + [b_p_1] + [b_p_2] + [b_p_3] + [b_p_4] + [b_p_5] + [b_p_6] + [b_p_7] + [b_p_8]
               + [b_wie_l] + [b_wie_p]
               + [b_skocz_l] + [b_skocz_p]
               + [b_gon_l] + [b_gon_p])

### czarne

## pionki [x,y]
c_p_1 = [1, 7, 1, 'p']
c_p_2 = [2, 7, 1, 'p']
c_p_3 = [3, 7, 1, 'p']
c_p_4 = [4, 7, 1, 'p']
c_p_5 = [5, 7, 1, 'p']
c_p_6 = [6, 7, 1, 'p']
c_p_7 = [7, 7, 1, 'p']
c_p_8 = [8, 7, 1, 'p']

## figury [x,y]

# wieża
c_wie_l = [1, 8, 1, 'w']
c_wie_p = [8, 8, 1, 'w']

# Skoczek
c_skocz_l = [2, 8, 1, 's']
c_skocz_p = [7, 8, 1, 's']

# goniec
c_gon_l = [3, 8, 1, 'g']
c_gon_p = [6, 8, 1, 'g']

# król królowa
c_hetman = [5, 8, 1, 'h']
c_krol = [4, 8, 1, 'k']

czarne_lista = ([c_krol] + [c_hetman]
                + [c_p_1] + [c_p_2] + [c_p_3] + [c_p_4] + [c_p_5] + [c_p_6] + [c_p_7] + [c_p_8]
                + [c_wie_l] + [c_wie_p]
                + [c_skocz_l] + [c_skocz_p]
                + [c_gon_l] + [c_gon_p])

############################################ szachownica
print('     A |  B |  C |  D |  E |  F |  G |  H |')
for y_chessboard in range(8, 0, -1):

    print('   ____ ____ ____ ____ ____ ____ ____ ____')
    print(y_chessboard, '|', end='')
    for x_chessboard in range(1, 9, 1):
        kind = None
        for x, y, zywe, rodzaj in biale_lista:
            if y == y_chessboard and x == x_chessboard and zywe == 1:
                kind = rodzaj
                color = 'b'
                break
        for x, y, zywe, rodzaj in czarne_lista:
            if y == y_chessboard and x == x_chessboard and zywe == 1:
                kind = rodzaj
                color = 'c'
                break
        if kind == None:
            print(f'    ', end='')
        elif kind != None:
            print(f' {color}{kind} ', end='')
        print('|', end='')
    print('')
print('   ____ ____ ____ ____ ____ ____ ____ ____')


##################################################################### gra
while biale_lista[0][2] == 1 and czarne_lista[0][2] == 1:
    legit = False
    while legit == False:
        print('Ruch białego gracza.')
        start = input('Wybierz figurę (np b2): ')

        x_litera_start = fun.znak_do_liczby(start[0])

        y_liczba_start = int(start[1])
        a = 0
        rodzaj_figury = ''
        for x, y, zywy, rodzaj in biale_lista:
            if x == x_litera_start and y == y_liczba_start and zywy == 1:
                rodzaj_figury = rodzaj
                break
            a += 1

        stop = input('Na które pole przesuwasz (np b4)? ')
        x_litera_stop = fun.znak_do_liczby(stop[0])

        y_liczba_stop = int(stop[1])
        ruch = None
        biala_figura = None
        czarne_figura = None
        for x, y, zywy, rodzaj in biale_lista:
            if x == x_litera_stop and y == y_liczba_stop and zywy == 1:
                biala_figura = 1
                break
        c = 0
        for x, y, zywy, rodzaj in czarne_lista:
            if x == x_litera_stop and y == y_liczba_stop and zywy == 1:
                czarne_figura = 1
                break
            c += 1

        ########################################################################################## pionki
        ######### ruch początkowy
        if rodzaj_figury == 'p' and y_liczba_start == 2 and y_liczba_stop == biale_lista[a][1] + 2:
            for x, y, zywy, rodzaj in biale_lista:
                if (y == y_liczba_start + 1 or y == y_liczba_start + 2) and x == x_litera_start and zywy == 1:
                    ruch = 0

            for x, y, zywy, rodzaj in czarne_lista:
                if (y == y_liczba_start + 1 or y == y_liczba_start + 2) and x == x_litera_start and zywy == 1:
                    ruch = 0

            if ruch != 0:
                biale_lista[a][1] = biale_lista[a][1] + 2
                legit = True

        ######### ruch zwykły
        elif rodzaj_figury == 'p' and x_litera_start == x_litera_stop and y_liczba_stop == biale_lista[a][
            1] + 1 and zywy == 1:
            for x, y, zywy, rodzaj in biale_lista:
                if y == y_liczba_start + 1 and x == x_litera_start and zywy == 1:
                    ruch = 0

            for x, y, zywy, rodzaj in czarne_lista:
                if y == y_liczba_start + 1 and x == x_litera_start and zywy == 1:
                    ruch = 0
            if ruch != 0:
                biale_lista[a][1] = biale_lista[a][1] + 1
                legit = True

        ######### bicie
        elif rodzaj_figury == 'p' and abs(x_litera_start - x_litera_stop) == 1 and y_liczba_stop == biale_lista[a][1] + 1:
            for x, y, zywy, rodzaj in biale_lista:
                if y + 1 == y_liczba_stop and (x + 1 == x_litera_stop or x - 1 == x_litera_stop) and zywy == 1:
                    ruch = 0

            for x, y, zywy, rodzaj in czarne_lista:
                if x == x_litera_stop and y == y_liczba_stop and zywy == 1:
                    biale_lista[a][0:2] = x, y
                    czarne_lista[c][2] = 0
                    legit = True

        ######## Zmiana figury
        if rodzaj_figury == 'p' and biale_lista[a][1] == 8 and biale_lista[a][2] == 1:
                zmiana_figury = input('Podaj na jaką figurę chcesz zmienić pionka. [g]oniec, [k]rólowa, [s]koczek, [w]ieża')
                biale_lista[a][3] = zmiana_figury



        ########################################################################################## wieża
        if rodzaj_figury == 'w' and (x_litera_start == x_litera_stop or y_liczba_start == y_liczba_stop)\
                and not (x_litera_start == x_litera_stop and y_liczba_start == y_liczba_stop):

            if y_liczba_start - y_liczba_stop > 0:
                poczatek = y_liczba_stop
                koniec = y_liczba_start
                znak = 'y'
            elif y_liczba_start - y_liczba_stop < 0:
                poczatek = y_liczba_start
                koniec = y_liczba_stop
                znak = 'y'
            elif x_litera_start - x_litera_stop > 0:
                poczatek = x_litera_stop
                koniec = x_litera_start
                znak = 'x'
            elif x_litera_start - x_litera_stop < 0:
                poczatek = x_litera_start
                koniec = x_litera_stop
                znak = 'x'
            ######### bicie
            if czarne_figura == 1 and 1==1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break


            ######### ruch
            if czarne_figura != 1 and biala_figura != 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            if ruch != 0 and czarne_figura == 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                czarne_lista[c][2] = 0
                legit = True
            elif ruch != 0 and biala_figura != 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## skoczek
        if rodzaj_figury == 's' and \
                (abs(x_litera_start - x_litera_stop) == 2 and abs(y_liczba_start - y_liczba_stop) == 1) \
                or (abs(x_litera_start - x_litera_stop) == 1 and abs(y_liczba_start - y_liczba_stop) == 2):

            ######### ruch & bicie
            if czarne_figura == 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                czarne_lista[c][2] = 0
                legit = True
            elif biala_figura != 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## goniec
        if rodzaj_figury == 'g' and abs(x_litera_start - x_litera_stop) == abs(y_liczba_start - y_liczba_stop):
            d = 1
            liczba_ruchow = abs(y_liczba_start - y_liczba_stop)

            ##### bicie i ruch
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in biale_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                d += 1
            d = 1
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in czarne_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif ruch == 0:
                        break
                d += 1

            if czarne_figura == 1 and ruch != 0:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                czarne_lista[c][2] = 0
                legit = True
            elif biala_figura != 1 and ruch != 0:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## hetman

        if rodzaj_figury == 'h' and (x_litera_start == x_litera_stop or y_liczba_start == y_liczba_stop) \
                and not (x_litera_start == x_litera_stop and y_liczba_start == y_liczba_stop):

            if y_liczba_start - y_liczba_stop > 0:
                poczatek = y_liczba_stop
                koniec = y_liczba_start
                znak = 'y'
            elif y_liczba_start - y_liczba_stop < 0:
                poczatek = y_liczba_start
                koniec = y_liczba_stop
                znak = 'y'
            elif x_litera_start - x_litera_stop > 0:
                poczatek = x_litera_stop
                koniec = x_litera_start
                znak = 'x'
            elif x_litera_start - x_litera_stop < 0:
                poczatek = x_litera_start
                koniec = x_litera_stop
                znak = 'x'
            ######### bicie
            if czarne_figura == 1 and 1 == 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            ######### ruch
            if czarne_figura != 1 and biala_figura != 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            if ruch != 0 and czarne_figura == 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                czarne_lista[c][2] = 0
                legit = True
            elif ruch != 0 and biala_figura != 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        elif rodzaj_figury == 'h' and abs(x_litera_start - x_litera_stop) == abs(y_liczba_start - y_liczba_stop):
            d = 1
            liczba_ruchow = abs(y_liczba_start - y_liczba_stop)

            ##### bicie i ruch
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in biale_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                d += 1
            d = 1
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in czarne_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif ruch == 0:
                        break
                d += 1

            if czarne_figura == 1 and ruch != 0:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                czarne_lista[c][2] = 0
                legit = True
            elif biala_figura != 1 and ruch != 0:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## krol

        if rodzaj_figury == 'k' and abs(y_liczba_start - y_liczba_stop) <= 1 and abs(x_litera_start-x_litera_stop) <= 1:
            if czarne_figura == 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                czarne_lista[c][2] = 0
                legit = True
            elif biala_figura != 1:
                biale_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        if legit == False:
            print('Wykonałeś niedozwolony ruch. Powtórz go!')

############################################################################################################################################ czarny
    if czarne_lista[0][2] == 0:
        break

    ############################################ szachownica
    print('     A |  B |  C |  D |  E |  F |  G |  H |')
    for y_chessboard in range(8, 0, -1):

        print('   ____ ____ ____ ____ ____ ____ ____ ____')
        print(y_chessboard, '|', end='')
        # print('|', end='')
        for x_chessboard in range(1, 9, 1):
            kind = None
            for x, y, zywe, rodzaj in biale_lista:
                if y == y_chessboard and x == x_chessboard and zywe == 1:
                    kind = rodzaj
                    color = 'b'
                    break
            for x, y, zywe, rodzaj in czarne_lista:
                if y == y_chessboard and x == x_chessboard and zywe == 1:
                    kind = rodzaj
                    color = 'c'
                    break

            if kind == None:
                print(f'    ', end='')
            elif kind != None:
                print(f' {color}{kind} ', end='')
            print('|', end='')
        print('')
    print('   ____ ____ ____ ____ ____ ____ ____ ____')

    legit = False
    while legit == False:
        print('Ruch czarnego gracza.')
        start = input('Wybierz figurę (np b2): ')

        x_litera_start = fun.znak_do_liczby(start[0])

        y_liczba_start = int(start[1])
        a = 0
        rodzaj_figury = ''
        for x, y, zywy, rodzaj in czarne_lista:
            if x == x_litera_start and y == y_liczba_start and zywy == 1:
                rodzaj_figury = rodzaj
                break
            a += 1

        stop = input('Na które pole przesuwasz (np b4)? ')
        x_litera_stop = fun.znak_do_liczby(stop[0])

        y_liczba_stop = int(stop[1])
        ruch = None
        biala_figura = None
        czarne_figura = None
        for x, y, zywy, rodzaj in czarne_lista:
            if x == x_litera_stop and y == y_liczba_stop and zywy == 1:
                czarne_figura = 1
                break
        c = 0
        for x, y, zywy, rodzaj in biale_lista:
            if x == x_litera_stop and y == y_liczba_stop and zywy == 1:
                biala_figura = 1
                break
            c += 1

        ########################################################################################## pionki
        ######### ruch początkowy
        if rodzaj_figury == 'p' and y_liczba_start == 7 and y_liczba_stop == czarne_lista[a][1] - 2:
            for x, y, zywy, rodzaj in czarne_lista:
                if (y == y_liczba_start - 1 or y == y_liczba_start - 2) and x == x_litera_start and zywy == 1:
                    ruch = 0

            for x, y, zywy, rodzaj in biale_lista:
                if (y == y_liczba_start - 1 or y == y_liczba_start - 2) and x == x_litera_start and zywy == 1:
                    ruch = 0

            if ruch != 0:
                czarne_lista[a][1] = czarne_lista[a][1] - 2
                legit = True

        ######### ruch zwykły
        elif rodzaj_figury == 'p' and x_litera_start == x_litera_stop and y_liczba_stop == czarne_lista[a][
            1] - 1 and zywy == 1:
            for x, y, zywy, rodzaj in czarne_lista:
                if y == y_liczba_start - 1 and x == x_litera_start and zywy == 1:
                    ruch = 0
                    break
            for x, y, zywy, rodzaj in biale_lista:
                if y == y_liczba_start - 1 and x == x_litera_start and zywy == 1:
                    ruch = 0
                    break
            if ruch != 0:
                czarne_lista[a][1] = czarne_lista[a][1] - 1
                legit = True

        ######### bicie
        elif rodzaj_figury == 'p' and abs(x_litera_start - x_litera_stop) == 1 and y_liczba_stop == czarne_lista[a][1] - 1:
            for x, y, zywy, rodzaj in czarne_lista:
                if y == y_liczba_stop - 1 and (x + 1 == x_litera_stop or x - 1 == x_litera_stop) and zywy == 1:
                    ruch = 0

            for x, y, zywy, rodzaj in biale_lista:
                if x == x_litera_stop and y == y_liczba_stop and zywy == 1:
                    czarne_lista[a][0:2] = x, y
                    biale_lista[c][2] = 0
                    legit = True

        ######### wyjątki
        if rodzaj_figury == 'p' and czarne_lista[a][1] == 1 and czarne_lista[a][2] == 1:
            zmiana_figury = input('Podaj na jaką figurę chcesz zmienić pionka. [g]oniec, [k]rólowa, [s]koczek, [w]ieża')
            czarne_lista[a][3] = zmiana_figury

        ########################################################################################## wieża
        if rodzaj_figury == 'w' and (x_litera_start == x_litera_stop or y_liczba_start == y_liczba_stop) \
                and not (x_litera_start == x_litera_stop and y_liczba_start == y_liczba_stop):

            if y_liczba_start - y_liczba_stop > 0:
                poczatek = y_liczba_stop
                koniec = y_liczba_start
                znak = 'y'
            elif y_liczba_start - y_liczba_stop < 0:
                poczatek = y_liczba_start
                koniec = y_liczba_stop
                znak = 'y'
            elif x_litera_start - x_litera_stop > 0:
                poczatek = x_litera_stop
                koniec = x_litera_start
                znak = 'x'
            elif x_litera_start - x_litera_stop < 0:
                poczatek = x_litera_start
                koniec = x_litera_stop
                znak = 'x'
            ######### bicie
            if biala_figura == 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            ######### ruch
            if czarne_figura != 1 and biala_figura != 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            if ruch != 0 and biala_figura == 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                biale_lista[c][2] = 0
                legit = True
            elif ruch != 0 and czarne_figura != 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## skoczek
        if rodzaj_figury == 's' and \
                (abs(x_litera_start - x_litera_stop) == 2 and abs(y_liczba_start - y_liczba_stop) == 1) \
                or (abs(x_litera_start - x_litera_stop) == 1 and abs(y_liczba_start - y_liczba_stop) == 2):

            ######### ruch & bicie
            if biala_figura == 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                biale_lista[c][2] = 0
                legit = True
            elif czarne_figura != 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## goniec
        if rodzaj_figury == 'g' and abs(x_litera_start - x_litera_stop) == abs(y_liczba_start - y_liczba_stop):
            d = 1
            liczba_ruchow = abs(y_liczba_start - y_liczba_stop)

            ##### bicie i ruch
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in biale_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                d += 1
            d = 1
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in czarne_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif ruch == 0:
                        break
                d += 1

            if biala_figura == 1 and ruch != 0:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                biale_lista[c][2] = 0
                legit = True
            elif czarne_figura != 1 and ruch != 0:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## hetman

        if rodzaj_figury == 'h' and (x_litera_start == x_litera_stop or y_liczba_start == y_liczba_stop) \
                and not (x_litera_start == x_litera_stop and y_liczba_start == y_liczba_stop):

            if y_liczba_start - y_liczba_stop > 0:
                poczatek = y_liczba_stop
                koniec = y_liczba_start
                znak = 'y'
            elif y_liczba_start - y_liczba_stop < 0:
                poczatek = y_liczba_start
                koniec = y_liczba_stop
                znak = 'y'
            elif x_litera_start - x_litera_stop > 0:
                poczatek = x_litera_stop
                koniec = x_litera_start
                znak = 'x'
            elif x_litera_start - x_litera_stop < 0:
                poczatek = x_litera_start
                koniec = x_litera_stop
                znak = 'x'
            ######### bicie
            if biala_figura == 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            ######### ruch
            if czarne_figura != 1 and biala_figura != 1:
                for iteracja in range(poczatek + 1, koniec):
                    for x, y, zywy, rodzaj in biale_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break
                    for x, y, zywy, rodzaj in czarne_lista:
                        if x == iteracja and y == y_liczba_start and zywy == 1 and znak == 'x':
                            ruch = 0
                            break
                        if y == iteracja and x == x_litera_start and zywy == 1 and znak == 'y':
                            ruch = 0
                            break

            if ruch != 0 and biala_figura == 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                biale_lista[c][2] = 0
                legit = True
            elif ruch != 0 and biala_figura != 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        elif rodzaj_figury == 'h' and abs(x_litera_start - x_litera_stop) == abs(y_liczba_start - y_liczba_stop):
            d = 1
            liczba_ruchow = abs(y_liczba_start - y_liczba_stop)

            ##### bicie i ruch
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in biale_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                d += 1
            d = 1
            while d < liczba_ruchow:
                for x, y, zywy, rodzaj_figury in czarne_lista:
                    if x_litera_stop > x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # right - up
                        if x == x_litera_start + d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif x_litera_stop > x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # right - down
                        if x == x_litera_start + d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop < y_liczba_start and d <= liczba_ruchow:  # left - down
                        if x == x_litera_start - d and y == y_liczba_start - d:
                            ruch = 0
                            break
                    elif x_litera_stop < x_litera_start and y_liczba_stop > y_liczba_start and d <= liczba_ruchow:  # left - up
                        if x == x_litera_start - d and y == y_liczba_start + d:
                            ruch = 0
                            break
                    elif ruch == 0:
                        break
                d += 1

            if biala_figura == 1 and ruch != 0:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                biale_lista[c][2] = 0
                legit = True
            elif czarne_figura != 1 and ruch != 0:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        ########################################################################################## krol

        if rodzaj_figury == 'k' and abs(y_liczba_start - y_liczba_stop) <= 1 and abs(x_litera_start - x_litera_stop) <= 1:
            if biala_figura == 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                biale_lista[c][2] = 0
                legit = True
            elif czarne_figura != 1:
                czarne_lista[a][0:2] = x_litera_stop, y_liczba_stop
                legit = True

        if biale_lista[0][2] == 0:
            break

        if legit == False:
            print('Wykonałeś niedozwolony ruch. Powtórz go!')

    ############################################ szachownica
    print('     A |  B |  C |  D |  E |  F |  G |  H |')
    for y_chessboard in range(8, 0, -1):

        print('   ____ ____ ____ ____ ____ ____ ____ ____')
        print(y_chessboard, '|', end='')
        for x_chessboard in range(1, 9, 1):
            kind = None
            for x, y, zywe, rodzaj in biale_lista:
                if y == y_chessboard and x == x_chessboard and zywe == 1:
                    kind = rodzaj
                    color = 'b'
                    break
            for x, y, zywe, rodzaj in czarne_lista:
                if y == y_chessboard and x == x_chessboard and zywe == 1:
                    kind = rodzaj
                    color = 'c'
                    break

            if kind == None:
                print(f'    ', end='')
            elif kind != None:
                print(f' {color}{kind} ', end='')
            print('|', end='')
        print('')
    print('   ____ ____ ____ ____ ____ ____ ____ ____')


if biale_lista[0][2] == 0:
    print('Czarny wygrywa!')
else:
    print('Biały wygrywa!')