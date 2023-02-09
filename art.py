import time
from colors import blue, brown, gold, green, grey, red, yellow
from utils import clear, CENT


def welcome_art():
    """
    Welcome page art of the ox and wagon.
    """
    print(f"""
                                  .::::::::::-.                     .::::::-
                                .hmMMMMMMMMMMNddds\...//M\\\\.../hddddmMMMMMMNo
                                 :NM-/NMMMMMMMMMMMMM{blue("$$")}NMMMMm{blue("&&")}MMMMMMMMMMMMMMy
                                 .sm/`-yMMMMMMMMMMMM{blue("$$")}MMMMMN{blue("&&")}MMMMMMMMMMMMMh`
                                  -Nd`  :MMMMMMMMMMM{blue("$$")}MMMMMN{blue("&&")}MMMMMMMMMMMMh`
                                   -Nh` .yMMMMMMMMMM{blue("$$")}MMMMMN{blue("&&")}MMMMMMMMMMMm/
    {brown("`oo/``-hd:  ``")}                 .sNd  :MMMMMMMMMM{blue("$$")}MMMMMN{blue("&&")}MMMMMMMMMMm/
      {brown(".yNmMMh")}{red("//")}{brown("+syysso-")}             {grey("-mh` :MMMMMMMMMM")}{blue("$$")}{grey("MMMMMN")}{blue("&&")}{grey("MMMMMMMMMMd")}
    {brown(".shMMMMN")}{red("//")}{brown("dmNMMMMMMMMMMMMs`")}     {grey("`:```-o++++oooo+:/ooooo+:+o+++oooo++/")}
    {brown("`///omh")}{red("//")}{brown("dMMMMMMMMMMMMMMMN/")}{red(":::::/+ooso--/ydh//+s+/ossssso:--syN///os:")}
          {brown("/MMMMMMMMMMMMMMMMMMd.")}     {red("`/++-.-yy/")}{grey("...")}{red("osydh/-+oo:-`o//")}{grey("...")}{red("oyodh+")}
          {brown("-hMMmssddd+:dMMmNMMh.")}     {red("`.-=mmk.")}//^^^\\\\{red(".^^`:++:^^o:")}//^^^\\\\{red("`::")}
          {brown(".sMMmo.    -dMd--:mN/`")}           ||--X--||          ||--X--||
{green("..........")}{brown("/yddy/:")}{green("...")}{brown("+hmo-")}{green("...")}{brown("hdd:")}{green("............")}\\\\=v=//{green("............")}\\\\=v=//{green(".........")}
{green("===============================================================================")}
{green("======================")}{yellow("+--------------------------------+")}{green("=======================")}
{green("======================")}{yellow("|           Welcome to           |")}{green("=======================")}
{green("======================")}{yellow("|      Python Oregon Trail       |")}{green("=======================")}
{green("======================")}{yellow("+--------------------------------+")}{green("=======================")}
{green("===============================================================================")}
    """)  # noqa
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def static_wagon(GAME, INVENTORY, PLAYER):
    """
    A static version of the animation below.
    This is for showing the stats as the game progresses.
    """
    clear()
    print(f"""
                                                                        ...
                                                  :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                                  .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                                   :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                                 {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                                 {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                                 {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                                    {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa


def animate_wagon(GAME, INVENTORY, PLAYER):
    """
    A 2.4 second animation of the ox pulling the wagon across the screen.
    """
    clear()
    print(f"""
                                                                        ...
                                                  :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                                  .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                                   :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                                 {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                                 {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                                 {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                                    {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                                      ...
                                                :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                                .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                                 :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                               {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                               {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                               {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                                  {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                                    ...
                                              :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                              .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                               :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                             {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                             {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                             {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                                {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                                  ...
                                            :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                            .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                             :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                           {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                           {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                           {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                              {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                                ...
                                          :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                          .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                           :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                         {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                         {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                         {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                            {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                              ...
                                        :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                        .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                         :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                       {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                       {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                       {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                          {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                            ...
                                      :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                      .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                       :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                     {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                     {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                     {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                        {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                          ...
                                    :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                    .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                     :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                   {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                   {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                   {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                      {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                        ...
                                  :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                  .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                   :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
                 {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
                 {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
                 {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                    {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                      ...
                                :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                                .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                                 :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
               {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
               {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
               {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                  {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                    ...
                              :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                              .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                               :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
             {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
             {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
             {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
                {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                  ...
                            :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                            .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                             :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
           {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
           {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
           {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
              {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                                ...
                          :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                          .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                           :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
         {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
         {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
         {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
            {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                              ...
                        :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                        .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                         :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
       {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
       {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
       {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
          {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                            ...
                      :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                      .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                       :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
     {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
     {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
     {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
        {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                          ...
                    :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                    .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                     :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
   {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
   {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
   {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
      {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
    time.sleep(0.15)
    clear()
    print(f"""
                                        ...
                  :YGGBGGBPJJ{blue("!^.")}~~~{blue(".^?")}JJYGGGBY
                  .GG!B@@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@@P
                   :#7 Y@@@@@@{blue("#G")}@@@{blue("#G")}@@@@@@@G
  {brown(":^.:7.")}             {grey("!&~ #@@@@@")}{blue("#G")}{grey("@@@")}{blue("#G")}{grey("@@@@@@G:")}
  {brown("~5##@J")}{red("7")}{brown("5P557Y5Y!.")}  {red(".J~:5PPGBG55GGG5PPPGBGG!")}
  {brown("7J5BB")}{red("B")}{brown("&@@@@@@@@G")}{red("^^^^7J?~?")}5?JPJ{red("J7JY?~")}J5?JPJ{red("7")}
    {brown(".J@@BY5Y7##&5")}    {red(":~")} ^Y?  5JY{red(".~!")} ^GJ  G5{red("G.")}
{green("^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}7PG?PY{green("^^^^^^")}!PBJ5{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
