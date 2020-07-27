from flask import Blueprint, request, jsonify, g
from models.user import User
from schemas.user import UserSchema
from schemas.likes import LikeSchema
from schemas.dislike import DislikeSchema
from app import db
from lib.secure_route import secure_route
from marshmallow import ValidationError
from models.likes import Like
from models.dislikes import Dislike


user_schema = UserSchema()
like_schema = LikeSchema()
dislike_schema = DislikeSchema()

# GET all users

router = Blueprint(__name__, 'users')

@router.route('/users', methods=['GET'])
@secure_route
def get_users():
  users = User.query.all()
  print('hello')
  return user_schema.jsonify(users, many=True), 200


@router.route('/likes', methods=['GET', 'POST'])
@secure_route
def like():
  like_data = request.get_json()
  like_instance = Like(
    liker_id=g.current_user.id,
    liked_id=like_data['liked_id']
  )
  like_instance.save()
  # user_1_likers=Like.query.filter_by(liked_id=like_data['liked_id'])
  likers_of_user=Like.query.filter_by(liked_id=g.current_user.id).all()
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  print('')
  print('')
  print(likers_of_user)
  print('')
  print('')
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  print('USER 1 LIKERS')
  return like_schema.jsonify(like_data)

@router.route('/dislikes', methods=['POST'])
@secure_route
def dislike():
  dislike_data = request.get_json()
  dislike_instance = Dislike(
    disliker_id=g.current_user.id,
    disliked_id=dislike_data['disliked_id']
  )
  print(dislike_instance)
  dislike_instance.save()
  return dislike_schema.jsonify(dislike_data)













