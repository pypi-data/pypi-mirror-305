import json
from individual.tests.test_helpers import (
    create_individual,
    create_group_with_individual,
    add_individual_to_group,
    IndividualGQLTestCase,
)


class IndividualGQLQueryTest(IndividualGQLTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.individual_a, cls.group_a, _ = create_group_with_individual(
            cls.admin_user.username,
            group_override={'location': cls.village_a},
            individual_override={'location': cls.village_a},
        )
        cls.individual_a_no_group = create_individual(
            cls.admin_user.username,
            payload_override={'location': cls.village_a},
        )
        cls.individual_a_group_no_loc, cls.group_no_loc, _ = create_group_with_individual(
            cls.admin_user.username,
            individual_override={'location': cls.village_a},
        )

        cls.individual_no_loc_group_a = create_individual(cls.admin_user.username)
        add_individual_to_group(
            cls.admin_user.username,
            cls.individual_no_loc_group_a,
            cls.group_a,
        )

        cls.individual_no_loc_no_group = create_individual(cls.admin_user.username)

        cls.individual_b, cls.group_b, _ = create_group_with_individual(
            cls.admin_user.username,
            group_override={'location': cls.village_b},
            individual_override={'location': cls.village_b},
        )


    def test_group_query_general_permission(self):
        date_created = str(self.group_a.date_created).replace(' ', 'T')
        query_str = f'''query {{
          group(dateCreated_Gte: "{date_created}") {{
            totalCount
            pageInfo {{
              hasNextPage
              hasPreviousPage
              startCursor
              endCursor
            }}
            edges {{
              node {{
                id
                uuid
                code
                head {{
                  id
                  firstName
                  lastName
                }}
              }}
            }}
          }}
        }}'''

        # Anonymous User sees nothing
        response = self.query(query_str)

        content = json.loads(response.content)
        self.assertEqual(content['errors'][0]['message'], 'Unauthorized')

        # IMIS admin sees everything
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.admin_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        group_data = content['data']['group']

        group_uuids = list(
            e['node']['uuid'] for e in group_data['edges']
        )
        self.assertTrue(str(self.group_a.uuid) in group_uuids)
        self.assertTrue(str(self.group_b.uuid) in group_uuids)
        self.assertTrue(str(self.group_no_loc.uuid) in group_uuids)

        # Health Enrollment Officier (role=1) sees nothing
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.med_enroll_officer_token}"}
        )
        content = json.loads(response.content)
        self.assertEqual(content['errors'][0]['message'], 'Unauthorized')

    def test_group_query_row_security(self):
        date_created = str(self.group_a.date_created).replace(' ', 'T')
        query_str = f'''query {{
          group(dateCreated_Gte: "{date_created}") {{
            totalCount
            pageInfo {{
              hasNextPage
              hasPreviousPage
              startCursor
              endCursor
            }}
            edges {{
              node {{
                id
                uuid
                code
                location {{
                  id uuid code name type
                  parent {{
                    id uuid code name type
                    parent {{
                      id uuid code name type
                      parent {{
                        id uuid code name type
                      }}
                    }}
                  }}
                }}
              }}
            }}
          }}
        }}'''

        # SP officer A sees only groups from their assigned districts
        # and groups without location
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.dist_a_user_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        group_data = content['data']['group']

        group_uuids = list(
            e['node']['uuid'] for e in group_data['edges']
        )
        self.assertTrue(str(self.group_a.uuid) in group_uuids)
        self.assertFalse(str(self.group_b.uuid) in group_uuids)
        self.assertTrue(str(self.group_no_loc.uuid) in group_uuids)

        # SP officer B sees only group from their assigned district
        # and groups without location
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.dist_b_user_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        group_data = content['data']['group']

        group_uuids = list(
            e['node']['uuid'] for e in group_data['edges']
        )
        self.assertFalse(str(self.group_a.uuid) in group_uuids)
        self.assertTrue(str(self.group_b.uuid) in group_uuids)
        self.assertTrue(str(self.group_no_loc.uuid) in group_uuids)


    def test_group_history_query_row_security(self):
        def send_group_history_query(group_uuid, as_user_token):
            query_str = f'''query {{
              groupHistory(
                isDeleted: false,
                id: "{group_uuid}",
                first: 10,
                orderBy: ["-version"]
              ) {{
                totalCount
                pageInfo {{
                  hasNextPage
                  hasPreviousPage
                  startCursor
                  endCursor
                }}
                edges {{
                  node {{
                    id
                    isDeleted
                    dateCreated
                    dateUpdated
                    code
                    jsonExt
                    version
                    userUpdated {{
                      username
                    }}
                  }}
                }}
              }}
            }}'''

            return self.query(
                query_str,
                headers={"HTTP_AUTHORIZATION": f"Bearer {as_user_token}"}
            )

        # SP officer A sees only group from their assigned districts and
        # groups wihtout location
        permitted_uuids = [
            self.group_a.uuid,
            self.group_no_loc.uuid,
        ]

        not_permitted_uuids = [
            self.group_b.uuid,
        ]

        for uuid in permitted_uuids:
            response = send_group_history_query(uuid, self.dist_a_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertTrue(content['data']['groupHistory']['totalCount'] > 0)

        for uuid in not_permitted_uuids:
            response = send_group_history_query(uuid, self.dist_a_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertEqual(content['data']['groupHistory']['totalCount'], 0)


        # SP officer B sees only group from their assigned district and
        # groups wihtout location
        permitted_uuids = [
            self.group_b.uuid,
            self.group_no_loc.uuid,
        ]

        not_permitted_uuids = [
            self.group_a.uuid,
        ]

        for uuid in permitted_uuids:
            response = send_group_history_query(uuid, self.dist_b_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertTrue(content['data']['groupHistory']['totalCount'] > 0)

        for uuid in not_permitted_uuids:
            response = send_group_history_query(uuid, self.dist_b_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertEqual(content['data']['groupHistory']['totalCount'], 0)


    def test_individual_query_general_permission(self):
        date_created = str(self.individual_a.date_created).replace(' ', 'T')
        query_str = f'''query {{
          individual(dateCreated_Gte: "{date_created}") {{
            totalCount
            pageInfo {{
              hasNextPage
              hasPreviousPage
              startCursor
              endCursor
            }}
            edges {{
              node {{
                id
                uuid
                firstName
                lastName
                dob
              }}
            }}
          }}
        }}'''

        # Anonymous User sees nothing
        response = self.query(query_str)

        content = json.loads(response.content)
        self.assertEqual(content['errors'][0]['message'], 'Unauthorized')

        # IMIS admin sees everything
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.admin_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        individual_data = content['data']['individual']

        individual_uuids = list(
            e['node']['uuid'] for e in individual_data['edges']
        )
        self.assertTrue(str(self.individual_a.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_b.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_a_no_group.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_a_group_no_loc.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_no_group.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_group_a.uuid) in individual_uuids)

        # Health Enrollment Officier (role=1) sees nothing
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.med_enroll_officer_token}"}
        )
        content = json.loads(response.content)
        self.assertEqual(content['errors'][0]['message'], 'Unauthorized')


    def test_individual_query_row_security(self):
        date_created = str(self.individual_a.date_created).replace(' ', 'T')
        query_str = f'''query {{
          individual(dateCreated_Gte: "{date_created}") {{
            totalCount
            pageInfo {{
              hasNextPage
              hasPreviousPage
              startCursor
              endCursor
            }}
            edges {{
              node {{
                id
                uuid
                firstName
                lastName
                dob
                location {{
                  id uuid code name type
                  parent {{
                    id uuid code name type
                    parent {{
                      id uuid code name type
                      parent {{
                        id uuid code name type
                      }}
                    }}
                  }}
                }}
              }}
            }}
          }}
        }}'''

        # SP officer A sees only individual from their assigned districts
        # individuals wihtout location, and individuals whose group has no location
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.dist_a_user_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        individual_data = content['data']['individual']

        individual_uuids = list(
            e['node']['uuid'] for e in individual_data['edges']
        )
        self.assertTrue(str(self.individual_a.uuid) in individual_uuids)
        self.assertFalse(str(self.individual_b.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_a_no_group.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_a_group_no_loc.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_no_group.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_group_a.uuid) in individual_uuids)

        # SP officer B sees only individual from their assigned district,
        # individuals wihtout location, and individuals whose group has no location
        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.dist_b_user_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        individual_data = content['data']['individual']

        individual_uuids = list(
            e['node']['uuid'] for e in individual_data['edges']
        )
        self.assertFalse(str(self.individual_a.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_b.uuid) in individual_uuids)
        self.assertFalse(str(self.individual_a_no_group.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_a_group_no_loc.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_no_group.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_group_a.uuid) in individual_uuids)


    def test_individual_query_with_group(self):
        date_created = str(self.individual_a.date_created).replace(' ', 'T')
        query_str = f'''query {{
          individual(dateCreated_Gte: "{date_created}", groupId: "{self.group_a.id}") {{
            totalCount
            pageInfo {{
              hasNextPage
              hasPreviousPage
              startCursor
              endCursor
            }}
            edges {{
              node {{
                id
                uuid
                firstName
                lastName
                dob
              }}
            }}
          }}
        }}'''

        response = self.query(
            query_str,
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.admin_token}"}
        )
        self.assertResponseNoErrors(response)

        content = json.loads(response.content)
        individual_data = content['data']['individual']

        individual_uuids = list(
            e['node']['uuid'] for e in individual_data['edges']
        )
        self.assertTrue(str(self.individual_a.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_group_a.uuid) in individual_uuids)
        self.assertFalse(str(self.individual_b.uuid) in individual_uuids)
        self.assertFalse(str(self.individual_a_no_group.uuid) in individual_uuids)


    def test_individual_history_query_row_security(self):
        def send_individual_history_query(individual_uuid, as_user_token):
            query_str = f'''query {{
              individualHistory(
                isDeleted: false,
                id: "{individual_uuid}",
                first: 10,
                orderBy: ["-version"]
              ) {{
                totalCount
                pageInfo {{
                  hasNextPage
                  hasPreviousPage
                  startCursor
                  endCursor
                }}
                edges {{
                  node {{
                    id
                    isDeleted
                    dateCreated
                    dateUpdated
                    firstName
                    lastName
                    dob
                    jsonExt
                    version
                    userUpdated {{
                      username
                    }}
                  }}
                }}
              }}
            }}'''

            return self.query(
                query_str,
                headers={"HTTP_AUTHORIZATION": f"Bearer {as_user_token}"}
            )

        # SP officer A sees only individual from their assigned districts
        # individuals wihtout location, and individuals whose group has no location
        permitted_uuids = [
            self.individual_a.uuid,
            self.individual_a_no_group.uuid,
            self.individual_a_group_no_loc.uuid,
            self.individual_no_loc_no_group.uuid,
            self.individual_no_loc_group_a.uuid,
        ]

        not_permitted_uuids = [
            self.individual_b.uuid,
        ]

        for uuid in permitted_uuids:
            response = send_individual_history_query(uuid, self.dist_a_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertTrue(content['data']['individualHistory']['totalCount'] > 0)

        for uuid in not_permitted_uuids:
            response = send_individual_history_query(uuid, self.dist_a_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertEqual(content['data']['individualHistory']['totalCount'], 0)


        # SP officer B sees only individual from their assigned district,
        # individuals wihtout location, and individuals whose group has no location
        permitted_uuids = [
            self.individual_b.uuid,
            self.individual_a_group_no_loc.uuid,
            self.individual_no_loc_no_group.uuid,
            self.individual_no_loc_group_a.uuid,
        ]

        not_permitted_uuids = [
            self.individual_a.uuid,
            self.individual_a_no_group.uuid,
        ]

        for uuid in permitted_uuids:
            response = send_individual_history_query(uuid, self.dist_b_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertTrue(content['data']['individualHistory']['totalCount'] > 0)

        for uuid in not_permitted_uuids:
            response = send_individual_history_query(uuid, self.dist_b_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertEqual(content['data']['individualHistory']['totalCount'], 0)


    def test_group_individual_query_row_security(self):
        def send_group_individual_query(group_uuid, as_user_token):
            query_str = f'''query {{
              groupIndividual(
                    group_Id: "{group_uuid}"
                ) {{
                totalCount
                pageInfo {{
                  hasNextPage
                  hasPreviousPage
                  startCursor
                  endCursor
                }}
                edges {{
                  node {{
                    id
                    individual {{
                      id
                      uuid
                      firstName
                      lastName
                      dob
                    }}
                    group {{
                      id
                      code
                    }}
                    role
                    recipientType
                    isDeleted
                    dateCreated
                    dateUpdated
                    jsonExt
                  }}
                }}
              }}
            }}'''

            return self.query(
                query_str,
                headers={"HTTP_AUTHORIZATION": f"Bearer {as_user_token}"}
            )

        # SP officer A sees only group individuals from their assigned districts
        response = send_group_individual_query(self.group_a.uuid, self.dist_a_user_token)
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(content['data']['groupIndividual']['totalCount'], 2)

        group_data = content['data']['groupIndividual']

        individual_uuids = list(
            e['node']['individual']['uuid'] for e in group_data['edges']
        )
        self.assertTrue(str(self.individual_a.uuid) in individual_uuids)
        self.assertTrue(str(self.individual_no_loc_group_a.uuid) in individual_uuids)

        # SP officer A shouldn't see group individuals from other districts
        response = send_group_individual_query(self.group_b.uuid, self.dist_a_user_token)
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(content['data']['groupIndividual']['totalCount'], 0)

        # SP officer B sees only group individuals from their assigned district
        response = send_group_individual_query(self.group_b.uuid, self.dist_b_user_token)
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(content['data']['groupIndividual']['totalCount'], 1)

        group_data = content['data']['groupIndividual']
        self.assertEqual(str(self.individual_b.uuid), group_data['edges'][0]['node']['individual']['uuid'])

        # SP officer B shouldn't see group individuals from other districts
        response = send_group_individual_query(self.group_a.uuid, self.dist_b_user_token)
        self.assertResponseNoErrors(response)
        content = json.loads(response.content)
        self.assertEqual(content['data']['groupIndividual']['totalCount'], 0)

    def test_group_individual_history_query_row_security(self):
        def send_group_individual_history_query(individual_uuid, as_user_token):
            query_str = f'''query {{
              groupIndividualHistory(
                individual_Id: "{individual_uuid}",
                first: 10,
                orderBy: ["-version"]
              ) {{
                totalCount
                pageInfo {{
                  hasNextPage
                  hasPreviousPage
                  startCursor
                  endCursor
                }}
                edges {{
                  node {{
                    id
                    individual {{
                      id
                      uuid
                      firstName
                      lastName
                      dob
                    }}
                    group {{
                      id
                      code
                    }}
                    isDeleted
                    dateCreated
                    dateUpdated
                    role
                    jsonExt
                    version
                    userUpdated {{
                      username
                    }}
                  }}
                }}
              }}
            }}'''

            return self.query(
                query_str,
                headers={"HTTP_AUTHORIZATION": f"Bearer {as_user_token}"}
            )

        # SP officer A sees only individuals from their assigned districts and
        # from groups wihtout location
        permitted_uuids = [
            self.individual_a.uuid,
            self.individual_a_group_no_loc.uuid,
            self.individual_no_loc_group_a.uuid,
        ]

        not_permitted_uuids = [
            self.individual_b.uuid,
        ]

        for i, uuid in enumerate(permitted_uuids):
            response = send_group_individual_history_query(uuid, self.dist_a_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertTrue(
                content['data']['groupIndividualHistory']['totalCount'] > 0,
                f'Expected uuid at position {i} of permitted_uuids to have groupIndividualHistory records, but got 0'
            )

        for uuid in not_permitted_uuids:
            response = send_group_individual_history_query(uuid, self.dist_a_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertEqual(content['data']['groupIndividualHistory']['totalCount'], 0)

        # SP officer B sees only group from their assigned district and
        # from groups wihtout location
        permitted_uuids = [
            self.individual_b.uuid,
            self.individual_a_group_no_loc.uuid,
        ]

        not_permitted_uuids = [
            self.individual_a.uuid,
            self.individual_no_loc_group_a.uuid,
        ]

        for uuid in permitted_uuids:
            response = send_group_individual_history_query(uuid, self.dist_b_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertTrue(content['data']['groupIndividualHistory']['totalCount'] > 0)

        for uuid in not_permitted_uuids:
            response = send_group_individual_history_query(uuid, self.dist_b_user_token)
            self.assertResponseNoErrors(response)
            content = json.loads(response.content)
            self.assertEqual(content['data']['groupIndividualHistory']['totalCount'], 0)
