# class MatchSchema(ma.SQLAlchemyAutoSchema):
#   class Meta:
#     model = Match
#     load_instance = True

# matches_table = db.Table('matches_table',
#   db.Column('id', db.Integer, db.ForeignKey('matches.id'), primary_key=True),
#   db.Column('user_1_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
#   db.Column('user_2_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
# )