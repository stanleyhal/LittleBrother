import random

header1 = """
  _      _ _   _   _      ____            _   _
 | |    (_) | | | | |    |  _ \          | | | |
 | |     _| |_| |_| | ___| |_) |_ __ ___ | |_| |__   ___ _ __
 | |    | | __| __| |/ _ \  _ <| '__/ _ \| __| '_ \ / _ \ '__|
 | |____| | |_| |_| |  __/ |_) | | | (_) | |_| | | |  __/ |
 |______|_|\__|\__|_|\___|____/|_|  \___/ \__|_| |_|\___|_|
"""

header2 = """

 /$$       /$$   /$$     /$$     /$$           /$$$$$$$                        /$$     /$$
| $$      |__/  | $$    | $$    | $$          | $$__  $$                      | $$    | $$
| $$       /$$ /$$$$$$ /$$$$$$  | $$  /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$   /$$$$$$
| $$      | $$|_  $$_/|_  $$_/  | $$ /$$__  $$| $$$$$$$  /$$__  $$ /$$__  $$|_  $$_/  | $$__  $$ /$$__  $$ /$$__  $$
| $$      | $$  | $$    | $$    | $$| $$$$$$$$| $$__  $$| $$  \__/| $$  \ $$  | $$    | $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$  | $$ /$$| $$ /$$| $$| $$_____/| $$  \ $$| $$      | $$  | $$  | $$ /$$| $$  | $$| $$_____/| $$
| $$$$$$$$| $$  |  $$$$/|  $$$$/| $$|  $$$$$$$| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/| $$  | $$|  $$$$$$$| $$
|________/|__/   \___/   \___/  |__/ \_______/|_______/ |__/       \______/    \___/  |__/  |__/ \_______/|__/
"""

header5 = """
 ___        __  ___________  ___________  ___       _______
|"  |      |" \\("     _   ")("     _   ")|"  |     /"     "|
||  |      ||  |)__/  \\__/  )__/  \\__/ ||  |    (: ______)
|:  |      |:  |   \\_ /        \\_ /    |:  |     \\/    |
 \\  |___   |.  |   |.  |        |.  |     \\  |___  // ___)_
( \\_|:  \\  /\\  |\\  \\:  |        \\:  |    ( \\_|:  \\(:      "|
 \\_______)(__\\_|_)  \\__|         \\__|     \\_______)\\_______)
 _______    _______     ______  ___________  __    __    _______   _______
|   _  "\\  /"      \\   /    " \\("     _   ")/" |  | "\\  /"     "| /"      \\
(. |_)  :)|:        | // ____  \\)__/  \\__/(:  (__)  :)(: ______)|:        |
|:     \\/ |_____/   )/  /    ) :)  \\_ /    \\/      \\/  \\/    |  |_____/   )
(|  _  \\  //      /(: (____/ //   |.  |    //  __  \\  // ___)_  //      /
|: |_)  :)|:  __   \\ \\        /    \\:  |   (:  (  )  :)(:      "||:  __   \\
(_______/ |__|  \\___) \"_____/      \\__|    \\__|  |__/  \\_______)|__|  \\___)
"""

header6 = """
 _      ____  ______  ______  _        ___  ____   ____    ___   ______  __ __    ___  ____
| T    l    j|      T|      T| T      /  _]|    \\ |    \\  /   \\ |      T|  T  T  /  _]|    \\
| |     |  T |      ||      || |     /  [_ |  o  )|  D  )Y     Y|      ||  l  | /  [_ |  D  )
| l___  |  | l_j  l_jl_j  l_j| l___ Y    _]|     T|    / |  O  |l_j  l_j|  _  |Y    _]|    /
|     T |  |   |  |    |  |  |     T|   [_ |  O  ||    \\ |     |  |  |  |  |  ||   [_ |    \\
|     | j  l   |  |    |  |  |     ||     T|     ||  .  Yl     !  |  |  |  |  ||     T|  .  Y
l_____j|____j  l__j    l__j  l_____jl_____jl_____jl__j\\_j \\___/   l__j  l__j__jl_____jl__j\\_j
"""

header7 = """
 _    _    _      _    _       ___             _    _
| |  <_> _| |_  _| |_ | | ___ | . > _ _  ___ _| |_ | |_  ___  _ _
| |_ | |  | |    | |  | |/ ._>| . \| '_>/ . \ | |  | . |/ ._>| '_>
|___||_|  |_|    |_|  |_|\___.|___/|_|  \___/ |_|  |_|_|\___.|_|
"""

header8 = """
     _                   ______
 ___/__) ,        /)    (, /    )           /)
(, /      _/__/_ //  _    /---(  __  ____/_(/    _  __
  /    _(_(__(__(/__(/_) / ____)/ (_(_) (__/ )__(/_/ (_
 (_____               (_/ (
        )
"""

