import json
from graphene_django.utils.testing import GraphQLTestCase
from mixer.backend.django import mixer
from content.models import AscendancyModel, CharacterModel, PassiveSkillModel
from content.schema import schema


class ContentUnitTestCase(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema

    def setup(self):
        self.character1 = mixer.blend(CharacterModel, name="marauder")
        self.character2 = mixer.blend(CharacterModel, name="marauder")
        self.character3 = mixer.blend(CharacterModel, name="ranger")

        self.ascendant1 = mixer.blend(AscendancyModel, character=self.character1)
        self.ascendant2 = mixer.blend(AscendancyModel, character=self.character1)
        self.ascendant3 = mixer.blend(AscendancyModel, character=self.character3)

        self.passive1 = mixer.blend(PassiveSkillModel, name="Armour, Attack Speed")
        self.passive2 = mixer.blend(PassiveSkillModel, name="Armour, Movement Speed")
        self.passive3 = mixer.blend(PassiveSkillModel, name="Undeniable")

    def test_query_character(self):
        self.setup()
        response = self.query(
            """
            query {
                characters {
                    id
                    name
                }
            }
            """
        )
        self.assertResponseNoErrors(response)

    def test_query_ascendancy(self):
        self.setup()
        self.ascendant1 = mixer.blend(AscendancyModel, character=self.character1)
        self.ascendant2 = mixer.blend(AscendancyModel, character=self.character1)
        self.ascendant3 = mixer.blend(AscendancyModel, character=self.character3)

        response = self.query(
            """
            query {
                ascendants {
                    id
                    name
                    character {
                        id
                        name
                    }
                }
            }
            """
        )
        self.assertResponseNoErrors(response)

    def test_query_ascendancy_filter(self):
        self.setup()
        response = self.query(
            """
            query ascendants($character: String!){
                ascendants(character: $character) {
                    id
                    name
                    character {
                        id
                        name
                    }
                }
            }
            """,
            variables={"character": "marauder"},
        )
        data = json.loads(response.content).get("data").get("ascendants")
        self.assertResponseNoErrors(response)
        self.assertEqual(len(data), 2)

    def test_query_passive_skill(self):
        self.setup()
        response = self.query(
            """
            query {
                passiveSkills {
                    id
                    name
                }
            }
            """
        )
        data = json.loads(response.content).get("data").get("passiveSkills")
        self.assertResponseNoErrors(response)
        self.assertEqual(len(data), 3)

    def test_query_passive_skill_filter(self):
        self.setup()
        response = self.query(
            """
            query passiveSkills($search: String!){
                passiveSkills(search: $search) {
                    id
                    name
                }
            }
            """,
            variables={"search": "speed"},
        )
        data = json.loads(response.content).get("data").get("passiveSkills")
        self.assertResponseNoErrors(response)
        self.assertEqual(len(data), 2)
