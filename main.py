# -*- coding: utf-8 -*-
import moedas
from datetime import datetime
import tweepy
from time import sleep


def authentication():
    import tweepy
    auth = tweepy.OAuthHandler('y6fukObkpSjzBxmvjC6SGmuS8', '4lzourDn9G401pYmcjcMdGLGjf5aNn4QWt7GNBnigjHBtOQ18g')
    auth.set_access_token('1318621717816889349-M3NfaDMydbplb4l0YxG4skFrjrUm7e',
                          'kQdaLbsA2vxr7GsygxTjUFXunZnElBryiyTHS5qCLmZGz')
    api = tweepy.API(auth, wait_on_rate_limit=False)
    return api


def return_time(only_minute=False, only_hour=False):
    hour = datetime.now().hour
    minute = datetime.now().minute
    if not only_hour and not only_minute:
        if minute == 0:
            minute = str(minute) + '0'
        return str(hour) + ':' + str(minute)
    elif only_hour:
        return hour
    elif only_minute:
        return minute


api = authentication()

contador = 0
try:
    dolar_antigo = moedas.cotacao_dolar()
    euro_antigo = moedas.cotacao_euro()
    libra_antigo = 'x'
except Exception as e:
    print('Ocorrou um erro: ', e)
while True:
    sleep(2)
    minute = return_time(only_minute=True)
    hour = return_time(only_hour=True)
    if minute == 0:
        minute = str(minute) + '0'
    hmin = return_time()

    if int(minute) % 15 == 0:
        print(f'vendo se há diferença, às {hmin}')
        print(f'Dolar = {moedas.cotacao_dolar()} Euro = {moedas.cotacao_euro()}')
        try:
            dolar = moedas.cotacao_dolar()
            euro = moedas.cotacao_euro()
            libra = moedas.cotacao_libra()
        except Exception as e:
            print('Ocorreu um erro:', e)

        try:
            # Dolar
            if dolar_antigo == dolar:
                post_dolar = ''
            elif dolar_antigo > dolar:
                post_dolar = f"Dólar caiu :) -> R${dolar}  "
                dolar_antigo = dolar
            else:
                post_dolar = f"Dólar subiu :( -> R${dolar}"
                dolar_antigo = dolar

            # Euro
            if euro_antigo == euro:
                post_euro = ''
            elif euro_antigo > euro:
                post_euro = f"\nEuro caiu :) -> R${euro}"
                euro_antigo = euro
            else:
                post_euro = f"\nEuro subiu :( -> R${euro}"
                euro_antigo = euro

            # Libra
            if libra_antigo == libra:
                post_libra = ''
            elif libra_antigo > libra:
                post_libra = f'\nLibra Caiu :) -> R${libra}'
                libra_antigo = libra
            else:
                post_libra = f'\nLibra subiu :( -> R${libra}'
                libra_antigo = libra

            if post_dolar == '' and post_euro == '' and post_libra == '':
                print('Nada foi postado.')
                sleep(61)
            else:
                api.update_status(f'{post_dolar}{post_euro}{post_libra}\nàs {hmin}'.strip())
                print('Postei.')
                sleep(61)
        except tweepy.error.TweepError as e:
            print(f'Ocorreu um erro: {e}')
            pass
        except Exception as error:
            print(f'Aconteceu um erro --> {error}')
            pass
        finally:
            sleep(30)
            contador += 1
            print('end of loop num', contador)
            print(20 * '=-')
