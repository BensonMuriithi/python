#Format strings

name = "Benson Muriithi"
age = 20 ; height = 170; weight = 64 #centimetres and kilograms
eyes = "brown"; teeth = "white" ; hair = "black"

print "Lat\'s talk about %s." % name
print "He is %d centimetres tall." % height
print "He is %d kilograms heavy." % weight
print "That\'s actually quite light."
print "He\'s got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s but can change depending on the beverage consumed." % teeth

#using multiple format 'holders'
print "Is I add %d, %d and %d, I get %d" % (age, height, weight, age + height + weight)