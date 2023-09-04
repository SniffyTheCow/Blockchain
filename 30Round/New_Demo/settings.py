from os import environ

SESSION_CONFIGS = [
    dict(
        name='Blockchain_Chat_1',
        app_sequence=['public_goods_simple', 'instructions', 'quiz', 'Round_2', 'Round_1',
                      'Round_3', 'Round_33', 'Round_22', 'Round_11', 'Round_222',
                      'Round_333', 'Round_111', 'Round_1111', 'Round_3333', 'Round_2222',
                      'six_player_instructions', 'Round_5A',
                      'Round_2A', 'Round_1A', 'Round_6A', 'Round_4A', 'Round_3A', 'Round_44A', 'Round_66A',
                      'Round_55A', 'Round_22A', 'Round_33A', 'Round_11A', 'Round_333A', 'Round_444A',
                      'Round_111A', 'Round_222A', 'Round_666A', 'Round_555A', 'exit_survey_CB'],
        num_demo_participants=6,
    ),

    dict(
        name='Blockchain_Chat_2',
        app_sequence=['public_goods_simple', 'instructions', 'quiz', 'Round_2', 'Round_1',
                      'Round_3', 'Round_33', 'Round_22', 'Round_11', 'Round_222',
                      'Round_333', 'Round_111', 'Round_1111', 'Round_3333', 'Round_2222',
                      'six_player_instructions', 'Round_5A',
                      'Round_2A', 'Round_1A', 'Round_6A', 'Round_4A', 'Round_3A', 'Round_44A', 'Round_66A',
                      'Round_55A', 'Round_22A', 'Round_33A', 'Round_11A', 'Round_333A', 'Round_444A',
                      'Round_111A', 'Round_222A', 'Round_666A', 'Round_555A', 'exit_survey_CB'],
        num_demo_participants=6,
    ),

    dict(
        name='Blockchain_Chat_3',
        app_sequence=['public_goods_simple', 'instructions', 'quiz', 'Round_2', 'Round_1',
                      'Round_3', 'Round_33', 'Round_22', 'Round_11', 'Round_222',
                      'Round_333', 'Round_111', 'Round_1111', 'Round_3333', 'Round_2222',
                      'six_player_instructions', 'Round_5A',
                      'Round_2A', 'Round_1A', 'Round_6A', 'Round_4A', 'Round_3A', 'Round_44A', 'Round_66A',
                      'Round_55A', 'Round_22A', 'Round_33A', 'Round_11A', 'Round_333A', 'Round_444A',
                      'Round_111A', 'Round_222A', 'Round_666A', 'Round_555A', 'exit_survey_CB'],
        num_demo_participants=6,
    ),


]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4684667878377'
