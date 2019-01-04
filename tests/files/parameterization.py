EXPECTED = {'X683': {'extensibility-implied': False,
          'imports': {},
          'object-classes': {},
          'object-sets': {},
          'types': {'A': {'type': 'B',
                          'parameters': ['B']},
                    'A-Boolean': {'type': 'A',
                                  'chosen-parameters': ['BOOLEAN']},
                    'A-Integer': {'type': 'A',
                                  'chosen-parameters': ['INTEGER']},
                    'B': {'type': 'SEQUENCE',
                          'parameters': ['A', 'B'],
                          'members': [
                              {'type': 'A',
                               'name': 'a',
                               'tag': {'number': 0},
                               'optional': False},
                              {'type': 'B',
                               'name': 'b',
                               'tag': {'number': 1},
                               'optional': True}]},
                    'B-BooleanInteger': {'type': 'B',
                                         'chosen-parameters': ['BOOLEAN',
                                                               'INTEGER']}},
          'values': {}}}
