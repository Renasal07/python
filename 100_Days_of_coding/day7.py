# Day 7 learning python Nesting

tvShow = input( "What is your favourite tv show? ")
if tvShow == "peppa pig":
    print( "Ugh, why?")
    faveCharacter = input( "Who is your favourite character?" )
else:
    faveCharacter = ""
    if faveCharacter == "daddy pig":
        print( "Right answer")
    else:
        print( "Nah, Daddy Pig's the greatest" )
if tvShow == "paw patrol":
    print( "Aww, sad tìmes")
else:
    print( "Yeah, that's cool and all..")