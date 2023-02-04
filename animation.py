import time
from colors import brown, green, orange, red, yellow
from utils import clear


def static_wagon(GAME, INVENTORY, PLAYER):
    """
    A static version of the animation below.
    This is for showing the stats as the game progresses.
    """
    clear()
    print(f"""
                                                                        ...
                                                  :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                                  .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                                   :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                                 {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                                 {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                                 {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                                    {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^")}

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
                                                  :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                                  .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                                   :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                                 {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                                 {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                                 {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                                    {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^")}

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
                                                :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                                .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                                 :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                               {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                               {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                               {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                                  {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^")}

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
                                              :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                              .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                               :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                             {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                             {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                             {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                                {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^")}

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
                                            :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                            .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                             :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                           {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                           {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                           {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                              {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^")}

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
                                          :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                          .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                           :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                         {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                         {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                         {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                            {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^")}

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
                                        :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                        .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                         :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                       {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                       {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                       {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                          {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^")}

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
                                      :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                      .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                       :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                     {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                     {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                     {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                        {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^")}

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
                                    :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                    .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                     :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                   {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                   {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                   {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                      {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^")}

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
                                  :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                  .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                   :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
                 {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
                 {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
                 {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                    {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^")}

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
                                :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                                .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                                 :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
               {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
               {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
               {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                  {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^")}

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
                              :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                              .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                               :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
             {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
             {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
             {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
                {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^")}

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
                            :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                            .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                             :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
           {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
           {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
           {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
              {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^^^")}

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
                          :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                          .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                           :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
         {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
         {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
         {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
            {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

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
                        :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                        .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                         :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
       {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
       {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
       {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
          {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

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
                      :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                      .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                       :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
     {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
     {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
     {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
        {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

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
                    :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                    .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                     :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
   {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
   {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
   {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
      {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

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
                  :YGGBGGBPJJ{red("!^.")}~~~{red(".^?")}JJYGGGBY
                  .GG!B@@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@@P
                   :#7 Y@@@@@@{red("#G")}@@@{red("#G")}@@@@@@@G
 {brown(":^.:7.")}             !&~ #@@@@@{red("#G")}@@@{red("#G")}@@@@@@G:
 {brown("~5##@J75P557Y5Y!.")}  {orange(".J~:5PPGBG55GGG5PPPGBGG!")}
 {brown("7J5BBB&@@@@@@@@G")}^^^^{orange("7J?~?")}{yellow("5?JPJ")}{orange("J7JY?~")}{yellow("J5?JPJ7")}
    {brown(".J@@BY5Y7##&5")}    {orange(":~")} {yellow("^Y?GG5JY")}{orange(".~!")} {orange("^")}{yellow("GJGG55G.")}
{green("^^^^")}{brown("~G555")}{green("^^^")}{brown("JB!5&J")}{green("^^^^^^^")}{yellow("7PG?PY~")}{green("^^:^^")}{yellow("!PBJ5P!")}{green("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")}

{"Date:":>39}  {GAME.date_string}
{"Weather:":>39}  {GAME.weather}
{"Health:":>39}  {PLAYER.health}
{"Food:":>39}  {str(INVENTORY.food) + " pounds"}
{"Next landmark:":>39}  {str(GAME.next_destination_distance) + " miles"}
{"Miles traveled:":>39}  {str(GAME.distance_traveled) + " miles"}
    """)  # noqa
