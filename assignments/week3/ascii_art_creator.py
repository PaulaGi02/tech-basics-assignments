import random


#choose a width for the length of the meadow
width = int(input("Enter the width of the meadow 5-10 "))
#choose hoe many flowers you want
count = int(input("How many flowers do you want on your meadow? 1-4"))
#chose a season spring, summer, winter, autumn
season = int(input("Do you prefer mushrooms, cactuses, or flowers? "))

meadow = ["_._.v_-_.__-_ ,___v"]
flowers  = [r"""   
          
                         @@@@
                        @@()@@
                         @@@@
                          /
                       \ |
                       \\|// """, r""" wWWWw 
                                       (___)
                                         Y
                                       \ |/
                                       \\|/// """ , r""" 
                                                         _(_)_
                                                        (_)@(_)
                                                          (_)\
                                                             `|/
                                                             \|
                                                              | /
                                                           \\\|// """ , r"""
                                                                             vVVVv
                                                                             (___)
                                                                               Y
                                                                              \|/
                                                                             \ | /
                                                                            \\\|/// """, r"""
                                                                                               _ 
                                                                                             _(_)_ 
                                                                                            (_)@(_)
                                                                                             /(_)
                                                                                              \|/
                                                                                              \|///

"""]

cactuses = [r"""     w
      /'\
      |`|
   _  |'|  _
  /.\ |`| /,\
  |'(_|.|_).|
  \.'`.'`.`'/
   `--.'.--'
      |.|
      |`|
      |.|""", r"""  ,*-.
                    |  |
                ,.  |  |
                | |_|  | ,.
                `---.  |_| |
                    |  .--`
                    |  |
                    |  | """, r"""    _  _
                                     | || | _
                                    -| || || |
                                     | || || |-
                                      \_  || |
                                        |  _/
                                       -| | \
                                        |_|-    """, r"""     _
                                                             / \        
                                                           , | | ,     
                                                          ((_| |_))  
                                                          `--, ,--` 
                                                             | |    
                                                             | |  """, r"""   _                 
                                                                           _ ( )                 
                                                                          ( \| | _              
                                                                           \,. |/ )               
                                                                             |  /'                 
                                                                             | |  """]

mushrooms = [r""" .-'''-.
                 /* * * *\
                :_.-:`:-._;
                    (_)
                 \|/(_)\|/""", r"""   ,xXXXXx,
                                     ,XXXXXXXX,
                                     XXXXXXXXXX
                                     `'''XX'''`
                                         XX
                                         XX
                                         XX  """, r"""     __.......__
                                                         ."           ".
                                                        :               :
                                                        :               :
                                                         `.._________..'
                                                              :   :
                                                              :   :
                                                              :   :
                                                              `...'""" , r"""      .-'~~~-.
                                                                                 .'o  oOOOo`.
                                                                                :~~~-.oOo   o`.
                                                                                 `. \ ~-.  oOOo.
                                                                                   `.; / ~.  OO:
                                                                                   .'  ;-- `.o.'
                                                                                  ,'  ; ~~--'~
                                                                                  ;  ;
                                                                            __\\;_\\//___\|/""" , r"""          
                                                                                                             ;.-""--..
                                                                                                           ,8o.  o88. `.
                                                                                                         `;888P  `788P  :
                                                                                                          `-._         ./
                                                                                                              ";"-P----'
                                                                                                              /  /
                                                                                                              |  |
                                                                                                             /   |
                                                                                                               """]