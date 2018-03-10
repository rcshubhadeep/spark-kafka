def get_user_session_id(user_dict):
    return user_dict['cookieid']


def get_Visited_count(rdd):
    coockie_id_stream = rdd.map(lambda x: get_user_session_id(x))
    cid_count = coockie_id_stream.countByValueAndWindow(60, 20)
    return cid_count
