import os
import quanbot.replies
import quanbot.user_state

ACCESS_TOKEN = os.environ.get('FB_PAGE_ACCESS_TOKEN', 'conf_this')


def handler_message(user, message):
    replies = quanbot.replies.Replies(
            access_token=ACCESS_TOKEN,
            recipient_id=user.recipient_id,
            )
    user_state = quanbot.user_state.UserState(
            replies=replies,
            )
    for field in [
                        'location',
                        'negations',
                        '_next_behavior',
                        ]:
        if field in user.json:
            setattr(user_state, field, user.json[field])
    user_state.run_behavior(message)
    return user_state


# def get_pq_conn():
#     import os
#     import psycopg2
#     import urlparse

#     urlparse.uses_netloc.append("postgres")
#     url = urlparse.urlparse(os.environ["DATABASE_URL"])

#     conn = psycopg2.connect(
#         database=url.path[1:],
#         user=url.username,
#         password=url.password,
#         host=url.hostname,
#         port=url.port
#     )
#     return conn