header9 = """
   __ _ _   _   _        ___           _   _
  / /(_) |_| |_| | ___  / __\_ __ ___ | |_| |__   ___ _ __
 / / | | __| __| |/ _ \/__\// '__/ _ \| __| '_ \ / _ \ '__|
/ /__| | |_| |_| |  __/ \/  \ | | (_) | |_| | | |  __/ |
\____/_|\__|\__|_|\___\_____/_|  \___/ \__|_| |_|\___|_|
"""

header11 = """
  |     _)  |    |    |        __ )               |    |
  |      |  __|  __|  |   _ \  __ \    __|  _ \   __|  __ \    _ \   __|
  |      |  |    |    |   __/  |   |  |    (   |  |    | | |   __/  |
 _____| _| \__| \__| _| \___| ____/  _|   \___/  \__| _| |_| \___| _|
"""

header12 = """
 __    _ _   _   _     _____         _   _
|  |  |_| |_| |_| |___| __  |___ ___| |_| |_ ___ ___
|  |__| |  _|  _| | -_| __ -|  _| . |  _|   | -_|  _|
|_____|_|_| |_| |_|___|_____|_| |___|_| |_|_|___|_|

                 \\\\
                  \\\\_   \\\\
                   (')   \\\\_
 LittleBrother -> / )=.---(') <- Privacy
                o( )o( )_-\_
"""

header13 = """
 __         __     ______   ______   __         ______
/\ \       /\ \   /\__  _\ /\__  _\ /\ \       /\  ___\
\ \ \____  \ \ \  \/_/\ \/ \/_/\ \/ \ \ \____  \ \  __\
 \ \_____\  \ \_\    \ \_\    \ \_\  \ \_____\  \ \_____\
  \/_____/   \/_/     \/_/     \/_/   \/_____/   \/_____/

 ______     ______     ______     ______   __  __     ______     ______
/\  == \   /\  == \   /\  __ \   /\__  _\ /\ \_\ \   /\  ___\   /\  == \
\ \  __<   \ \  __<   \ \ \/\ \  \/_/\ \/ \ \  __ \  \ \  __\   \ \  __<
 \ \_____\  \ \_\ \_\  \ \_____\    \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\
  \/_____/   \/_/ /_/   \/_____/     \/_/   \/_/\/_/   \/_____/   \/_/ /_/
"""

header14 = """
    __    _ __  __  __     ____             __  __
   / /   (_) /_/ /_/ /__  / __ )_________  / /_/ /_  ___  _____
  / /   / / __/ __/ / _ \/ __  / ___/ __ \/ __/ __ \/ _ \/ ___/
 / /___/ / /_/ /_/ /  __/ /_/ / /  / /_/ / /_/ / / /  __/ /
/_____/_/\__/\__/_/\___/_____/_/   \____/\__/_/ /_/\___/_/
"""

header15 = """
,--.   ,--.  ,--.    ,--.  ,--.       ,-----.                  ,--.  ,--.
|  |   `--',-'  '-.,-'  '-.|  | ,---. |  |) /_ ,--.--. ,---. ,-'  '-.|  ,---.  ,---. ,--.--.
|  |   ,--.'-.  .-''-.  .-'|  || .-. :|  .-.  \|  .--'| .-. |'-.  .-'|  .-.  || .-. :|  .--'
|  '--.|  |  |  |    |  |  |  |\   --.|  '--' /|  |   ' '-' '  |  |  |  | |  |\   --.|  |
`-----'`--'  `--'    `--'  `--' `----'`------' `--'    `---'   `--'  `--' `--' `----'`--'
"""

header16 = """
 _____   __ __   __   __         ______              __   __
|     |_|__|  |_|  |_|  |.-----.|   __ \.----.-----.|  |_|  |--.-----.----.
|       |  |   _|   _|  ||  -__||   __ <|   _|  _  ||   _|     |  -__|   _|
|_______|__|____|____|__||_____||______/|__| |_____||____|__|__|_____|__|
"""

header17 = """
 ____ ____ ____ ____ ____ ____
||L |||i |||t |||t |||l |||e ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
 ____ ____ ____ ____ ____ ____ ____
||B |||r |||o |||t |||h |||e |||r ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
"""

header18 = """

@@@      @@@ @@@@@@@ @@@@@@@ @@@      @@@@@@@@
@@!      @@!   @!!     @!!   @@!      @@!
@!!      !!@   @!!     @!!   @!!      @!!!:!
!!:      !!:   !!:     !!:   !!:      !!:
: ::.: : :      :       :    : ::.: : : :: ::


@@@@@@@  @@@@@@@   @@@@@@  @@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@
@@!  @@@ @@!  @@@ @@!  @@@   @!!   @@!  @@@ @@!      @@!  @@@
@!@!@!@  @!@!!@!  @!@  !@!   @!!   @!@!@!@! @!!!:!   @!@!!@!
!!:  !!! !!: :!!  !!:  !!!   !!:   !!:  !!! !!:      !!: :!!
:: : ::   :   : :  : :. :     :     :   : : : :: ::   :   : :
"""

def lb_header():
    headers = [header1, header2, header5, header6, header7, header8, header9,
        header11, header12, header13, header14, header15, header16, header17, header18]
    return(random.choice(headers))