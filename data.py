users = {
  "1234": {"reffer_id": "5841656536", "flag": True, "real_name": "bot"},
  "1257": {"reffer_id": "5841656536", "flag": True, "real_name": "bot"},
  "1236": {"reffer_id":  None, "flag": True, "real_name": "bot"},
  "1479": {"reffer_id": "5841656536", "flag": True, "real_name": "bot"},
  "3154": {"reffer_id": "5841656536", "flag": False, "real_name": "bot"},
  "6234": {"reffer_id": "5841656536", "flag": True, "real_name": "bot"}
}

def get_user_ball(user_id):
  ball = 0
  for user in users.values():
    if user_id == user['reffer_id'] and user['flag']: ball += 1
  return ball
