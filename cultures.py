class Species:
    def __init__(self, name, homeworld, lifespan):
        self.name = name
        self.homeworld = homeworld
        self.lifespan = lifespan

    def describe(self):
        return f"The {self.name} are from {self.homeworld} with an average lifespan of {self.lifespan} years."

    def communicate(self):
        return "They communicate in their unique language."

class Moclins(Species):
    def __init__(self, name, homeworld, lifespan, telepathic_ability):
        super().__init__(name, homeworld, lifespan)
        self.telepathic_ability = telepathic_ability

    def communicate(self):
        if self.telepathic_ability:
            return "Moclins communicate telepathically."
        else:
            return "Moclins communicate verbally."

class Krills(Species):
    def __init__(self, name, homeworld, lifespan, warrior_culture):
        super().__init__(name, homeworld, lifespan)
        self.warrior_culture = warrior_culture

    def communicate(self):
        return "Krills communicate through a mix of vocal sounds and body language."

    def fight_style(self):
        if self.warrior_culture:
            return "Krills are fierce warriors with a strong code of honor."
        else:
            return "Krills are peaceful and avoid conflict."

class Union(Species):
    def __init__(self, name, homeworld, lifespan, diplomacy_skill):
        super().__init__(name, homeworld, lifespan)
        self.diplomacy_skill = diplomacy_skill

    def communicate(self):
        return "The Union uses advanced technology for universal translation."

    def negotiate(self):
        if self.diplomacy_skill:
            return "Union excels in diplomacy and conflict resolution."
        else:
            return "Union struggles with diplomatic relations."

# Example usage:
moclin = Moclins("Moclin", "Moclina", 120, telepathic_ability=True)
krill = Krills("Krill", "Krillia", 80, warrior_culture=True)
union = Union("Union", "Earth", 90, diplomacy_skill=True)

print(moclin.describe())
print(moclin.communicate())

print(krill.describe())
print(krill.communicate())
print(krill.fight_style())

print(union.describe())
print(union.communicate())
print(union.negotiate())
