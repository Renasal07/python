#Day 4 telling a CUSTOM story

print ("=== Your Adventure Simulator ===")
print ("""You'll be asked a bunch of questions then we'll make you up an amazing story with you as the star!""")
print ()
Name = input ("Your name: ")
enemy = input("Your worst enemy's name: ")
superPower = input ("Your super power: ")
print ()
print ("Our story begins as our hero name approaches a foreboding castle...")
print ("Suddenly a bolt of lightning striked the ground at the feet of", Name)
print ("'Our final battle begins!' shouts the evil", enemy,
"clearly missing the fact that", Name, "has the power of", superPower, "which means they'll win quite easily")
# CHAGING TEXT COLOUR
print("\033[31m'Our final battle begins! '\030[0m shouts the evil", enemy, "clearly missing the fact that", Name, "has the power of\033[35m", superPower, "\033[Omwhich means they'll win quite eastly")