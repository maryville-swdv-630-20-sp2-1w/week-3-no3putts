'''
Answer the following questions:

1. What are the parent and child classes here?
   - The Parent is the Spell class
   - The child classes are Accio and Confundo

2. What are the base and sub-classes?
   - The base class is the Spell class
   - The sub-classes are Accio and Confundo

3. What is the output from this code?   Try without running if you can
    - Accio
    - Summoning Charm Accio
    - No description
    - Confundus Charm Confundo
    - Causes the victim to become confused and befuddled.

4. When study_spell(Confundo()) executes...what get_description method gets called and why?
    - Because Confundo overrides the get_description() method in Spell, the Confundo.get_description() method gets called

5. The statement print Accio() needs to print ‘This charm summons an object to the caster, potentially over a significant distance’)? Write down the code that we need to add and/or change.
    - The class Accio needs to change to this:

      class Accio(Spell):
        def __init__(self):
            Spell.__init__(self, 'Accio', 'Summoning Charm')

        def get_description(self):
            return 'This charm summons an object to the caster, potentially over a significant distance'

'''


class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()

    def get_description(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')


class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'


def study_spell(spell):
    print(spell)


spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())
print(Accio())

