"""
Exercise "Animals"

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

All you need to know in order to solve this exercise, you'll find in the cars_oop- and rpg1-files.

Define a class named Animal.
Each object of this class shall have the attributes name, sound, height, weight, legs, female.
Name and sound are strings. Height and weight are floating point numbers. Legs is a integer. Female is boolean.

Add to the class meaningful methods __init__ and __repr__.
Call these methods to create objects of the class Animal and to print them out in the main program.

Write a class method named make_noise, which prints out the animal's sound in the console.
Call this method in the main program.

Define another class Dog, which inherits from Animal.
Each object of this class shall have the attributes tail_length and hunts_sheep.
Tail_length is a floating point number. Hunts_sheep is boolean.

Add to the class meaningful methods __init__ and __repr__.
In writing the constructor of Dog, try to reuse code from the class Animal.
Call these methods to create objects of the class Dog and to print them out in the main program.

Call the method make_noise on Dog objects in the main program.

Write a class method named wag_tail for Dog.
This method prints out into the console something like
"The dog Snoopy wags its 32cm long tail"
Call this method in the main program.

Write a function mate(mother, father). Both parameters are of type Dog.
This function shall return a new object of type Dog.
In this function, make meaningful rules for the new dogs attributes.
Make sure that this function only accepts dogs with the correct sex as arguments.

In the main program, call this method and print out the new dog.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


class Animal:

    def __init__(self, name, sound, height_in_cm, weight_in_kg, legs, is_female):
        self.name = name
        self.sound = sound
        self.height_in_cm = height_in_cm
        self.weight_in_kg = weight_in_kg
        self.legs = legs
        self.is_female = is_female

    # def female_check(self): i will try to make this work later
    #     if (self.is_female == True):
    #        sex_answer = "Yes"
    #
    #     else:
    #         sex_answer = "No"

    def __repr__(self):
        return f'this animal is named {self.name} and sounds like this "{self.sound}". the height of this animal is {self.height_in_cm} cm, it has a weight of {self.weight_in_kg} kg and {self.legs} legs. is it female? {self.is_female}'

    def make_noise(self):
        print(f"{self.sound}!!!")


class Dog(Animal):

    def __init__(self, name, sound, height_in_cm, weight_in_kg, tail_length_in_cm, legs, is_female, hunts_sheep):
        super().__init__(name, sound, height_in_cm, weight_in_kg, legs, is_female)

        self.tail_length_in_cm = tail_length_in_cm
        self.hunts_sheep = hunts_sheep


    def mate_check(self):
        if self.is_female == True:
            male_mater = False
        else:
            male_mater = True

    def __repr__(self):
        return f'this animal is named {self.name} and sounds like this "{self.sound}". the height of this animal is {self.height_in_cm}cm, it weighs {self.weight_in_kg}kg, it´s tail is {self.tail_length_in_cm} cm long and has {self.legs} legs. is it female? {self.is_female} does it hunt sheep?? {self.hunts_sheep}'


# name of self + tail length
    def wag_tail(self):
        print(f"{self.name} wagged it´s {self.tail_length_in_cm}cm long tail. this dog is very happy")


    #mating function doesn´t work
    # def mate(self, mating_dog2):
    #     i = 0
    #     puppies = []
    #     if len(self.is_female) == 4 & len(mating_dog2.is_female) or len(self.is_female) == 5 & len(mating_dog2.is_female) == 4:
    #         puppy = Dog("puppy", "woof", 20, 2, 10, 4, True, True)
    #         puppies[i] + puppy
    #         print(puppies)
    #         i += 1
    #
    #     else:
    #         print("I don´t think you know how the birds and the bees work..." )
    #



# instances of the Animal Class
snake = Animal("steve", "SSSSSSS", 25.78, 5, 0, True)
cat = Animal("calvin", "MEOW", 30, 12, 4, False)

# instances of the Dog Class

dog = Dog("mac", "WOOF",50, 50, 15, 4, False, True)
dog1 = Dog("kim", "female WOOF", 40, 40, 12, 4, True, False )
# print(snake) #prints the __repr__  Fstring of the Animal Class
# print(cat) #prints the __repr__  Fstring of the Animal Class
#snake.make_noise()  # calls the make noise function

# Dog instances
#
# print(dog)
# dog.make_noise()
#
# dog.wag_tail()

Dog.mate(dog, dog1)
