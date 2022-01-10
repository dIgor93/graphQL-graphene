from graphene import ObjectType, String, Schema, List, Int


class Weapon(ObjectType):
    name = String()
    velocity = Int()
    damage = Int()

    def resolve_name(self, info):
        return 'Blaster'

    def resolve_velocity(self, info):
        return 20

    def resolve_damage(self, info):
        return 500


class SpaceShip(ObjectType):
    name = String()
    weight = Int()
    weapons = List(Weapon)

    def resolve_name(self, info):
        return 'Stranger'

    def resolve_weight(self, info):
        return 2300

    def resolve_weapons(self, info):
        return [
            {
                'name': 'Blaster',
                'velocity': 20,
                'damage': 500
            }
        ]


class Query(ObjectType):
    spaceships = List(SpaceShip)

    def resolve_spaceships(self, info):
        return [
            {

            }
        ]


schema = Schema(query=Query, types=[SpaceShip, Weapon, ])

query_string = '''
{
    spaceships {
        name,
        weapons {
            name,
            velocity,
            damage
        }
    }
}'''

result = schema.execute(query_string)
if result.data:
    print(result.data)
else:
    print(result.errors)
